#!/usr/bin/env python3
"""
Form Submission to CRM Router
===============================
Relay▸Launch Integration Cookbook

Receives form submissions via webhook, validates the data, enriches it with
additional context, and routes leads to the appropriate CRM pipeline based
on configurable business rules.

This is the glue between your website forms (Typeform, Gravity Forms,
Webflow, custom) and your CRM. Instead of dumping every lead into a single
pile, this script scores and routes them so your sales team sees the right
leads in the right pipeline.

Flow:
    1. Receive form submission via POST webhook
    2. Normalize and validate required fields
    3. Enrich with company data (optional, via Clearbit or similar)
    4. Score the lead based on business rules
    5. Route to the correct HubSpot pipeline and stage
    6. Return confirmation

Setup:
    1. Set environment variables (see below)
    2. Run the server: python form-to-crm-router.py
    3. Point your form's webhook to: https://your-server.com/webhook/form
    4. Configure routing rules in ROUTING_RULES below

Environment Variables:
    HUBSPOT_ACCESS_TOKEN    — HubSpot private app access token
    WEBHOOK_SECRET          — Shared secret for webhook signature verification (optional)
    FLASK_PORT              — Port to run the server on (optional, default: 5000)
    ENRICHMENT_API_KEY      — API key for lead enrichment service (optional)
    LOG_LEVEL               — Logging level (optional, default: INFO)

Expected Form Payload:
    {
        "email": "jane@example.com",
        "first_name": "Jane",
        "last_name": "Smith",
        "company": "Acme Corp",
        "phone": "+1-555-0100",
        "message": "Interested in automation consulting",
        "form_id": "contact-page",
        "budget_range": "$5k-$10k",
        "company_size": "11-50",
        "source": "google_ads"
    }
"""

import os
import sys
import re
import hmac
import hashlib
import json
import logging
from datetime import datetime, timezone
from typing import Any, Optional

import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

load_dotenv()

HUBSPOT_ACCESS_TOKEN = os.environ.get("HUBSPOT_ACCESS_TOKEN")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")
FLASK_PORT = int(os.environ.get("FLASK_PORT", 5000))
ENRICHMENT_API_KEY = os.environ.get("ENRICHMENT_API_KEY")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

if not HUBSPOT_ACCESS_TOKEN:
    print("ERROR: HUBSPOT_ACCESS_TOKEN is required")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("form-to-crm")

# ---------------------------------------------------------------------------
# Flask App
# ---------------------------------------------------------------------------

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Routing Rules
# ---------------------------------------------------------------------------

# Business rules that determine where a lead goes.
# Each rule is evaluated in order. The first match wins.
# Modify these to reflect your actual sales pipelines.

ROUTING_RULES = [
    {
        "name": "Enterprise",
        "description": "Large companies with big budgets go to enterprise pipeline",
        "conditions": {
            "company_size": ["201-500", "501-1000", "1000+"],
            "budget_range": ["$25k-$50k", "$50k-$100k", "$100k+"],
        },
        "match_mode": "any",  # "any" = OR, "all" = AND
        "pipeline_id": "enterprise",
        "stage": "qualification",
        "owner_email": None,  # Auto-assign based on round-robin
        "priority": "high",
    },
    {
        "name": "Mid-Market",
        "description": "Medium businesses or decent budget",
        "conditions": {
            "company_size": ["51-200", "201-500"],
            "budget_range": ["$10k-$25k", "$25k-$50k"],
        },
        "match_mode": "any",
        "pipeline_id": "mid-market",
        "stage": "qualification",
        "owner_email": None,
        "priority": "medium",
    },
    {
        "name": "SMB",
        "description": "Small businesses — default pipeline",
        "conditions": {
            "company_size": ["1-10", "11-50"],
            "budget_range": ["$1k-$5k", "$5k-$10k"],
        },
        "match_mode": "any",
        "pipeline_id": "smb",
        "stage": "new-lead",
        "owner_email": None,
        "priority": "normal",
    },
    {
        "name": "Inbound — General",
        "description": "Catch-all for leads that don't match other rules",
        "conditions": {},
        "match_mode": "any",
        "pipeline_id": "default",
        "stage": "new-lead",
        "owner_email": None,
        "priority": "normal",
    },
]

# Map form source values to HubSpot lifecycle stages
SOURCE_TO_LIFECYCLE = {
    "google_ads": "marketingqualifiedlead",
    "facebook_ads": "marketingqualifiedlead",
    "linkedin_ads": "marketingqualifiedlead",
    "organic": "lead",
    "referral": "salesqualifiedlead",
    "partner": "salesqualifiedlead",
    "direct": "lead",
    "email_campaign": "marketingqualifiedlead",
}

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$")

