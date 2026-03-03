#!/usr/bin/env python3
"""
Stripe to Slack Payment Notifications
======================================
Relay▸Launch Integration Cookbook

Listens for Stripe webhook events and sends formatted Slack notifications
for successful payments, failed payments, and new subscriptions.

Setup:
    1. Set environment variables (see below)
    2. Run: python stripe-to-slack-notifications.py
    3. Configure Stripe webhook endpoint to point at your server's /webhook/stripe path
    4. Select events: payment_intent.succeeded, payment_intent.payment_failed,
       customer.subscription.created, customer.subscription.updated

Environment Variables:
    STRIPE_SECRET_KEY       — Stripe secret key (sk_live_... or sk_test_...)
    STRIPE_WEBHOOK_SECRET   — Stripe webhook signing secret (whsec_...)
    SLACK_WEBHOOK_URL       — Slack incoming webhook URL
    SLACK_CHANNEL           — Slack channel override (optional, default: #payments)
    FLASK_PORT              — Port to run the server on (optional, default: 5000)
    LOG_LEVEL               — Logging level (optional, default: INFO)

Stripe Webhook Setup:
    In your Stripe Dashboard → Developers → Webhooks → Add endpoint:
    URL: https://your-server.com/webhook/stripe
    Events to listen for:
        - payment_intent.succeeded
        - payment_intent.payment_failed
        - customer.subscription.created
        - customer.subscription.updated
        - charge.refunded
"""

import os
import sys
import json
import logging
from datetime import datetime, timezone
from decimal import Decimal

import stripe
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

load_dotenv()

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL", "#payments")
FLASK_PORT = int(os.environ.get("FLASK_PORT", 5000))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

# Validate required configuration
_missing = []
if not STRIPE_SECRET_KEY:
    _missing.append("STRIPE_SECRET_KEY")
if not STRIPE_WEBHOOK_SECRET:
    _missing.append("STRIPE_WEBHOOK_SECRET")
if not SLACK_WEBHOOK_URL:
    _missing.append("SLACK_WEBHOOK_URL")

if _missing:
    print(f"ERROR: Missing required environment variables: {', '.join(_missing)}")
    print("Copy .env.example to .env and fill in your values.")
    sys.exit(1)

stripe.api_key = STRIPE_SECRET_KEY

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("stripe-to-slack")

# ---------------------------------------------------------------------------
# Flask App
# ---------------------------------------------------------------------------

app = Flask(__name__)


# ---------------------------------------------------------------------------
# Slack Messaging
# ---------------------------------------------------------------------------


def send_slack_message(blocks: list, fallback_text: str) -> bool:
    """
    Send a Block Kit message to Slack via incoming webhook.

    Args:
        blocks: Slack Block Kit block list.
        fallback_text: Plain-text fallback for notifications.

    Returns:
        True if the message was sent successfully, False otherwise.
    """
    payload = {
        "channel": SLACK_CHANNEL,
        "text": fallback_text,
        "blocks": blocks,
    }

    try:
        resp = requests.post(
            SLACK_WEBHOOK_URL,
            json=payload,
            timeout=10,
            headers={"Content-Type": "application/json"},
        )
        if resp.status_code != 200:
            logger.error(
                "Slack API returned %s: %s", resp.status_code, resp.text
            )
            return False
        logger.info("Slack notification sent: %s", fallback_text)
        return True
    except requests.RequestException as exc:
        logger.error("Failed to send Slack message: %s", exc)
        return False


# ---------------------------------------------------------------------------
# Currency Formatting
# ---------------------------------------------------------------------------


def format_amount(amount_cents: int, currency: str = "usd") -> str:
    """
    Format a Stripe amount (in smallest currency unit) to a human-readable string.

    Args:
        amount_cents: Amount in the smallest currency unit (e.g., cents for USD).
        currency: Three-letter ISO currency code.

    Returns:
        Formatted string like "$49.99 USD".
    """
    # Most currencies use 2 decimal places; some (JPY, KRW) use 0
    zero_decimal_currencies = {
        "bif", "clp", "djf", "gnf", "jpy", "kmf", "krw", "mga",
        "pyg", "rwf", "ugx", "vnd", "vuv", "xaf", "xof", "xpf",
    }

    currency_lower = currency.lower()
    if currency_lower in zero_decimal_currencies:
        amount = amount_cents
    else:
        amount = Decimal(amount_cents) / Decimal(100)

    symbols = {"usd": "$", "eur": "€", "gbp": "£", "cad": "CA$", "aud": "A$"}
    symbol = symbols.get(currency_lower, "")

    return f"{symbol}{amount:,.2f} {currency.upper()}"


