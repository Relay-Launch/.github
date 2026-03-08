#!/usr/bin/env python3
"""
Email Report Generator
=======================
Relay▸Launch Integration Cookbook

Aggregates data from a CSV file or SQLite database, computes key metrics,
generates a formatted HTML email report, and sends it via SMTP.

Perfect for daily/weekly business summaries — revenue, new customers,
conversion rates, or any other metrics your team needs to see regularly.

Setup:
    1. Prepare your data source (CSV file or SQLite database)
    2. Set environment variables (see below)
    3. Customize the metrics and HTML template to fit your business
    4. Run manually or set up a cron job

Environment Variables:
    SMTP_HOST       — SMTP server hostname (e.g., smtp.gmail.com)
    SMTP_PORT       — SMTP server port (e.g., 587 for TLS)
    SMTP_USERNAME   — SMTP authentication username
    SMTP_PASSWORD   — SMTP authentication password (use app password for Gmail)
    SMTP_FROM       — Sender email address
    SMTP_TO         — Comma-separated recipient email addresses
    SMTP_USE_TLS    — Use TLS (optional, default: true)
    DATA_SOURCE     — Path to CSV file or SQLite database
    DATA_TYPE       — "csv" or "sqlite" (optional, default: csv)
    DATA_QUERY      — SQL query for sqlite sources (optional)
    REPORT_TITLE    — Report title (optional, default: "Business Report")
    LOG_LEVEL       — Logging level (optional, default: INFO)

Cron Example (daily at 8am):
    0 8 * * * cd /path/to/integration-cookbook && /path/to/venv/bin/python recipes/email-report-generator.py

Gmail Setup:
    1. Enable 2-factor authentication on your Google account
    2. Generate an App Password: Google Account → Security → App passwords
    3. Use that App Password as SMTP_PASSWORD
"""

import os
import sys
import csv
import sqlite3
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timezone, timedelta
from decimal import Decimal, InvalidOperation
from typing import Any
from collections import defaultdict

from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

load_dotenv()

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_FROM = os.environ.get("SMTP_FROM")
SMTP_TO = os.environ.get("SMTP_TO", "")
SMTP_USE_TLS = os.environ.get("SMTP_USE_TLS", "true").lower() in ("true", "1", "yes")
DATA_SOURCE = os.environ.get("DATA_SOURCE", "data/report_data.csv")
DATA_TYPE = os.environ.get("DATA_TYPE", "csv").lower()
DATA_QUERY = os.environ.get("DATA_QUERY", "SELECT * FROM transactions")
REPORT_TITLE = os.environ.get("REPORT_TITLE", "Business Report")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

_missing = []
if not SMTP_USERNAME:
    _missing.append("SMTP_USERNAME")
if not SMTP_PASSWORD:
    _missing.append("SMTP_PASSWORD")
if not SMTP_FROM:
    _missing.append("SMTP_FROM")
if not SMTP_TO:
    _missing.append("SMTP_TO")

if _missing:
    print(f"ERROR: Missing required environment variables: {', '.join(_missing)}")
    sys.exit(1)

RECIPIENTS = [addr.strip() for addr in SMTP_TO.split(",") if addr.strip()]

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("email-report")

# ---------------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------------


def load_csv_data(filepath: str) -> list[dict[str, str]]:
    """
    Load data from a CSV file.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of dicts (one per row), keyed by column header.
    """
    if not os.path.exists(filepath):
        logger.error("CSV file not found: %s", filepath)
        raise FileNotFoundError(f"CSV file not found: {filepath}")

    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    logger.info("Loaded %d rows from CSV: %s", len(rows), filepath)
    return rows


def load_sqlite_data(db_path: str, query: str) -> list[dict[str, Any]]:
    """
    Load data from a SQLite database using a query.

    Args:
        db_path: Path to the SQLite database file.
        query: SQL SELECT query to execute.

    Returns:
        List of dicts (one per row), keyed by column name.
    """
    if not os.path.exists(db_path):
        logger.error("Database file not found: %s", db_path)
        raise FileNotFoundError(f"Database file not found: {db_path}")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.execute(query)
        rows = [dict(row) for row in cursor.fetchall()]
        logger.info("Loaded %d rows from SQLite: %s", len(rows), db_path)
        return rows
    finally:
        conn.close()


