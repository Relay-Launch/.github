# Relay▸Launch Business Audit Framework

## What This Is

The Business Audit Framework is a structured diagnostic toolkit developed by Relay▸Launch to evaluate the operational health, growth trajectory, and strategic positioning of small businesses. It provides consultants and business owners with a repeatable, evidence-based methodology for identifying what is working, what is breaking, and where the highest-leverage opportunities for improvement exist.

This is not a surface-level assessment. Each audit checklist is designed to expose root causes rather than symptoms. A business that "feels busy" may score poorly on workflow efficiency. A business with strong revenue may reveal fragile customer retention. The framework makes these realities visible and actionable.

## Who Should Use This

- **Relay▸Launch consultants** conducting client engagements, discovery sessions, or quarterly business reviews
- **Small business owners** performing self-assessments before seeking outside help or making strategic investments
- **Operations managers** benchmarking internal processes against best practices
- **Fractional COOs and advisors** who need a structured intake process for new clients

## Core Methodology

The framework follows a four-phase approach:

### Phase 1: Discovery Audit

Run through each checklist relevant to the engagement scope. Every item is evaluated honestly — not aspirationally. The goal is to capture the current state, not the intended state. Each item receives a score from 1 (Critical Gap) to 5 (Optimized) using the scoring rubric provided.

### Phase 2: Scoring and Benchmarking

Individual item scores roll up into category scores, which roll up into an overall Business Health Score. This score is not a grade — it is a diagnostic instrument. A score of 2.8 does not mean the business is failing; it means specific areas need attention and the framework will tell you which ones.

### Phase 3: Priority Matrix

Audit findings are mapped onto an effort-versus-impact matrix. This prevents the common mistake of fixing easy but low-impact problems while ignoring difficult but transformational ones. The priority matrix produces a ranked action list that respects both the business's capacity for change and the urgency of each finding.

### Phase 4: Action Planning

The ranked findings become a 30/60/90-day action plan. Quick wins (low effort, high impact) are scheduled first. Strategic initiatives (high effort, high impact) are scoped and sequenced. Low-impact items are deprioritized or eliminated. This phase is where the audit becomes a roadmap.

## Framework Structure

```
business-audit-framework/
│
├── README.md                          # This file
│
├── checklists/
│   ├── operations-audit.md            # Workflow, documentation, tools, capacity
│   ├── digital-presence-audit.md      # Website, SEO, social, brand, reputation
│   ├── revenue-growth-audit.md        # Revenue channels, pricing, CAC, retention
│   └── customer-journey-audit.md      # Full lifecycle from awareness to advocacy
│
├── scoring/
│   ├── scoring-rubric.md              # 1-5 scale definitions and methodology
│   └── priority-matrix.md             # Effort vs. impact prioritization framework
│
└── tools/
    └── audit-score-calculator.py      # CLI tool for computing health scores
```

## How to Conduct an Audit

### Step 1: Select Scope

Not every engagement requires every checklist. A business struggling with lead generation needs the Digital Presence and Customer Journey audits. A business with operational chaos needs the Operations audit. A business that has plateaued needs the Revenue and Growth audit. Choose based on the presenting problem, but consider running all four for a comprehensive baseline.

### Step 2: Gather Evidence

Before scoring, collect the raw materials. This includes:

- Access to the business's tools (CRM, project management, analytics, accounting)
- Interviews with the owner and at least two team members (if applicable)
- Review of the last 12 months of financial data
- Screenshots or access to all customer-facing digital properties
- Documentation of existing SOPs, if any exist

### Step 3: Score Each Item

Walk through each checklist item and assign a score using the scoring rubric in `scoring/scoring-rubric.md`. Add notes for any item scored 3 or below — these notes become the foundation of the action plan.

### Step 4: Calculate the Health Score

Use the CLI tool (`tools/audit-score-calculator.py`) or calculate manually using the methodology described in the scoring rubric. The tool will generate a formatted report with category breakdowns and priority flags.

### Step 5: Build the Priority Matrix

Transfer all items scored 3 or below into the priority matrix template (`scoring/priority-matrix.md`). Estimate effort and impact for each. This produces the ranked action list.

### Step 6: Deliver Findings

Present the audit results with three components:

1. **The Health Score** — a single number that captures overall business health
2. **The Category Breakdown** — where strengths and weaknesses live
3. **The Priority Action List** — what to fix first, second, and third

## Scoring Overview

| Score | Label | Meaning |
|-------|-------|---------|
| 1 | Critical Gap | This area is absent or actively causing harm to the business |
| 2 | Significant Weakness | Functionality exists but is unreliable, inconsistent, or far below standard |
| 3 | Functional | Meets minimum requirements but has clear room for improvement |
| 4 | Strong | Well-executed with minor refinements possible |
| 5 | Optimized | Best-in-class execution; focus shifts to maintenance and iteration |

## Interpreting the Overall Health Score

| Range | Interpretation |
|-------|---------------|
| 1.0 – 1.9 | **Crisis**: The business has foundational issues that threaten viability. Immediate intervention required. |
| 2.0 – 2.9 | **Unstable**: The business is functioning but significant gaps create risk and limit growth. Focused remediation needed. |
| 3.0 – 3.4 | **Developing**: Core operations work but the business is leaving meaningful value on the table. Strategic improvements will accelerate growth. |
| 3.5 – 3.9 | **Solid**: The business is well-run with specific areas for optimization. Fine-tuning and scaling are the priorities. |
| 4.0 – 4.4 | **Strong**: High-performing across most dimensions. Focus on the remaining gaps and scaling what works. |
| 4.5 – 5.0 | **Optimized**: Operating at or near best-in-class. Shift focus to innovation, market expansion, and maintaining standards. |

## Principles

1. **Measure the actual, not the aspirational.** Score what exists today, not what is planned or intended.
2. **Root causes over symptoms.** A missed deadline is a symptom. The absence of a project management system is the root cause.
3. **Impact over activity.** Posting on social media daily is activity. Generating qualified leads from social media is impact.
4. **Capacity-aware recommendations.** A two-person business cannot execute a 47-item action plan. Prioritize ruthlessly.
5. **Progress over perfection.** Moving from a 2 to a 3 is more valuable than moving from a 4 to a 5. Focus on the biggest gaps first.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-02 | Initial release of the Business Audit Framework |

---

Built by [Relay▸Launch](https://relaylaunch.com) — Automation, Operations, and Strategic Planning for Small Businesses.
