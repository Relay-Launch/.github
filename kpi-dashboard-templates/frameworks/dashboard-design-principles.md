# Dashboard Design Principles

**By Relay▸Launch** | Practical Guide to Building Dashboards People Actually Use

---

## The Problem With Most Dashboards

We have reviewed hundreds of business dashboards over the years, and roughly 80% of them share the same failure mode: they were built to display data rather than to support decisions. The result is a screen full of numbers that nobody looks at after the first two weeks.

A good dashboard gets opened every morning. A great dashboard changes how a team operates. The difference is not the data — it is the design.

This guide covers the principles we apply when building dashboards for clients. These come from deployment experience, not theory. Every recommendation here has been tested in real businesses where the dashboard either got adopted or it did not.

---

## Principle 1: Start With Decisions, Not Data

Before you open a single tool, answer these three questions:

1. **Who is the audience?** A CEO and a warehouse manager need different dashboards. Not different data on the same dashboard — different dashboards entirely.
2. **What decisions does this dashboard support?** Write them down. "Should we increase ad spend this week?" is a decision. "Revenue" is not.
3. **What action will someone take after looking at this?** If the answer is "nothing, they just need to know," you are building a report, not a dashboard. That is fine, but call it what it is and design accordingly.

The most common mistake we see is building a dashboard that answers the question "what happened?" without answering "so what?" or "what should I do about it?"

### The Decision-Backward Method

Start with a decision your team makes regularly:

> "Should we hire another support agent this quarter?"

Work backward to the metrics that inform that decision:

- Ticket volume trend (is it growing?)
- Average response time (is quality slipping?)
- Tickets per agent (is the current team at capacity?)
- Customer satisfaction score (is slow support hurting retention?)

Now you have a dashboard section. Four metrics, one decision. That is the right ratio.

---

## Principle 2: Visual Hierarchy — The 5-Second Test

The most important information on your dashboard should be comprehensible within five seconds of glancing at the screen. If someone has to study it, you have failed.

### The Three Tiers

Design your dashboard in three visual tiers:

**Tier 1 — The Headline (top of screen, largest elements)**
- 2-4 big numbers that answer "how is the business doing right now?"
- Large font, high contrast, with trend indicators (up/down arrows or sparklines)
- Example: Revenue MTD, Active Customers, Cash Position, NPS

**Tier 2 — The Context (middle of screen, medium elements)**
- Supporting metrics that explain the headlines
- Charts, small tables, or secondary scorecards
- Example: Revenue by channel, customer acquisition trend, top support issues

**Tier 3 — The Detail (bottom or secondary tabs)**
- Drill-down data for people who want to investigate
- Full tables, detailed breakdowns, historical comparisons
- Example: Revenue by SKU, individual rep performance, daily transaction log

Most dashboards fail because everything is Tier 2. There is no headline, no hierarchy, just a wall of equally-sized charts competing for attention.

### Layout Patterns That Work

```
┌─────────────────────────────────────────────────────┐
│  TIER 1: Big Numbers (Scorecards)                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │
│  │ Revenue  │ │ Customers│ │  Margin  │ │  NPS   │ │
│  │  $847K   │ │   1,247  │ │  42.3%   │ │   67   │ │
│  │  ▲ 12%   │ │  ▲ 8%   │ │  ▼ 1.2%  │ │  ▲ 5   │ │
│  └──────────┘ └──────────┘ └──────────┘ └────────┘ │
├─────────────────────────────────────────────────────┤
│  TIER 2: Context Charts                             │
│  ┌────────────────────┐ ┌──────────────────────────┐│
│  │                    │ │                          ││
│  │  Revenue Trend     │ │  Revenue by Channel      ││
│  │  (Line Chart)      │ │  (Bar Chart)             ││
│  │                    │ │                          ││
│  └────────────────────┘ └──────────────────────────┘│
├─────────────────────────────────────────────────────┤
│  TIER 3: Detail Tables                              │
│  ┌─────────────────────────────────────────────────┐│
│  │  Top Products / Detailed Breakdown / Drill-down ││
│  └─────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────┘
```

This is not the only valid layout, but it is the safest starting point. Variations include side-by-side Tier 1 and Tier 2, or tabbed layouts where each tab is a different tier.

---

## Principle 3: Data Density — Less Is More (Usually)

Edward Tufte's concept of "data-ink ratio" is relevant here, but we take a more practical stance: **every element on the dashboard should earn its place.**

### The Earning Test

For each metric, chart, or element on your dashboard, ask:

1. Does someone look at this every time they open the dashboard?
2. Has this metric ever triggered an action or conversation?
3. Would anyone notice if this were removed?

