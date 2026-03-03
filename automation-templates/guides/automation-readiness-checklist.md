# Automation Readiness Checklist

**A practical assessment tool by [Relay Launch](https://relaylaunch.com)**

---

Not every process should be automated. Some processes aren't ready yet. Others aren't worth the effort. And a few will actually get worse if you automate them prematurely.

This checklist helps you figure out which category your process falls into before you invest time and money building something. We use a version of this with every client engagement, and it's saved more than a few businesses from automating the wrong thing at the wrong time.

---

## How to Use This Checklist

For each process you're considering automating:

1. Walk through **Part 1** to confirm it's a good automation candidate.
2. Complete **Part 2** to verify you have the prerequisites in place.
3. Review **Part 3** to check for common pitfalls.
4. Score the process using the **rubric in Part 4**.

If a process scores well, move forward. If it doesn't, that doesn't mean "never" -- it means "not yet." Fix the gaps first, then revisit.

---

## Part 1: Is This Process a Good Automation Candidate?

Not all repetitive tasks are good candidates for automation. The best candidates share specific characteristics. Check each item that applies to the process you're evaluating.

### Volume and Frequency

- [ ] **The process happens regularly** -- at least weekly, ideally daily or more.
- [ ] **The volume is meaningful** -- it takes more than 15 minutes per week of someone's time.
- [ ] **Volume is growing or expected to grow** -- automating a process you do twice a month is rarely worth it.
- [ ] **The frequency is predictable** -- you know roughly when and how often this process runs.

*Why this matters:* Automation has a setup cost (time, money, maintenance). If the process doesn't happen often enough, you'll never recoup that investment. Our rule of thumb: if automating it won't save at least 2 hours per week, question whether it's worth doing right now.

### Consistency and Rules

- [ ] **The process follows clear, documented steps** -- or could be documented in under 30 minutes.
- [ ] **Decisions within the process are rule-based** -- "if X, then Y" rather than "use your judgment."
- [ ] **The inputs are structured and predictable** -- you know what data comes in and what format it's in.
- [ ] **The outputs are consistent** -- the same inputs should produce the same outputs every time.
- [ ] **Exceptions are rare and well-defined** -- less than 10-15% of cases require special handling.

*Why this matters:* Automation handles rules well and judgment poorly. If your process requires a human to read between the lines, interpret nuance, or make subjective calls, it's not ready for full automation. You might be able to automate the routine 85% and flag the exceptions for human review -- that's often the sweet spot.

### Impact and Value

- [ ] **Errors in this process have real consequences** -- missed follow-ups, delayed invoices, lost leads, compliance issues.
- [ ] **The person currently doing this work could be doing higher-value work instead.**
- [ ] **Speed matters** -- faster execution would improve customer experience, revenue, or operations.
- [ ] **The current manual process is a known bottleneck** -- other work is waiting on it.

*Why this matters:* Automating a process that nobody cares about saves time but doesn't move the needle. Prioritize automations that directly impact revenue, customer satisfaction, or your team's ability to focus on strategic work.

### Technical Feasibility

- [ ] **The tools involved have APIs or integrations** -- you can actually connect them.
- [ ] **The data you need is accessible digitally** -- not locked in PDFs, paper forms, or someone's head.
- [ ] **You have (or can get) the necessary credentials** -- API keys, admin access, OAuth permissions.
- [ ] **The process doesn't require interacting with legacy systems that have no API.**

*Why this matters:* The most perfectly designed automation is useless if you can't actually connect the tools. Check this before you start building, not after.

---

## Part 2: Prerequisites -- Are You Ready to Build?

These aren't nice-to-haves. These are requirements. Skipping them is the number one reason automations fail or cause more problems than they solve.

### Process Documentation

- [ ] **The current process is written down** -- step by step, not just "Sarah knows how to do it."
- [ ] **You've identified the trigger** -- what event starts this process? (A form submission, a time of day, an email, a status change.)
- [ ] **You've mapped the inputs** -- what data does the process need at each step?
- [ ] **You've mapped the outputs** -- what should exist at the end? (A new record, an email sent, a task created.)
- [ ] **You've documented the exceptions** -- what happens when things don't follow the normal path?
- [ ] **Someone besides the process owner can explain it** -- if only one person understands it, document it before automating it.

*Our experience:* About half the businesses we work with discover during this step that their process isn't as consistent as they thought. That's fine -- it means the documentation exercise itself was valuable. Fix the process, then automate it.

### Tool Access and Accounts

- [ ] **You have admin access to the tools involved** -- or someone who does is available.
- [ ] **API access is enabled** -- some tools require you to enable API access or upgrade your plan.
- [ ] **You have a dedicated service account or API key** -- don't use a personal account for automations (what happens when that person leaves?).
- [ ] **You've checked rate limits** -- know how many API calls your tools allow per minute/hour/day.
- [ ] **Your tool subscriptions include the features you need** -- some integrations are locked behind premium tiers.

### Data Quality

- [ ] **Your data is clean and consistent** -- automation amplifies data quality issues, it doesn't fix them.
- [ ] **Required fields are actually populated** -- if your CRM has 40% blank phone numbers, an automation that texts clients will fail 40% of the time.
- [ ] **Naming conventions are consistent** -- if "Acme Corp" and "acme corp." and "ACME" are three different records, fix that first.
- [ ] **Duplicate records are under control** -- automation on top of messy data creates messy automation.

*Hard truth:* If your data is a mess, automating a process that relies on that data will make things worse, not better. We've seen automations send duplicate emails, create ghost records, and trigger infinite loops -- all because the underlying data wasn't clean. Invest in data cleanup before you invest in automation.

### Team Readiness

- [ ] **The team knows automation is coming** -- and understands why.
- [ ] **Someone is designated as the automation owner** -- who monitors it, fixes it when it breaks, and updates it when the process changes.
- [ ] **The team is trained on the new workflow** -- automation usually changes how people interact with a process, even if they're not the ones building it.
- [ ] **There's a plan for the transition period** -- when do you switch from manual to automated? Is there a parallel-run phase?
- [ ] **The team understands what the automation does and doesn't do** -- "the system handles it" is not a sufficient explanation.

---

## Part 3: Common Pitfalls -- Things That Will Bite You

These are the mistakes we see most often. Read through them and honestly assess whether any apply to your situation.

### Automating a Broken Process

- [ ] **Confirm: the manual process actually works well.** If the current process has problems (inconsistent results, frequent errors, confusion about steps), fix the process before automating it. Automation makes a process faster. It doesn't make a bad process good.

### Overbuilding on Day One

- [ ] **Confirm: you're starting with the simplest version.** Automate the core 80% first. Add edge cases, error handling, and optimizations in v2 and v3. We've seen projects stall because someone tried to handle every possible scenario before launching. Ship the simple version. Learn from it. Iterate.

### No Monitoring Plan

- [ ] **Confirm: you have a way to know when the automation fails.** Every automation will fail eventually -- an API goes down, data arrives in an unexpected format, a credential expires. If you don't have monitoring and alerts, you won't know until a customer complains (or worse, you'll never know). At minimum: error notifications to email or Slack, and a weekly review of execution logs.

### Single Point of Failure

- [ ] **Confirm: more than one person understands the automation.** If the person who built it leaves, can someone else maintain it? Is it documented? Can someone else access the platform? The "hit by a bus" test applies to automations just as much as it applies to processes.

### Ignoring the Human Element

- [ ] **Confirm: you've considered how this affects the people involved.** Automation can feel threatening to employees who currently do the work manually. It can also create frustration if customers start receiving robotic, impersonal communications. Think about the experience from every stakeholder's perspective.

### Credential and Security Gaps

- [ ] **Confirm: credentials are stored securely and not tied to a personal account.** Use a shared credential vault (1Password, LastPass, your platform's built-in credential store). Rotate API keys on a schedule. Don't put secrets in plain text in workflow nodes.

### No Rollback Plan

- [ ] **Confirm: you can revert to the manual process if needed.** What if the automation starts misbehaving? What if the platform has an outage? Having a documented fallback plan means a technical issue doesn't become a business crisis.

### Scope Creep

- [ ] **Confirm: you've defined what this automation does and doesn't do.** It's tempting to keep adding "just one more step" to an automation. Before you know it, a simple notification workflow has become a 40-node monster that nobody understands. Define the scope up front and resist the urge to expand it before v1 is stable.

---

## Part 4: Scoring Rubric

Use this rubric to score each potential automation and prioritize your efforts.

### Scoring Instructions

For each category, assign a score from 1-5 based on the criteria below. Then calculate the total.

| Category | 1 (Low) | 3 (Medium) | 5 (High) |
|----------|---------|------------|----------|
| **Frequency** | Monthly or less | Weekly | Daily or more |
| **Time Saved** | < 30 min/week | 1-3 hours/week | 3+ hours/week |
| **Consistency** | Lots of judgment calls | Some rules, some judgment | Almost entirely rule-based |
| **Error Impact** | Minor inconvenience | Noticeable but recoverable | Revenue loss, compliance risk, or customer impact |
| **Technical Feasibility** | Major integration gaps | Some custom work needed | All tools have APIs/integrations |
| **Data Quality** | Significant cleanup needed | Minor issues to address | Clean and consistent |
| **Team Readiness** | No buy-in, no owner | Some support, owner identified | Full support, trained team |

### Score Interpretation

| Total Score | Recommendation |
|-------------|---------------|
| **28-35** | Strong candidate. Start building. This is a high-impact, low-risk automation that your team is ready for. |
| **21-27** | Good candidate with caveats. Address the low-scoring areas before you begin. Usually worth doing, but don't skip the prep work. |
| **14-20** | Marginal candidate. The ROI may not justify the effort right now. Revisit after addressing the gaps, or look for a simpler version of the automation that scores higher. |
| **7-13** | Not ready. Focus on process documentation, data cleanup, or tool evaluation first. Automating now would likely create more problems than it solves. |

### Scoring Template

Copy this for each process you're evaluating:

```
Process Name: _________________________________
Date Evaluated: _______________________________
Evaluated By: _________________________________

Frequency:             ___/5
Time Saved:            ___/5
Consistency:           ___/5
Error Impact:          ___/5
Technical Feasibility: ___/5
Data Quality:          ___/5
Team Readiness:        ___/5

TOTAL:                 ___/35

Recommendation:        ___________________
Notes:                 ___________________
```

---

## Part 5: After the Checklist -- Next Steps

### If You Scored 21+

1. **Document the workflow** in detail -- trigger, steps, conditions, outputs.
2. **Choose your platform** (see our [platform comparison guide](choosing-your-platform.md)).
3. **Build a v1** focusing on the core happy path -- no edge cases yet.
4. **Test with real data** but in a sandboxed environment.
5. **Run in parallel** with the manual process for 1-2 weeks.
6. **Go live** and monitor closely for the first month.
7. **Iterate** based on what you learn.

### If You Scored 14-20

1. **Identify the lowest-scoring categories** -- those are your gaps.
2. **Create an action plan** to address each gap (document the process, clean up data, get team buy-in, etc.).
3. **Set a target date** to re-evaluate (usually 2-4 weeks).
4. **Consider a simpler version** of the automation that avoids the problem areas.

### If You Scored Below 14

1. **Don't automate this yet.** Seriously.
2. **Focus on fundamentals** -- process documentation, data hygiene, tool evaluation.
3. **Look for quick wins elsewhere** -- there's almost always a higher-scoring process you should tackle first.
4. **Revisit in 1-3 months** after foundational work is done.

---

## Quick-Start: Top 5 Automations for Small Business

If you're not sure where to start, these are the automations we build most often:

1. **Lead capture to CRM** -- Form submission goes straight into your CRM with enrichment and sales team notification. ([Template](../workflows/lead-capture-to-crm.json))
2. **Invoice reminders** -- Graduated follow-ups on unpaid invoices, from courtesy reminder through final notice and escalation. ([Template](../workflows/invoice-follow-up.json))
3. **New client onboarding** -- Welcome email, task creation, calendar scheduling, and team notification triggered by a signed contract. ([Template](../workflows/client-onboarding-sequence.json))
4. **Weekly reporting** -- Automated data pull from multiple sources, formatted and delivered to your inbox every Monday.
5. **Social media scheduling** -- Content from a spreadsheet or CMS auto-published on schedule across platforms.

---

## One More Thing

The goal of automation isn't to automate everything. It's to automate the right things so your team can focus on work that actually requires a human -- strategy, relationships, creative problem-solving, the stuff machines aren't good at.

Start with the process that scored highest. Get one automation running smoothly. Learn from the experience. Then do the next one.

If you want help identifying your highest-impact automation opportunities, we do exactly that in our operations audit. It's a structured assessment of your workflows, tools, and team that produces a prioritized automation roadmap tailored to your business.

[Learn more at Relay Launch](https://relaylaunch.com) | [Book an operations audit](https://relaylaunch.com/contact)

---

*This checklist is maintained by [Relay Launch](https://relaylaunch.com). Use it freely, share it with your team, adapt it to your needs. Part of the [Relay Launch Automation Templates](../README.md) collection.*
