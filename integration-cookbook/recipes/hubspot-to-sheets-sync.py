#!/usr/bin/env python3
"""
HubSpot CRM to Google Sheets Sync
===================================
Relay▸Launch Integration Cookbook

Syncs HubSpot CRM contacts to a Google Sheet on a schedule. Handles pagination,
field mapping, and update-or-create logic so your spreadsheet always reflects
the current state of your CRM.

Design:
    - Fetches all contacts from HubSpot (with pagination)
    - Maps HubSpot properties to spreadsheet columns
    - Updates existing rows (matched by email) or appends new ones
    - Preserves any manual columns you've added to the right side of the sheet
    - Logs every action for auditability

Setup:
    1. Create a HubSpot private app with "crm.objects.contacts.read" scope
    2. Create a Google Cloud service account and share your Google Sheet with it
    3. Set environment variables (see below)
    4. Run manually or on a cron schedule

Environment Variables:
    HUBSPOT_ACCESS_TOKEN            — HubSpot private app access token
    GOOGLE_SHEETS_CREDENTIALS_FILE  — Path to Google service account JSON
    GOOGLE_SHEET_ID                 — Google Sheet ID (from the URL)
    GOOGLE_SHEET_TAB_NAME           — Tab/worksheet name (optional, default: "Contacts")
    HUBSPOT_BATCH_SIZE              — Contacts per API page (optional, default: 100, max: 100)
    LOG_LEVEL                       — Logging level (optional, default: INFO)

Cron Example (every 30 minutes):
    */30 * * * * cd /path/to/integration-cookbook && /path/to/venv/bin/python recipes/hubspot-to-sheets-sync.py >> /var/log/hubspot-sync.log 2>&1
"""

import os
import sys
import json
import logging
from datetime import datetime, timezone
from typing import Any

import requests
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

load_dotenv()

HUBSPOT_ACCESS_TOKEN = os.environ.get("HUBSPOT_ACCESS_TOKEN")
GOOGLE_SHEETS_CREDENTIALS_FILE = os.environ.get("GOOGLE_SHEETS_CREDENTIALS_FILE", "credentials.json")
GOOGLE_SHEET_ID = os.environ.get("GOOGLE_SHEET_ID")
GOOGLE_SHEET_TAB_NAME = os.environ.get("GOOGLE_SHEET_TAB_NAME", "Contacts")
HUBSPOT_BATCH_SIZE = min(int(os.environ.get("HUBSPOT_BATCH_SIZE", 100)), 100)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

_missing = []
if not HUBSPOT_ACCESS_TOKEN:
    _missing.append("HUBSPOT_ACCESS_TOKEN")
if not GOOGLE_SHEET_ID:
    _missing.append("GOOGLE_SHEET_ID")
if not os.path.exists(GOOGLE_SHEETS_CREDENTIALS_FILE):
    _missing.append(f"GOOGLE_SHEETS_CREDENTIALS_FILE (file not found: {GOOGLE_SHEETS_CREDENTIALS_FILE})")

if _missing:
    print(f"ERROR: Missing required configuration: {', '.join(_missing)}")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("hubspot-to-sheets")

# ---------------------------------------------------------------------------
# Field Mapping
# ---------------------------------------------------------------------------

# Maps HubSpot contact properties to spreadsheet column headers.
# Modify this to include whichever HubSpot properties matter to your business.
FIELD_MAP = {
    "email": "Email",
    "firstname": "First Name",
    "lastname": "Last Name",
    "company": "Company",
    "phone": "Phone",
    "jobtitle": "Job Title",
    "lifecyclestage": "Lifecycle Stage",
    "hs_lead_status": "Lead Status",
    "createdate": "Created Date",
    "lastmodifieddate": "Last Modified",
    "hubspot_owner_id": "Owner ID",
}

# The HubSpot property names we need to request
HUBSPOT_PROPERTIES = list(FIELD_MAP.keys())

# Spreadsheet column headers in order
SHEET_HEADERS = ["HubSpot ID"] + [FIELD_MAP[prop] for prop in HUBSPOT_PROPERTIES] + ["Last Synced"]


# ---------------------------------------------------------------------------
# HubSpot API Client
# ---------------------------------------------------------------------------

HUBSPOT_API_BASE = "https://api.hubapi.com"


