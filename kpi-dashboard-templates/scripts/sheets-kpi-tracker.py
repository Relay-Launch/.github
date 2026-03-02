#!/usr/bin/env python3
"""
Relay Launch — Google Sheets KPI Tracker Generator
===================================================

This script uses the Google Sheets API to create a fully formatted KPI tracking
spreadsheet with:
  - A Dashboard tab with scorecard layout and conditional formatting
  - A Weekly Data Entry tab with validation and formulas
  - A Historical Data tab for trend tracking
  - A Definitions tab documenting each metric
  - Conditional formatting (green/yellow/red) based on targets
  - Sparkline formulas for inline trend visualization
  - Named ranges for clean formula references

PREREQUISITES
=============

1. Python 3.8+

2. Install dependencies:
       pip install google-auth google-auth-oauthlib google-api-python-client

3. Create a Google Cloud project and enable the Google Sheets API:
       a. Go to https://console.cloud.google.com/
       b. Create a new project (or select an existing one)
       c. Navigate to APIs & Services > Library
       d. Search for "Google Sheets API" and enable it
       e. Search for "Google Drive API" and enable it

4. Create OAuth 2.0 credentials:
       a. Go to APIs & Services > Credentials
       b. Click "Create Credentials" > "OAuth client ID"
       c. Application type: "Desktop app"
       d. Download the JSON file and save it as "credentials.json"
          in the same directory as this script

5. First run will open a browser window for Google account authorization.
   The resulting token is saved to "token.json" for subsequent runs.

USAGE
=====

    python sheets-kpi-tracker.py

    # With custom business name
    python sheets-kpi-tracker.py --business "Acme Corp"

    # With custom KPI preset
    python sheets-kpi-tracker.py --preset saas
    python sheets-kpi-tracker.py --preset ecommerce
    python sheets-kpi-tracker.py --preset services
    python sheets-kpi-tracker.py --preset retail
    python sheets-kpi-tracker.py --preset restaurant

The script will create a new Google Sheet in your Drive and print the URL.

Part of the Relay Launch KPI Dashboard Templates collection.
https://relaylaunch.com
"""

import argparse
import os
import sys
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Lazy-import Google client libraries so the module can be parsed even when
# the packages are not installed (e.g., for linting or testing purposes).
# ---------------------------------------------------------------------------

def _import_google_libs():
    """Import Google API client libraries and return them as a namespace dict."""
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
    except ImportError:
        print("ERROR: Required packages not installed.")
        print("Run: pip install google-auth google-auth-oauthlib google-api-python-client")
        sys.exit(1)
    return {
        "Request": Request,
        "Credentials": Credentials,
        "InstalledAppFlow": InstalledAppFlow,
        "build": build,
        "HttpError": HttpError,
    }


# ---------------------------------------------------------------------------
# Configuration: KPI presets by business type
# ---------------------------------------------------------------------------

