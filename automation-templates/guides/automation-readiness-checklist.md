# Automation Readiness Checklist

> Before you automate anything, make sure it's worth automating.

Not every process should be automated. Some are too messy, some change too often, and some aren't worth the setup time. This checklist helps you figure out which processes are ready for automation and which ones need work first.

---

## Step 1: Identify Candidates

A process is a good automation candidate if you can check most of these boxes:

- [ ] It runs at least weekly (or more frequently)
- [ ] It follows the same steps every time with little variation
- [ ] It involves moving data between two or more tools
- [ ] It's currently done manually by a person
- [ ] The person doing it describes it as tedious or repetitive
- [ ] Errors or delays in this process have a measurable cost
- [ ] The process has clear inputs and outputs

**Red flags — think twice before automating:**
- [ ] The process changes every few weeks
- [ ] It requires subjective human judgment at most steps
- [ ] There's no documented process — people just "figure it out"
- [ ] Only one person knows how it works and they can't explain it clearly

---

## Step 2: Pre-Automation Prerequisites

Before you build anything, confirm these are in place:

### The Process

- [ ] The process is documented (even a rough outline counts)
- [ ] You've mapped the trigger — what kicks off this process?
- [ ] You've mapped the steps — what happens in order?
- [ ] You've identified the inputs (data, files, notifications)
- [ ] You've identified the outputs (records created, emails sent, status updated)
- [ ] You know who currently owns this process
- [ ] You've timed it — how long does the manual version take?

### The Tools

- [ ] The tools involved have APIs or are supported by your automation platform
- [ ] You have admin access to the tools that need to be connected
- [ ] API keys or OAuth connections can be set up
- [ ] You've checked rate limits — will your volume hit any walls?

### The Data

- [ ] The data flowing through this process is structured (not free-form)
- [ ] Field names and formats are consistent (dates are always dates, emails are always emails)
- [ ] There's a unique identifier to match records across systems
- [ ] You've identified edge cases — what happens when data is missing or malformed?

### The Team

- [ ] Someone on the team can maintain this automation once it's built
- [ ] The team understands the automation will change their workflow
- [ ] There's a plan for what happens when the automation breaks (and it will, eventually)

---

## Step 3: Prioritize by Impact

Rate each automation candidate on two dimensions:

**Impact (1-5):**
- 1 = Saves a few minutes per week
- 3 = Saves hours per week or reduces meaningful errors
- 5 = Eliminates a major bottleneck or unlocks new capacity

**Effort (1-5):**
- 1 = Simple, two tools, linear flow, done in an hour
- 3 = Multiple tools, some conditional logic, half a day
- 5 = Complex logic, custom API work, multi-day project

**Priority Matrix:**

| | Low Effort (1-2) | Medium Effort (3) | High Effort (4-5) |
|---|---|---|---|
| **High Impact (4-5)** | Do first | Do second | Plan carefully |
| **Medium Impact (3)** | Quick win | Evaluate ROI | Probably skip |
| **Low Impact (1-2)** | If time allows | Skip | Definitely skip |

---

## Step 4: Build Checklist

When you're ready to build:

- [ ] Choose your automation platform (see our [platform comparison guide](choosing-your-platform.md))
- [ ] Set up the trigger and verify it fires correctly
- [ ] Build the workflow one step at a time — test each step before adding the next
- [ ] Handle the error cases: What happens if a step fails? Who gets notified?
- [ ] Add logging — every automation should record what it did and when
- [ ] Test with real data (not just sample data)
- [ ] Run it in "shadow mode" alongside the manual process for at least a week
- [ ] Document the automation: what it does, where it lives, how to fix it
- [ ] Hand off to the person who will own it going forward
- [ ] Set a calendar reminder to review it in 30 days

---

## Common Pitfalls

**Automating a broken process.** If the manual process is inconsistent, the automation will just break faster. Fix the process first, then automate it.

**Over-automating.** Not everything needs to be automated. If it takes 2 minutes once a week, a 4-hour automation build has negative ROI for months.

**No error handling.** Every automation will eventually fail — an API changes, a field goes missing, a rate limit gets hit. Build in notifications so you know when it breaks.

**No documentation.** If the person who built it leaves and nobody knows how it works, you've created a new problem.

**Ignoring the human side.** People need to know their workflow is changing. Surprising someone with "your job is different now" creates resistance. Involve the team early.

---

## Quick-Start: Top 5 Automations for Small Business

If you're not sure where to start, these are the automations we build most often:

1. **Lead capture → CRM** — Form submission goes straight into your CRM with a notification to the sales team
2. **Invoice reminders** — Automatic follow-ups on overdue invoices at 3, 7, and 14 days
3. **New client onboarding** — Welcome email, task creation, and calendar invite triggered by a signed contract
4. **Weekly reporting** — Automated data pull and formatted report delivered to your inbox
5. **Social media scheduling** — Content from a spreadsheet auto-published on schedule

---

*Part of the [Relay▸Launch Automation Templates](../README.md) collection.*
