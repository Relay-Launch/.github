# Sales Pipeline Dashboard — Template Spec

**By Relay▸Launch** | Pipeline Visibility, Conversion Tracking & Revenue Forecasting

---

## Purpose

This dashboard gives sales leaders and their teams real-time visibility into the sales pipeline. It answers three questions that matter every single day:

1. **Do we have enough pipeline to hit our number?**
2. **Where are deals getting stuck?**
3. **What is our realistic revenue forecast for this period?**

**Primary audience:** VP Sales, Sales Manager, Account Executives, Revenue Operations
**Decision frequency:** Daily pipeline review, weekly forecast, monthly strategy
**Design priority:** Actionable detail with clear funnel visibility

---

## Layout Mockup

```
┌─────────────────────────────────────────────────────────────────────────┐
│  SALES PIPELINE DASHBOARD                           As of: 2026-02-27 │
│  Q1 FY2026  |  Week 9  |  Revenue Target: $2.7M  |  Updated: Live    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌─────────────┐ │
│  │  PIPELINE     │ │  WEIGHTED     │ │  CLOSED WON   │ │   CLOSE     │ │
│  │   VALUE       │ │  FORECAST     │ │    MTD        │ │   RATE      │ │
│  │              │ │               │ │               │ │             │ │
│  │   $4.82M     │ │   $1.93M      │ │   $1.41M      │ │   31.2%     │ │
│  │   ▲ 8%       │ │   ▲ $210K     │ │   52% of      │ │   ▼ 2.1pp   │ │
│  │  vs LM       │ │  vs last wk   │ │   target      │ │  vs LQ      │ │
│  │              │ │               │ │               │ │             │ │
│  │  Coverage:   │ │  Gap to       │ │  ████████░░░  │ │  Target:    │ │
│  │  1.8x target │ │  target: $770K│ │               │ │   35%       │ │
│  └───────────────┘ └───────────────┘ └───────────────┘ └─────────────┘ │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PIPELINE FUNNEL                        STAGE CONVERSION RATES          │
│                                                                         │
│  Lead/Prospect     ████████████████████████████████████  347 ($4.82M)  │
│                              ↓  72% advance                             │
│  Discovery         ██████████████████████████░░░░░░░░░  250 ($3.47M)  │
│                              ↓  56% advance                             │
│  Proposal Sent     █████████████████░░░░░░░░░░░░░░░░░░  140 ($2.18M)  │
│                              ↓  64% advance                             │
│  Negotiation       ███████████░░░░░░░░░░░░░░░░░░░░░░░░   90 ($1.52M)  │
│                              ↓  68% advance                             │
│  Closed Won        ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░   61 ($1.41M)  │
│                                                                         │
│  Closed Lost MTD: 42 deals ($680K)  |  Avg Loss Reason: Budget (38%)  │
│                                                                         │
├────────────────────────────────┬────────────────────────────────────────┤
│  DEAL VELOCITY                 │  FORECAST BREAKDOWN                    │
│                                │                                        │
│  Metric         Now    Target  │  Category        Amount    Confidence  │
│  ──────────────────────────── │  ──────────────────────────────────── │
│  Avg Deal Size  $23.1K  $25K  │  Closed Won      $1.41M    100%       │
│  Avg Sales      34 days  30d  │  Commit          $520K      90%       │
│    Cycle                       │  Best Case       $380K      60%       │
│  Leads/Month    85      100   │  Upside          $290K      25%       │
│  Win Rate       31.2%   35%   │  ──────────────────────────────────── │
│                                │  Weighted Total  $2.17M               │
│  Velocity:                     │  Gap to Target   ($530K)   ● Yellow  │
│  $56.3K/day                    │                                        │
│  Target: $65K/day              │  Coverage Ratio: 1.8x                  │
│  ● Yellow                      │  Healthy Range:  2.5-3.5x  ● Red     │
│                                │                                        │
├────────────────────────────────┴────────────────────────────────────────┤
│  PIPELINE BY REP                                                        │
│                                                                         │
│  Rep             Pipeline  Weighted  Closed   % of     Win    Avg      │
│                   Value    Forecast  Won MTD  Quota    Rate   Cycle    │
│  ────────────────────────────────────────────────────────────────────  │
│  Sarah Chen      $1.24M    $496K    $412K     61%  ●  38%    28d      │
│  Marcus Johnson  $1.08M    $432K    $380K     56%  ●  33%    31d      │
│  Priya Patel     $890K     $356K    $295K     44%  ●  29%    38d  ●   │
│  David Kim       $820K     $328K    $220K     33%  ●  25%    42d  ●   │
│  Lisa Torres     $770K     $308K    $103K     15%  ●  27%    34d      │
│                                                                         │
│  ● = On track (>50% of quota)   ● = Monitor (30-50%)   ● = At risk    │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  DEALS REQUIRING ATTENTION                                              │
│                                                                         │
│  ⚠ Stale Deals (>14 days no activity):                                 │
│    • Acme Corp — $85K — Negotiation — Last activity: Feb 10            │
│    • GlobalTech — $62K — Proposal Sent — Last activity: Feb 8          │
│    • Riverside Mfg — $45K — Discovery — Last activity: Feb 5           │
│                                                                         │
│  ⚠ Closing This Week (in Negotiation stage):                           │
│    • DataFlow Inc — $120K — Expected close: Feb 28 — Owner: S. Chen   │
│    • Summit Health — $78K — Expected close: Mar 3 — Owner: M. Johnson │
│    • BrightPath — $55K — Expected close: Mar 1 — Owner: P. Patel     │
│                                                                         │
│  ⚠ Slipped Deals (past expected close date):                           │
│    • NorthStar Labs — $95K — Expected: Feb 14 — 13 days overdue      │
│    • ClearView — $42K — Expected: Feb 21 — 6 days overdue            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Recommended Metrics

### Tier 1 — Headline Scorecards

| Metric | Definition | Formula | Why It Matters |
|--------|-----------|---------|----------------|
| **Total Pipeline Value** | Sum of all open opportunity values across all stages | `SUM(opportunity_amount) WHERE stage != Closed` | Shows whether you have enough raw pipeline to work |
| **Weighted Forecast** | Pipeline value adjusted by stage-based win probability | `SUM(opportunity_amount x stage_probability)` | More realistic revenue prediction than raw pipeline |
| **Closed Won MTD** | Revenue closed this month/quarter | `SUM(opportunity_amount) WHERE stage = 'Closed Won' AND close_date in current period` | Progress toward target |
| **Win Rate** | Percentage of opportunities that close successfully | `Closed Won / (Closed Won + Closed Lost) x 100` | Overall sales effectiveness |

### Tier 2 — Funnel and Velocity

| Metric | Definition | Formula |
|--------|-----------|---------|
| **Stage Conversion Rates** | Percentage of deals advancing from one stage to the next | `Deals entering next stage / Deals entering current stage x 100` |
| **Average Deal Size** | Mean value of closed-won deals | `Total closed-won revenue / Number of closed-won deals` |
| **Average Sales Cycle** | Mean days from opportunity creation to close | `AVG(close_date - created_date) for closed-won deals` |
| **Pipeline Velocity** | Revenue throughput of the pipeline per day | `(Number of deals x Win Rate x Avg Deal Size) / Avg Sales Cycle` |
| **Pipeline Coverage Ratio** | Multiple of pipeline to target | `Total Pipeline Value / Revenue Target` |
| **Leads per Month** | New opportunities entering the pipeline | `COUNT of new opportunities created in period` |

### Tier 3 — Rep and Deal Detail

| Metric | Definition | Purpose |
|--------|-----------|---------|
| **Pipeline by Rep** | Each rep's open pipeline value and weighted forecast | Coaching and resource allocation |
| **Quota Attainment by Rep** | Each rep's closed revenue vs. individual quota | Performance management |
| **Stale Deal Count** | Deals with no logged activity in 14+ days | Pipeline hygiene |
| **Deals by Loss Reason** | Categorized reasons for closed-lost deals | Product and positioning feedback |
| **Average Discount Rate** | Mean discount given on closed deals | Pricing discipline |
| **Time in Stage** | Average days spent in each pipeline stage | Bottleneck identification |

---

## Pipeline Stage Definitions

Define these clearly and ensure the entire sales team agrees on when a deal moves between stages. Ambiguous stage definitions are the number one cause of unreliable forecasts.

| Stage | Definition | Entry Criteria | Exit Criteria | Probability Weight |
|-------|-----------|---------------|---------------|-------------------|
| **Lead / Prospect** | Initial contact or inbound inquiry. Not yet qualified. | Any new lead or outbound target | Qualification call completed | 10% |
| **Discovery** | Qualified opportunity. Understanding needs, budget, timeline, and authority. | BANT or MEDDIC qualification passed | Pain point confirmed, stakeholders identified, timeline established | 25% |
| **Proposal Sent** | Formal proposal or quote delivered to the prospect. | Decision maker has seen proposal | Prospect provides feedback on proposal | 50% |
| **Negotiation** | Active discussion on terms, pricing, scope, or contract details. | Prospect is negotiating (not stalling) | Verbal commitment or rejection | 75% |
| **Closed Won** | Deal signed and revenue recognized or contract executed. | Signed agreement received | — | 100% |
| **Closed Lost** | Opportunity is dead. Reason logged. | Prospect declined or went dark after defined follow-up cadence | — | 0% |

### Stage Probability Notes

The probability weights above are starting points. After 6 months of data, replace them with your actual historical conversion rates. If your Discovery-to-Proposal rate is actually 45% (not the assumed 50%), update the model. Forecast accuracy depends entirely on these probabilities being calibrated to your real data.

---

## Deal Velocity Formula

Pipeline velocity tells you how much revenue your pipeline generates per day. It is the single best predictor of whether you will hit your target.

```
                 Number of Deals x Win Rate (%) x Average Deal Size ($)