KPI_PRESETS = {
    "saas": {
        "label": "SaaS",
        "kpis": [
            {
                "name": "Monthly Recurring Revenue (MRR)",
                "unit": "$",
                "format": "currency",
                "target": 100000,
                "yellow_pct": 0.90,
                "definition": "Sum of all active subscription amounts normalized to monthly.",
                "formula_note": "=SUM of subscription amounts",
            },
            {
                "name": "MRR Growth Rate",
                "unit": "%",
                "format": "percent",
                "target": 10,
                "yellow_pct": 0.80,
                "definition": "Month-over-month percentage change in MRR.",
                "formula_note": "=(Current MRR - Prior MRR) / Prior MRR * 100",
            },
            {
                "name": "Customer Churn Rate",
                "unit": "%",
                "format": "percent_inverse",
                "target": 3,
                "yellow_pct": 1.25,
                "definition": "Percentage of customers who cancel in a given month.",
                "formula_note": "=Customers Lost / Customers at Start of Month * 100",
            },
            {
                "name": "Net Revenue Retention",
                "unit": "%",
                "format": "percent",
                "target": 105,
                "yellow_pct": 0.95,
                "definition": "Revenue retained from existing customers including expansion.",
                "formula_note": "=(Start MRR - Churn - Contraction + Expansion) / Start MRR * 100",
            },
            {
                "name": "Customer Acquisition Cost (CAC)",
                "unit": "$",
                "format": "currency_inverse",
                "target": 500,
                "yellow_pct": 1.25,
                "definition": "Total sales and marketing spend per new customer.",
                "formula_note": "=Total S&M Spend / New Customers",
            },
            {
                "name": "LTV:CAC Ratio",
                "unit": "x",
                "format": "ratio",
                "target": 3.0,
                "yellow_pct": 0.80,
                "definition": "Customer lifetime value divided by acquisition cost.",
                "formula_note": "=LTV / CAC",
            },
            {
                "name": "Active Customers",
                "unit": "#",
                "format": "number",
                "target": 500,
                "yellow_pct": 0.90,
                "definition": "Count of customers with active subscriptions.",
                "formula_note": "=COUNT of active accounts",
            },
            {
                "name": "NPS Score",
                "unit": "pts",
                "format": "number",
                "target": 50,
                "yellow_pct": 0.80,
                "definition": "Net Promoter Score from customer surveys.",
                "formula_note": "=% Promoters - % Detractors",
            },
        ],
    },
    "ecommerce": {
        "label": "E-Commerce",
        "kpis": [
            {
                "name": "Revenue",
                "unit": "$",
                "format": "currency",
                "target": 200000,
                "yellow_pct": 0.90,
                "definition": "Total gross revenue from orders.",
                "formula_note": "=SUM of order totals",
            },
            {
                "name": "Conversion Rate",
                "unit": "%",
                "format": "percent",
                "target": 3.0,
                "yellow_pct": 0.80,
                "definition": "Percentage of site visitors who complete a purchase.",
                "formula_note": "=Orders / Unique Sessions * 100",
            },
            {
                "name": "Average Order Value (AOV)",
                "unit": "$",
                "format": "currency",
                "target": 65,
                "yellow_pct": 0.90,
                "definition": "Average dollar amount per transaction.",
                "formula_note": "=Revenue / Number of Orders",
            },
            {
                "name": "Customer Acquisition Cost",
                "unit": "$",
                "format": "currency_inverse",
                "target": 25,
                "yellow_pct": 1.25,
                "definition": "Total acquisition spend per new customer.",
                "formula_note": "=Total Acquisition Spend / New Customers",
            },
            {
                "name": "Cart Abandonment Rate",
                "unit": "%",
                "format": "percent_inverse",
                "target": 65,
                "yellow_pct": 1.10,
                "definition": "Percentage of carts that do not convert to orders.",
                "formula_note": "=(1 - Orders / Carts Created) * 100",
            },
            {
                "name": "Repeat Purchase Rate",
                "unit": "%",
                "format": "percent",
                "target": 30,
                "yellow_pct": 0.80,
                "definition": "Percentage of customers with 2+ purchases.",
                "formula_note": "=Customers with 2+ Orders / Total Customers * 100",
            },
            {
                "name": "Gross Margin",
                "unit": "%",
                "format": "percent",
                "target": 45,
                "yellow_pct": 0.90,
                "definition": "Revenue minus COGS as a percentage.",
                "formula_note": "=(Revenue - COGS) / Revenue * 100",
            },
            {
                "name": "Return Rate",
                "unit": "%",
                "format": "percent_inverse",
                "target": 8,
                "yellow_pct": 1.25,
                "definition": "Percentage of orders returned.",
                "formula_note": "=Returned Orders / Total Orders * 100",
            },
        ],
    },
    "services": {
        "label": "Professional Services",
        "kpis": [
            {
                "name": "Revenue",
                "unit": "$",
                "format": "currency",
                "target": 150000,
                "yellow_pct": 0.90,
                "definition": "Total recognized revenue for the period.",
                "formula_note": "=SUM of invoiced revenue",
            },
            {
                "name": "Billable Utilization",
                "unit": "%",
                "format": "percent",
                "target": 72,
                "yellow_pct": 0.90,
                "definition": "Percentage of available hours billed to clients.",
                "formula_note": "=Billable Hours / Total Available Hours * 100",
            },
            {
                "name": "Effective Bill Rate",
                "unit": "$",
                "format": "currency",
                "target": 185,
                "yellow_pct": 0.90,
                "definition": "Actual revenue per billable hour worked.",
                "formula_note": "=Revenue / Billable Hours",
            },
            {
                "name": "Project Profit Margin",
                "unit": "%",
                "format": "percent",
                "target": 35,
                "yellow_pct": 0.85,
                "definition": "Profitability after direct labor and expenses.",
                "formula_note": "=(Revenue - Direct Costs) / Revenue * 100",
            },
            {
                "name": "Pipeline Value (Weighted)",
                "unit": "$",
                "format": "currency",
                "target": 450000,
                "yellow_pct": 0.80,
                "definition": "Weighted value of active proposals and opportunities.",
                "formula_note": "=SUM(Opportunity Value * Win Probability)",
            },
            {
                "name": "Win Rate",
                "unit": "%",
                "format": "percent",
                "target": 35,
                "yellow_pct": 0.80,
                "definition": "Percentage of proposals that convert to engagements.",
                "formula_note": "=Proposals Won / Total Proposals * 100",
            },
            {
                "name": "Client Satisfaction (NPS)",
                "unit": "pts",
                "format": "number",
                "target": 55,
                "yellow_pct": 0.80,
                "definition": "Net Promoter Score from client surveys.",
                "formula_note": "=% Promoters - % Detractors",
            },
            {
                "name": "Revenue Per Employee",
                "unit": "$",
                "format": "currency",
                "target": 18000,
                "yellow_pct": 0.85,
                "definition": "Monthly revenue divided by headcount.",
                "formula_note": "=Revenue / FTE Headcount",
            },
        ],
    },
    "retail": {
        "label": "Retail",
        "kpis": [
            {
                "name": "Total Revenue",
                "unit": "$",
                "format": "currency",
                "target": 300000,
                "yellow_pct": 0.90,
                "definition": "Total net sales for the period.",
                "formula_note": "=SUM of daily register totals",
            },
            {
                "name": "Same-Store Sales Growth",
                "unit": "%",
                "format": "percent",
                "target": 4,
                "yellow_pct": 0.50,
                "definition": "Revenue growth from stores open 12+ months vs. prior year.",
                "formula_note": "=(Current Period - Prior Year Same Period) / Prior Year * 100",
            },
            {
                "name": "Sales Per Square Foot",
                "unit": "$",
                "format": "currency",
                "target": 350,
                "yellow_pct": 0.90,
                "definition": "Net sales divided by total selling square footage.",
                "formula_note": "=Net Sales / Selling Sq Ft",
            },
            {
                "name": "Conversion Rate (Traffic)",
                "unit": "%",
                "format": "percent",
                "target": 28,
                "yellow_pct": 0.85,
                "definition": "Percentage of store visitors who make a purchase.",
                "formula_note": "=Transactions / Foot Traffic Count * 100",
            },
            {
                "name": "Average Transaction Value",
                "unit": "$",
                "format": "currency",
                "target": 48,
                "yellow_pct": 0.90,
                "definition": "Average dollar amount per transaction.",
                "formula_note": "=Net Sales / Number of Transactions",
            },
            {
                "name": "Inventory Turnover",
                "unit": "x",
                "format": "ratio",
                "target": 5.0,
                "yellow_pct": 0.80,
                "definition": "How quickly inventory sells through.",
                "formula_note": "=COGS / Average Inventory Value",
            },
            {
                "name": "Gross Margin",
                "unit": "%",
                "format": "percent",
                "target": 50,
                "yellow_pct": 0.92,
                "definition": "Revenue minus COGS as a percentage.",
                "formula_note": "=(Revenue - COGS) / Revenue * 100",
            },
            {
                "name": "Shrinkage Rate",
                "unit": "%",
                "format": "percent_inverse",
                "target": 1.5,
                "yellow_pct": 1.30,
                "definition": "Inventory loss from theft, damage, and errors.",
                "formula_note": "=(Book Inventory - Actual Inventory) / Book Inventory * 100",
            },
        ],
    },
    "restaurant": {
        "label": "Food & Beverage",
        "kpis": [
            {
                "name": "Total Revenue",
                "unit": "$",
                "format": "currency",
                "target": 120000,
                "yellow_pct": 0.90,
                "definition": "Total revenue for the period.",
                "formula_note": "=SUM of daily sales",
            },
            {
                "name": "Food Cost Percentage",
                "unit": "%",
                "format": "percent_inverse",
                "target": 30,
                "yellow_pct": 1.10,
                "definition": "Cost of food ingredients as percentage of food sales.",
                "formula_note": "=(Beginning Inv + Purchases - Ending Inv) / Food Sales * 100",
            },
            {
                "name": "Labor Cost Percentage",
                "unit": "%",
                "format": "percent_inverse",
                "target": 28,
                "yellow_pct": 1.10,
                "definition": "Total labor expense as percentage of total revenue.",
                "formula_note": "=Total Labor Cost / Total Revenue * 100",
            },
            {
                "name": "Prime Cost Percentage",
                "unit": "%",
                "format": "percent_inverse",
                "target": 60,
                "yellow_pct": 1.05,
                "definition": "Combined food + labor cost as percentage of revenue.",
                "formula_note": "=(Food Cost + Labor Cost) / Revenue * 100",
            },
            {
                "name": "Average Check Size",
                "unit": "$",
                "format": "currency",
                "target": 32,
                "yellow_pct": 0.90,
                "definition": "Average revenue per guest.",
                "formula_note": "=Total Revenue / Number of Covers",
            },
            {
                "name": "Table Turnover Rate",
                "unit": "x",
                "format": "ratio",
                "target": 2.0,
                "yellow_pct": 0.80,
                "definition": "Number of times each seat is occupied per service.",
                "formula_note": "=Covers Served / Available Seats",
            },
            {
                "name": "Customer Count (Covers)",
                "unit": "#",
                "format": "number",
                "target": 3800,
                "yellow_pct": 0.90,
                "definition": "Total guests served in the period.",
                "formula_note": "=SUM of daily cover counts",
            },
            {
                "name": "Food Waste Percentage",
                "unit": "%",
                "format": "percent_inverse",
                "target": 5,
                "yellow_pct": 1.30,
                "definition": "Variance between theoretical and actual food cost.",
                "formula_note": "=(Actual Food Cost - Theoretical) / Theoretical * 100",
            },
        ],
    },
}

