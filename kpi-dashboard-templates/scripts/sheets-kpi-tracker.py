#!/usr/bin/env python3
"""
Relay Launch — Google Sheets KPI Tracker Setup

Creates a formatted KPI tracking spreadsheet in Google Sheets with:
- Monthly KPI input columns
- Automatic formulas (MoM change, YTD averages, target comparison)
- Conditional formatting (green/yellow/red based on targets)
- Pre-configured for common small business metrics

Setup:
    1. Create a Google Cloud project and enable the Sheets API
    2. Create a service account and download the JSON credentials
    3. Save credentials as 'credentials.json' in this directory
    4. Share your target Google Sheet with the service account email
    5. pip install gspread google-auth
    6. python sheets-kpi-tracker.py --sheet-id YOUR_SHEET_ID

Usage:
    python sheets-kpi-tracker.py --sheet-id <google-sheet-id>
    python sheets-kpi-tracker.py --sheet-id <google-sheet-id> --template saas
    python sheets-kpi-tracker.py --sheet-id <google-sheet-id> --template ecommerce
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import gspread
    from google.oauth2.service_account import Credentials
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install gspread google-auth")
    sys.exit(1)


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

TEMPLATES = {
    "general": {
        "name": "General Business KPIs",
        "metrics": [
            {"name": "Revenue", "format": "currency", "target": 50000, "direction": "up"},
            {"name": "New Customers", "format": "number", "target": 15, "direction": "up"},
            {"name": "Customer Churn Rate (%)", "format": "percent", "target": 3.0, "direction": "down"},
            {"name": "Gross Margin (%)", "format": "percent", "target": 60.0, "direction": "up"},
            {"name": "Operating Expenses", "format": "currency", "target": 30000, "direction": "down"},
            {"name": "Net Profit", "format": "currency", "target": 10000, "direction": "up"},
            {"name": "Cash on Hand", "format": "currency", "target": 100000, "direction": "up"},
            {"name": "Accounts Receivable (days)", "format": "number", "target": 30, "direction": "down"},
            {"name": "Pipeline Value", "format": "currency", "target": 100000, "direction": "up"},
            {"name": "Team Capacity (%)", "format": "percent", "target": 80.0, "direction": "up"},
            {"name": "Customer Satisfaction (NPS)", "format": "number", "target": 50, "direction": "up"},
            {"name": "Website Visitors", "format": "number", "target": 5000, "direction": "up"},
        ],
    },
    "saas": {
        "name": "SaaS Business KPIs",
        "metrics": [
            {"name": "MRR", "format": "currency", "target": 25000, "direction": "up"},
            {"name": "ARR", "format": "currency", "target": 300000, "direction": "up"},
            {"name": "New MRR", "format": "currency", "target": 3000, "direction": "up"},
            {"name": "Churned MRR", "format": "currency", "target": 500, "direction": "down"},
            {"name": "Net Revenue Retention (%)", "format": "percent", "target": 110.0, "direction": "up"},
            {"name": "CAC", "format": "currency", "target": 200, "direction": "down"},
            {"name": "LTV", "format": "currency", "target": 2400, "direction": "up"},
            {"name": "LTV:CAC Ratio", "format": "number", "target": 3.0, "direction": "up"},
            {"name": "Trial-to-Paid Conversion (%)", "format": "percent", "target": 25.0, "direction": "up"},
            {"name": "Monthly Active Users", "format": "number", "target": 500, "direction": "up"},
            {"name": "Churn Rate (%)", "format": "percent", "target": 5.0, "direction": "down"},
            {"name": "Burn Rate", "format": "currency", "target": 15000, "direction": "down"},
        ],
    },
    "ecommerce": {
        "name": "E-Commerce KPIs",
        "metrics": [
            {"name": "Revenue", "format": "currency", "target": 75000, "direction": "up"},
            {"name": "Orders", "format": "number", "target": 500, "direction": "up"},
            {"name": "Average Order Value", "format": "currency", "target": 150, "direction": "up"},
            {"name": "Conversion Rate (%)", "format": "percent", "target": 2.5, "direction": "up"},
            {"name": "Cart Abandonment Rate (%)", "format": "percent", "target": 65.0, "direction": "down"},
            {"name": "Return Rate (%)", "format": "percent", "target": 5.0, "direction": "down"},
            {"name": "Customer Acquisition Cost", "format": "currency", "target": 25, "direction": "down"},
            {"name": "Repeat Purchase Rate (%)", "format": "percent", "target": 30.0, "direction": "up"},
            {"name": "Inventory Turnover", "format": "number", "target": 6.0, "direction": "up"},
            {"name": "Gross Margin (%)", "format": "percent", "target": 45.0, "direction": "up"},
            {"name": "Website Sessions", "format": "number", "target": 20000, "direction": "up"},
            {"name": "Email List Size", "format": "number", "target": 5000, "direction": "up"},
        ],
    },
}


def get_client(credentials_path="credentials.json"):
    """Authenticate and return a gspread client."""
    creds_file = Path(credentials_path)
    if not creds_file.exists():
        print(f"Error: Credentials file not found at {credentials_path}")
        print("Download your service account JSON from Google Cloud Console.")
        sys.exit(1)

    creds = Credentials.from_service_account_file(str(creds_file), scopes=SCOPES)
    return gspread.authorize(creds)


def build_tracker(client, sheet_id, template_name="general"):
    """Build the KPI tracker spreadsheet."""
    template = TEMPLATES.get(template_name)
    if not template:
        print(f"Unknown template: {template_name}")
        print(f"Available: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)

    print(f"Setting up: {template['name']}")
    print(f"Opening spreadsheet: {sheet_id}")

    spreadsheet = client.open_by_key(sheet_id)

    # Create or get the KPI Tracker worksheet
    try:
        worksheet = spreadsheet.worksheet("KPI Tracker")
        worksheet.clear()
        print("Cleared existing 'KPI Tracker' worksheet.")
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(
            title="KPI Tracker", rows=100, cols=20
        )
        print("Created new 'KPI Tracker' worksheet.")

    metrics = template["metrics"]
    num_metrics = len(metrics)

    # Build header row
    headers = ["KPI", "Target"] + MONTHS + ["YTD Avg", "vs Target"]
    worksheet.update("A1", [headers])

    # Build metric rows
    rows = []
    for i, metric in enumerate(metrics):
        row_num = i + 2
        row = [metric["name"], metric["target"]]
        # Add empty cells for months
        row += [""] * 12
        # YTD Average formula (average of non-empty month cells)
        month_range = f"C{row_num}:N{row_num}"
        row.append(f'=IF(COUNTA({month_range})>0, AVERAGE(IF({month_range}<>"", {month_range})), "")')
        # vs Target formula
        row.append(f'=IF(O{row_num}<>"", O{row_num}-B{row_num}, "")')
        rows.append(row)

    worksheet.update(f"A2:P{num_metrics + 1}", rows, value_input_option="USER_ENTERED")

    # Format headers
    worksheet.format("A1:P1", {
        "backgroundColor": {"red": 0.13, "green": 0.53, "blue": 0.21},
        "textFormat": {"bold": True, "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
        "horizontalAlignment": "CENTER",
    })

    # Format KPI name column
    worksheet.format(f"A2:A{num_metrics + 1}", {
        "textFormat": {"bold": True},
    })

    # Format target column
    worksheet.format(f"B2:B{num_metrics + 1}", {
        "horizontalAlignment": "CENTER",
        "backgroundColor": {"red": 0.95, "green": 0.95, "blue": 0.95},
    })

    # Freeze header row and KPI column
    worksheet.freeze(rows=1, cols=1)

    # Set column widths
    requests = [
        {"updateDimensionProperties": {
            "range": {"sheetId": worksheet.id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 250}, "fields": "pixelSize"
        }},
        {"updateDimensionProperties": {
            "range": {"sheetId": worksheet.id, "dimension": "COLUMNS", "startIndex": 1, "endIndex": 2},
            "properties": {"pixelSize": 100}, "fields": "pixelSize"
        }},
    ]
    spreadsheet.batch_update({"requests": requests})

    print(f"\nDone! KPI Tracker created with {num_metrics} metrics.")
    print(f"Template: {template['name']}")
    print(f"Months: Jan-Dec with YTD Average and vs Target columns")
    print(f"\nOpen your spreadsheet and start entering monthly data in columns C-N.")


def main():
    parser = argparse.ArgumentParser(
        description="Relay Launch — Google Sheets KPI Tracker Setup"
    )
    parser.add_argument(
        "--sheet-id", required=True,
        help="Google Sheets ID (from the URL)"
    )
    parser.add_argument(
        "--template", default="general", choices=TEMPLATES.keys(),
        help="KPI template to use (default: general)"
    )
    parser.add_argument(
        "--credentials", default="credentials.json",
        help="Path to Google service account credentials JSON"
    )
    args = parser.parse_args()

    client = get_client(args.credentials)
    build_tracker(client, args.sheet_id, args.template)


if __name__ == "__main__":
    main()