# ---------------------------------------------------------------------------
# Event Handlers
# ---------------------------------------------------------------------------


def handle_payment_succeeded(event: dict) -> bool:
    """Handle payment_intent.succeeded events."""
    pi = event["data"]["object"]
    amount = format_amount(pi["amount"], pi["currency"])
    customer_id = pi.get("customer", "unknown")
    description = pi.get("description", "No description")

    # Try to fetch customer email
    customer_email = "N/A"
    if customer_id and customer_id != "unknown":
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer_email = customer.get("email", "N/A")
        except stripe.error.StripeError as exc:
            logger.warning("Could not fetch customer %s: %s", customer_id, exc)

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Payment Successful",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Amount:*\n{amount}"},
                {"type": "mrkdwn", "text": f"*Customer:*\n{customer_email}"},
                {"type": "mrkdwn", "text": f"*Description:*\n{description}"},
                {
                    "type": "mrkdwn",
                    "text": f"*Payment Intent:*\n`{pi['id']}`",
                },
            ],
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"Received at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
                }
            ],
        },
    ]

    return send_slack_message(blocks, f"Payment received: {amount} from {customer_email}")


def handle_payment_failed(event: dict) -> bool:
    """Handle payment_intent.payment_failed events."""
    pi = event["data"]["object"]
    amount = format_amount(pi["amount"], pi["currency"])
    customer_id = pi.get("customer", "unknown")

    # Extract failure details
    last_error = pi.get("last_payment_error", {})
    failure_message = last_error.get("message", "Unknown failure reason")
    failure_code = last_error.get("code", "unknown")

    customer_email = "N/A"
    if customer_id and customer_id != "unknown":
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer_email = customer.get("email", "N/A")
        except stripe.error.StripeError:
            pass

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Payment Failed",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Amount:*\n{amount}"},
                {"type": "mrkdwn", "text": f"*Customer:*\n{customer_email}"},
                {"type": "mrkdwn", "text": f"*Failure Reason:*\n{failure_message}"},
                {"type": "mrkdwn", "text": f"*Error Code:*\n`{failure_code}`"},
            ],
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "View in Stripe"},
                    "url": f"https://dashboard.stripe.com/payments/{pi['id']}",
                }
            ],
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"Received at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
                }
            ],
        },
    ]

    return send_slack_message(
        blocks,
        f"PAYMENT FAILED: {amount} from {customer_email} — {failure_message}",
    )


def handle_subscription_created(event: dict) -> bool:
    """Handle customer.subscription.created events."""
    sub = event["data"]["object"]
    customer_id = sub.get("customer", "unknown")
    status = sub.get("status", "unknown")

    # Extract plan/price details
    items = sub.get("items", {}).get("data", [])
    plan_details = []
    total_amount = 0
    currency = "usd"

    for item in items:
        price = item.get("price", {})
        amount = price.get("unit_amount", 0)
        curr = price.get("currency", "usd")
        interval = price.get("recurring", {}).get("interval", "month")
        nickname = price.get("nickname") or price.get("product", "Plan")
        plan_details.append(f"{nickname} — {format_amount(amount, curr)}/{interval}")
        total_amount += amount
        currency = curr

    plan_summary = "\n".join(plan_details) if plan_details else "No plan details"

    customer_email = "N/A"
    if customer_id and customer_id != "unknown":
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer_email = customer.get("email", "N/A")
        except stripe.error.StripeError:
            pass

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "New Subscription",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Customer:*\n{customer_email}"},
                {"type": "mrkdwn", "text": f"*Status:*\n{status.title()}"},
                {"type": "mrkdwn", "text": f"*Plan:*\n{plan_summary}"},
                {
                    "type": "mrkdwn",
                    "text": f"*Subscription ID:*\n`{sub['id']}`",
                },
            ],
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"Received at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
                }
            ],
        },
    ]

    return send_slack_message(
        blocks,
        f"New subscription: {customer_email} subscribed to {plan_summary}",
    )