# ---------------------------------------------------------------------------
# Color definitions (RGB for Google Sheets API)
# ---------------------------------------------------------------------------

COLORS = {
    "white": {"red": 1.0, "green": 1.0, "blue": 1.0},
    "light_gray": {"red": 0.95, "green": 0.95, "blue": 0.95},
    "medium_gray": {"red": 0.85, "green": 0.85, "blue": 0.85},
    "dark_gray": {"red": 0.3, "green": 0.3, "blue": 0.3},
    "brand_navy": {"red": 0.13, "green": 0.17, "blue": 0.26},
    "brand_blue": {"red": 0.26, "green": 0.52, "blue": 0.96},
    "green": {"red": 0.20, "green": 0.66, "blue": 0.33},
    "green_bg": {"red": 0.85, "green": 0.95, "blue": 0.87},
    "yellow": {"red": 0.95, "green": 0.76, "blue": 0.19},
    "yellow_bg": {"red": 1.0, "green": 0.97, "blue": 0.85},
    "red": {"red": 0.90, "green": 0.22, "blue": 0.21},
    "red_bg": {"red": 0.98, "green": 0.87, "blue": 0.87},
}


# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]


def authenticate(google_libs):
    """Authenticate with Google and return credentials."""
    Credentials = google_libs["Credentials"]
    Request = google_libs["Request"]
    InstalledAppFlow = google_libs["InstalledAppFlow"]

    creds = None
    token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "token.json")
    creds_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credentials.json")

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(creds_path):
                print(f"ERROR: credentials.json not found at {creds_path}")
                print()
                print("To set up Google API credentials:")
                print("  1. Go to https://console.cloud.google.com/")
                print("  2. Create a project and enable Google Sheets API + Google Drive API")
                print("  3. Create OAuth 2.0 credentials (Desktop app type)")
                print("  4. Download the JSON and save as 'credentials.json' next to this script")
                print()
                print("See the docstring at the top of this script for full setup instructions.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, "w") as token_file:
            token_file.write(creds.to_json())

    return creds


# ---------------------------------------------------------------------------
# Sheet creation helpers
# ---------------------------------------------------------------------------

def create_spreadsheet(service, title):
    """Create a new spreadsheet with four tabs and return its ID and sheet metadata."""
    spreadsheet_body = {
        "properties": {"title": title},
        "sheets": [
            {"properties": {"title": "Dashboard", "index": 0}},
            {"properties": {"title": "Weekly Data", "index": 1}},
            {"properties": {"title": "Historical", "index": 2}},
            {"properties": {"title": "Definitions", "index": 3}},
        ],
    }
    result = service.spreadsheets().create(body=spreadsheet_body).execute()
    return result["spreadsheetId"], result["sheets"]


def get_sheet_id(sheets, title):
    """Get the numeric sheetId for a tab by its title."""
    for sheet in sheets:
        if sheet["properties"]["title"] == title:
            return sheet["properties"]["sheetId"]
    return None


def _fmt_header(sheet_id, row_start, row_end, col_start, col_end,
                bg_color=None, text_color=None, bold=True, font_size=10):
    """Return a repeatCell request dict for header formatting."""
    cell_format = {"textFormat": {"bold": bold, "fontSize": font_size}}
    if bg_color:
        cell_format["backgroundColor"] = bg_color
    if text_color:
        cell_format["textFormat"]["foregroundColor"] = text_color

    return {
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": row_start,
                "endRowIndex": row_end,
                "startColumnIndex": col_start,
                "endColumnIndex": col_end,
            },
            "cell": {"userEnteredFormat": cell_format},
            "fields": "userEnteredFormat(backgroundColor,textFormat)",
        }
    }