If the answer to all three is "no," remove it. You can always bring it back.

### What to Cut First

- **Pie charts.** They are almost never the right choice. Humans are bad at comparing angles and areas. Use horizontal bar charts instead. The only acceptable pie chart is one with two or three slices where you want to show a part-to-whole relationship that is immediately obvious (e.g., "70% of revenue comes from repeat customers").

- **3D effects.** Never. Not ever. They distort data perception and add no information.

- **Excessive decimal places.** Revenue of $847,293.47 on a dashboard is noise. Round to $847K. The dashboard is for direction, not precision. The source data still has the details.

- **Redundant labels.** If your chart title says "Monthly Revenue Trend (Jan-Dec 2025)" and the axis labels say the same thing, you have two labels doing one job.

- **Legends when you can label directly.** If a line chart has two lines, label them on the chart rather than making the viewer look back and forth between the chart and a legend.

### What to Keep

- **Sparklines.** Small, inline trend indicators next to big numbers. They add enormous context in minimal space. "Revenue is $847K" is okay. "Revenue is $847K ▁▃▅▇▆▅▇" is much better because you see the trajectory.

- **Comparison context.** A number alone is meaningless. Always show it relative to something: last period, same period last year, target, or budget.

- **Conditional formatting.** Green, yellow, red status indicators (used correctly — see the Color section below) help the eye jump to problems without reading every number.

---

## Principle 4: Color Usage — A Functional Tool, Not Decoration

Color on dashboards has exactly one job: to encode meaning. If a color does not mean something, it should not be there.

### The Three Rules of Dashboard Color

**Rule 1: Use a restrained palette.**

Pick 3-4 colors maximum for your entire dashboard:
- A **primary brand color** for headers and visual identity
- A **neutral gray** for axes, borders, and secondary text
- **Green and red** (or blue and orange for accessibility) for positive/negative status
- One **accent color** for highlighting or call-to-action elements

Most of the dashboard should be black text on a white or light gray background. The less color you use, the more powerful each use of color becomes.

**Rule 2: Red means bad. Green means good. Do not violate this.**

Every culture and every tool conditions users to read red as "problem" and green as "okay." If you use red to mean "high priority" (which might be good), you will confuse people. If you use green for your brand color on a chart bar that represents churned customers, the visual signal contradicts the data signal.

Status colors:
- **Green:** On track, at or above target, healthy
- **Yellow/Amber:** Warning, approaching threshold, needs attention
- **Red:** Off track, below threshold, requires immediate action
- **Gray:** No target set, or data not yet available

**Rule 3: Account for color blindness.**

Approximately 8% of men and 0.5% of women have some form of color vision deficiency, most commonly red-green. This means that in a meeting of 12 people, there is a good chance at least one person cannot distinguish your red from your green.

Mitigations:
- Use symbols in addition to color (checkmark for good, X for bad, dash for warning)
- Use blue/orange instead of green/red where possible
- Add text labels ("On Track," "At Risk," "Off Track") alongside color coding
- Test your dashboard with a color blindness simulator (many are available as browser extensions)

### Color Anti-Patterns

- **Rainbow charts.** A bar chart with 12 different colored bars is visual noise. Use one color and vary the shade, or use a single color with the key bar highlighted.
- **Background colors on data cells.** A spreadsheet where every cell has a background color is harder to read, not easier. Reserve cell coloring for status indicators only.
- **Brand colors everywhere.** Your company's brand palette was designed for marketing materials, not data visualization. A hot pink brand color does not belong on chart axes.

---

## Principle 5: Update Cadence — Freshness Determines Trust

A dashboard with stale data is worse than no dashboard at all. It trains people to not trust the numbers, and once trust is lost, it takes months to rebuild.

### Match Cadence to Decision Frequency

| Decision Type | Example | Data Freshness Needed | Update Method |
|---------------|---------|----------------------|---------------|
| Strategic | "Should we enter a new market?" | Monthly or quarterly | Manual review is fine |
| Tactical | "Should we increase ad spend this week?" | Daily or weekly | Semi-automated |
| Operational | "Which orders ship today?" | Real-time or hourly | Fully automated |

### Cadence Recommendations by Dashboard Type

**Executive Dashboard:**
- Update: Weekly (Monday morning before leadership meeting)
- Method: Automated data pull + 30-minute manual review for accuracy
- Staleness threshold: If it is Wednesday and the dashboard still shows last week's data, something is broken

**Sales Dashboard:**
- Update: Daily (CRM data is typically near real-time)
- Method: Direct CRM integration or daily automated export
- Staleness threshold: Yesterday's data should be visible by 9 AM today

