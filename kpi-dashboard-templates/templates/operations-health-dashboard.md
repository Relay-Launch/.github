# Operations Health Dashboard — Template Spec

**By Relay▸Launch** | Process Efficiency, Throughput & Capacity Management

---

## Purpose

This dashboard gives operations leaders visibility into the health and efficiency of their core business processes. It answers:

1. **Are we delivering on time and at the quality level we promised?**
2. **Where are the bottlenecks and failure points in our processes?**
3. **Do we have the capacity to handle current and projected demand?**

Unlike the executive dashboard (which answers "how is the business doing?") and the sales dashboard (which answers "will we hit our number?"), this dashboard answers "are we running well?" It is the early warning system for delivery problems, quality degradation, and capacity constraints.

**Primary audience:** COO, Operations Manager, Team Leads, Process Owners
**Decision frequency:** Daily operational, weekly tactical, monthly strategic
**Design priority:** Anomaly detection — surface problems fast so they can be addressed before they impact customers

---

## Layout Mockup

```
┌─────────────────────────────────────────────────────────────────────────┐
│  OPERATIONS HEALTH DASHBOARD                        As of: 2026-02-27 │
│  Updated: Every 4 hours  |  Owner: Operations Manager                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  OVERALL HEALTH:  ████████████████████████████████░░░░  87/100  ● Good │
│                                                                         │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌─────────────┐ │
│  │  ON-TIME      │ │  ERROR /      │ │  CAPACITY     │ │  THROUGHPUT │ │
│  │  DELIVERY     │ │  DEFECT RATE  │ │  UTILIZATION  │ │             │ │
│  │               │ │               │ │               │ │             │ │
│  │   94.2%       │ │    1.8%       │ │    78%        │ │  342/day    │ │
│  │   ▲ 1.3pp     │ │    ▼ 0.4pp   │ │    ▲ 5pp      │ │   ▲ 12%    │ │
│  │  vs LW        │ │   vs LW      │ │   vs LW       │ │  vs LW     │ │
│  │               │ │               │ │               │ │             │ │
│  │  Target: 95%  │ │  Target:<2.0% │ │  Sweet: 70-85%│ │ Max: 420/d │ │
│  │  ● Yellow     │ │  ● Green      │ │  ● Green      │ │ ● Green    │ │
│  └───────────────┘ └───────────────┘ └───────────────┘ └─────────────┘ │
│                                                                         │
├────────────────────────────────┬────────────────────────────────────────┤
│  PROCESS EFFICIENCY            │  THROUGHPUT TREND (12 WEEKS)           │
│                                │                                        │
│  Process        Cycle   Target │  420 ┤              ┌──  Max Capacity  │
│                  Time          │  380 ┤         ╭───╯                   │
│  ──────────────────────────── │  340 ┤    ╭───╯        ← Current      │
│  Order Fulfill.  2.4d   2.0d  │  300 ┤───╯                             │
│    ● Yellow      ▂▃▃▃▄▄▅▅    │  260 ┤                                  │
│                                │  220 ┤                                  │
│  Customer Onb.   5.1d   5.0d  │      └──┬──┬──┬──┬──┬──┬──┬──┬──┬──  │
│    ● Yellow      ▅▅▅▅▅▅▅▅    │      W1    W3    W5    W7    W9   W12  │
│                                │                                        │
│  Support Res.    3.8h   4.0h  │  ── Actual  ╌╌ Capacity Ceiling       │
│    ● Green       ▅▅▄▄▃▃▃▃    │  ▓▓ Demand Forecast (next 4 weeks)    │
│                                │                                        │
│  Invoice Proc.   1.2d   1.5d  │                                        │
│    ● Green       ▅▄▃▃▃▂▂▂    │                                        │
│                                │                                        │
│  Quality Review  3.2d   3.0d  │                                        │
│    ● Yellow      ▃▃▃▄▄▄▅▅    │                                        │
│                                │                                        │
├────────────────────────────────┴────────────────────────────────────────┤
│                                                                         │
│  ERROR / DEFECT ANALYSIS                                                │
│                                                                         │
│  Error Category           Count   % of Total   Trend (8wk)   Status    │
│  ────────────────────────────────────────────────────────────────────  │
│  Data Entry Errors          12      28.6%       ▅▅▄▃▃▃▃▃     ● Green  │
│  Shipping/Delivery Errors    9      21.4%       ▃▃▃▃▄▄▅▅     ● Yellow │
│  Process Compliance          7      16.7%       ▃▃▃▃▃▃▃▃     ● Green  │
│  System/Technical Errors     6      14.3%       ▃▃▃▃▃▃▅▇     ● Red    │
│  Communication Gaps          5      11.9%       ▅▄▃▃▃▃▃▃     ● Green  │
│  Other                       3       7.1%       ▃▃▃▃▃▃▃▃     ● Green  │
│  ────────────────────────────────────────────────────────────────────  │
│  Total Errors This Week:    42      Error Rate: 1.8%                   │
│  Total Units Processed:  2,394      Prior Week: 2.2%                   │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  CAPACITY PLANNING                                                      │
│                                                                         │
│  Resource / Process      Current    Max       Utilization   Headroom   │
│  ────────────────────────────────────────────────────────────────────  │
│  Production Team (FTE)      8.0      10.0       80%          2.0 FTE  │
│  Warehouse (orders/day)     342       420       81%          78/day    │
│  Support Queue (tickets/d)   67        85       79%          18/day   │
│  Server Capacity (req/s)   4,200    6,000       70%          1,800    │
│  Shipping Dock (pallets/d)   24        30       80%          6/day    │
│  ────────────────────────────────────────────────────────────────────  │
│                                                                         │
│  ⚠ Projected Capacity Breach:                                          │
│    Warehouse throughput will exceed 90% utilization by Week 14 if      │
│    current growth trend (8% WoW) continues. Recommend contingency     │
│    planning by Mar 14. Owner: Warehouse Manager.                       │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  SLA COMPLIANCE                                                         │
│                                                                         │
│  SLA                         Target    Actual    Status   Streak       │
│  ────────────────────────────────────────────────────────────────────  │
│  Order shipped within 24h     95%      94.2%    ● Yellow  Missed 2wk  │
│  Support response < 1h        90%      93.1%    ● Green   Met 8wk     │
│  Support resolution < 4h      85%      87.4%    ● Green   Met 5wk     │
│  Invoice accuracy             99%      99.6%    ● Green   Met 12wk    │
│  Onboarding < 5 business d    90%      88.7%    ● Yellow  Missed 1wk  │
│  System uptime                99.9%    99.97%   ● Green   Met 26wk    │
│                                                                         │
│  SLA Breach Log (Last 7 Days):                                         │
│    • Feb 25: 3 orders shipped late — root cause: supplier delay        │
│    • Feb 24: 2 onboardings exceeded 5 days — pending client docs      │
│    • Feb 22: 4 orders shipped late — root cause: staffing shortage    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Recommended Metrics

### Tier 1 — Headline Health Indicators

| Metric | Definition | Formula | Target Guidance |
|--------|-----------|---------|-----------------|
| **On-Time Delivery Rate** | Percentage of orders/deliverables completed by the promised date | `(Units delivered on time / Total units delivered) x 100` | 95%+ for most operations. Below 90% is a red flag. |
| **Error / Defect Rate** | Percentage of output with quality issues requiring rework or correction | `(Units with errors / Total units processed) x 100` | Below 2% for most operations. Six Sigma target is 0.00034%. Be realistic about your starting point. |
| **Capacity Utilization** | Percentage of total capacity currently in use | `(Actual output / Maximum possible output) x 100` | 70-85% is the sweet spot. Below 60% means waste. Above 90% means no buffer for spikes. |
| **Throughput** | Total units of work completed per period | `COUNT of completed work units per period` | Context-dependent. Track trend and compare to capacity ceiling. |

### Tier 2 — Process Efficiency

| Metric | Definition | Formula |
|--------|-----------|---------|
| **Cycle Time** | Time from start to completion of a process | `AVG(completion_timestamp - start_timestamp)` |
| **Lead Time** | Time from customer request to delivery (includes wait time) | `AVG(delivery_timestamp - request_timestamp)` |
| **First Pass Yield** | Percentage of units that pass quality check on first attempt without rework | `(Units passing first check / Total units checked) x 100` |
| **Rework Rate** | Percentage of completed work that requires correction | `(Units requiring rework / Total units completed) x 100` |
| **Process Compliance Rate** | Percentage of process steps completed according to SOP | `(Compliant process instances / Total process instances) x 100` |
| **Cost Per Unit** | Total operational cost divided by units produced | `Total operational costs / Total units completed` |

### Tier 3 — Deep Diagnostic Metrics

| Metric | Definition | Purpose |
|--------|-----------|---------|
| **Bottleneck Identification** | Which process step has the longest queue or wait time | Pinpoint where work gets stuck |
| **Error by Category** | Breakdown of errors by type (data entry, shipping, system, etc.) | Direct root cause analysis |
| **Overtime Hours** | Hours worked beyond standard schedule | Early warning for burnout and understaffing |
| **Equipment/System Downtime** | Time critical systems or equipment are unavailable | Infrastructure reliability |
| **Employee Productivity** | Units completed per employee per period | Staffing and training effectiveness |
| **Backlog Age** | Age distribution of pending work items | Queue health and prioritization |
| **Customer Complaints** | Volume and category of customer complaints | External quality signal |

---

## Process Efficiency Framework

### Measuring Cycle Time Properly

Cycle time is one of the most misunderstood metrics. It is not just "how long the work takes." It includes three components:

```
Cycle Time = Processing Time + Wait Time + Rework Time