# Disposable email domains to reject
DISPOSABLE_DOMAINS = {
    "mailinator.com", "guerrillamail.com", "tempmail.com", "throwaway.email",
    "sharklasers.com", "guerrillamailblock.com", "grr.la", "dispostable.com",
    "yopmail.com", "trashmail.com", "10minutemail.com", "fakeinbox.com",
}


def validate_submission(data: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a form submission.

    Args:
        data: The form submission payload.

    Returns:
        Tuple of (is_valid, list_of_error_messages).
    """
    errors = []

    # Required fields
    email = data.get("email", "").strip()
    if not email:
        errors.append("Email is required")
    elif not EMAIL_REGEX.match(email):
        errors.append(f"Invalid email format: {email}")
    else:
        domain = email.split("@")[1].lower()
        if domain in DISPOSABLE_DOMAINS:
            errors.append(f"Disposable email addresses are not accepted: {domain}")

    first_name = data.get("first_name", "").strip()
    if not first_name:
        errors.append("First name is required")
    elif len(first_name) > 100:
        errors.append("First name is too long (max 100 characters)")

    last_name = data.get("last_name", "").strip()
    if not last_name:
        errors.append("Last name is required")

    # Optional but validate if present
    phone = data.get("phone", "").strip()
    if phone and len(phone) < 7:
        errors.append("Phone number appears invalid (too short)")

    return (len(errors) == 0, errors)


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------


def normalize_submission(data: dict[str, Any]) -> dict[str, Any]:
    """
    Clean and normalize form submission data.

    Args:
        data: Raw form submission payload.

    Returns:
        Normalized data dict.
    """
    normalized = {}

    # Strip whitespace from all string values
    for key, value in data.items():
        if isinstance(value, str):
            normalized[key] = value.strip()
        else:
            normalized[key] = value

    # Normalize email to lowercase
    if "email" in normalized:
        normalized["email"] = normalized["email"].lower()

    # Title-case names
    if "first_name" in normalized:
        normalized["first_name"] = normalized["first_name"].title()
    if "last_name" in normalized:
        normalized["last_name"] = normalized["last_name"].title()

    # Normalize phone — strip non-digit characters except leading +
    if "phone" in normalized and normalized["phone"]:
        phone = normalized["phone"]
        if phone.startswith("+"):
            normalized["phone"] = "+" + re.sub(r"[^\d]", "", phone[1:])
        else:
            normalized["phone"] = re.sub(r"[^\d]", "", phone)

    # Add metadata
    normalized["_received_at"] = datetime.now(timezone.utc).isoformat()
    normalized["_source_ip"] = request.remote_addr if request else "unknown"

    return normalized


# ---------------------------------------------------------------------------
# Enrichment
# ---------------------------------------------------------------------------


def enrich_lead(data: dict[str, Any]) -> dict[str, Any]:
    """
    Enrich lead data with company information from an external service.

    Uses Clearbit-style enrichment if an API key is configured. Falls back
    gracefully if enrichment is unavailable or fails.

    Args:
        data: Normalized form submission data.

    Returns:
        Data dict with enrichment fields added.
    """
    if not ENRICHMENT_API_KEY:
        logger.debug("No enrichment API key configured — skipping enrichment")
        return data

    email = data.get("email", "")
    if not email:
        return data

    try:
        resp = requests.get(
            "https://company.clearbit.com/v2/companies/find",
            params={"domain": email.split("@")[1]},
            headers={"Authorization": f"Bearer {ENRICHMENT_API_KEY}"},
            timeout=5,
        )

        if resp.status_code == 200:
            company_data = resp.json()
            data["_enrichment"] = {
                "company_name": company_data.get("name"),
                "industry": company_data.get("category", {}).get("industry"),
                "employee_count": company_data.get("metrics", {}).get("employees"),
                "annual_revenue": company_data.get("metrics", {}).get("estimatedAnnualRevenue"),
                "country": company_data.get("geo", {}).get("country"),
                "description": company_data.get("description"),
            }
            logger.info("Enrichment successful for %s", email.split("@")[1])
        elif resp.status_code == 404:
            logger.debug("No enrichment data found for %s", email.split("@")[1])
        else:
            logger.warning("Enrichment API returned %d", resp.status_code)

    except requests.RequestException as exc:
        logger.warning("Enrichment request failed: %s", exc)

    return data


# ---------------------------------------------------------------------------
# Lead Scoring & Routing
# ---------------------------------------------------------------------------


def score_lead(data: dict[str, Any]) -> int:
    """
    Calculate a simple lead score based on available data.

    Scoring rubric (0–100):
        - Has company name: +15
        - Has phone number: +10
        - Has budget range: +20
        - Has company size: +15
        - Paid source (ads): +10
        - Referral/partner source: +20
        - Has message/description: +10
        - Enrichment data available: +10

    Args:
        data: Normalized and enriched form submission.

    Returns:
        Integer score between 0 and 100.
    """
    score = 0

    if data.get("company"):
        score += 15
    if data.get("phone"):
        score += 10
    if data.get("budget_range"):
        score += 20
    if data.get("company_size"):
        score += 15

    source = data.get("source", "").lower()
    if source in ("referral", "partner"):
        score += 20
    elif source in ("google_ads", "facebook_ads", "linkedin_ads"):
        score += 10

    if data.get("message"):
        score += 10
    if data.get("_enrichment"):
        score += 10

    return min(score, 100)


def route_lead(data: dict[str, Any]) -> dict[str, Any]:
    """
    Determine the correct CRM pipeline and stage based on routing rules.

    Evaluates rules in order. The first matching rule wins.

    Args:
        data: Normalized, enriched, and scored form submission.

    Returns:
        The matching routing rule dict.
    """
    for rule in ROUTING_RULES:
        conditions = rule.get("conditions", {})

        if not conditions:
            # Catch-all rule — always matches
            logger.info("Lead routed to catch-all rule: %s", rule["name"])
            return rule

        match_mode = rule.get("match_mode", "any")
        matches = []

        for field, accepted_values in conditions.items():
            field_value = data.get(field, "")
            matches.append(field_value in accepted_values)

        if match_mode == "all" and all(matches):
            logger.info("Lead routed to rule: %s (all conditions matched)", rule["name"])
            return rule
        elif match_mode == "any" and any(matches):
            logger.info("Lead routed to rule: %s (at least one condition matched)", rule["name"])
            return rule

    # Should never reach here if catch-all rule exists
    logger.warning("No routing rule matched — using defaults")
    return ROUTING_RULES[-1]


# ---------------------------------------------------------------------------
# HubSpot CRM Integration
# ---------------------------------------------------------------------------

HUBSPOT_API_BASE = "https://api.hubapi.com"


def find_existing_contact(email: str) -> Optional[str]:
    """
    Search HubSpot for an existing contact by email.

    Args:
        email: Contact email address.

    Returns:
        HubSpot contact ID if found, None otherwise.
    """
    headers = {
        "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "filterGroups": [
            {
                "filters": [
                    {
                        "propertyName": "email",
                        "operator": "EQ",
                        "value": email,
                    }
                ]
            }
        ],
        "properties": ["email", "firstname", "lastname"],
        "limit": 1,
    }

    try:
        resp = requests.post(
            f"{HUBSPOT_API_BASE}/crm/v3/objects/contacts/search",
            headers=headers,
            json=payload,
            timeout=10,
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
        if results:
            return results[0]["id"]
    except requests.RequestException as exc:
        logger.error("HubSpot contact search failed: %s", exc)

    return None


def create_or_update_hubspot_contact(
    data: dict[str, Any],
    routing: dict[str, Any],
    lead_score: int,
) -> Optional[str]:
    """
    Create or update a contact in HubSpot with the routed pipeline info.

    Args:
        data: Normalized and enriched form data.
        routing: The matched routing rule.
        lead_score: Calculated lead score.

    Returns:
        HubSpot contact ID on success, None on failure.
    """
    headers = {
        "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    # Map form data to HubSpot properties
    properties = {
        "email": data.get("email", ""),
        "firstname": data.get("first_name", ""),
        "lastname": data.get("last_name", ""),
        "company": data.get("company", ""),
        "phone": data.get("phone", ""),
        "jobtitle": data.get("job_title", ""),
        "hs_lead_status": routing.get("stage", "new-lead"),
        "lifecyclestage": SOURCE_TO_LIFECYCLE.get(
            data.get("source", "").lower(), "lead"
        ),
    }

    # Add custom properties if available
    if data.get("message"):
        properties["message"] = data["message"]

    if data.get("budget_range"):
        properties["budget_range"] = data["budget_range"]

    # Add enrichment data
    enrichment = data.get("_enrichment", {})
    if enrichment.get("industry"):
        properties["industry"] = enrichment["industry"]

    # Add lead score and routing metadata as a note
    note_body = (
        f"Lead Score: {lead_score}/100\n"
        f"Pipeline: {routing['name']}\n"
        f"Priority: {routing['priority']}\n"
        f"Source: {data.get('source', 'unknown')}\n"
        f"Form: {data.get('form_id', 'unknown')}\n"
        f"Received: {data.get('_received_at', '')}"
    )

    # Check if contact exists
    existing_id = find_existing_contact(data.get("email", ""))

    try:
        if existing_id:
            # Update existing contact
            resp = requests.patch(
                f"{HUBSPOT_API_BASE}/crm/v3/objects/contacts/{existing_id}",
                headers=headers,
                json={"properties": properties},
                timeout=10,
            )
            resp.raise_for_status()
            contact_id = existing_id
            logger.info("Updated existing HubSpot contact: %s", contact_id)
        else:
            # Create new contact
            resp = requests.post(
                f"{HUBSPOT_API_BASE}/crm/v3/objects/contacts",
                headers=headers,
                json={"properties": properties},
                timeout=10,
            )
            resp.raise_for_status()
            contact_id = resp.json()["id"]
            logger.info("Created new HubSpot contact: %s", contact_id)

        # Create an engagement note with routing details
        _create_note(contact_id, note_body, headers)

        return contact_id

    except requests.RequestException as exc:
        logger.error("HubSpot contact creation/update failed: %s", exc)
        if hasattr(exc, "response") and exc.response is not None:
            logger.error("Response: %s", exc.response.text[:500])
        return None


def _create_note(contact_id: str, body: str, headers: dict) -> None:
    """Create an engagement note on a HubSpot contact."""
    try:
        note_payload = {
            "properties": {
                "hs_timestamp": datetime.now(timezone.utc).isoformat(),
                "hs_note_body": body,
            },
            "associations": [
                {
                    "to": {"id": contact_id},
                    "types": [
                        {
                            "associationCategory": "HUBSPOT_DEFINED",
                            "associationTypeId": 202,  # note to contact
                        }
                    ],
                }
            ],
        }
        resp = requests.post(
            f"{HUBSPOT_API_BASE}/crm/v3/objects/notes",
            headers=headers,
            json=note_payload,
            timeout=10,
        )
        resp.raise_for_status()
        logger.debug("Created note on contact %s", contact_id)
    except requests.RequestException as exc:
        logger.warning("Failed to create note on contact %s: %s", contact_id, exc)


# ---------------------------------------------------------------------------
# Webhook Endpoint
# ---------------------------------------------------------------------------


def verify_webhook_signature(payload: bytes, signature: str) -> bool:
    """
    Verify the webhook signature using HMAC-SHA256.

    Args:
        payload: Raw request body bytes.
        signature: The signature from the request header.

    Returns:
        True if the signature is valid or no secret is configured.
    """
    if not WEBHOOK_SECRET:
        return True

    expected = hmac.new(
        WEBHOOK_SECRET.encode("utf-8"),
        payload,
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(f"sha256={expected}", signature)


@app.route("/webhook/form", methods=["POST"])
def form_webhook():
    """
    Receive and process form submissions.

    Accepts JSON or form-encoded POST data. Validates, enriches, scores,
    routes, and creates/updates the contact in HubSpot.
    """
    # Verify signature if configured
    if WEBHOOK_SECRET:
        signature = request.headers.get("X-Webhook-Signature", "")
        if not verify_webhook_signature(request.get_data(), signature):
            logger.warning("Invalid webhook signature from %s", request.remote_addr)
            return jsonify({"error": "Invalid signature"}), 401

    # Parse payload
    if request.is_json:
        data = request.get_json(silent=True) or {}
    else:
        data = request.form.to_dict()

    if not data:
        return jsonify({"error": "Empty or invalid payload"}), 400

    logger.info(
        "Received form submission from %s (form_id: %s)",
        data.get("email", "unknown"),
        data.get("form_id", "unknown"),
    )

    # Step 1: Normalize
    data = normalize_submission(data)

    # Step 2: Validate
    is_valid, errors = validate_submission(data)
    if not is_valid:
        logger.warning("Validation failed: %s", errors)
        return jsonify({"error": "Validation failed", "details": errors}), 422

    # Step 3: Enrich
    data = enrich_lead(data)

    # Step 4: Score
    lead_score = score_lead(data)
    logger.info("Lead score for %s: %d/100", data["email"], lead_score)

    # Step 5: Route
    routing = route_lead(data)

    # Step 6: Create/update in CRM
    contact_id = create_or_update_hubspot_contact(data, routing, lead_score)

    if contact_id:
        return jsonify({
            "status": "success",
            "contact_id": contact_id,
            "pipeline": routing["name"],
            "priority": routing["priority"],
            "lead_score": lead_score,
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Failed to create/update CRM contact. The submission was logged.",
        }), 502


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "form-to-crm-router",
        "rules_count": len(ROUTING_RULES),
    }), 200


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    logger.info("Starting Form-to-CRM Router on port %d", FLASK_PORT)
    logger.info("Loaded %d routing rules", len(ROUTING_RULES))
    for rule in ROUTING_RULES:
        logger.info("  Rule: %s — %s", rule["name"], rule["description"])

    app.run(
        host="0.0.0.0",
        port=FLASK_PORT,
        debug=(LOG_LEVEL == "DEBUG"),
    )