**Operations Dashboard:**
- Update: Daily or real-time depending on the operation
- Method: Direct system integration
- Staleness threshold: Depends on operation speed. A warehouse needs hourly. A consulting firm needs daily.

**Financial Dashboard:**
- Update: Monthly (aligned with close process)
- Method: Manual export from accounting system after reconciliation
- Staleness threshold: Available within 5 business days of month-end

### The Ownership Rule

Every dashboard needs a single named owner. Not a team. Not "the data team." One person whose job includes:

- Verifying data accuracy at each update
- Investigating anomalies before the review meeting
- Adding annotations for unusual data points (e.g., "Revenue dip on 3/15 due to payment processor outage — not a real decline")
- Fielding questions about methodology

If nobody owns the dashboard, nobody will trust it, and nobody will use it.

---

## Principle 6: Audience Targeting — One Dashboard, One Audience

The biggest structural mistake in dashboard design is trying to serve multiple audiences with a single view. A CEO and a marketing manager need fundamentally different things:

| Attribute | Executive Audience | Manager Audience | Individual Contributor |
|-----------|-------------------|-----------------|----------------------|
| **Metrics** | 4-6 company-level KPIs | 8-12 department KPIs | Detailed activity metrics |
| **Time horizon** | Monthly and quarterly trends | Weekly trends | Daily and hourly |
| **Granularity** | High-level rollups | Team and channel breakdowns | Individual task and record level |
| **Interaction** | View only (no filtering needed) | Filter by team, period, segment | Filter, sort, drill down |
| **Update cadence** | Weekly | Daily | Real-time |
| **Design priority** | Clarity and speed | Context and comparison | Completeness and detail |

### Building for Each Audience

**For Executives:**
- Maximum 6 metrics on the primary view
- Every number should have a comparison (vs. target, vs. last period)
- Include a brief text summary or annotation for each metric
- No interactive filters — the view should be ready to read as-is
- Design for projection on a conference room screen (large fonts, high contrast)

**For Managers:**
- Include both team-level and individual-level views
- Add filters for time period, team member, segment
- Include trend lines covering at least 8-12 data points (weeks or months)
- Add drill-down capability: click a number to see contributing details
- Design for a laptop screen at a desk

**For Individual Contributors:**
- Focus on "my stuff" — my pipeline, my tasks, my metrics
- Real-time or near-real-time data
- Action-oriented: what should I work on next?
- Design for frequent checking throughout the day

### The Tab Strategy

If you must serve multiple audiences in one tool (common in Google Sheets or Looker Studio), use tabs or pages:

- **Tab 1: Executive Summary** — 4-6 big numbers, minimal interaction
- **Tab 2: Department Overview** — Team-level metrics with basic filtering
- **Tab 3: Detailed Data** — Full tables, all filters, drill-down capability
- **Tab 4: Definitions** — What each metric means, how it is calculated, data sources

The definitions tab is not optional. When someone asks "how is this number calculated?" in a meeting, you should be able to point to a tab rather than trying to remember the formula.

---

## Principle 7: Context Makes Numbers Meaningful

A number without context is just a number. "Revenue was $847K" tells you almost nothing. Context transforms data into information.

### Types of Context

**Temporal context:** How does this compare to last period?
```
Revenue: $847K (▲ 12% vs. last month)
```

**Target context:** How does this compare to our goal?
```
Revenue: $847K / $900K target (94% of goal)
```

**Historical context:** What is the trend?
```
Revenue: $847K ▁▂▃▅▃▅▆▇▆▅▆▇
              Jan ─────────── Dec
```

**Benchmark context:** How does this compare to peers?
```
Revenue per employee: $210K (industry median: $185K)
```

**Annotation context:** What happened to cause this?
```
Revenue: $847K (▼ 8% — attributable to Q3 pricing change)
```

### The Minimum Viable Context

At absolute minimum, every metric on a dashboard should have:
1. The current value
2. A comparison to one reference point (prior period, target, or both)
3. A directional indicator (up, down, flat)

If you cannot provide all three, the metric is not ready for the dashboard. Park it in the source data until you can contextualize it.

---

## Principle 8: Handling Missing and Incomplete Data

Real-world data is messy. Your dashboard design must account for this rather than pretending it does not exist.

### Rules for Missing Data

1. **Never show $0 when you mean "no data."** Zero is a value. Unknown is not a value. Display "N/A" or "—" for missing data, and $0 when the actual value is zero.

