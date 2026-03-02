#!/usr/bin/env python3
"""
Relay Launch — CSV to HTML Dashboard Generator
===============================================

Reads a CSV of business metrics and generates a standalone HTML dashboard
report with:
  - KPI scorecard cards with status coloring
  - Inline SVG bar charts comparing current vs. target
  - A detailed data table with trend indicators
  - A summary statistics section
  - Fully self-contained HTML (no external dependencies, works offline)
  - Print-friendly styling

No external Python dependencies required — uses only the standard library.

USAGE
=====

    # Generate dashboard from a CSV file
    python csv-to-dashboard.py --input metrics.csv --output dashboard.html

    # With custom title and business name
    python csv-to-dashboard.py --input metrics.csv --output report.html \
        --title "Q1 2026 Performance" --business "Acme Corp"

    # Generate a sample CSV to get started
    python csv-to-dashboard.py --sample sample_metrics.csv

    # Then generate the dashboard from the sample
    python csv-to-dashboard.py --input sample_metrics.csv --output demo.html

EXPECTED CSV FORMAT
===================

    metric,value,target,previous,unit
    Revenue,847000,900000,756000,$
    Gross Margin,42.3,44.0,43.5,%
    New Customers,34,38,29,#
    Churn Rate,2.1,2.0,1.8,%
    NPS Score,67,65,62,pts

Columns:
    metric   — Name of the KPI (required)
    value    — Current period value (required)
    target   — Target/goal value (optional, use 0 or leave blank to skip)
    previous — Previous period value (optional, use 0 or leave blank to skip)
    unit     — Display unit: $, %, #, pts, x, or any string (optional)

If the 'unit' column is missing, the script will auto-detect formatting
based on the metric name (e.g., names containing "%" or "rate" get
percentage formatting).

Part of the Relay Launch KPI Dashboard Templates collection.
https://relaylaunch.com
"""