Velocity ($/day) = ───────────────────────────────────────────────────────
                              Average Sales Cycle (days)
```

**Example:**
```
90 qualified deals x 31.2% win rate x $23,100 avg deal size
─────────────────────────────────────────────────────────── = $18,963/day
                     34 days avg cycle
```

**Monthly velocity:** $18,963 x 30 = $568,890

If your monthly target is $675,000, you need to increase one or more of the four inputs:
- More deals entering the pipeline
- Higher win rate (better qualification, better selling)
- Larger deal sizes (upselling, better targeting)
- Shorter sales cycles (faster follow-up, better process)

---

## Forecast Categories

Use a structured forecast methodology rather than relying on individual rep optimism:

| Category | Definition | Criteria | Confidence |
|----------|-----------|----------|------------|
| **Closed** | Signed, booked revenue | Contract executed | 100% |
| **Commit** | Rep commits this will close in the period | Verbal agreement, procurement engaged, no known blockers | 85-95% |
| **Best Case** | Strong opportunity likely to close in period | Proposal sent, positive signals, but not yet committed | 50-70% |
| **Upside** | Possible but not counted in plan | Early stage or uncertain timing | 15-30% |
| **Omitted** | In pipeline but not forecast for this period | Will not close this period | 0% for current period |

### Building the Forecast

```
Forecast = Closed + (Commit x 0.90) + (Best Case x 0.60) + (Upside x 0.25)
```

Review and recategorize deals weekly. The forecast should narrow over the course of the quarter:
- Week 1-4: Wide spread between Best Case and Commit
- Week 5-8: Spread narrows as deals advance or stall
- Week 9-12: Most revenue should be in Closed or Commit

### Forecast Accuracy Tracking

Track forecast accuracy over time to improve:

```
Forecast Accuracy = 1 - ABS(Forecast - Actual) / Actual
```

Target: >80% accuracy by week 8 of the quarter. If accuracy is consistently below 70%, investigate stage definitions, probability weights, and rep forecasting discipline.

---

## Data Sources

| Source | What It Provides | Connection |
|--------|-----------------|------------|
| **CRM** (HubSpot, Salesforce, Pipedrive, Close) | Opportunities, stages, amounts, activities, close dates | API or native reporting |
| **Email / Calendar** | Activity tracking, meeting counts | CRM integration or Zapier |
| **Proposal Tool** (PandaDoc, Proposify, DocuSign) | Proposal sent dates, view tracking, signature status | CRM integration |
| **Marketing Automation** (HubSpot, Mailchimp, ActiveCampaign) | Lead source attribution, campaign performance | CRM integration |
| **Accounting System** | Actual booked revenue for closed-won verification | Manual reconciliation or API |

### CRM Hygiene Requirements

This dashboard is only as good as the CRM data. Enforce these rules:

1. **Every deal has an amount.** No $0 or blank amounts in the pipeline.
2. **Every deal has an expected close date.** Updated at least weekly.
3. **Stage changes are logged.** Automatic in most CRMs; verify it is on.
4. **Activity is logged.** At minimum: calls, emails, meetings. Automatic logging preferred.
5. **Closed-lost deals have a reason.** Mandatory field. Standardized picklist, not free text.
6. **Pipeline is reviewed weekly.** Stale deals (>30 days no activity) are either updated or closed.

---

## Refresh Schedule

| Component | Refresh | Owner |
|-----------|---------|-------|
| Pipeline values and stages | Real-time (CRM sync) | CRM auto-sync |
| Forecast categories | Weekly (Friday afternoon) | Each rep + manager review |
| Win rate and velocity calculations | Weekly (Monday morning) | RevOps or Sales Manager |
| Rep quota attainment | Weekly | RevOps or Sales Manager |
| Stale deal alerts | Daily (automated) | CRM automation |
| Loss reason analysis | Monthly | Sales Manager |

### Meeting Cadence

**Daily Standup (15 minutes)**
- Quick scan of Tier 1 scorecards
- Any deals closing today/this week?
- Any deals stuck or at risk?

**Weekly Pipeline Review (45 minutes)**
- Full funnel review by stage
- Forecast recategorization
- Stale deal cleanup
- Rep-level pipeline discussion

**Monthly Sales Review (60 minutes)**
- Win/loss analysis
- Conversion rate trends
- Velocity trends
- Quota and territory adjustments
- Pipeline generation assessment (is marketing delivering enough leads?)

---

## Implementation: Google Sheets

### Tab Structure

**Tab 1: Dashboard** — The visual layout shown in the mockup
**Tab 2: Pipeline Data** — Raw deal data exported from CRM (or connected via Zapier)
**Tab 3: Rep Quotas** — Individual rep targets and quota data
**Tab 4: Historical** — Weekly snapshots for trend calculation
**Tab 5: Definitions** — Stage definitions, probability weights, metric formulas

### Key Formulas

**Weighted Pipeline:**
```
=SUMPRODUCT(pipeline_amounts, stage_probabilities)
```

**Win Rate:**
```
=COUNTIFS(stage, "Closed Won") / (COUNTIFS(stage, "Closed Won") + COUNTIFS(stage, "Closed Lost"))
```

**Average Sales Cycle:**
```
=AVERAGEIFS(cycle_days, stage, "Closed Won", close_date, ">=" & start_of_period)
```

**Pipeline Coverage:**
```
=SUM(pipeline_amounts) / quarterly_target
```

**Velocity:**
```
=(COUNTA(open_deals) * win_rate * avg_deal_size) / avg_sales_cycle
```

### Conditional Formatting Rules

| Element | Green | Yellow | Red |
|---------|-------|--------|-----|
| Pipeline coverage | >= 3.0x | 2.0-3.0x | < 2.0x |
| Win rate | >= target | Within 5pp of target | > 5pp below target |
| Rep quota attainment | >= 50% at midpoint | 35-50% at midpoint | < 35% at midpoint |
| Deal age (days in stage) | < avg for stage | 1-2x avg for stage | > 2x avg for stage |
| Sales cycle | <= target | Up to 1.3x target | > 1.3x target |

---

## Common Pipeline Dashboard Mistakes

1. **Counting pipeline that is not real.** If a deal has been in "Discovery" for 6 months with no activity, it is not pipeline. It is wishful thinking. Enforce pipeline hygiene.

2. **Not distinguishing pipeline coverage by time horizon.** Having 3x coverage is great for this quarter. Having 3x coverage for next quarter is meaningless if 80% of it is early-stage.

3. **Averaging win rate across all reps.** A team win rate of 30% might mask one rep at 50% and another at 10%. Show rep-level data.

4. **Ignoring deal age.** A $100K deal that has been in negotiation for 90 days is not a $100K deal. It is either a $0 loss or a deal with a serious blocker. Age decay should reduce weighted value.

5. **Forecast = Pipeline x Probability.** This is a starting point, not a forecast. Real forecasting requires judgment calls on individual deals layered on top of the math.

---

*This template is part of the Relay▸Launch KPI Dashboard Templates collection. For implementation assistance, contact [relaylaunch.com](https://relaylaunch.com).*
