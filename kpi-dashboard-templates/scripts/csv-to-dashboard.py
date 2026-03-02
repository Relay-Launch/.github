#!/usr/bin/env python3
"""
Relay Launch — CSV to HTML Dashboard Generator

Reads a CSV of business metrics and generates a standalone HTML dashboard
report with KPI cards, data tables, and trend indicators.

No external dependencies required — uses only Python standard library.

Usage:
    python csv-to-dashboard.py --input metrics.csv --output dashboard.html
    python csv-to-dashboard.py --input metrics.csv --output dashboard.html --title "March 2026 Report"

Expected CSV format:
    metric,value,target,previous
    Revenue,47200,60000,43700
    New Customers,12,15,10
    Churn Rate,1.8,3.0,2.4
    ...

Columns:
    metric   - Name of the KPI
    value    - Current period value
    target   - Target/goal value (optional, use 0 to skip)
    previous - Previous period value (optional, use 0 to skip)
"""

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path


def read_metrics(filepath):
    """Read metrics from a CSV file."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    metrics = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            metric = {
                "name": row.get("metric", "").strip(),
                "value": float(row.get("value", 0)),
                "target": float(row.get("target", 0)),
                "previous": float(row.get("previous", 0)),
            }
            if metric["name"]:
                metrics.append(metric)
    return metrics


def calculate_status(value, target, previous):
    """Determine status color and trend."""
    # Trend
    if previous > 0:
        change = ((value - previous) / previous) * 100
        if change > 0:
            trend = f"+{change:.1f}%"
            trend_class = "trend-up"
        elif change < 0:
            trend = f"{change:.1f}%"
            trend_class = "trend-down"
        else:
            trend = "0%"
            trend_class = "trend-flat"
    else:
        trend = "—"
        trend_class = "trend-flat"

    # Status vs target
    if target > 0:
        pct = (value / target) * 100
        if pct >= 90:
            status_class = "status-good"
        elif pct >= 70:
            status_class = "status-warn"
        else:
            status_class = "status-bad"
        target_text = f"{pct:.0f}% of target"
    else:
        status_class = "status-neutral"
        target_text = ""

    return {
        "trend": trend,
        "trend_class": trend_class,
        "status_class": status_class,
        "target_text": target_text,
    }


def format_number(value):
    """Format a number for display."""
    if value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    elif value >= 10_000:
        return f"${value:,.0f}"
    elif value >= 100:
        return f"{value:,.0f}"
    elif value == int(value):
        return f"{int(value)}"
    else:
        return f"{value:.1f}"


def generate_html(metrics, title):
    """Generate a complete HTML dashboard."""
    generated_at = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    # Build KPI cards
    cards_html = ""
    for m in metrics:
        status = calculate_status(m["value"], m["target"], m["previous"])
        display_value = format_number(m["value"])

        cards_html += f"""
        <div class="kpi-card {status['status_class']}">
            <div class="kpi-name">{m['name']}</div>
            <div class="kpi-value">{display_value}</div>
            <div class="kpi-meta">
                <span class="{status['trend_class']}">{status['trend']} vs prev</span>
                {'<span class="kpi-target">' + status['target_text'] + '</span>' if status['target_text'] else ''}
            </div>
        </div>"""

    # Build data table
    table_rows = ""
    for m in metrics:
        status = calculate_status(m["value"], m["target"], m["previous"])
        table_rows += f"""
            <tr>
                <td class="metric-name">{m['name']}</td>
                <td class="metric-value">{format_number(m['value'])}</td>
                <td>{format_number(m['target']) if m['target'] > 0 else '—'}</td>
                <td>{format_number(m['previous']) if m['previous'] > 0 else '—'}</td>
                <td class="{status['trend_class']}">{status['trend']}</td>
                <td><span class="status-dot {status['status_class']}"></span> {status['target_text'] or '—'}</td>
            </tr>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            background: #0d1117; color: #e6edf3; padding: 32px; line-height: 1.5;
        }}
        .dashboard {{ max-width: 1100px; margin: 0 auto; }}
        .header {{ margin-bottom: 32px; }}
        .header h1 {{ font-size: 1.8rem; font-weight: 700; margin-bottom: 4px; }}
        .header p {{ color: #8b949e; font-size: 0.9rem; }}
        .kpi-grid {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px; margin-bottom: 40px;
        }}
        .kpi-card {{
            background: #161b22; border: 1px solid #21262d; border-radius: 8px;
            padding: 20px; border-top: 3px solid #21262d;
        }}
        .kpi-card.status-good {{ border-top-color: #238636; }}
        .kpi-card.status-warn {{ border-top-color: #d29922; }}
        .kpi-card.status-bad {{ border-top-color: #da3633; }}
        .kpi-name {{ font-size: 0.8rem; color: #8b949e; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px; }}
        .kpi-value {{ font-size: 1.8rem; font-weight: 700; margin-bottom: 8px; }}
        .kpi-meta {{ font-size: 0.8rem; color: #8b949e; display: flex; gap: 12px; flex-wrap: wrap; }}
        .kpi-target {{ color: #8b949e; }}
        .trend-up {{ color: #238636; }}
        .trend-up::before {{ content: "\\2191 "; }}
        .trend-down {{ color: #da3633; }}
        .trend-down::before {{ content: "\\2193 "; }}
        .trend-flat {{ color: #8b949e; }}
        table {{ width: 100%; border-collapse: collapse; background: #161b22; border-radius: 8px; overflow: hidden; }}
        th {{ background: #21262d; text-align: left; padding: 12px 16px; font-size: 0.8rem;
             text-transform: uppercase; letter-spacing: 0.05em; color: #8b949e; }}
        td {{ padding: 12px 16px; border-top: 1px solid #21262d; font-size: 0.9rem; }}
        .metric-name {{ font-weight: 600; }}
        .metric-value {{ font-weight: 700; }}
        .status-dot {{
            display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 6px;
        }}
        .status-dot.status-good {{ background: #238636; }}
        .status-dot.status-warn {{ background: #d29922; }}
        .status-dot.status-bad {{ background: #da3633; }}
        .status-dot.status-neutral {{ background: #484f58; }}
        .section-title {{ font-size: 1.1rem; font-weight: 600; margin-bottom: 16px; color: #e6edf3; }}
        .footer {{ margin-top: 40px; text-align: center; color: #484f58; font-size: 0.8rem; }}
        .footer a {{ color: #58a6ff; }}
        @media print {{
            body {{ background: #fff; color: #000; }}
            .kpi-card {{ background: #f6f8fa; border-color: #d0d7de; }}
            table {{ background: #fff; }}
            th {{ background: #f6f8fa; color: #000; }}
            td {{ border-color: #d0d7de; }}
        }}
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>{title}</h1>
            <p>Generated {generated_at} by Relay Launch KPI Dashboard Tools</p>
        </div>

        <div class="kpi-grid">{cards_html}
        </div>

        <div class="section-title">Detailed Breakdown</div>
        <table>
            <thead>
                <tr>
                    <th>Metric</th>
                    <th>Current</th>
                    <th>Target</th>
                    <th>Previous</th>
                    <th>Change</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>{table_rows}
            </tbody>
        </table>

        <div class="footer">
            <p>Relay Launch &mdash; Operational clarity. Strategic momentum. Real results.</p>
        </div>
    </div>
</body>
</html>"""
    return html


def generate_sample_csv(output_path):
    """Generate a sample CSV file for testing."""
    sample = [
        ["metric", "value", "target", "previous"],
        ["Revenue", "47200", "60000", "43700"],
        ["New Customers", "12", "15", "10"],
        ["Churn Rate (%)", "1.8", "3.0", "2.4"],
        ["Gross Margin (%)", "62", "60", "58"],
        ["Operating Expenses", "28500", "30000", "29100"],
        ["Net Profit", "12400", "10000", "8900"],
        ["Pipeline Value", "134000", "100000", "98000"],
        ["Avg Deal Size", "7400", "7000", "6100"],
        ["Website Visitors", "4800", "5000", "4200"],
        ["Conversion Rate (%)", "2.3", "2.5", "2.1"],
        ["NPS Score", "72", "50", "68"],
        ["Team Capacity (%)", "78", "80", "82"],
    ]
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(sample)
    print(f"Sample CSV written to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Relay Launch — CSV to HTML Dashboard Generator"
    )
    parser.add_argument("--input", type=str, help="Input CSV file path")
    parser.add_argument("--output", type=str, default="dashboard.html", help="Output HTML file path")
    parser.add_argument("--title", type=str, default="Business KPI Dashboard", help="Dashboard title")
    parser.add_argument("--sample", type=str, help="Generate a sample CSV file at this path")
    args = parser.parse_args()

    if args.sample:
        generate_sample_csv(args.sample)
        return

    if not args.input:
        parser.print_help()
        print("\nExamples:")
        print("  python csv-to-dashboard.py --sample sample.csv")
        print("  python csv-to-dashboard.py --input sample.csv --output report.html")
        return

    metrics = read_metrics(args.input)
    if not metrics:
        print("No metrics found in the CSV file.")
        sys.exit(1)

    html = generate_html(metrics, args.title)

    output_path = Path(args.output)
    output_path.write_text(html)
    print(f"Dashboard generated: {output_path}")
    print(f"Metrics: {len(metrics)}")
    print(f"Open {output_path} in a browser to view.")


if __name__ == "__main__":
    main()