import argparse
import csv
import html as html_module
import math
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def read_metrics(filepath):
    """Read metrics from a CSV file and return a list of dicts."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    metrics = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("metric", "").strip()
            if not name:
                continue

            value_str = row.get("value", "0").strip()
            target_str = row.get("target", "0").strip()
            previous_str = row.get("previous", "0").strip()
            unit = row.get("unit", "").strip()

            # Parse numeric values, handling blanks and non-numeric gracefully
            try:
                value = float(value_str) if value_str else 0.0
            except ValueError:
                value = 0.0
            try:
                target = float(target_str) if target_str else 0.0
            except ValueError:
                target = 0.0
            try:
                previous = float(previous_str) if previous_str else 0.0
            except ValueError:
                previous = 0.0

            # Auto-detect unit if not provided
            if not unit:
                name_lower = name.lower()
                if any(kw in name_lower for kw in ["revenue", "cost", "profit", "cash",
                                                     "mrr", "arr", "arpu", "aov",
                                                     "ltv", "cac", "value", "spend"]):
                    unit = "$"
                elif any(kw in name_lower for kw in ["rate", "margin", "%", "percent",
                                                       "retention", "conversion",
                                                       "utilization", "churn"]):
                    unit = "%"
                elif any(kw in name_lower for kw in ["nps", "score", "csat"]):
                    unit = "pts"
                elif any(kw in name_lower for kw in ["ratio", "turnover"]):
                    unit = "x"
                else:
                    unit = "#"

            metrics.append({
                "name": name,
                "value": value,
                "target": target,
                "previous": previous,
                "unit": unit,
            })

    return metrics


# ---------------------------------------------------------------------------
# Metric analysis
# ---------------------------------------------------------------------------

def analyze_metric(m):
    """Compute status, trend, and display values for a metric."""
    value = m["value"]
    target = m["target"]
    previous = m["previous"]
    unit = m["unit"]

    # Determine if lower is better (inverse metrics)
    name_lower = m["name"].lower()
    lower_is_better = any(kw in name_lower for kw in [
        "churn", "cost", "expense", "abandonment", "error",
        "defect", "waste", "shrinkage", "return rate",
        "burn", "attrition", "turnover rate",
    ])

    # -- Trend vs previous --
    if previous > 0:
        change_pct = ((value - previous) / previous) * 100
        change_abs = value - previous
        if abs(change_pct) < 0.1:
            trend_direction = "flat"
        elif change_pct > 0:
            trend_direction = "down" if lower_is_better else "up"
        else:
            trend_direction = "up" if lower_is_better else "down"
        trend_text = f"{'+' if change_pct > 0 else ''}{change_pct:.1f}%"
    else:
        change_pct = 0
        change_abs = 0
        trend_direction = "flat"
        trend_text = "--"

    # -- Status vs target --
    if target > 0:
        if lower_is_better:
            # For inverse metrics: at or below target = good
            ratio = target / value if value > 0 else 1.0
        else:
            ratio = value / target if target > 0 else 0.0

        pct_of_target = (value / target) * 100 if target > 0 else 0

        if ratio >= 0.95:
            status = "good"
        elif ratio >= 0.80:
            status = "warn"
        else:
            status = "bad"

        target_text = f"{pct_of_target:.0f}% of target"
    else:
        status = "neutral"
        target_text = ""
        pct_of_target = 0
        ratio = 0

    # -- Formatted display value --
    display_value = format_value(value, unit)
    display_target = format_value(target, unit) if target > 0 else "--"
    display_previous = format_value(previous, unit) if previous > 0 else "--"

    return {
        **m,
        "display_value": display_value,
        "display_target": display_target,
        "display_previous": display_previous,
        "status": status,
        "trend_direction": trend_direction,
        "trend_text": trend_text,
        "target_text": target_text,
        "pct_of_target": pct_of_target,
        "change_pct": change_pct,
        "change_abs": change_abs,
        "lower_is_better": lower_is_better,
    }


def format_value(value, unit):
    """Format a numeric value with its unit for display."""
    if unit == "$":
        if abs(value) >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
        elif abs(value) >= 10_000:
            return f"${value:,.0f}"
        elif abs(value) >= 100:
            return f"${value:,.0f}"
        else:
            return f"${value:,.2f}"
    elif unit == "%":
        return f"{value:.1f}%"
    elif unit == "x":
        return f"{value:.1f}x"
    elif unit == "pts":
        return f"{value:.0f}"
    else:
        if value == int(value) and abs(value) < 1_000_000:
            return f"{int(value):,}"
        elif abs(value) >= 1000:
            return f"{value:,.0f}"
        else:
            return f"{value:.1f}"


# ---------------------------------------------------------------------------
# SVG chart generation
# ---------------------------------------------------------------------------

def svg_bar_chart(analyzed_metrics, width=700, bar_height=28, padding=4):
    """Generate an inline SVG horizontal bar chart comparing values to targets.

    Only includes metrics that have a target > 0.
    """
    chartable = [m for m in analyzed_metrics if m["target"] > 0]
    if not chartable:
        return ""

    label_width = 200
    chart_left = label_width + 10
    chart_width = width - chart_left - 80
    row_height = bar_height + padding * 2
    total_height = len(chartable) * row_height + 40  # extra for axis

    # Find max value for scaling (max of value or target)
    max_val = max(max(m["value"], m["target"]) for m in chartable)
    if max_val == 0:
        max_val = 1

    def scale(v):
        return (v / max_val) * chart_width

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {total_height}" '
        f'style="width:100%;max-width:{width}px;height:auto;font-family:-apple-system,'
        f'BlinkMacSystemFont,sans-serif;font-size:12px;">'
    ]

    for i, m in enumerate(chartable):
        y = i * row_height + 10
        bar_y = y + padding

        # Status color
        colors = {
            "good": "#238636",
            "warn": "#d29922",
            "bad": "#da3633",
            "neutral": "#6e7681",
        }
        fill = colors.get(m["status"], "#6e7681")

        # Label
        label = html_module.escape(m["name"])
        svg_parts.append(
            f'<text x="{label_width}" y="{bar_y + bar_height / 2 + 4}" '
            f'text-anchor="end" fill="#e6edf3" font-size="12">{label}</text>'
        )

        # Target background bar
        target_w = scale(m["target"])
        svg_parts.append(
            f'<rect x="{chart_left}" y="{bar_y}" width="{target_w}" '
            f'height="{bar_height}" rx="3" fill="#21262d"/>'
        )

        # Actual value bar
        value_w = max(scale(m["value"]), 2)
        svg_parts.append(
            f'<rect x="{chart_left}" y="{bar_y}" width="{value_w}" '
            f'height="{bar_height}" rx="3" fill="{fill}" opacity="0.85"/>'
        )

        # Value label
        val_label = html_module.escape(m["display_value"])
        svg_parts.append(
            f'<text x="{chart_left + value_w + 6}" y="{bar_y + bar_height / 2 + 4}" '
            f'fill="#e6edf3" font-size="11" font-weight="600">{val_label}</text>'
        )

    # Legend at bottom
    legend_y = total_height - 15
    svg_parts.append(
        f'<rect x="{chart_left}" y="{legend_y}" width="12" height="12" rx="2" fill="#21262d"/>'
        f'<text x="{chart_left + 18}" y="{legend_y + 10}" fill="#8b949e" font-size="11">Target</text>'
        f'<rect x="{chart_left + 80}" y="{legend_y}" width="12" height="12" rx="2" fill="#238636" opacity="0.85"/>'
        f'<text x="{chart_left + 98}" y="{legend_y + 10}" fill="#8b949e" font-size="11">Actual</text>'
    )

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def svg_sparkline(values, width=120, height=32, color="#4285f4"):
    """Generate a tiny inline SVG sparkline from a list of values."""
    if not values or len(values) < 2:
        return ""
    vals = [float(v) for v in values if v is not None]
    if len(vals) < 2:
        return ""

    min_v = min(vals)
    max_v = max(vals)
    val_range = max_v - min_v if max_v != min_v else 1

    points = []
    step = width / (len(vals) - 1)
    for i, v in enumerate(vals):
        x = i * step
        y = height - 4 - ((v - min_v) / val_range) * (height - 8)
        points.append(f"{x:.1f},{y:.1f}")

    polyline = " ".join(points)
    return (
        f'<svg viewBox="0 0 {width} {height}" style="width:{width}px;height:{height}px;">'
        f'<polyline points="{polyline}" fill="none" stroke="{color}" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
        f'<circle cx="{points[-1].split(",")[0]}" cy="{points[-1].split(",")[1]}" '
        f'r="3" fill="{color}"/>'
        f'</svg>'
    )


# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------

def compute_summary(analyzed):
    """Compute summary stats across all metrics."""
    total = len(analyzed)
    with_target = [m for m in analyzed if m["target"] > 0]
    good = sum(1 for m in with_target if m["status"] == "good")
    warn = sum(1 for m in with_target if m["status"] == "warn")
    bad = sum(1 for m in with_target if m["status"] == "bad")

    improving = sum(1 for m in analyzed if m["trend_direction"] == "up" or
                    (m["trend_direction"] == "flat" and m["change_pct"] == 0 and m["previous"] > 0))
    declining = sum(1 for m in analyzed if m["trend_direction"] == "down")

    return {
        "total": total,
        "with_target": len(with_target),
        "good": good,
        "warn": warn,
        "bad": bad,
        "improving": improving,
        "declining": declining,
        "health_pct": (good / len(with_target) * 100) if with_target else 0,
    }


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

def generate_html(metrics, title, business_name):
    """Generate a complete standalone HTML dashboard."""
    analyzed = [analyze_metric(m) for m in metrics]
    summary = compute_summary(analyzed)
    bar_chart = svg_bar_chart(analyzed)
    generated_at = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    # -- KPI Cards --
    cards_html = ""
    for m in analyzed:
        status_class = f"status-{m['status']}"
        trend_class = f"trend-{m['trend_direction']}"
        trend_arrow = {"up": "&#8593;", "down": "&#8595;", "flat": "&#8212;"}
        arrow = trend_arrow.get(m["trend_direction"], "")

        target_badge = ""
        if m["target_text"]:
            target_badge = f'<span class="kpi-target">{html_module.escape(m["target_text"])}</span>'

        cards_html += f"""
        <div class="kpi-card {status_class}">
            <div class="kpi-name">{html_module.escape(m['name'])}</div>
            <div class="kpi-value">{html_module.escape(m['display_value'])}</div>
            <div class="kpi-meta">
                <span class="{trend_class}">{arrow} {html_module.escape(m['trend_text'])} vs prev</span>
                {target_badge}
            </div>
        </div>"""

    # -- Summary Cards --
    summary_html = f"""
    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-number">{summary['total']}</div>
            <div class="summary-label">Total KPIs Tracked</div>
        </div>
        <div class="summary-card summary-good">
            <div class="summary-number">{summary['good']}</div>
            <div class="summary-label">On Track</div>
        </div>
        <div class="summary-card summary-warn">
            <div class="summary-number">{summary['warn']}</div>
            <div class="summary-label">Monitor</div>
        </div>
        <div class="summary-card summary-bad">
            <div class="summary-number">{summary['bad']}</div>
            <div class="summary-label">Action Needed</div>
        </div>
    </div>"""

    # -- Data Table --
    table_rows = ""
    for m in analyzed:
        trend_class = f"trend-{m['trend_direction']}"
        trend_arrow = {"up": "&#8593;", "down": "&#8595;", "flat": "&#8212;"}
        arrow = trend_arrow.get(m["trend_direction"], "")
        status_dot = f'<span class="status-dot status-{m["status"]}"></span>'

        table_rows += f"""
            <tr>
                <td class="metric-name">{html_module.escape(m['name'])}</td>
                <td class="metric-value">{html_module.escape(m['display_value'])}</td>
                <td>{html_module.escape(m['display_target'])}</td>
                <td>{html_module.escape(m['display_previous'])}</td>
                <td class="{trend_class}">{arrow} {html_module.escape(m['trend_text'])}</td>
                <td>{status_dot} {html_module.escape(m['target_text']) or '--'}</td>
            </tr>"""

    # -- Chart Section --
    chart_section = ""
    if bar_chart:
        chart_section = f"""
        <div class="section">
            <div class="section-title">Performance vs. Target</div>
            <div class="chart-container">
                {bar_chart}
            </div>
        </div>"""

    # -- Assemble full HTML --
    esc_title = html_module.escape(title)
    esc_business = html_module.escape(business_name)

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc_title} — {esc_business}</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            background: #0d1117;
            color: #e6edf3;
            padding: 32px;
            line-height: 1.5;
        }}

        .dashboard {{ max-width: 1200px; margin: 0 auto; }}

        /* --- Header --- */
        .header {{ margin-bottom: 32px; border-bottom: 1px solid #21262d; padding-bottom: 20px; }}
        .header h1 {{ font-size: 1.8rem; font-weight: 700; margin-bottom: 2px; }}
        .header .subtitle {{ color: #58a6ff; font-size: 1rem; font-weight: 500; margin-bottom: 8px; }}
        .header .meta {{ color: #8b949e; font-size: 0.85rem; }}

        /* --- Summary Grid --- */
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 32px;
        }}
        .summary-card {{
            background: #161b22;
            border: 1px solid #21262d;
            border-radius: 8px;
            padding: 16px;
            text-align: center;
        }}
        .summary-card.summary-good {{ border-left: 3px solid #238636; }}
        .summary-card.summary-warn {{ border-left: 3px solid #d29922; }}
        .summary-card.summary-bad {{ border-left: 3px solid #da3633; }}
        .summary-number {{ font-size: 2rem; font-weight: 700; }}
        .summary-label {{ font-size: 0.8rem; color: #8b949e; text-transform: uppercase; letter-spacing: 0.05em; }}

        /* --- KPI Cards --- */
        .section {{ margin-bottom: 36px; }}
        .section-title {{
            font-size: 1.1rem; font-weight: 600; margin-bottom: 16px;
            color: #e6edf3; padding-bottom: 8px; border-bottom: 1px solid #21262d;
        }}
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
        }}
        .kpi-card {{
            background: #161b22;
            border: 1px solid #21262d;
            border-radius: 8px;
            padding: 20px;
            border-top: 3px solid #21262d;
            transition: border-color 0.15s;
        }}
        .kpi-card.status-good {{ border-top-color: #238636; }}
        .kpi-card.status-warn {{ border-top-color: #d29922; }}
        .kpi-card.status-bad {{ border-top-color: #da3633; }}
        .kpi-card.status-neutral {{ border-top-color: #6e7681; }}
        .kpi-name {{
            font-size: 0.78rem; color: #8b949e; text-transform: uppercase;
            letter-spacing: 0.05em; margin-bottom: 8px;
        }}
        .kpi-value {{ font-size: 1.8rem; font-weight: 700; margin-bottom: 8px; }}
        .kpi-meta {{
            font-size: 0.8rem; color: #8b949e;
            display: flex; gap: 12px; flex-wrap: wrap; align-items: center;
        }}
        .kpi-target {{ color: #8b949e; }}

        /* --- Trend Indicators --- */
        .trend-up {{ color: #238636; }}
        .trend-down {{ color: #da3633; }}
        .trend-flat {{ color: #8b949e; }}

        /* --- Chart --- */
        .chart-container {{
            background: #161b22;
            border: 1px solid #21262d;
            border-radius: 8px;
            padding: 24px;
            overflow-x: auto;
        }}

        /* --- Data Table --- */
        table {{
            width: 100%;
            border-collapse: collapse;
            background: #161b22;
            border-radius: 8px;
            overflow: hidden;
        }}
        th {{
            background: #21262d;
            text-align: left;
            padding: 12px 16px;
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #8b949e;
            font-weight: 600;
        }}
        td {{
            padding: 12px 16px;
            border-top: 1px solid #21262d;
            font-size: 0.9rem;
        }}
        tr:hover {{ background: #1c2128; }}
        .metric-name {{ font-weight: 600; }}
        .metric-value {{ font-weight: 700; }}

        /* --- Status Dots --- */
        .status-dot {{
            display: inline-block; width: 8px; height: 8px;
            border-radius: 50%; margin-right: 6px; vertical-align: middle;
        }}
        .status-dot.status-good {{ background: #238636; }}
        .status-dot.status-warn {{ background: #d29922; }}
        .status-dot.status-bad {{ background: #da3633; }}
        .status-dot.status-neutral {{ background: #484f58; }}

        /* --- Footer --- */
        .footer {{
            margin-top: 48px;
            text-align: center;
            color: #484f58;
            font-size: 0.8rem;
            padding-top: 24px;
            border-top: 1px solid #21262d;
        }}
        .footer a {{ color: #58a6ff; text-decoration: none; }}
        .footer a:hover {{ text-decoration: underline; }}

        /* --- Responsive --- */
        @media (max-width: 768px) {{
            body {{ padding: 16px; }}
            .summary-grid {{ grid-template-columns: repeat(2, 1fr); }}
            .kpi-grid {{ grid-template-columns: 1fr; }}
        }}

        /* --- Print --- */
        @media print {{
            body {{ background: #fff; color: #1f2328; padding: 16px; font-size: 10pt; }}
            .dashboard {{ max-width: 100%; }}
            .kpi-card, .summary-card, .chart-container, table {{
                background: #fff; border-color: #d0d7de;
            }}
            th {{ background: #f6f8fa; color: #1f2328; }}
            td {{ border-color: #d0d7de; }}
            .kpi-name, .summary-label, .kpi-meta {{ color: #656d76; }}
            .header {{ border-color: #d0d7de; }}
            .section-title {{ border-color: #d0d7de; color: #1f2328; }}
            .footer {{ border-color: #d0d7de; color: #656d76; }}
            .trend-up {{ color: #1a7f37; }}
            .trend-down {{ color: #cf222e; }}
            .status-dot.status-good {{ background: #1a7f37; }}
            .status-dot.status-warn {{ background: #9a6700; }}
            .status-dot.status-bad {{ background: #cf222e; }}
        }}
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>{esc_title}</h1>
            <div class="subtitle">{esc_business}</div>
            <div class="meta">
                Generated {generated_at} &middot;
                {summary['total']} KPIs tracked &middot;
                {summary['good']} on track, {summary['warn']} monitoring, {summary['bad']} action needed
            </div>
        </div>

        {summary_html}

        <div class="section">
            <div class="section-title">KPI Scorecards</div>
            <div class="kpi-grid">{cards_html}
            </div>
        </div>

        {chart_section}

        <div class="section">
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
        </div>

        <div class="footer">
            <p>
                Generated by <a href="https://relaylaunch.com">Relay&#9659;Launch</a>
                KPI Dashboard Templates &middot;
                Operational clarity. Strategic momentum. Real results.
            </p>
        </div>
    </div>
</body>
</html>"""

    return page_html


