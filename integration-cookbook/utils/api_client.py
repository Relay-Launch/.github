#!/usr/bin/env python3
"""
Reusable API Client
====================
Relay▸Launch Integration Cookbook

A production-ready base HTTP client class with:
    - Automatic retries with exponential backoff
    - Rate limiting (token bucket algorithm)
    - Response caching (TTL-based, in-memory)
    - Structured logging
    - Timeout configuration
    - Authentication helpers (API key, Bearer token, Basic auth)

Designed to be subclassed for any REST API. The base class handles the
plumbing so your API-specific code can focus on business logic.

Usage:
    # Direct usage
    client = APIClient(
        base_url="https://api.example.com/v1",
        auth_token="your-api-key",
        rate_limit=10,  # max 10 requests per second
    )
    response = client.get("/users", params={"page": 1})

    # Subclassed for a specific API
    class StripeClient(APIClient):
        def __init__(self, api_key):
            super().__init__(
                base_url="https://api.stripe.com/v1",
                auth_token=api_key,
                auth_scheme="basic",
                rate_limit=25,
            )

        def list_customers(self, limit=100):
            return self.get("/customers", params={"limit": limit})

        def create_customer(self, email, name):
            return self.post("/customers", data={"email": email, "name": name})
"""

import os
import time
import json
import hashlib
import logging
import threading
from datetime import datetime, timezone
from typing import Any, Optional
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logger = logging.getLogger("api-client")


# ---------------------------------------------------------------------------
# Rate Limiter (Token Bucket)
# ---------------------------------------------------------------------------


class TokenBucketRateLimiter:
    """
    Thread-safe token bucket rate limiter.

    Allows bursts up to the bucket size while maintaining a steady
    average rate over time. This is the same algorithm used by most
    API providers to enforce their rate limits.
    """

    def __init__(self, rate: float, burst: Optional[int] = None):
        """
        Args:
            rate: Maximum sustained requests per second.
            burst: Maximum burst size (defaults to rate).
        """
        self.rate = rate
        self.burst = burst or int(rate)
        self.tokens = float(self.burst)
        self.last_refill = time.monotonic()
        self._lock = threading.Lock()

    def acquire(self, timeout: float = 30.0) -> bool:
        """
        Acquire a token, blocking until one is available or timeout.

        Args:
            timeout: Maximum seconds to wait for a token.

        Returns:
            True if a token was acquired, False if timed out.
        """
        deadline = time.monotonic() + timeout

        while True:
            with self._lock:
                self._refill()
                if self.tokens >= 1:
                    self.tokens -= 1
                    return True

            # Wait a bit before trying again
            if time.monotonic() >= deadline:
                return False

            # Sleep for the expected time until next token
            sleep_time = min(1.0 / self.rate, deadline - time.monotonic())
            if sleep_time > 0:
                time.sleep(sleep_time)

    def _refill(self) -> None:
        """Add tokens based on elapsed time."""
        now = time.monotonic()
        elapsed = now - self.last_refill
        self.tokens = min(self.burst, self.tokens + elapsed * self.rate)
        self.last_refill = now


# ---------------------------------------------------------------------------
# Response Cache
# ---------------------------------------------------------------------------