def _fmt_col_width(sheet_id, col_start, col_end, width):
    """Return a request dict to set column pixel width."""
    return {
        "updateDimensionProperties": {
            "range": {
                "sheetId": sheet_id,
                "dimension": "COLUMNS",
                "startIndex": col_start,
                "endIndex": col_end,
            },
            "properties": {"pixelSize": width},
            "fields": "pixelSize",
        }
    }


def _fmt_cond(sheet_id, row_start, row_end, col_start, col_end,
              condition_type, values, bg_color):
    """Return an addConditionalFormatRule request dict."""
    return {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {
                        "sheetId": sheet_id,
                        "startRowIndex": row_start,
                        "endRowIndex": row_end,
                        "startColumnIndex": col_start,
                        "endColumnIndex": col_end,
                    }
                ],
                "booleanRule": {
                    "condition": {
                        "type": condition_type,
                        "values": [{"userEnteredValue": v} for v in values],
                    },
                    "format": {"backgroundColor": bg_color},
                },
            },
            "index": 0,
        }
    }


def _freeze(sheet_id, rows=0, cols=0):
    """Return a request dict to freeze rows and/or columns."""
    props = {}
    fields = []
    if rows:
        props["frozenRowCount"] = rows
        fields.append("gridProperties.frozenRowCount")
    if cols:
        props["frozenColumnCount"] = cols
        fields.append("gridProperties.frozenColumnCount")
    return {
        "updateSheetProperties": {
            "properties": {
                "sheetId": sheet_id,
                "gridProperties": props,
            },
            "fields": ",".join(fields),
        }
    }