def handle_subscription_updated(event: dict) -> bool:
    """Handle customer.subscription.updated events — especially cancellations."""
    sub = event["data"]["object"]
    previous = event["data"].get("previous_attributes", {})
    customer_id = sub.get("customer", "unknown")

    customer_email = "N/A"
    if customer_id and customer_id != "unknown":
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer_email = customer.get("email", "N/A")
        except stripe.error.StripeError:
            pass

    # Detect cancellation
    if sub.get("cancel_at_period_end") and not previous.get("cancel_at_period_end"):
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Subscription Cancellation Scheduled",
                    "emoji": True,
                },
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Customer:*\n{customer_email}"},
                    {
                        "type": "mrkdwn",
                        "text": f"*Cancels At:*\n{datetime.fromtimestamp(sub.get('current_period_end', 0), tz=timezone.utc).strftime('%Y-%m-%d')}",
                    },
                    {"type": "mrkdwn", "text": f"*Subscription:*\n`{sub['id']}`"},
                ],
            },
        ]
        return send_slack_message(
            blocks,
            f"Subscription cancellation: {customer_email} will cancel at period end",
        )

    # Detect status change
    if "status" in previous:
        old_status = previous["status"]
        new_status = sub["status"]
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Subscription Status Changed",
                    "emoji": True,
                },
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Customer:*\n{customer_email}"},
                    {"type": "mrkdwn", "text": f"*Change:*\n{old_status} → {new_status}"},
                    {"type": "mrkdwn", "text": f"*Subscription:*\n`{sub['id']}`"},
                ],
            },
        ]
        return send_slack_message(
            blocks,
            f"Subscription update: {customer_email} changed from {old_status} to {new_status}",
        )

    logger.debug("Subscription updated but no notable changes detected for %s", sub["id"])
    return True


def handle_charge_refunded(event: dict) -> bool:
    """Handle charge.refunded events."""
    charge = event["data"]["object"]
    amount_refunded = format_amount(charge.get("amount_refunded", 0), charge.get("currency", "usd"))
    customer_id = charge.get("customer", "unknown")

    customer_email = "N/A"
    if customer_id and customer_id != "unknown":
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer_email = customer.get("email", "N/A")
        except stripe.error.StripeError:
            pass

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Refund Issued",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Refund Amount:*\n{amount_refunded}"},
                {"type": "mrkdwn", "text": f"*Customer:*\n{customer_email}"},
                {"type": "mrkdwn", "text": f"*Charge:*\n`{charge['id']}`"},
            ],
        },
    ]

    return send_slack_message(blocks, f"Refund issued: {amount_refunded} to {customer_email}")


# ---------------------------------------------------------------------------
# Event Dispatch
# ---------------------------------------------------------------------------

EVENT_HANDLERS = {
    "payment_intent.succeeded": handle_payment_succeeded,
    "payment_intent.payment_failed": handle_payment_failed,
    "customer.subscription.created": handle_subscription_created,
    "customer.subscription.updated": handle_subscription_updated,
    "charge.refunded": handle_charge_refunded,
}


# ---------------------------------------------------------------------------
# Webhook Endpoint
# ---------------------------------------------------------------------------


@app.route("/webhook/stripe", methods=["POST"])
def stripe_webhook():
    """
    Receive and process Stripe webhook events.

    Verifies the webhook signature using the Stripe library, dispatches to
    the appropriate handler, and returns a 200 to acknowledge receipt.
    """
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    if not sig_header:
        logger.warning("Received webhook without Stripe-Signature header")
        return jsonify({"error": "Missing signature"}), 400

    # Verify webhook signature
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        logger.error("Invalid webhook payload")
        return jsonify({"error": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError:
        logger.error("Invalid webhook signature")
        return jsonify({"error": "Invalid signature"}), 400

    event_type = event.get("type", "unknown")
    event_id = event.get("id", "unknown")
    logger.info("Received event: %s (%s)", event_type, event_id)

    # Dispatch to handler
    handler = EVENT_HANDLERS.get(event_type)
    if handler:
        try:
            success = handler(event)
            if not success:
                logger.warning(
                    "Handler for %s returned failure for event %s",
                    event_type,
                    event_id,
                )
        except Exception:
            logger.exception(
                "Unhandled error processing %s event %s", event_type, event_id
            )
            # Still return 200 so Stripe doesn't retry — we logged the error
            return jsonify({"status": "error", "event": event_id}), 200
    else:
        logger.debug("No handler registered for event type: %s", event_type)

    return jsonify({"status": "received", "event": event_id}), 200


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint for monitoring."""
    return jsonify({"status": "healthy", "service": "stripe-to-slack"}), 200


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    logger.info("Starting Stripe-to-Slack webhook listener on port %d", FLASK_PORT)
    logger.info("Listening for events: %s", ", ".join(EVENT_HANDLERS.keys()))

    app.run(
        host="0.0.0.0",
        port=FLASK_PORT,
        debug=(LOG_LEVEL == "DEBUG"),
    )
