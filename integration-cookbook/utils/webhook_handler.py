#!/usr/bin/env python3
"""
Reusable Webhook Handler
=========================
Relay▸Launch Integration Cookbook

A production-ready Flask-based webhook handler utility with:
    - Signature verification (HMAC-SHA256, Stripe, custom)
    - Automatic retry detection and idempotency
    - Structured JSON logging
    - Request validation and parsing
    - Configurable event routing
    - Health check endpoint

Usage:
    from utils.webhook_handler import WebhookHandler

    handler = WebhookHandler(
        secret="your-webhook-secret",
        signature_header="X-Webhook-Signature",
        signature_scheme="hmac-sha256",
    )

    @handler.on("payment.completed")
    def handle_payment(event_data):
        print(f"Payment received: {event_data}")
        return True

    # Run standalone
    handler.run(port=5000)

    # Or mount on an existing Flask app
    app = Flask(__name__)
    handler.register(app, url_prefix="/webhooks")
"""

import os
import hmac
import hashlib
import json
import time
import logging
import uuid
from datetime import datetime, timezone
from functools import wraps
from typing import Any, Callable, Optional

from flask import Flask, Blueprint, request, jsonify, g

# ---------------------------------------------------------------------------
# Structured Logger
# ---------------------------------------------------------------------------


class StructuredLogger:
    """
    A thin wrapper around Python's logging module that outputs structured
    JSON log lines. Makes it easy to parse logs in production with tools
    like Datadog, CloudWatch, or ELK.
    """

    def __init__(self, name: str, level: str = "INFO"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper(), logging.INFO))

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(message)s"))
            self.logger.addHandler(handler)

    def _log(self, level: str, message: str, **kwargs):
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": level,
            "message": message,
            **kwargs,
        }
        log_method = getattr(self.logger, level.lower(), self.logger.info)
        log_method(json.dumps(entry, default=str))

    def info(self, message: str, **kwargs):
        self._log("INFO", message, **kwargs)

    def warning(self, message: str, **kwargs):
        self._log("WARNING", message, **kwargs)

    def error(self, message: str, **kwargs):
        self._log("ERROR", message, **kwargs)

    def debug(self, message: str, **kwargs):
        self._log("DEBUG", message, **kwargs)


# ---------------------------------------------------------------------------
# Idempotency Store
# ---------------------------------------------------------------------------


class IdempotencyStore:
    """
    In-memory store for tracking processed event IDs to prevent
    duplicate processing on webhook retries.

    For production use with multiple workers, replace this with a
    Redis-backed or database-backed implementation.
    """

    def __init__(self, max_size: int = 10000, ttl_seconds: int = 86400):
        """
        Args:
            max_size: Maximum number of event IDs to track.
            ttl_seconds: How long to remember an event ID (default: 24h).
        """
        self._store: dict[str, float] = {}
        self._max_size = max_size
        self._ttl = ttl_seconds

    def has_been_processed(self, event_id: str) -> bool:
        """Check if an event ID has already been processed."""
        self._cleanup()
        return event_id in self._store

    def mark_processed(self, event_id: str) -> None:
        """Mark an event ID as processed."""
        self._store[event_id] = time.time()

    def _cleanup(self) -> None:
        """Remove expired entries and enforce max size."""
        now = time.time()
        cutoff = now - self._ttl

        # Remove expired
        expired = [k for k, v in self._store.items() if v < cutoff]
        for k in expired:
            del self._store[k]

        # If still over max size, remove oldest
        if len(self._store) > self._max_size:
            sorted_keys = sorted(self._store.keys(), key=lambda k: self._store[k])
            for k in sorted_keys[: len(self._store) - self._max_size]:
                del self._store[k]


# ---------------------------------------------------------------------------
# Signature Verification
# ---------------------------------------------------------------------------