# ---------------------------------------------------------------------------
# Tab population functions
# ---------------------------------------------------------------------------

def populate_dashboard(service, spreadsheet_id, sheet_id, kpis, preset_label, business_name):
    """Write the Dashboard tab: title, scorecards, status formulas, sparklines."""
    today = datetime.now().strftime("%Y-%m-%d")

    rows = [
        [f"{business_name} -- KPI Dashboard ({preset_label})", "", "", "", "", f"As of: {today}"],
        [""],
        ["SCORECARD", "", "Current", "Target", "% of Target", "Status", "Trend (8 wk)"],
    ]

    for i, kpi in enumerate(kpis):
        sheet_row = len(rows) + 1  # 1-indexed row in Sheets for this KPI
        latest_col = chr(ord("C") + 11)  # Column N = 12th week in Weekly Data
        current_ref = f"='Weekly Data'!{latest_col}{i + 2}"
        pct_formula = f"=IF(D{sheet_row}<>0, C{sheet_row}/D{sheet_row}, 0)"
        status_formula = (
            f'=IF(E{sheet_row}>=0.95, "GREEN", '
            f'IF(E{sheet_row}>=0.80, "YELLOW", "RED"))'
        )
        sparkline_formula = (
            f"=SPARKLINE('Historical'!C{i + 2}:J{i + 2}, "
            '{"charttype","line";"linewidth",2;"color","#4285f4"})'
        )
        rows.append([
            kpi["name"],
            kpi["unit"],
            current_ref,
            kpi["target"],
            pct_formula,
            status_formula,
            sparkline_formula,
        ])

    rows.append([""])
    rows.append(["NOTES & ANNOTATIONS"])
    rows.append(["Enter weekly context here: anomalies, root causes, action items."])
    rows.append([""])
    rows.append([
        "GREEN = On track (>=95% of target)  |  "
        "YELLOW = Monitor (80-95%)  |  "
        "RED = Action needed (<80%)"
    ])
    rows.append([""])
    rows.append(["Dashboard generated by Relay Launch KPI Dashboard Templates"])
    rows.append(["https://relaylaunch.com"])

    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range="Dashboard!A1",
        valueInputOption="USER_ENTERED",
        body={"values": rows},
    ).execute()

    # -- Formatting --
    kpi_start = 3
    kpi_end = kpi_start + len(kpis)
    status_col = 5
    reqs = [
        # Title row
        _fmt_header(sheet_id, 0, 1, 0, 7,
                    bg_color=COLORS["brand_navy"], text_color=COLORS["white"],
                    bold=True, font_size=14),
        # Column headers
        _fmt_header(sheet_id, 2, 3, 0, 7,
                    bg_color=COLORS["medium_gray"], text_color=COLORS["dark_gray"],
                    bold=True, font_size=10),
        # Column widths
        _fmt_col_width(sheet_id, 0, 1, 280),
        _fmt_col_width(sheet_id, 1, 2, 50),
        _fmt_col_width(sheet_id, 2, 3, 120),
        _fmt_col_width(sheet_id, 3, 4, 100),
        _fmt_col_width(sheet_id, 4, 5, 110),
        _fmt_col_width(sheet_id, 5, 6, 90),
        _fmt_col_width(sheet_id, 6, 7, 200),
        # Conditional formatting on Status column
        _fmt_cond(sheet_id, kpi_start, kpi_end, status_col, status_col + 1,
                  "TEXT_EQ", ["GREEN"], COLORS["green_bg"]),
        _fmt_cond(sheet_id, kpi_start, kpi_end, status_col, status_col + 1,
                  "TEXT_EQ", ["YELLOW"], COLORS["yellow_bg"]),
        _fmt_cond(sheet_id, kpi_start, kpi_end, status_col, status_col + 1,
                  "TEXT_EQ", ["RED"], COLORS["red_bg"]),
        # Freeze top 3 rows
        _freeze(sheet_id, rows=3),
    ]
    service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body={"requests": reqs},
    ).execute()