Where:
  Processing Time = Active hands-on-keyboard or hands-on-product time
  Wait Time       = Time spent in queues, awaiting approvals, or blocked
  Rework Time     = Time spent correcting errors from the first pass
```

In most operations, wait time is 60-80% of total cycle time. This means the biggest improvement opportunity is usually reducing wait time (better handoffs, faster approvals, smaller batch sizes), not making people work faster.

### Process Efficiency Ratio

```
Efficiency Ratio = Processing Time / Total Cycle Time x 100
```

| Rating | Efficiency Ratio | Interpretation |
|--------|-----------------|----------------|
| Excellent | > 50% | More than half the time is productive work |
| Good | 30-50% | Typical for well-managed operations |
| Needs improvement | 15-30% | Significant wait time or rework |
| Poor | < 15% | Process is mostly waiting — redesign needed |

---

## Error Rate Analysis

### Categorization Framework

Standardize your error categories. This taxonomy works for most operations:

| Category | Examples | Typical Root Causes |
|----------|---------|-------------------|
| **Human / Data Entry** | Typos, wrong quantities, incorrect addresses | Training gaps, fatigue, poor UI design |
| **Process / Compliance** | Skipped steps, out-of-sequence execution | Unclear SOPs, lack of checklists, shortcuts under pressure |
| **System / Technical** | Software bugs, integration failures, hardware issues | Technical debt, insufficient testing, infrastructure gaps |
| **Communication** | Miscommunication between teams, missed handoffs | Unclear ownership, poor documentation, tool fragmentation |
| **External / Vendor** | Supplier errors, shipping carrier issues | Vendor quality, insufficient vendor management |
| **Planning / Capacity** | Overcommitment, missed deadlines due to insufficient resources | Forecasting errors, inadequate capacity planning |

### Error Cost Estimation

Not all errors are equal. Track the cost of each error type:

```
Error Cost = Direct Rework Cost + Customer Impact Cost + Opportunity Cost