2. **Gray out stale data.** If a metric has not been updated on schedule, visually indicate this. A simple approach: show the last-known value in gray italic with a note like "Last updated: Feb 14."

3. **Exclude incomplete periods from trends.** If it is March 15, showing March's month-to-date revenue on a chart next to full-month data for January and February is visually misleading. The March bar will look like a decline even if the business is growing. Either annualize the partial month, exclude it, or clearly mark it as partial.

4. **Document data gaps.** If you know that Q2 2024 data is unreliable because of a system migration, annotate it on the dashboard rather than letting people draw conclusions from bad data.

---

## Principle 9: Progressive Disclosure

Do not show everything at once. Layer information so that casual viewers see the summary and curious viewers can dig in.

### Implementation Approaches

**In Google Sheets:**
- Use the tab structure described above
- Use grouped rows (Data > Group rows) to create expandable detail sections
- Use named ranges and VLOOKUP to create a summary sheet that pulls from detail tabs

**In Looker Studio:**
- Use page navigation for different detail levels
- Use drill-down chart types (bar charts that expand when clicked)
- Use optional filters that default to the most common view

**In HTML reports:**
- Use expandable/collapsible sections (details/summary HTML elements)
- Use linked sections: summary at top, detailed tables below with anchor links
- Use color intensity to draw eyes to anomalies

### What Goes Behind the Fold

- Individual transaction data
- Full date-range historical tables
- Methodology documentation
- Secondary and tertiary metrics
- Comparative benchmarks and footnotes

---

## Principle 10: Design for the Review Meeting

Most dashboards are consumed in meetings. Design for that context.

### Meeting-Optimized Design

1. **Design for projection.** Use minimum 16px font for any data that will be shown on a conference room screen. Test readability from 10 feet away.

2. **Build a natural narrative flow.** The dashboard should tell a story from top to bottom or left to right: "Here is where we are → here is the trend → here is what is driving it → here is what needs attention."

3. **Highlight the conversation starters.** Use red/yellow status indicators to direct the meeting to the metrics that need discussion. A meeting where every metric is green should take 5 minutes. The dashboard should make it obvious when that is the case.

4. **Leave space for notes.** In Google Sheets, include a column or section for meeting notes. In Looker Studio, use text boxes that can be updated. The dashboard should capture the "so what" alongside the "what."

5. **Include an "as of" date.** Always. Prominently. If someone walks into the meeting not knowing whether they are looking at last week's data or last month's data, the first five minutes will be wasted.

---

## Quick Reference: Dashboard Design Checklist

Use this checklist before launching a new dashboard:

- [ ] I can name the specific audience for this dashboard
- [ ] I can list 3-5 decisions this dashboard supports
- [ ] The most important metrics are visually dominant (Tier 1)
- [ ] Every metric has at least one comparison point (target, prior period, or trend)
- [ ] Color is used for status, not decoration
- [ ] The dashboard passes a color blindness check
- [ ] There is a defined update cadence and a named owner
- [ ] Missing data is handled explicitly (not shown as zero)
- [ ] The dashboard is readable from 10 feet away (if used in meetings)
- [ ] There is a definitions section explaining each metric
- [ ] The "as of" date is prominently displayed
- [ ] I have removed at least two elements that were not earning their place

---

## Tools and Implementation Notes

### Google Sheets
- Strengths: Familiar, collaborative, free, good conditional formatting
- Weaknesses: Limited chart types, performance with large datasets, no real-time
- Best for: Small teams, weekly-cadence dashboards, initial implementations

### Looker Studio
- Strengths: Beautiful, shareable, connects to live data, free
- Weaknesses: Steeper learning curve, limited interactivity compared to paid BI tools
- Best for: Client-facing reports, dashboards connected to Google Analytics or BigQuery

### Power BI
- Strengths: Powerful data modeling, excellent visualizations, strong filtering
- Weaknesses: Microsoft ecosystem dependency, learning curve, licensing costs
- Best for: Organizations already using Microsoft 365, complex data models

### Notion / Airtable Dashboards
- Strengths: Integrated with operational data, flexible, good for teams already using them
- Weaknesses: Limited visualization, no real charting, formula limitations
- Best for: Team-level operational dashboards where the data already lives in Notion/Airtable

### HTML/Static Reports
- Strengths: No login required, works offline, can be emailed, completely customizable
- Weaknesses: Not interactive, requires rebuilding for each update
- Best for: Monthly board reports, client deliverables, one-off analyses

---

*These principles are the foundation of every measurement system Relay▸Launch builds. If you want help applying them to your business, reach out at [relaylaunch.com](https://relaylaunch.com).*
