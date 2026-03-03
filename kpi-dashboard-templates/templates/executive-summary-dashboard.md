# Executive Summary Dashboard — Template Spec

**By Relay▸Launch** | CEO & Leadership Team Dashboard

---

## Purpose

This dashboard gives the CEO and leadership team a weekly snapshot of business health. It should be the first thing opened on Monday morning and the primary reference in the weekly leadership meeting.

**Primary audience:** CEO, COO, CFO, department heads
**Decision frequency:** Weekly strategic, monthly planning
**Design priority:** Clarity and speed — comprehensible in under 10 seconds

---

## Layout Mockup

```
┌─────────────────────────────────────────────────────────────────────────┐
│  RELAY▸LAUNCH CLIENT — EXECUTIVE DASHBOARD          As of: 2026-02-27 │
│  Week 9 of 52  |  Fiscal Q1  |  Updated: Monday 8:00 AM               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌─────────────┐ │
│  │   REVENUE     │ │  GROSS MARGIN │ │   CASH ON     │ │  CUSTOMER   │ │
│  │    MTD        │ │               │ │    HAND       │ │   COUNT     │ │
│  │              │ │               │ │               │ │             │ │
│  │   $847K      │ │    42.3%      │ │   $1.24M      │ │   1,247     │ │
│  │   ▲ 12%      │ │    ▼ 1.2pp   │ │   ▲ $80K      │ │   ▲ 34      │ │
│  │  vs LM       │ │   vs LM      │ │   vs LM       │ │  net new    │ │
│  │              │ │               │ │               │ │             │ │
│  │  Target:$900K│ │  Target: 44%  │ │  Runway: 8mo  │ │ Target:1300 │ │
│  │  ████████░░  │ │  ████████░░░  │ │  ● Healthy    │ │ ████████░░  │ │
│  │     94%      │ │     96%       │ │               │ │    96%      │ │
│  └───────────────┘ └───────────────┘ └───────────────┘ └─────────────┘ │
│                                                                         │
├────────────────────────────────┬────────────────────────────────────────┤
│  REVENUE TREND (12 MONTHS)    │  REVENUE BY CHANNEL                    │
│                                │                                        │
│  $900K ┤                  ╭──  │  Direct Sales  ████████████████  62%   │
│  $800K ┤             ╭───╯    │  Partnerships  ████████░░░░░░░  24%   │
│  $700K ┤        ╭───╯        │  Inbound       ████░░░░░░░░░░░  11%   │
│  $600K ┤  ╭────╯             │  Other         █░░░░░░░░░░░░░░   3%   │
│  $500K ┤──╯                   │                                        │
│        └──┬──┬──┬──┬──┬──┬──  │  vs. Last Quarter:                     │
│        Mar   Jun   Sep   Dec  │  Direct    ▲ 8%                        │
│                                │  Partners  ▲ 15%                       │
│  ── Actual  ╌╌ Target         │  Inbound   ▼ 3%                        │
│                                │  Other     ── flat                     │
├────────────────────────────────┴────────────────────────────────────────┤
│  KEY METRICS SUMMARY                                                    │
│                                                                         │
│  Metric               Actual    Target    Status    Trend (8wk)        │
│  ─────────────────────────────────────────────────────────────────      │
│  Revenue MTD          $847K     $900K     ● Yellow  ▂▃▄▅▅▆▆▇          │
│  Gross Margin         42.3%     44.0%     ● Yellow  ▇▇▆▆▅▅▅▅          │
│  New Customers        34        38        ● Yellow  ▃▃▄▅▄▅▅▆          │
│  Churn Rate           2.1%      <2.0%     ● Red     ▃▃▃▃▄▄▅▅          │
│  NPS                  67        65        ● Green   ▅▅▅▆▆▆▇▇          │
│  Cash Position        $1.24M    >$1M      ● Green   ▅▅▅▅▅▆▆▆          │
│  Employee Headcount   47        50        ● Yellow  ▅▅▅▅▆▆▆▆          │
│  AR Aging >60 days    $42K      <$30K     ● Red     ▃▃▃▄▄▅▅▆          │
│                                                                         │
│  ● Green = On track   ● Yellow = Monitor   ● Red = Action needed       │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  ITEMS REQUIRING ATTENTION                                              │
│                                                                         │
│  1. Churn rate trending upward for 4 consecutive weeks. Q1 cohort      │
│     showing 15% higher 30-day churn than Q4. Customer Success team     │
│     investigating — initial finding points to onboarding gap in new    │
│     pricing tier. Action owner: VP Customer Success. Due: Mar 7.       │
│                                                                         │
│  2. AR aging >60 days increased $12K this month. Three accounts        │
│     represent 80% of the balance. Finance team following up.           │
│     Action owner: Controller. Due: Mar 5.                              │
│                                                                         │
│  3. Headcount 3 below plan. Two engineering roles open >45 days.       │
│     Recruiting pipeline has 4 candidates in final rounds.              │
│     Action owner: VP Engineering. Due: Mar 14.                         │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  NOTES & ANNOTATIONS                                                    │
│                                                                         │
│  • Revenue dip in Week 7 due to payment processor migration (2-day     │
│    delay in processing). Actual bookings were on track.                │
│  • Gross margin decline partially attributable to one-time vendor      │
│    cost increase; renegotiation in progress.                           │
│  • NPS survey response rate: 34% (target: 30%). Sample is reliable.   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Recommended Metrics

### Tier 1 — Headline Scorecards (Always Visible)

| Metric | Definition | Formula | Data Source |
|--------|-----------|---------|-------------|
| **Revenue MTD** | Total recognized revenue for the current month | SUM of invoiced/recognized revenue | Accounting system (QuickBooks, Xero, etc.) |
| **Gross Margin** | Revenue minus direct costs as a percentage | (Revenue - COGS) / Revenue x 100 | Accounting system |
| **Cash on Hand** | Current bank balance + liquid investments | Sum of operating accounts | Bank feed or manual entry |
| **Active Customers** | Count of customers with active subscriptions or contracts | COUNT of active customer records | CRM or billing system |

### Tier 2 — Key Metrics Table

| Metric | Definition | Formula | Data Source |
|--------|-----------|---------|-------------|
| **New Customers** | Net new customers acquired this period | New - Churned | CRM |
| **Customer Churn Rate** | Percentage of customers lost this period | Customers lost / Customers at start of period x 100 | CRM or billing system |
| **NPS Score** | Net Promoter Score from latest survey cycle | % Promoters - % Detractors | Survey tool (Delighted, Typeform, etc.) |
| **Employee Headcount** | Current full-time equivalent employees | Count of active employees | HRIS or payroll system |
| **AR Aging >60 Days** | Total accounts receivable past 60 days due | SUM of invoices with age > 60 days | Accounting system |
| **Revenue by Channel** | Revenue broken down by acquisition or delivery channel | SUM of revenue grouped by channel tag | CRM + Accounting system |

### Tier 3 — Drill-Down Detail (Secondary Tab/Page)

| Metric | Definition | Purpose |
|--------|-----------|---------|
| Revenue by product/service line | Revenue per offering | Identify growth and decline areas |
| Customer acquisition by source | New customers by marketing channel | Evaluate marketing spend allocation |
| Top 10 customers by revenue | Revenue concentration | Monitor customer dependency risk |
| Monthly burn rate | Total operating expenses per month | Cash management |
| Revenue per employee | Total revenue / headcount | Operational efficiency trend |
| Pipeline value | Weighted value of open opportunities | Forward-looking revenue indicator |

---

## Data Sources and Integration

### Primary Data Sources

| Source | What It Provides | Connection Method | Update Frequency |
|--------|-----------------|-------------------|-----------------|
| **Accounting System** (QuickBooks, Xero, FreshBooks) | Revenue, COGS, margins, AR aging, cash position | API integration or CSV export | Weekly (after Friday close) |
| **CRM** (HubSpot, Salesforce, Pipedrive) | Customer count, new customers, churn, pipeline | API integration | Daily (auto-sync) |
| **Bank Accounts** | Cash balances | Plaid integration or manual entry | Weekly |
| **HRIS / Payroll** (Gusto, Rippling, ADP) | Headcount, labor costs | CSV export | Monthly |
| **Survey Tool** (Delighted, Typeform, SurveyMonkey) | NPS, CSAT | API or manual entry | Monthly |

### Integration Approaches (Simplest to Most Complex)

1. **Manual entry in Google Sheets** — One person spends 30-60 minutes weekly pulling numbers from each source. Works for teams under 20. Low cost, high reliability if the owner is disciplined.

2. **Zapier / Make automations** — Automated data flows from source systems to Google Sheets. Medium setup effort, low ongoing maintenance. Works well for CRM and survey data.

3. **Looker Studio with native connectors** — Connect Looker Studio directly to Google Sheets (as a data warehouse), Google Analytics, or BigQuery. Best visual output, moderate setup.

4. **Custom scripts** — Use `sheets-kpi-tracker.py` (included in this collection) to automate Google Sheets creation and formatting. Most flexible, requires Python knowledge.

---

## Refresh Schedule

| Component | Refresh Timing | Owner | Method |
|-----------|---------------|-------|--------|
| Revenue MTD | Every Monday by 8:00 AM | Finance / Controller | Manual pull from accounting system |
| Cash position | Every Monday by 8:00 AM | Finance / Controller | Bank login or Plaid sync |
| Customer metrics | Every Monday by 8:00 AM | CRM Admin or RevOps | CRM export or API sync |
| NPS | First Monday of month | Customer Success | Survey tool export |
| Headcount | First Monday of month | HR / People Ops | HRIS export |
| AR Aging | Every Monday by 8:00 AM | Finance / Controller | Accounting system report |
| Annotations | Every Monday by 9:00 AM | Dashboard Owner | Manual entry based on context |

### Recommended Meeting Cadence

**Weekly Leadership Meeting (Monday, 30 minutes)**
- Review Tier 1 scorecards (5 minutes)
- Discuss red and yellow metrics (15 minutes)
- Review action items from last week (5 minutes)
- Assign new action items (5 minutes)

**Monthly Deep Dive (First Monday, 60 minutes)**
- All of the above, plus:
- Tier 3 drill-down review (15 minutes)
- Trend analysis: 3-month and 12-month trajectories (15 minutes)
- Target review: are current targets still appropriate? (5 minutes)

---

## Implementation Guide

### Google Sheets Implementation

**Tab 1: Dashboard** (the view shown in the mockup above)
- Use `IMPORTRANGE` or direct cell references to pull from data tabs
- Conditional formatting rules for status colors:
  - Green: actual >= 95% of target
  - Yellow: actual between 80% and 95% of target
  - Red: actual < 80% of target
- Sparklines: `=SPARKLINE(B2:M2, {"charttype","line";"linewidth",2;"color","#4285f4"})`
- Progress bars: `=REPT("█", ROUND(percentage*10, 0)) & REPT("░", 10-ROUND(percentage*10, 0))`

**Tab 2: Data Entry**
- Weekly data entry rows with date, metric, value columns
- Data validation on metric names (dropdown list)
- Conditional formatting to highlight missing entries

**Tab 3: Historical Data**
- Full historical record by week
- Formulas for WoW change, MoM change, YoY change
- Used as source for Tier 2 trend charts

**Tab 4: Definitions**
- Metric name, definition, formula, data source, owner, target, threshold definitions
- This tab is the source of truth for methodology questions

### Looker Studio Implementation

- **Page 1:** Scorecard widgets for Tier 1 metrics, time series chart for revenue trend, bar chart for channel breakdown
- **Page 2:** Key metrics table with conditional formatting, detail drill-downs
- **Page 3:** Historical trends with date range filter
- **Data source:** Google Sheets (the data entry and historical tabs)
- **Refresh:** Automatic when underlying Google Sheets data changes

---

## Customization Notes

### Adjusting for Business Type

**SaaS Companies:**
- Replace "Revenue MTD" with "MRR"
- Add "Net Revenue Retention" to Tier 1
- Replace "AR Aging" with "CAC Payback Period"

**E-Commerce:**
- Add "Conversion Rate" and "AOV" to Tier 1
- Replace "Active Customers" with "Monthly Active Customers" (transactional, not subscription)
- Add "Inventory Value" to Tier 2

**Professional Services:**
- Add "Billable Utilization" to Tier 1
- Replace "Active Customers" with "Active Engagements"
- Add "Backlog" to Tier 2

**Retail:**
- Add "Same-Store Sales" to Tier 1
- Add "Inventory Turnover" and "Sales Per Square Foot" to Tier 2
- Replace "AR Aging" with "Shrinkage Rate"

---

## Status Threshold Configuration

Customize these thresholds based on your business context:

```
METRIC              GREEN              YELLOW             RED
──────────────────────────────────────────────────────────────────
Revenue MTD         >= 95% of target   80-95% of target   < 80% of target
Gross Margin        >= target          Within 2pp          > 2pp below target
Cash Runway         > 6 months         3-6 months          < 3 months
New Customers       >= 90% of target   75-90% of target   < 75% of target
Churn Rate          <= target          Up to 1.5x target  > 1.5x target
NPS                 >= target          Within 10 points    > 10 points below
Headcount           Within 5% of plan  5-15% below plan   > 15% below plan
AR Aging >60d       <= target          Up to 1.5x target  > 1.5x target
```

---

*This template is part of the Relay▸Launch KPI Dashboard Templates collection. For implementation assistance, contact [relaylaunch.com](https://relaylaunch.com).*