Where:
  Direct Rework Cost    = Labor hours to fix x hourly rate + material costs
  Customer Impact Cost  = Credits issued + churn risk + support costs
  Opportunity Cost      = Revenue from work that could have been done instead
```

This lets you prioritize error reduction efforts by economic impact, not just frequency.

### Error Trend Analysis

A flat error rate is not necessarily good if volume is growing. Track both:

- **Absolute error count:** Total errors per period (is the problem growing?)
- **Error rate:** Errors as percentage of total units (is the rate improving?)
- **Error rate by category:** Which types are improving and which are getting worse?

---

## Capacity Utilization

### The Utilization Sweet Spot

```
  0%          60%      70%        85%     90%        100%
  |───────────|────────|──────────|───────|──────────|
  Waste       Caution  ◄ Sweet ► Caution  Danger
                        Spot
```

- **Below 60%:** You are paying for capacity you are not using. Either reduce capacity (staff, space, equipment) or find ways to increase demand.
- **60-70%:** Acceptable for volatile workloads with seasonal peaks.
- **70-85%:** Optimal range. Enough capacity to handle normal variation and small spikes without overtime or degraded quality.
- **85-90%:** Caution zone. Small demand increases will push you into overtime and quality risk.
- **Above 90%:** Danger zone. No buffer for spikes. Quality degrades, staff burns out, delivery timelines slip.

### Capacity Planning Table

Track capacity across all constrained resources:

| Resource | Unit of Measure | Current Capacity | Current Demand | Utilization | Growth Rate | Weeks Until 90% |
|----------|----------------|-----------------|----------------|-------------|-------------|-----------------|
| Production team | Orders/day | 420 | 342 | 81% | +8%/week | 6 weeks |
| Support queue | Tickets/day | 85 | 67 | 79% | +5%/week | 11 weeks |
| Warehouse space | Pallets | 500 | 380 | 76% | +3%/week | 18 weeks |

The "Weeks Until 90%" column is the most important one. It tells you when you need to add capacity, which informs hiring timelines, lease negotiations, and equipment purchases.

```
Weeks Until X% = (Target Utilization - Current Utilization) / Weekly Growth Rate in Utilization Points
```

---

## SLA Compliance Tracking

### Defining SLAs

Every SLA needs five components:

1. **Metric:** What exactly is being measured (e.g., "time from order received to order shipped")
2. **Target:** The threshold (e.g., "within 24 hours")
3. **Measurement method:** How you calculate it (e.g., "timestamp difference between order confirmation and shipping label creation")
4. **Scope:** What is included and excluded (e.g., "excludes weekends and holidays, excludes custom orders")
5. **Consequence:** What happens when the SLA is breached (e.g., "customer notified proactively, root cause logged, credit offered if applicable")

### SLA Dashboard Elements

For each SLA, show:

```
┌─────────────────────────────────────────────────────┐
│  ORDER SHIPMENT SLA                                  │
│                                                      │
│  Target: 95% of orders shipped within 24 hours       │
│  Current: 94.2%  ● Yellow (within 1pp of target)    │
│  Trend: ▅▅▅▆▆▅▅▅  (8-week)                         │
│  Streak: Missed target 2 consecutive weeks           │
│  Worst day this week: Tuesday (89.1% — staffing)     │
│  Best day this week: Thursday (97.8%)                │
│                                                      │
│  Breach Log:                                         │
│  • 9 orders shipped late this week                   │
│  • Root causes: Supplier delay (5), Staffing (3),   │
│    System issue (1)                                  │
└─────────────────────────────────────────────────────┘
```

---

## Data Sources

| Source | What It Provides | Connection |
|--------|-----------------|------------|
| **Project Management** (Asana, Monday, Jira, Trello) | Task completion times, backlog, throughput | API or CSV export |
| **ERP / Order Management** (NetSuite, SAP, custom) | Order processing times, fulfillment data | API or database query |
| **Helpdesk** (Zendesk, Freshdesk, Intercom) | Ticket volume, response times, resolution times | API or native reporting |
| **Warehouse Management** (ShipStation, ShipBob, custom) | Shipping data, fulfillment times, error rates | API or CSV export |
| **Quality Tracking** (spreadsheet, custom tool) | Error logs, inspection results, rework tracking | Manual entry or API |
| **HR / Time Tracking** (Gusto, Toggl, Harvest) | Hours worked, overtime, headcount | API or CSV export |
| **Infrastructure Monitoring** (Datadog, UptimeRobot, Pingdom) | System uptime, performance metrics | API or webhook alerts |

---

## Refresh Schedule

| Component | Frequency | Owner | Method |
|-----------|-----------|-------|--------|
| Throughput and volume | Every 4 hours or real-time | Ops system auto-sync | Automated |
| Error/defect counts | Daily (end of day) | Quality lead | Manual entry or automated from QA system |
| Cycle times | Daily | Process owner | Automated from task management tool |
| Capacity utilization | Daily | Ops manager | Calculated from throughput + capacity data |
| SLA compliance | Daily | Ops manager | Automated from source systems |
| Capacity forecast | Weekly (Monday) | Ops manager | Manual calculation based on trend |
| Root cause analysis | Within 24h of any breach | Relevant team lead | Manual entry in breach log |

### Meeting Cadence

**Daily Ops Standup (10 minutes)**
- Scan Tier 1 scorecards
- Any SLA breaches in last 24 hours?
- Any capacity concerns today?
- Any blocked work items?

**Weekly Ops Review (30 minutes)**
- Tier 1 and Tier 2 metrics review
- Error trend analysis
- Capacity forecast update
- Process improvement action items

**Monthly Ops Deep Dive (60 minutes)**
- Full metric review including Tier 3
- Root cause analysis patterns
- Cost per unit trends
- Capacity planning for next quarter
- Process improvement priorities

---

## Implementation: Google Sheets

### Tab Structure

**Tab 1: Dashboard** — Visual layout from mockup
**Tab 2: Daily Log** — Daily data entry for throughput, errors, cycle times
**Tab 3: Error Log** — Individual error records with category, root cause, resolution
**Tab 4: Capacity Model** — Resource capacities, current demand, projections
**Tab 5: SLA Tracker** — SLA definitions, daily compliance data, breach log
**Tab 6: Historical** — Weekly rollups for trend calculations
**Tab 7: Definitions** — Metric definitions, SLA specs, category taxonomies

### Key Formulas

**On-Time Delivery Rate:**
```
=COUNTIFS(delivery_status, "On Time") / COUNTA(delivery_status)
```

**Error Rate:**
```
=COUNTIFS(error_log_date, ">=" & week_start, error_log_date, "<=" & week_end) / SUM(daily_throughput_range)
```

**Capacity Utilization:**
```
=SUM(actual_throughput_range) / (max_capacity * working_days_in_period)
```

**Weeks Until 90% Utilization:**
```
=IF(weekly_growth_rate > 0, (0.90 - current_utilization) / weekly_growth_rate, "N/A")
```

**Composite Health Score (0-100):**
```
= (on_time_rate / target_on_time * 25)
+ ((1 - error_rate) / (1 - target_error_rate) * 25)
+ (IF(utilization >= 0.7, IF(utilization <= 0.85, 1, (0.95 - utilization) / 0.10), utilization / 0.7) * 25)
+ (throughput / target_throughput * 25)
```

### Conditional Formatting

| Element | Green | Yellow | Red |
|---------|-------|--------|-----|
| On-Time Delivery | >= 95% | 90-95% | < 90% |
| Error Rate | < target | Target to 1.5x target | > 1.5x target |
| Utilization | 70-85% | 60-70% or 85-90% | < 60% or > 90% |
| Cycle Time | <= target | 1.0-1.3x target | > 1.3x target |
| SLA Compliance | >= target | Within 2pp of target | > 2pp below target |

---

## Operational Health Score

The composite health score in the dashboard header (87/100 in the mockup) is calculated by weighting the four Tier 1 metrics:

| Component | Weight | Scoring |
|-----------|--------|---------|
| On-Time Delivery | 30% | Linear scale: 100% delivery = 30 points, 90% = 27, etc. |
| Error Rate | 25% | Inverse scale: 0% errors = 25 points, target rate = 22.5, etc. |
| Capacity Utilization | 20% | Bell curve: 77.5% (midpoint of sweet spot) = 20, decreasing toward 0% and 100% |
| Throughput vs. Target | 25% | Linear scale: 100% of target = 25 points, capped at 25 |

This gives you a single number that represents overall operational health. It is a communication tool, not a diagnostic tool. When the score drops, drill into the components to find the cause.

---

## Common Operations Dashboard Mistakes

1. **Measuring activity instead of outcomes.** "Number of emails sent" is activity. "Orders fulfilled on time" is an outcome. Dashboards should focus on outcomes.

2. **No distinction between leading and lagging indicators.** Backlog growth is a leading indicator of future delivery delays. On-time rate is a lagging indicator that tells you about problems that already happened. You need both, but leading indicators are more actionable.

3. **Ignoring the capacity ceiling.** A throughput chart that shows steady growth looks great until you realize the team is at 95% utilization and quality is slipping. Always show throughput relative to capacity.

4. **Treating all errors equally.** A data entry typo that takes 2 minutes to fix is not the same as a shipping error that costs $200 and damages a customer relationship. Weight errors by impact.

5. **No root cause tracking.** Knowing your error rate is 1.8% is useful. Knowing that 40% of errors are caused by one unclear step in the fulfillment process is actionable. Always categorize and log root causes.

---

*This template is part of the Relay▸Launch KPI Dashboard Templates collection. For implementation assistance, contact [relaylaunch.com](https://relaylaunch.com).*