def populate_weekly_data(service, spreadsheet_id, sheet_id, kpis, business_name):
    """Write the Weekly Data tab: 12 week columns with auto-calc columns."""
    today = datetime.now()
    week_headers = []
    for i in range(12):
        d = today - timedelta(weeks=(11 - i))
        week_headers.append(f"Wk {d.strftime('%m/%d')}")

    header = ["KPI", "Unit"] + week_headers + ["Current (Latest)", "WoW Change", "WoW Change %"]
    rows = [header]

    for i, kpi in enumerate(kpis):
        r = i + 2  # 1-indexed data row
        latest = chr(ord("C") + 11)   # col N
        prev = chr(ord("C") + 10)     # col M
        row = [kpi["name"], kpi["unit"]]
        row += [""] * 12  # empty week cells for data entry
        row.append(f"={latest}{r}")
        row.append(f"={latest}{r}-{prev}{r}")
        row.append(f"=IF({prev}{r}<>0, ({latest}{r}-{prev}{r})/{prev}{r}, 0)")
        rows.append(row)

    rows += [
        [""],
        ["INSTRUCTIONS:"],
        ["Enter actual KPI values each week in the corresponding column (C through N)."],
        ["The Current, WoW Change, and WoW Change % columns compute automatically."],
        ["The Dashboard tab pulls the Current column to populate its scorecards."],
    ]

    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range="'Weekly Data'!A1",
        valueInputOption="USER_ENTERED",
        body={"values": rows},
    ).execute()

    reqs = [
        _fmt_header(sheet_id, 0, 1, 0, len(header),
                    bg_color=COLORS["brand_navy"], text_color=COLORS["white"],
                    bold=True, font_size=10),
        _fmt_col_width(sheet_id, 0, 1, 280),
        _fmt_col_width(sheet_id, 1, 2, 50),
        _freeze(sheet_id, rows=1, cols=2),
    ]
    # Alternating row shading
    for i in range(len(kpis)):
        if i % 2 == 1:
            reqs.append(_fmt_header(
                sheet_id, i + 1, i + 2, 0, len(header),
                bg_color=COLORS["light_gray"], bold=False, font_size=10,
            ))

    service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body={"requests": reqs},
    ).execute()