class SignatureVerifier:
    """
    Verifies webhook signatures using various schemes.

    Supported schemes:
        - hmac-sha256: Standard HMAC-SHA256 (most webhooks)
        - hmac-sha1: HMAC-SHA1 (GitHub)
        - stripe: Stripe's timestamp-based signature scheme
        - none: No verification (development only)
    """

    def __init__(self, secret: str, scheme: str = "hmac-sha256"):
        self.secret = secret
        self.scheme = scheme.lower()

    def verify(self, payload: bytes, signature: str) -> bool:
        """
        Verify a webhook signature.

        Args:
            payload: Raw request body bytes.
            signature: Signature string from the request header.

        Returns:
            True if valid, False otherwise.
        """
        if self.scheme == "none":
            return True

        if not signature:
            return False

        if self.scheme == "hmac-sha256":
            return self._verify_hmac(payload, signature, hashlib.sha256, "sha256")
        elif self.scheme == "hmac-sha1":
            return self._verify_hmac(payload, signature, hashlib.sha1, "sha1")
        elif self.scheme == "stripe":
            return self._verify_stripe(payload, signature)
        else:
            raise ValueError(f"Unknown signature scheme: {self.scheme}")

    def _verify_hmac(
        self,
        payload: bytes,
        signature: str,
        hash_func: Callable,
        prefix: str,
    ) -> bool:
        """Verify standard HMAC signature."""
        expected = hmac.new(
            self.secret.encode("utf-8"),
            payload,
            hash_func,
        ).hexdigest()

        # Handle signatures with or without prefix (e.g., "sha256=abc123")
        if signature.startswith(f"{prefix}="):
            signature = signature[len(prefix) + 1:]

        return hmac.compare_digest(expected, signature)

    def _verify_stripe(self, payload: bytes, signature: str) -> bool:
        """
        Verify Stripe webhook signature.

        Stripe signatures look like: t=1234567890,v1=abc123,v0=def456
        """
        try:
            parts = dict(item.split("=", 1) for item in signature.split(","))
            timestamp = parts.get("t", "")
            v1_signature = parts.get("v1", "")

            if not timestamp or not v1_signature:
                return False

            # Check timestamp tolerance (5 minutes)
            if abs(time.time() - int(timestamp)) > 300:
                return False

            # Compute expected signature
            signed_payload = f"{timestamp}.{payload.decode('utf-8')}"
            expected = hmac.new(
                self.secret.encode("utf-8"),
                signed_payload.encode("utf-8"),
                hashlib.sha256,
            ).hexdigest()

            return hmac.compare_digest(expected, v1_signature)

        except (ValueError, KeyError):
            return False


# ---------------------------------------------------------------------------
# Webhook Handler
# ---------------------------------------------------------------------------