def load_data() -> list[dict[str, Any]]:
    """Load data from the configured source."""
    if DATA_TYPE == "sqlite":
        return load_sqlite_data(DATA_SOURCE, DATA_QUERY)
    else:
        return load_csv_data(DATA_SOURCE)


# ---------------------------------------------------------------------------
# Metrics Computation
# ---------------------------------------------------------------------------


def safe_decimal(value: Any) -> Decimal:
    """Safely convert a value to Decimal, returning 0 on failure."""
    if value is None or value == "":
        return Decimal("0")
    try:
        return Decimal(str(value).replace(",", "").replace("$", ""))
    except (InvalidOperation, ValueError):
        return Decimal("0")


def compute_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Compute business metrics from the data.

    This function expects rows with columns like:
        date, amount, status, category, customer_email

    Customize the column names and calculations below to match your data.

    Args:
        rows: List of data row dicts.

    Returns:
        Dict of computed metrics.
    """
    if not rows:
        return {
            "total_rows": 0,
            "total_revenue": Decimal("0"),
            "average_order": Decimal("0"),
            "success_count": 0,
            "failure_count": 0,
            "success_rate": 0.0,
            "unique_customers": 0,
            "by_category": {},
            "by_day": {},
            "top_customers": [],
        }

    # Core revenue metrics
    amounts = [safe_decimal(row.get("amount", 0)) for row in rows]
    total_revenue = sum(amounts)
    average_order = total_revenue / len(amounts) if amounts else Decimal("0")

    # Status breakdown
    success_count = sum(
        1 for row in rows
        if str(row.get("status", "")).lower() in ("success", "completed", "paid", "active")
    )
    failure_count = sum(
        1 for row in rows
        if str(row.get("status", "")).lower() in ("failed", "declined", "refunded", "cancelled")
    )
    success_rate = (success_count / len(rows) * 100) if rows else 0.0

    # Unique customers
    customer_emails = {
        row.get("customer_email", row.get("email", "")).lower()
        for row in rows
        if row.get("customer_email") or row.get("email")
    }

    # Revenue by category
    by_category = defaultdict(lambda: {"count": 0, "revenue": Decimal("0")})
    for row in rows:
        cat = row.get("category", "Uncategorized")
        by_category[cat]["count"] += 1
        by_category[cat]["revenue"] += safe_decimal(row.get("amount", 0))

    # Revenue by day
    by_day = defaultdict(lambda: {"count": 0, "revenue": Decimal("0")})
    for row in rows:
        date_str = str(row.get("date", ""))[:10]  # Take YYYY-MM-DD portion
        if date_str:
            by_day[date_str]["count"] += 1
            by_day[date_str]["revenue"] += safe_decimal(row.get("amount", 0))

    # Top customers by revenue
    customer_revenue = defaultdict(Decimal)
    for row in rows:
        email = row.get("customer_email", row.get("email", "unknown"))
        customer_revenue[email] += safe_decimal(row.get("amount", 0))
    top_customers = sorted(
        customer_revenue.items(), key=lambda x: x[1], reverse=True
    )[:10]

    return {
        "total_rows": len(rows),
        "total_revenue": total_revenue,
        "average_order": average_order,
        "success_count": success_count,
        "failure_count": failure_count,
        "success_rate": success_rate,
        "unique_customers": len(customer_emails),
        "by_category": dict(by_category),
        "by_day": dict(sorted(by_day.items())),
        "top_customers": top_customers,
    }


# ---------------------------------------------------------------------------
# HTML Report Generation
# ---------------------------------------------------------------------------


def generate_html_report(metrics: dict[str, Any], report_date: str) -> str:
    """
    Generate a formatted HTML email report from computed metrics.

    Args:
        metrics: Dict of computed metrics from compute_metrics().
        report_date: Human-readable date string for the report header.

    Returns:
        Complete HTML string ready to be sent as an email body.
    """
    # Category rows
    _category_rows = []
    for cat, data in sorted(metrics["by_category"].items(), key=lambda x: x[1]["revenue"], reverse=True):
        _category_rows.append(f"""
            <tr>
                <td style="padding: 8px 12px; border-bottom: 1px solid #eee;">{cat}</td>
                <td style="padding: 8px 12px; border-bottom: 1px solid #eee; text-align: right;">{data['count']}</td>
                <td style="padding: 8px 12px; border-bottom: 1px solid #eee; text-align: right;">${data['revenue']:,.2f}</td>
            </tr>""")
    category_rows = "".join(_category_rows)

    # Daily trend rows
    _daily_rows = []
    for day, data in metrics["by_day"].items():
        _daily_rows.append(f"""
            <tr>
                <td style="padding: 8px 12px; border-bottom: 1px solid #eee;">{day}</td>
                <td style="padding: 8px 12px; border-bottom: 1px solid #eee; text-align: right;">{data['count']}</td>
                <td style="padding: 8px 12px; border-bottom: 1px solid #eee; text-align: right;">${data['revenue']:,.2f}</td>
            </tr>""")
    daily_rows = "".join(_daily_rows)

    # Top customers rows
    _top_customer_rows = []
    for email, revenue in metrics["top_customers"]:
        _top_customer_rows.append(f"""
            <tr>
                <td style="padding: 8px 12px; border-bottom: 1px solid #eee;">{email}</td>
                <td style="padding: 8px 12px; border-bottom: 1px solid #eee; text-align: right;">${revenue:,.2f}</td>
            </tr>""")
    top_customer_rows = "".join(_top_customer_rows)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{REPORT_TITLE}</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f5f5f5; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width: 640px; margin: 0 auto; background-color: #ffffff;">
        <!-- Header -->
        <tr>
            <td style="background-color: #1a1a2e; color: #ffffff; padding: 24px 32px;">
                <h1 style="margin: 0 0 4px 0; font-size: 22px; font-weight: 600;">{REPORT_TITLE}</h1>
                <p style="margin: 0; font-size: 14px; color: #a0a0b0;">{report_date}</p>
            </td>
        </tr>

        <!-- KPI Summary Cards -->
        <tr>
            <td style="padding: 24px 32px 8px;">
                <h2 style="margin: 0 0 16px 0; font-size: 16px; color: #333; text-transform: uppercase; letter-spacing: 1px;">Summary</h2>
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
                    <tr>
                        <td width="50%" style="padding: 0 8px 16px 0;">
                            <div style="background: #f0f4ff; border-radius: 8px; padding: 16px;">
                                <div style="font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">Total Revenue</div>
                                <div style="font-size: 28px; font-weight: 700; color: #1a1a2e; margin-top: 4px;">${metrics['total_revenue']:,.2f}</div>
                            </div>
                        </td>
                        <td width="50%" style="padding: 0 0 16px 8px;">
                            <div style="background: #f0fff4; border-radius: 8px; padding: 16px;">
                                <div style="font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">Transactions</div>
                                <div style="font-size: 28px; font-weight: 700; color: #1a1a2e; margin-top: 4px;">{metrics['total_rows']:,}</div>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td width="50%" style="padding: 0 8px 16px 0;">
                            <div style="background: #fff8f0; border-radius: 8px; padding: 16px;">
                                <div style="font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">Avg Order Value</div>
                                <div style="font-size: 28px; font-weight: 700; color: #1a1a2e; margin-top: 4px;">${metrics['average_order']:,.2f}</div>
                            </div>
                        </td>
                        <td width="50%" style="padding: 0 0 16px 8px;">
                            <div style="background: #f5f0ff; border-radius: 8px; padding: 16px;">
                                <div style="font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">Success Rate</div>
                                <div style="font-size: 28px; font-weight: 700; color: #1a1a2e; margin-top: 4px;">{metrics['success_rate']:.1f}%</div>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td width="50%" style="padding: 0 8px 16px 0;">
                            <div style="background: #f0f4ff; border-radius: 8px; padding: 16px;">
                                <div style="font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">Unique Customers</div>
                                <div style="font-size: 28px; font-weight: 700; color: #1a1a2e; margin-top: 4px;">{metrics['unique_customers']:,}</div>
                            </div>
                        </td>
                        <td width="50%" style="padding: 0 0 16px 8px;">
                            <div style="background: #fff0f0; border-radius: 8px; padding: 16px;">
                                <div style="font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">Failed</div>
                                <div style="font-size: 28px; font-weight: 700; color: #c0392b; margin-top: 4px;">{metrics['failure_count']:,}</div>
                            </div>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>

        <!-- Revenue by Category -->
        <tr>
            <td style="padding: 8px 32px 24px;">
                <h2 style="margin: 0 0 12px 0; font-size: 16px; color: #333; text-transform: uppercase; letter-spacing: 1px;">Revenue by Category</h2>
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border: 1px solid #eee; border-radius: 8px; overflow: hidden;">
                    <tr style="background-color: #f8f9fa;">
                        <th style="padding: 10px 12px; text-align: left; font-size: 12px; color: #666; text-transform: uppercase;">Category</th>
                        <th style="padding: 10px 12px; text-align: right; font-size: 12px; color: #666; text-transform: uppercase;">Count</th>
                        <th style="padding: 10px 12px; text-align: right; font-size: 12px; color: #666; text-transform: uppercase;">Revenue</th>
                    </tr>
                    {category_rows}
                </table>
            </td>
        </tr>

        <!-- Daily Trend -->
        <tr>
            <td style="padding: 0 32px 24px;">
                <h2 style="margin: 0 0 12px 0; font-size: 16px; color: #333; text-transform: uppercase; letter-spacing: 1px;">Daily Breakdown</h2>
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border: 1px solid #eee; border-radius: 8px; overflow: hidden;">
                    <tr style="background-color: #f8f9fa;">
                        <th style="padding: 10px 12px; text-align: left; font-size: 12px; color: #666; text-transform: uppercase;">Date</th>
                        <th style="padding: 10px 12px; text-align: right; font-size: 12px; color: #666; text-transform: uppercase;">Transactions</th>
                        <th style="padding: 10px 12px; text-align: right; font-size: 12px; color: #666; text-transform: uppercase;">Revenue</th>
                    </tr>
                    {daily_rows}
                </table>
            </td>
        </tr>

        <!-- Top Customers -->
        <tr>
            <td style="padding: 0 32px 24px;">
                <h2 style="margin: 0 0 12px 0; font-size: 16px; color: #333; text-transform: uppercase; letter-spacing: 1px;">Top Customers</h2>
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border: 1px solid #eee; border-radius: 8px; overflow: hidden;">
                    <tr style="background-color: #f8f9fa;">
                        <th style="padding: 10px 12px; text-align: left; font-size: 12px; color: #666; text-transform: uppercase;">Customer</th>
                        <th style="padding: 10px 12px; text-align: right; font-size: 12px; color: #666; text-transform: uppercase;">Revenue</th>
                    </tr>
                    {top_customer_rows}
                </table>
            </td>
        </tr>

        <!-- Footer -->
        <tr>
            <td style="background-color: #f8f9fa; padding: 20px 32px; border-top: 1px solid #eee;">
                <p style="margin: 0; font-size: 12px; color: #999; text-align: center;">
                    Generated by Relay&#9656;Launch Integration Cookbook<br>
                    {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}
                </p>
            </td>
        </tr>
    </table>
</body>
</html>"""

    return html