class ResponseCache:
    """
    Thread-safe, TTL-based in-memory response cache.

    Caches GET responses keyed by URL + params. Automatically evicts
    expired entries. For production multi-process deployments, replace
    with Redis.
    """

    def __init__(self, default_ttl: int = 300, max_size: int = 1000):
        """
        Args:
            default_ttl: Default cache TTL in seconds (default: 5 minutes).
            max_size: Maximum number of cached responses.
        """
        self.default_ttl = default_ttl
        self.max_size = max_size
        self._cache: dict[str, dict[str, Any]] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a cached response.

        Args:
            key: Cache key.

        Returns:
            Cached response data, or None if not found or expired.
        """
        with self._lock:
            entry = self._cache.get(key)
            if entry is None:
                return None

            if time.time() > entry["expires_at"]:
                del self._cache[key]
                return None

            entry["hits"] += 1
            return entry["data"]

    def set(self, key: str, data: Any, ttl: Optional[int] = None) -> None:
        """
        Store a response in the cache.

        Args:
            key: Cache key.
            data: Response data to cache.
            ttl: Cache TTL in seconds (uses default if not specified).
        """
        with self._lock:
            # Evict if at capacity
            if len(self._cache) >= self.max_size:
                self._evict()

            self._cache[key] = {
                "data": data,
                "expires_at": time.time() + (ttl or self.default_ttl),
                "created_at": time.time(),
                "hits": 0,
            }

    def invalidate(self, key: str) -> None:
        """Remove a specific entry from the cache."""
        with self._lock:
            self._cache.pop(key, None)

    def clear(self) -> None:
        """Clear all cached entries."""
        with self._lock:
            self._cache.clear()

    def _evict(self) -> None:
        """Evict expired entries, then oldest if still over capacity."""
        now = time.time()

        # Remove expired
        expired = [k for k, v in self._cache.items() if v["expires_at"] < now]
        for k in expired:
            del self._cache[k]

        # If still over capacity, remove least recently accessed
        if len(self._cache) >= self.max_size:
            sorted_keys = sorted(
                self._cache.keys(),
                key=lambda k: self._cache[k]["created_at"],
            )
            to_remove = len(self._cache) - self.max_size + 1
            for k in sorted_keys[:to_remove]:
                del self._cache[k]

    @property
    def stats(self) -> dict[str, int]:
        """Return cache statistics."""
        with self._lock:
            total_hits = sum(e["hits"] for e in self._cache.values())
            return {
                "size": len(self._cache),
                "max_size": self.max_size,
                "total_hits": total_hits,
            }


# ---------------------------------------------------------------------------
# API Client
# ---------------------------------------------------------------------------


class APIClient:
    """
    A reusable, production-ready REST API client.

    Handles authentication, retries, rate limiting, caching, and logging
    so subclasses can focus on API-specific business logic.

    Attributes:
        base_url: The API's base URL.
        session: The underlying requests.Session with retry adapter.
    """

    def __init__(
        self,
        base_url: str,
        auth_token: Optional[str] = None,
        auth_scheme: str = "bearer",
        auth_header: str = "Authorization",
        rate_limit: Optional[float] = None,
        rate_burst: Optional[int] = None,
        cache_ttl: int = 300,
        cache_enabled: bool = True,
        max_retries: int = 3,
        retry_backoff_factor: float = 0.5,
        retry_status_codes: Optional[list[int]] = None,
        timeout: int = 30,
        default_headers: Optional[dict[str, str]] = None,
        log_level: str = "INFO",
    ):
        """
        Args:
            base_url: API base URL (e.g., "https://api.example.com/v1").
            auth_token: Authentication token or API key.
            auth_scheme: Auth scheme — "bearer", "basic", "api-key", or "none".
            auth_header: Header name for auth (default: "Authorization").
            rate_limit: Max requests per second (None = no limit).
            rate_burst: Max burst size for rate limiter.
            cache_ttl: Default cache TTL in seconds.
            cache_enabled: Whether to cache GET responses.
            max_retries: Number of retry attempts for failed requests.
            retry_backoff_factor: Backoff multiplier between retries.
            retry_status_codes: HTTP status codes that trigger retries.
            timeout: Default request timeout in seconds.
            default_headers: Additional headers to include with every request.
            log_level: Logging level.
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.cache_enabled = cache_enabled

        # Configure logging
        logging.basicConfig(
            level=getattr(logging, log_level.upper(), logging.INFO),
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        )

        # Set up session with retry adapter
        self.session = requests.Session()

        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=retry_backoff_factor,
            status_forcelist=retry_status_codes or [429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Default headers
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "RelayLaunch-IntegrationCookbook/1.0",
        })

        if default_headers:
            self.session.headers.update(default_headers)

        # Authentication
        self._configure_auth(auth_token, auth_scheme, auth_header)

        # Rate limiter
        self.rate_limiter = (
            TokenBucketRateLimiter(rate=rate_limit, burst=rate_burst)
            if rate_limit
            else None
        )

        # Response cache
        self.cache = ResponseCache(default_ttl=cache_ttl) if cache_enabled else None

        # Request counter for logging
        self._request_count = 0

        logger.info(
            "APIClient initialized: base_url=%s, rate_limit=%s/s, cache=%s, retries=%d",
            self.base_url,
            rate_limit or "unlimited",
            "enabled" if cache_enabled else "disabled",
            max_retries,
        )

    def _configure_auth(
        self,
        token: Optional[str],
        scheme: str,
        header: str,
    ) -> None:
        """Configure authentication on the session."""
        if not token:
            return

        scheme = scheme.lower()

        if scheme == "bearer":
            self.session.headers[header] = f"Bearer {token}"
        elif scheme == "basic":
            # Token is used as username with empty password (Stripe-style)
            self.session.auth = (token, "")
        elif scheme == "api-key":
            self.session.headers[header] = token
        elif scheme == "none":
            pass
        else:
            raise ValueError(f"Unknown auth scheme: {scheme}")

    # -------------------------------------------------------------------
    # Cache Key Generation
    # -------------------------------------------------------------------

    @staticmethod
    def _cache_key(method: str, url: str, params: Optional[dict] = None) -> str:
        """Generate a deterministic cache key from request parameters."""
        key_data = f"{method}:{url}:{json.dumps(params or {}, sort_keys=True)}"
        return hashlib.sha256(key_data.encode()).hexdigest()

    # -------------------------------------------------------------------
    # Core Request Method
    # -------------------------------------------------------------------

    def request(
        self,
        method: str,
        path: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json_body: Optional[dict] = None,
        headers: Optional[dict] = None,
        timeout: Optional[int] = None,
        cache_ttl: Optional[int] = None,
        skip_cache: bool = False,
    ) -> requests.Response:
        """
        Send an HTTP request with rate limiting, caching, and logging.

        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE).
            path: URL path relative to base_url (e.g., "/users").
            params: Query string parameters.
            data: Form-encoded body data.
            json_body: JSON body data.
            headers: Additional headers for this request.
            timeout: Request timeout override.
            cache_ttl: Cache TTL override for this request.
            skip_cache: Skip cache for this request.

        Returns:
            requests.Response object.

        Raises:
            requests.RequestException: On network errors after retries.
            TimeoutError: If rate limiter times out.
        """
        url = f"{self.base_url}/{path.lstrip('/')}" if path else self.base_url
        method = method.upper()
        self._request_count += 1
        request_num = self._request_count

        # Check cache for GET requests
        if method == "GET" and self.cache_enabled and self.cache and not skip_cache:
            cache_key = self._cache_key(method, url, params)
            cached = self.cache.get(cache_key)
            if cached is not None:
                logger.debug("[#%d] Cache hit: %s %s", request_num, method, url)
                return cached

        # Rate limiting
        if self.rate_limiter:
            if not self.rate_limiter.acquire(timeout=30):
                raise TimeoutError(
                    f"Rate limiter timed out waiting for token: {method} {url}"
                )

        # Send request
        start_time = time.time()
        logger.debug("[#%d] %s %s", request_num, method, url)

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json_body,
                headers=headers,
                timeout=timeout or self.timeout,
            )

            elapsed = time.time() - start_time
            logger.info(
                "[#%d] %s %s → %d (%.2fs)",
                request_num,
                method,
                url,
                response.status_code,
                elapsed,
            )

            # Handle rate limit headers (common across many APIs)
            remaining = response.headers.get("X-RateLimit-Remaining")
            if remaining is not None:
                logger.debug(
                    "[#%d] Rate limit remaining: %s", request_num, remaining
                )
                if int(remaining) < 5:
                    logger.warning(
                        "[#%d] Rate limit nearly exhausted: %s remaining",
                        request_num,
                        remaining,
                    )

            # Cache successful GET responses
            if (
                method == "GET"
                and self.cache_enabled
                and self.cache
                and not skip_cache
                and 200 <= response.status_code < 300
            ):
                cache_key = self._cache_key(method, url, params)
                self.cache.set(cache_key, response, ttl=cache_ttl)

            return response

        except requests.RequestException as exc:
            elapsed = time.time() - start_time
            logger.error(
                "[#%d] %s %s failed after %.2fs: %s",
                request_num,
                method,
                url,
                elapsed,
                exc,
            )
            raise

    # -------------------------------------------------------------------
    # Convenience Methods
    # -------------------------------------------------------------------

    def get(self, path: str, params: Optional[dict] = None, **kwargs) -> requests.Response:
        """Send a GET request."""
        return self.request("GET", path, params=params, **kwargs)

    def post(
        self,
        path: str,
        data: Optional[dict] = None,
        json_body: Optional[dict] = None,
        **kwargs,
    ) -> requests.Response:
        """Send a POST request."""
        return self.request("POST", path, data=data, json_body=json_body, **kwargs)

    def put(
        self,
        path: str,
        data: Optional[dict] = None,
        json_body: Optional[dict] = None,
        **kwargs,
    ) -> requests.Response:
        """Send a PUT request."""
        return self.request("PUT", path, data=data, json_body=json_body, **kwargs)

    def patch(
        self,
        path: str,
        data: Optional[dict] = None,
        json_body: Optional[dict] = None,
        **kwargs,
    ) -> requests.Response:
        """Send a PATCH request."""
        return self.request("PATCH", path, data=data, json_body=json_body, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        """Send a DELETE request."""
        return self.request("DELETE", path, **kwargs)

    # -------------------------------------------------------------------
    # JSON Helpers
    # -------------------------------------------------------------------

    def get_json(self, path: str, params: Optional[dict] = None, **kwargs) -> Any:
        """GET and return parsed JSON response."""
        resp = self.get(path, params=params, **kwargs)
        resp.raise_for_status()
        return resp.json()

    def post_json(self, path: str, json_body: dict, **kwargs) -> Any:
        """POST JSON and return parsed JSON response."""
        resp = self.post(path, json_body=json_body, **kwargs)
        resp.raise_for_status()
        return resp.json()

    # -------------------------------------------------------------------
    # Pagination Helpers
    # -------------------------------------------------------------------

    def paginate(
        self,
        path: str,
        params: Optional[dict] = None,
        results_key: str = "results",
        next_key: str = "next",
        page_param: str = "page",
        limit_param: str = "limit",
        limit: int = 100,
        max_pages: int = 100,
    ) -> list[Any]:
        """
        Automatically paginate through a list endpoint.

        Supports two pagination styles:
            1. Cursor-based: Follows a "next" URL or cursor in the response
            2. Offset-based: Increments a page parameter

        Args:
            path: API endpoint path.
            params: Base query parameters.
            results_key: JSON key containing the results array.
            next_key: JSON key containing the next page URL/cursor.
            page_param: Query parameter name for page number.
            limit_param: Query parameter name for page size.
            limit: Number of results per page.
            max_pages: Safety limit on number of pages to fetch.

        Returns:
            Flattened list of all results across all pages.
        """
        all_results = []
        params = dict(params or {})
        params[limit_param] = limit
        current_page = 1

        while current_page <= max_pages:
            params[page_param] = current_page
            resp = self.get(path, params=params, skip_cache=True)
            resp.raise_for_status()
            data = resp.json()

            results = data.get(results_key, [])
            if not results:
                break

            all_results.extend(results)
            logger.info(
                "Paginate %s: page %d, got %d items (total: %d)",
                path,
                current_page,
                len(results),
                len(all_results),
            )

            # Check for next page
            next_value = data.get(next_key)
            if not next_value:
                break

            # If next_value is a URL, we could follow it directly,
            # but for simplicity we just increment the page
            current_page += 1

        return all_results

    # -------------------------------------------------------------------
    # Lifecycle
    # -------------------------------------------------------------------

    def close(self) -> None:
        """Close the underlying session and clean up resources."""
        self.session.close()
        if self.cache:
            self.cache.clear()
        logger.info("APIClient closed (total requests: %d)", self._request_count)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def __repr__(self) -> str:
        return (
            f"APIClient(base_url='{self.base_url}', "
            f"requests={self._request_count}, "
            f"cache={'on' if self.cache_enabled else 'off'})"
        )


# ---------------------------------------------------------------------------
# Example Subclass
# ---------------------------------------------------------------------------


class HubSpotClient(APIClient):
    """
    Example: HubSpot API client built on APIClient.

    Demonstrates how to subclass for a specific API with custom methods,
    pagination handling, and domain-specific error handling.
    """

    def __init__(self, access_token: str):
        super().__init__(
            base_url="https://api.hubapi.com",
            auth_token=access_token,
            auth_scheme="bearer",
            rate_limit=9,  # HubSpot free tier: 10 req/sec with safety margin
            cache_ttl=60,
            max_retries=3,
        )

    def list_contacts(self, limit: int = 100, properties: Optional[list[str]] = None) -> list[dict]:
        """List all contacts with pagination."""
        params = {"limit": min(limit, 100)}
        if properties:
            params["properties"] = ",".join(properties)

        all_contacts = []
        after = None

        while True:
            if after:
                params["after"] = after

            data = self.get_json("/crm/v3/objects/contacts", params=params)
            all_contacts.extend(data.get("results", []))

            after = data.get("paging", {}).get("next", {}).get("after")
            if not after:
                break

        return all_contacts

    def get_contact(self, contact_id: str) -> dict:
        """Get a single contact by ID."""
        return self.get_json(f"/crm/v3/objects/contacts/{contact_id}")

    def create_contact(self, properties: dict) -> dict:
        """Create a new contact."""
        return self.post_json(
            "/crm/v3/objects/contacts",
            json_body={"properties": properties},
        )


# ---------------------------------------------------------------------------
# Standalone Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    # Demo with a public API (no auth required)
    with APIClient(
        base_url="https://jsonplaceholder.typicode.com",
        rate_limit=5,
        cache_ttl=60,
    ) as client:
        # Fetch a single resource
        resp = client.get("/posts/1")
        print(f"Status: {resp.status_code}")
        print(f"Data: {json.dumps(resp.json(), indent=2)[:200]}...")

        # Fetch again — should be cached
        resp2 = client.get("/posts/1")
        print(f"\nCached request status: {resp2.status_code}")

        # Show cache stats
        if client.cache:
            print(f"Cache stats: {client.cache.stats}")