class WebhookHandler:
    """
    A reusable, production-ready webhook handler.

    Features:
        - Event-based routing with decorators
        - Automatic signature verification
        - Idempotency (duplicate detection)
        - Structured logging
        - Health check endpoint
        - Request ID tracking
        - Configurable error handling

    Example:
        handler = WebhookHandler(secret="whsec_abc123")

        @handler.on("order.created")
        def handle_order(data):
            process_order(data)
            return True

        handler.run(port=5000)
    """

    def __init__(
        self,
        secret: Optional[str] = None,
        signature_header: str = "X-Webhook-Signature",
        signature_scheme: str = "hmac-sha256",
        event_type_field: str = "event_type",
        event_id_field: str = "event_id",
        log_level: str = "INFO",
        enable_idempotency: bool = True,
        idempotency_ttl: int = 86400,
    ):
        """
        Args:
            secret: Shared secret for signature verification. None disables verification.
            signature_header: HTTP header name containing the signature.
            signature_scheme: Signature algorithm ("hmac-sha256", "hmac-sha1", "stripe", "none").
            event_type_field: JSON field name that contains the event type.
            event_id_field: JSON field name that contains the unique event ID.
            log_level: Logging level.
            enable_idempotency: Whether to track and skip duplicate events.
            idempotency_ttl: How long to remember processed events (seconds).
        """
        self.secret = secret
        self.signature_header = signature_header
        self.event_type_field = event_type_field
        self.event_id_field = event_id_field
        self.enable_idempotency = enable_idempotency

        self.logger = StructuredLogger("webhook-handler", log_level)
        self.verifier = SignatureVerifier(
            secret=secret or "",
            scheme=signature_scheme if secret else "none",
        )
        self.idempotency_store = IdempotencyStore(ttl_seconds=idempotency_ttl)

        # Event handler registry
        self._handlers: dict[str, Callable] = {}
        self._default_handler: Optional[Callable] = None
        self._error_handler: Optional[Callable] = None

        # Flask blueprint for mounting
        self.blueprint = Blueprint("webhooks", __name__)
        self._register_routes()

    def on(self, event_type: str) -> Callable:
        """
        Decorator to register a handler for a specific event type.

        Args:
            event_type: The event type string to handle (e.g., "payment.completed").

        Example:
            @handler.on("payment.completed")
            def handle_payment(data):
                # process payment
                return True
        """
        def decorator(func: Callable) -> Callable:
            self._handlers[event_type] = func
            self.logger.info(
                "Registered handler",
                event_type=event_type,
                handler=func.__name__,
            )
            return func
        return decorator

    def on_default(self, func: Callable) -> Callable:
        """
        Decorator to register a default handler for unrecognized event types.

        Example:
            @handler.on_default
            def handle_unknown(event_type, data):
                logger.warning(f"Unknown event: {event_type}")
        """
        self._default_handler = func
        return func

    def on_error(self, func: Callable) -> Callable:
        """
        Decorator to register a custom error handler.

        Example:
            @handler.on_error
            def handle_error(event_type, data, error):
                send_alert(f"Webhook processing failed: {error}")
        """
        self._error_handler = func
        return func

    def _register_routes(self) -> None:
        """Register Flask routes on the blueprint."""

        @self.blueprint.route("/webhook", methods=["POST"])
        def receive_webhook():
            return self._handle_request()

        @self.blueprint.route("/health", methods=["GET"])
        def health_check():
            return jsonify({
                "status": "healthy",
                "registered_events": list(self._handlers.keys()),
                "idempotency_enabled": self.enable_idempotency,
                "signature_verification": self.secret is not None,
            }), 200

    def _handle_request(self):
        """Core webhook request handling logic."""
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        start_time = time.time()

        self.logger.info(
            "Webhook received",
            request_id=request_id,
            remote_addr=request.remote_addr,
            content_length=request.content_length,
        )

        # Step 1: Verify signature
        if self.secret:
            signature = request.headers.get(self.signature_header, "")
            payload = request.get_data()

            if not self.verifier.verify(payload, signature):
                self.logger.warning(
                    "Signature verification failed",
                    request_id=request_id,
                    remote_addr=request.remote_addr,
                )
                return jsonify({"error": "Invalid signature"}), 401

        # Step 2: Parse payload
        try:
            data = request.get_json(force=True)
        except Exception:
            self.logger.error("Failed to parse JSON payload", request_id=request_id)
            return jsonify({"error": "Invalid JSON"}), 400

        if not data or not isinstance(data, dict):
            return jsonify({"error": "Empty or invalid payload"}), 400

        # Step 3: Extract event metadata
        event_type = data.get(self.event_type_field, "unknown")
        event_id = data.get(self.event_id_field, request_id)

        self.logger.info(
            "Processing event",
            request_id=request_id,
            event_type=event_type,
            event_id=event_id,
        )

        # Step 4: Check idempotency
        if self.enable_idempotency and self.idempotency_store.has_been_processed(event_id):
            self.logger.info(
                "Duplicate event skipped",
                request_id=request_id,
                event_id=event_id,
            )
            return jsonify({
                "status": "already_processed",
                "event_id": event_id,
            }), 200

        # Step 5: Dispatch to handler
        handler = self._handlers.get(event_type)

        if not handler and self._default_handler:
            handler = lambda d: self._default_handler(event_type, d)  # noqa: E731

        if not handler:
            self.logger.debug(
                "No handler for event type",
                event_type=event_type,
                request_id=request_id,
            )
            return jsonify({
                "status": "ignored",
                "reason": f"No handler registered for event type: {event_type}",
            }), 200

        try:
            result = handler(data)

            # Mark as processed
            if self.enable_idempotency:
                self.idempotency_store.mark_processed(event_id)

            elapsed = time.time() - start_time
            self.logger.info(
                "Event processed successfully",
                request_id=request_id,
                event_type=event_type,
                event_id=event_id,
                duration_ms=round(elapsed * 1000, 2),
                handler_result=bool(result),
            )

            return jsonify({
                "status": "processed",
                "event_id": event_id,
                "event_type": event_type,
            }), 200

        except Exception as exc:
            elapsed = time.time() - start_time
            self.logger.error(
                "Handler raised an exception",
                request_id=request_id,
                event_type=event_type,
                event_id=event_id,
                error=str(exc),
                duration_ms=round(elapsed * 1000, 2),
            )

            # Call custom error handler if registered
            if self._error_handler:
                try:
                    self._error_handler(event_type, data, exc)
                except Exception as err_exc:
                    self.logger.error(
                        "Error handler itself raised an exception",
                        error=str(err_exc),
                    )

            # Return 200 to prevent webhook retries for application errors.
            # The error is logged and can be investigated. Change to 500
            # if you want the sender to retry.
            return jsonify({
                "status": "error",
                "event_id": event_id,
                "message": "Processing failed — logged for investigation",
            }), 200

    def register(self, app: Flask, url_prefix: str = "") -> None:
        """
        Mount the webhook handler on an existing Flask app.

        Args:
            app: The Flask application.
            url_prefix: URL prefix for all webhook routes (e.g., "/webhooks").
        """
        app.register_blueprint(self.blueprint, url_prefix=url_prefix)
        self.logger.info(
            "Webhook handler mounted",
            url_prefix=url_prefix or "/",
            routes=["/webhook", "/health"],
        )

    def run(self, host: str = "0.0.0.0", port: int = 5000, debug: bool = False) -> None:
        """
        Run the webhook handler as a standalone Flask server.

        Args:
            host: Host to bind to.
            port: Port to listen on.
            debug: Enable Flask debug mode.
        """
        app = Flask(__name__)
        self.register(app)

        self.logger.info(
            "Starting webhook server",
            host=host,
            port=port,
            handlers=list(self._handlers.keys()),
        )

        app.run(host=host, port=port, debug=debug)


# ---------------------------------------------------------------------------
# Standalone Example
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Example: Run a webhook handler that prints received events
    secret = os.environ.get("WEBHOOK_SECRET")
    port = int(os.environ.get("FLASK_PORT", 5000))

    handler = WebhookHandler(
        secret=secret,
        signature_header="X-Webhook-Signature",
        signature_scheme="hmac-sha256",
        event_type_field="event_type",
        event_id_field="event_id",
    )

    @handler.on("test.event")
    def handle_test(data):
        print(f"Received test event: {json.dumps(data, indent=2)}")
        return True

    @handler.on_default
    def handle_default(event_type, data):
        print(f"Received unhandled event type '{event_type}': {json.dumps(data, indent=2)}")
        return True

    handler.run(port=port)