def fetch_all_hubspot_contacts() -> list[dict[str, Any]]:
    """
    Fetch all contacts from HubSpot CRM with full pagination.

    Returns:
        List of contact dicts, each containing 'id' and 'properties'.
    """
    contacts = []
    after = None
    page = 0

    headers = {
        "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    while True:
        page += 1
        params = {
            "limit": HUBSPOT_BATCH_SIZE,
            "properties": ",".join(HUBSPOT_PROPERTIES),
        }
        if after:
            params["after"] = after

        logger.info("Fetching HubSpot contacts page %d (after=%s)", page, after or "start")

        try:
            resp = requests.get(
                f"{HUBSPOT_API_BASE}/crm/v3/objects/contacts",
                headers=headers,
                params=params,
                timeout=30,
            )
            resp.raise_for_status()
        except requests.RequestException as exc:
            logger.error("HubSpot API request failed on page %d: %s", page, exc)
            if hasattr(exc, "response") and exc.response is not None:
                logger.error("Response body: %s", exc.response.text[:500])
            raise

        data = resp.json()
        results = data.get("results", [])
        contacts.extend(results)
        logger.info("Fetched %d contacts on page %d (total so far: %d)", len(results), page, len(contacts))

        # Check for next page
        paging = data.get("paging", {})
        next_link = paging.get("next", {})
        after = next_link.get("after")

        if not after:
            break

    logger.info("Finished fetching all HubSpot contacts: %d total", len(contacts))
    return contacts


# ---------------------------------------------------------------------------
# Google Sheets Client
# ---------------------------------------------------------------------------


def get_google_sheet() -> gspread.Worksheet:
    """
    Authenticate and return the target Google Sheets worksheet.

    Returns:
        gspread Worksheet object.
    """
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials = Credentials.from_service_account_file(
        GOOGLE_SHEETS_CREDENTIALS_FILE,
        scopes=scopes,
    )

    gc = gspread.authorize(credentials)
    spreadsheet = gc.open_by_key(GOOGLE_SHEET_ID)

    # Get or create the target worksheet
    try:
        worksheet = spreadsheet.worksheet(GOOGLE_SHEET_TAB_NAME)
    except gspread.exceptions.WorksheetNotFound:
        logger.info("Worksheet '%s' not found — creating it", GOOGLE_SHEET_TAB_NAME)
        worksheet = spreadsheet.add_worksheet(
            title=GOOGLE_SHEET_TAB_NAME,
            rows=1000,
            cols=len(SHEET_HEADERS),
        )

    return worksheet


def ensure_headers(worksheet: gspread.Worksheet) -> None:
    """
    Ensure the first row contains the expected column headers.
    Creates them if the sheet is empty; validates them if they exist.
    """
    existing = worksheet.row_values(1)

    if not existing:
        logger.info("Writing headers to empty sheet")
        worksheet.update("A1", [SHEET_HEADERS])
        worksheet.format("A1:Z1", {
            "textFormat": {"bold": True},
            "backgroundColor": {"red": 0.9, "green": 0.9, "blue": 0.95},
        })
        return

    # Check if headers match
    if existing[:len(SHEET_HEADERS)] != SHEET_HEADERS:
        logger.warning(
            "Sheet headers don't match expected headers. "
            "Expected: %s, Found: %s. Updating headers.",
            SHEET_HEADERS,
            existing[:len(SHEET_HEADERS)],
        )
        worksheet.update("A1", [SHEET_HEADERS])


# ---------------------------------------------------------------------------
# Contact-to-Row Mapping
# ---------------------------------------------------------------------------


def contact_to_row(contact: dict[str, Any]) -> list[str]:
    """
    Convert a HubSpot contact dict to a spreadsheet row.

    Args:
        contact: HubSpot contact object with 'id' and 'properties'.

    Returns:
        List of string values matching SHEET_HEADERS column order.
    """
    props = contact.get("properties", {})
    row = [str(contact.get("id", ""))]

    for prop_name in HUBSPOT_PROPERTIES:
        value = props.get(prop_name, "") or ""

        # Format dates for readability
        if prop_name in ("createdate", "lastmodifieddate") and value:
            try:
                dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
                value = dt.strftime("%Y-%m-%d %H:%M")
            except (ValueError, AttributeError):
                pass

        row.append(str(value))

    # Add sync timestamp
    row.append(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"))

    return row


# ---------------------------------------------------------------------------
# Sync Logic
# ---------------------------------------------------------------------------


def sync_contacts_to_sheet(contacts: list[dict], worksheet: gspread.Worksheet) -> dict:
    """
    Sync HubSpot contacts to the Google Sheet using update-or-create logic.

    Matches existing rows by HubSpot ID (column A). Updates matched rows
    in place; appends new contacts at the bottom.

    Args:
        contacts: List of HubSpot contact dicts.
        worksheet: Target gspread Worksheet.

    Returns:
        Dict with sync statistics: created, updated, unchanged, errors.
    """
    stats = {"created": 0, "updated": 0, "unchanged": 0, "errors": 0}

    # Build lookup of existing rows by HubSpot ID
    all_values = worksheet.get_all_values()
    existing_rows = {}  # hubspot_id -> row_number (1-indexed)

    for idx, row in enumerate(all_values[1:], start=2):  # Skip header
        if row and row[0]:
            existing_rows[row[0]] = idx

    logger.info(
        "Found %d existing contacts in sheet, syncing %d from HubSpot",
        len(existing_rows),
        len(contacts),
    )

    # Prepare batch updates and appends
    updates = []  # (range, values) tuples
    appends = []  # new row values

    for contact in contacts:
        try:
            row_data = contact_to_row(contact)
            hubspot_id = row_data[0]

            if hubspot_id in existing_rows:
                row_num = existing_rows[hubspot_id]
                # Check if data actually changed (exclude sync timestamp column)
                existing_data = all_values[row_num - 1][:len(row_data) - 1] if row_num - 1 < len(all_values) else []
                new_data = row_data[:len(row_data) - 1]

                if existing_data == new_data:
                    stats["unchanged"] += 1
                    continue

                # Update existing row
                cell_range = f"A{row_num}"
                updates.append((cell_range, [row_data]))
                stats["updated"] += 1
            else:
                appends.append(row_data)
                stats["created"] += 1

        except Exception as exc:
            logger.error(
                "Error processing contact %s: %s",
                contact.get("id", "unknown"),
                exc,
            )
            stats["errors"] += 1

    # Execute batch updates
    if updates:
        logger.info("Updating %d existing rows", len(updates))
        try:
            worksheet.batch_update([
                {"range": cell_range, "values": values}
                for cell_range, values in updates
            ])
        except Exception as exc:
            logger.error("Failed to batch update rows: %s", exc)
            stats["errors"] += len(updates)
            stats["updated"] -= len(updates)

    # Append new rows
    if appends:
        logger.info("Appending %d new rows", len(appends))
        try:
            worksheet.append_rows(appends, value_input_option="USER_ENTERED")
        except Exception as exc:
            logger.error("Failed to append new rows: %s", exc)
            stats["errors"] += len(appends)
            stats["created"] = 0

    return stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    """Run the HubSpot to Google Sheets sync."""
    start_time = datetime.now(timezone.utc)
    logger.info("=" * 60)
    logger.info("Starting HubSpot → Google Sheets sync at %s", start_time.strftime("%Y-%m-%d %H:%M:%S UTC"))

    try:
        # Step 1: Fetch contacts from HubSpot
        logger.info("Step 1/3: Fetching contacts from HubSpot...")
        contacts = fetch_all_hubspot_contacts()

        if not contacts:
            logger.warning("No contacts found in HubSpot. Nothing to sync.")
            return

        # Step 2: Connect to Google Sheet
        logger.info("Step 2/3: Connecting to Google Sheet...")
        worksheet = get_google_sheet()
        ensure_headers(worksheet)

        # Step 3: Sync contacts
        logger.info("Step 3/3: Syncing contacts to sheet...")
        stats = sync_contacts_to_sheet(contacts, worksheet)

        # Report results
        elapsed = (datetime.now(timezone.utc) - start_time).total_seconds()
        logger.info("-" * 40)
        logger.info("Sync complete in %.1f seconds", elapsed)
        logger.info(
            "Results: %d created, %d updated, %d unchanged, %d errors",
            stats["created"],
            stats["updated"],
            stats["unchanged"],
            stats["errors"],
        )
        logger.info("=" * 60)

        if stats["errors"] > 0:
            sys.exit(1)

    except Exception:
        logger.exception("Sync failed with unhandled error")
        sys.exit(1)


if __name__ == "__main__":
    main()