def populate_historical(service, spreadsheet_id, sheet_id, kpis):
    """Write the Historical tab: references last 8 weeks from Weekly Data for sparklines."""
    header = ["KPI"] + [f"Week {i + 1}" for i in range(8)]
    rows = [header]

    for i, kpi in enumerate(kpis):
        row = [kpi["name"]]
        for w in range(8):
            col = chr(ord("C") + 4 + w)  # cols G-N (weeks 5-12)
            row.append(f"='Weekly Data'!{col}{i + 2}")
        rows.append(row)

    rows += [
        [""],
        ["This tab feeds the sparkline charts on the Dashboard tab."],
        ["Data is pulled automatically from the Weekly Data tab (last 8 weeks)."],
    ]

    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range="Historical!A1",
        valueInputOption="USER_ENTERED",
        body={"values": rows},
    ).execute()

    reqs = [
        _fmt_header(sheet_id, 0, 1, 0, 9,
                    bg_color=COLORS["brand_navy"], text_color=COLORS["white"],
                    bold=True, font_size=10),
        _fmt_col_width(sheet_id, 0, 1, 280),
    ]
    service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body={"requests": reqs},
    ).execute()


def populate_definitions(service, spreadsheet_id, sheet_id, kpis, preset_label):
    """Write the Definitions tab: full KPI documentation with owner and source fields."""
    header = ["KPI", "Unit", "Definition", "Formula / Calculation",
              "Target", "Data Source", "Owner"]
    rows = [header]

    for kpi in kpis:
        target_display = str(kpi["target"])
        if kpi["unit"] not in ("$",):
            target_display += " " + kpi["unit"]
        rows.append([
            kpi["name"],
            kpi["unit"],
            kpi["definition"],
            kpi["formula_note"],
            target_display,
            "(Enter data source)",
            "(Enter owner name)",
        ])

    rows += [
        [""],
        ["ABOUT THIS SHEET"],
        [f"KPI preset: {preset_label}"],
        ["Generated by Relay Launch KPI Dashboard Templates"],
        ["https://relaylaunch.com"],
        [""],
        ["INSTRUCTIONS:"],
        ["Fill in Data Source and Owner for each KPI."],
        ["Data Source = where the number comes from (e.g., 'QuickBooks P&L report')."],
        ["Owner = the single person responsible for updating this metric each week."],
        ["Delete rows for KPIs that are not relevant. Add rows for custom KPIs."],
    ]

    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range="Definitions!A1",
        valueInputOption="USER_ENTERED",
        body={"values": rows},
    ).execute()

    reqs = [
        _fmt_header(sheet_id, 0, 1, 0, 7,
                    bg_color=COLORS["brand_navy"], text_color=COLORS["white"],
                    bold=True, font_size=10),
        _fmt_col_width(sheet_id, 0, 1, 250),
        _fmt_col_width(sheet_id, 1, 2, 50),
        _fmt_col_width(sheet_id, 2, 3, 400),
        _fmt_col_width(sheet_id, 3, 4, 350),
        _fmt_col_width(sheet_id, 4, 5, 100),
        _fmt_col_width(sheet_id, 5, 6, 200),
        _fmt_col_width(sheet_id, 6, 7, 150),
        _freeze(sheet_id, rows=1),
        # Wrap text in definition & formula columns
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 1,
                    "endRowIndex": len(kpis) + 1,
                    "startColumnIndex": 2,
                    "endColumnIndex": 4,
                },
                "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP"}},
                "fields": "userEnteredFormat.wrapStrategy",
            }
        },
    ]
    service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body={"requests": reqs},
    ).execute()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Relay Launch -- Generate a KPI tracking spreadsheet in Google Sheets",
    )
    parser.add_argument(
        "--business", default="My Business",
        help="Business name to display on the dashboard (default: 'My Business')",
    )
    parser.add_argument(
        "--preset", default="saas", choices=list(KPI_PRESETS.keys()),
        help="KPI preset for your business type (default: saas). "
             "Options: saas, ecommerce, services, retail, restaurant",
    )
    args = parser.parse_args()

    preset = KPI_PRESETS[args.preset]
    kpis = preset["kpis"]
    preset_label = preset["label"]
    business_name = args.business

    print("=" * 60)
    print("Relay Launch -- KPI Dashboard Generator")
    print("=" * 60)
    print(f"  Business:  {business_name}")
    print(f"  Preset:    {preset_label} ({len(kpis)} KPIs)")
    print()

    # Authenticate
    google_libs = _import_google_libs()
    creds = authenticate(google_libs)
    service = google_libs["build"]("sheets", "v4", credentials=creds)

    # Create spreadsheet
    title = f"{business_name} -- KPI Dashboard ({preset_label})"
    print(f"Creating spreadsheet: {title}")
    spreadsheet_id, sheets = create_spreadsheet(service, title)

    # Populate each tab
    tabs = [
        ("Dashboard",   populate_dashboard,   [get_sheet_id(sheets, "Dashboard"), kpis, preset_label, business_name]),
        ("Weekly Data",  populate_weekly_data, [get_sheet_id(sheets, "Weekly Data"), kpis, business_name]),
        ("Historical",   populate_historical,  [get_sheet_id(sheets, "Historical"), kpis]),
        ("Definitions",  populate_definitions, [get_sheet_id(sheets, "Definitions"), kpis, preset_label]),
    ]
    for tab_name, func, extra_args in tabs:
        print(f"  Populating {tab_name} tab...")
        func(service, spreadsheet_id, *extra_args)

    # Done
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
    print()
    print("Spreadsheet created successfully!")
    print(f"  URL: {url}")
    print()
    print("Next steps:")
    print("  1. Open the Definitions tab -- fill in Data Source and Owner for each KPI")
    print("  2. Enter your first week of data in the Weekly Data tab")
    print("  3. Review the Dashboard tab to see your scorecards update")
    print("  4. Set a recurring calendar event to update data weekly")
    print("  5. Bring the Dashboard tab to your weekly leadership meeting")
    print()
    print("Generated by Relay Launch -- https://relaylaunch.com")


if __name__ == "__main__":
    main()