# ---------------------------------------------------------------------------
# Sample CSV generation
# ---------------------------------------------------------------------------

def generate_sample_csv(output_path):
    """Generate a sample CSV file with realistic business metrics for testing."""
    rows = [
        ["metric", "value", "target", "previous", "unit"],
        ["Revenue", "847000", "900000", "756000", "$"],
        ["Gross Margin", "42.3", "44.0", "43.5", "%"],
        ["Net Profit", "124000", "135000", "98000", "$"],
        ["Cash on Hand", "1240000", "1000000", "1160000", "$"],
        ["New Customers", "34", "38", "29", "#"],
        ["Customer Churn Rate", "2.1", "2.0", "1.8", "%"],
        ["NPS Score", "67", "65", "62", "pts"],
        ["Revenue Per Employee", "18000", "19000", "17200", "$"],
        ["Conversion Rate", "3.2", "3.5", "2.9", "%"],
        ["Average Deal Size", "23100", "25000", "21800", "$"],
        ["Pipeline Coverage", "1.8", "2.5", "2.1", "x"],
        ["On-Time Delivery", "94.2", "95.0", "92.8", "%"],
        ["Error Rate", "1.8", "2.0", "2.2", "%"],
        ["Capacity Utilization", "78", "80", "73", "%"],
        ["Employee Satisfaction (eNPS)", "42", "45", "38", "pts"],
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"Sample CSV written to: {output_path}")
    print(f"  {len(rows) - 1} metrics included")
    print()
    print("Generate a dashboard from it:")
    print(f"  python csv-to-dashboard.py --input {output_path} --output dashboard.html")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Relay Launch — CSV to HTML Dashboard Generator. "
                    "Reads a CSV of business metrics and generates a standalone HTML dashboard.",
    )
    parser.add_argument(
        "--input", "-i", type=str,
        help="Path to input CSV file",
    )
    parser.add_argument(
        "--output", "-o", type=str, default="dashboard.html",
        help="Path for output HTML file (default: dashboard.html)",
    )
    parser.add_argument(
        "--title", "-t", type=str, default="Business KPI Dashboard",
        help="Dashboard title (default: 'Business KPI Dashboard')",
    )
    parser.add_argument(
        "--business", "-b", type=str, default="Relay Launch",
        help="Business name displayed on the dashboard (default: 'Relay Launch')",
    )
    parser.add_argument(
        "--sample", type=str,
        help="Generate a sample CSV file at this path (instead of building a dashboard)",
    )
    args = parser.parse_args()

    # Handle sample generation mode
    if args.sample:
        generate_sample_csv(args.sample)
        return

    # Require input for dashboard generation
    if not args.input:
        parser.print_help()
        print()
        print("Quick start:")
        print("  1. Generate a sample CSV:  python csv-to-dashboard.py --sample sample.csv")
        print("  2. Build the dashboard:    python csv-to-dashboard.py --input sample.csv")
        print("  3. Open dashboard.html in your browser")
        return

    # Read and validate metrics
    metrics = read_metrics(args.input)
    if not metrics:
        print("No metrics found in the CSV file.")
        print("Expected columns: metric, value, target, previous, unit")
        sys.exit(1)

    # Generate HTML
    html_content = generate_html(metrics, args.title, args.business)

    # Write output
    output_path = Path(args.output)
    output_path.write_text(html_content, encoding="utf-8")

    # Report results
    analyzed = [analyze_metric(m) for m in metrics]
    summary = compute_summary(analyzed)

    print(f"Dashboard generated: {output_path.resolve()}")
    print(f"  Metrics:      {summary['total']}")
    print(f"  On track:     {summary['good']}")
    print(f"  Monitoring:   {summary['warn']}")
    print(f"  Action needed:{summary['bad']}")
    print()
    print(f"Open in a browser:  file://{output_path.resolve()}")
    print()
    print("Generated by Relay Launch -- https://relaylaunch.com")


if __name__ == "__main__":
    main()