# ---------------------------------------------------------------------------
# Email Sending
# ---------------------------------------------------------------------------


def send_email(subject: str, html_body: str, text_body: str) -> bool:
    """
    Send an email via SMTP with both HTML and plain-text bodies.

    Args:
        subject: Email subject line.
        html_body: HTML email body.
        text_body: Plain-text fallback body.

    Returns:
        True if sent successfully, False otherwise.
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_FROM
    msg["To"] = ", ".join(RECIPIENTS)

    # Attach plain text and HTML (email clients prefer the last part)
    msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    try:
        if SMTP_USE_TLS:
            server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30)
            server.ehlo()
            server.starttls()
            server.ehlo()
        else:
            server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=30)

        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_FROM, RECIPIENTS, msg.as_string())
        server.quit()

        logger.info("Email sent successfully to %s", ", ".join(RECIPIENTS))
        return True

    except smtplib.SMTPAuthenticationError as exc:
        logger.error("SMTP authentication failed: %s", exc)
        logger.error("If using Gmail, make sure you're using an App Password")
        return False
    except smtplib.SMTPException as exc:
        logger.error("SMTP error: %s", exc)
        return False
    except Exception as exc:
        logger.error("Failed to send email: %s", exc)
        return False


# ---------------------------------------------------------------------------
# Plain-Text Report (Fallback)
# ---------------------------------------------------------------------------


def generate_text_report(metrics: dict[str, Any], report_date: str) -> str:
    """
    Generate a plain-text version of the report for email clients
    that don't render HTML.

    Args:
        metrics: Dict of computed metrics.
        report_date: Human-readable date string.

    Returns:
        Plain-text report string.
    """
    lines = [
        f"{REPORT_TITLE}",
        f"{report_date}",
        "=" * 50,
        "",
        "SUMMARY",
        "-" * 30,
        f"  Total Revenue:     ${metrics['total_revenue']:,.2f}",
        f"  Transactions:      {metrics['total_rows']:,}",
        f"  Avg Order Value:   ${metrics['average_order']:,.2f}",
        f"  Success Rate:      {metrics['success_rate']:.1f}%",
        f"  Unique Customers:  {metrics['unique_customers']:,}",
        f"  Failed:            {metrics['failure_count']:,}",
        "",
        "REVENUE BY CATEGORY",
        "-" * 30,
    ]

    for cat, data in sorted(metrics["by_category"].items(), key=lambda x: x[1]["revenue"], reverse=True):
        lines.append(f"  {cat:<20} {data['count']:>5} txns    ${data['revenue']:>10,.2f}")

    lines.extend(["", "TOP CUSTOMERS", "-" * 30])

    for email, revenue in metrics["top_customers"]:
        lines.append(f"  {email:<30} ${revenue:>10,.2f}")

    lines.extend([
        "",
        "=" * 50,
        f"Generated by Relay Launch Integration Cookbook",
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
    ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    """Load data, compute metrics, generate report, and send email."""
    logger.info("=" * 60)
    logger.info("Starting Email Report Generator")

    try:
        # Step 1: Load data
        logger.info("Step 1/4: Loading data from %s (%s)...", DATA_SOURCE, DATA_TYPE)
        rows = load_data()

        if not rows:
            logger.warning("No data found. Sending empty report notice.")
            report_date = datetime.now(timezone.utc).strftime("%B %d, %Y")
            send_email(
                subject=f"{REPORT_TITLE} — {report_date} (No Data)",
                html_body=f"<p>No data was available for the report period: {report_date}.</p>",
                text_body=f"No data was available for the report period: {report_date}.",
            )
            return

        # Step 2: Compute metrics
        logger.info("Step 2/4: Computing metrics from %d rows...", len(rows))
        metrics = compute_metrics(rows)

        # Step 3: Generate report
        logger.info("Step 3/4: Generating HTML report...")
        report_date = datetime.now(timezone.utc).strftime("%B %d, %Y")
        html_body = generate_html_report(metrics, report_date)
        text_body = generate_text_report(metrics, report_date)

        # Step 4: Send email
        logger.info("Step 4/4: Sending email to %s...", ", ".join(RECIPIENTS))
        subject = f"{REPORT_TITLE} — {report_date}"

        if metrics["failure_count"] > 0:
            subject += f" ({metrics['failure_count']} failed transactions)"

        success = send_email(subject, html_body, text_body)

        if success:
            logger.info("Report sent successfully!")
        else:
            logger.error("Failed to send report email")
            sys.exit(1)

    except Exception:
        logger.exception("Report generation failed with unhandled error")
        sys.exit(1)

    logger.info("=" * 60)


if __name__ == "__main__":
    main()
