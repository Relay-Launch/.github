# Operations Health Dashboard

> Is the machine running smoothly?

---

## Purpose

Give the operations manager or team leads a real-time view of process efficiency, throughput, and capacity. This dashboard answers: "Are things running on time, at quality, without burning out the team?"

---

## Recommended Metrics

| Metric | Definition | Target Example |
|---|---|---|
| **Throughput** | Units of work completed per period | 40 projects/month |
| **Cycle Time** | Average time from start to completion | < 5 business days |
| **On-Time Rate** | % of work delivered by deadline | > 90% |
| **Error / Rework Rate** | % of work requiring corrections | < 5% |
| **Capacity Utilization** | % of available capacity in use | 70-85% (sweet spot) |
| **Backlog Size** | Number of items waiting to start | Trending down |
| **SLA Compliance** | % of commitments met within agreed timeframe | > 95% |

---

## Layout

```
┌──────────────────────────────────────────────────────────┐
│  OPERATIONS HEALTH                          March 2026   │
├──────────────┬──────────────┬──────────────┬─────────────┤
│ THROUGHPUT   │ CYCLE TIME   │ ON-TIME      │ ERROR RATE  │
│ 38 / 40      │ 4.2 days     │ 91%          │ 3.1%        │
│ ● On target  │ ● On target  │ ● On target  │ ● On target │
├──────────────┴──────────────┴──────────────┴─────────────┤
│  CAPACITY UTILIZATION                                    │
│  ████████████████████████████████████░░░░░░░░  78%       │
│  ◄─── Underutilized ─── Sweet Spot ─── Overloaded ───►  │
│       < 60%              70-85%          > 90%           │
├──────────────────────────────────────────────────────────┤
│  WORK IN PROGRESS                                        │
│                                                          │
│  Backlog     ████████████████████  12 items              │
│  In Progress ██████████████       8 items                │
│  In Review   ████                 2 items                │
│  Completed   ████████████████████████████████  34 items  │
├──────────────────────────┬───────────────────────────────┤
│  BOTTLENECK ALERTS       │  TREND (8 weeks)             │
│  ⚠ Review queue growing  │  Throughput: ↑ Improving     │
│    (+3 items this week)  │  Cycle Time: → Stable        │
│  ⚠ Team member at 95%   │  Errors: ↓ Improving         │
│    capacity (J. Smith)   │  Capacity: ↑ Watch closely   │
└──────────────────────────┴───────────────────────────────┘
```

---

## Capacity Thresholds

| Range | Status | Action |
|---|---|---|
| Below 60% | Underutilized | Look for new work or reassign resources |
| 60-70% | Light | Comfortable buffer for unexpected work |
| 70-85% | Optimal | Productive with room for quality and flexibility |
| 85-90% | Heavy | Monitor closely, limit new commitments |
| Above 90% | Overloaded | Stop taking new work, redistribute, or hire |

---

## Data Sources

- **Project management:** Asana, Monday.com, ClickUp, Jira
- **Time tracking:** Toggl, Harvest, Clockify
- **Quality data:** Support tickets, rework logs, QA reports

---

*Part of the [Relay▸Launch KPI Dashboard Templates](../README.md) collection.*
