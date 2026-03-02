# SOP Starter Kit

**By [Relay Launch](https://relaylaunch.com)** | Helping small businesses build systems that scale

---

## What Is This?

This is a ready-to-use starter kit for building Standard Operating Procedures (SOPs) at your small business. It includes blank templates, a style guide, and fully worked examples you can adapt to your own operations.

Fork this repository, replace the examples with your own processes, and you have the foundation of an operations manual that grows with your business.

## Why SOPs Matter

Most small businesses run on tribal knowledge. The owner or a key employee holds critical processes in their head, and everything works fine -- until it doesn't. Someone gets sick, goes on vacation, or leaves the company, and suddenly nobody knows how to run payroll, onboard a new client, or close the books at month-end.

SOPs fix this by turning implicit knowledge into explicit documentation. Here is what that gets you in practice:

- **Consistency.** The process runs the same way every time, regardless of who is doing it. Clients get a uniform experience. Errors drop.
- **Faster training.** New hires can get productive in days instead of weeks because the playbook already exists. You stop repeating yourself.
- **Delegation without anxiety.** You can hand off work confidently when the steps are written down. This is how owners get out of the day-to-day.
- **Continuous improvement.** You cannot optimize a process you have not documented. Once it is on paper, you can spot bottlenecks, eliminate waste, and measure results.
- **Business value.** If you ever want to sell your business, acquirers pay a premium for companies with documented operations. It signals maturity and reduces risk.

You do not need to document everything on day one. Start with the processes that are most painful, most frequent, or most dependent on a single person. Build from there.

## What Is in This Kit

```
sop-starter-kit/
|
|-- README.md                          # You are here
|-- sop-style-guide.md                 # How to write SOPs consistently
|
|-- templates/
|   |-- sop-template.md                # Blank SOP template with guidance
|   |-- process-map-template.md        # Template for visual process documentation
|
|-- examples/
|   |-- employee-onboarding.md         # Complete onboarding SOP
|   |-- client-intake-process.md       # Complete client intake / sales SOP
|   |-- monthly-close-checklist.md     # Complete month-end financial close SOP
```

### Templates

The `templates/` directory contains blank starting points:

- **sop-template.md** -- A general-purpose SOP template with all the standard sections (Purpose, Scope, Procedure, etc.) and inline guidance comments explaining what to write in each section. Copy this file every time you document a new process.
- **process-map-template.md** -- A template for creating visual process maps using Markdown and ASCII flowcharts. Useful for complex processes where a numbered list is not enough and you need to show decision points, parallel paths, or handoffs between teams.

### Examples

The `examples/` directory contains three fully worked SOPs that demonstrate what good documentation looks like in practice:

- **employee-onboarding.md** -- Covers the full lifecycle from offer acceptance through the end of a new hire's first 90 days. Includes pre-arrival setup, Day 1 activities, training schedules, and check-in cadence.
- **client-intake-process.md** -- Documents the process from first contact with a prospective client through signed agreement and project kickoff. Covers qualification, discovery, proposal, and handoff to delivery.
- **monthly-close-checklist.md** -- A step-by-step financial close process for small businesses. Covers transaction reconciliation, accruals, reporting, and management review.

These examples are written for a generic small business (roughly 10 to 50 employees). You will need to adapt the specifics -- tools, titles, timelines -- to match your organization.

### Style Guide

**sop-style-guide.md** defines the conventions for writing SOPs at your company: tone, formatting, naming, versioning, and review schedules. Read this before writing your first SOP. Consistency across documents makes the whole system easier to navigate.

## How to Use This Kit

### Step 1: Read the Style Guide

Start with `sop-style-guide.md` to understand the conventions. Even if you modify them, having a shared standard from the beginning saves time later.

### Step 2: Identify Your First Three SOPs

Do not try to document everything at once. Pick three processes based on these criteria:

| Criteria | Why It Matters |
|---|---|
| High frequency | Processes you run daily or weekly have the most impact when standardized |
| High pain | If something breaks regularly or causes frustration, document it first |
| Key-person dependent | If only one person knows how to do it, that is a business risk |
| Client-facing | Inconsistency here directly affects revenue and reputation |

Common starting points: employee onboarding, client intake, invoicing, weekly reporting, inventory receiving, support ticket handling.

### Step 3: Copy the Template

Duplicate `templates/sop-template.md` and rename it following the naming convention in the style guide. Fill in each section, using the examples as a reference for level of detail.

### Step 4: Walk the Process

Do not write the SOP from memory. Actually perform the process (or sit with the person who does) and document each step as it happens. You will catch steps that people do unconsciously and skip when describing the process verbally.

### Step 5: Test with Someone Else

Hand the draft SOP to someone who has never done the process and ask them to follow it. Every place they get confused is a gap in your documentation. Revise accordingly.

### Step 6: Publish and Assign Ownership

Every SOP needs an owner -- someone responsible for keeping it current. This is typically the manager of the team that runs the process. Set a review date (quarterly is a good default) and put it on the calendar.

### Step 7: Build the Habit

SOPs are only useful if people actually reference them. Incorporate them into training, link to them in your project management tools, and reference them when processes go wrong. Over time, "check the SOP" becomes a natural reflex instead of "ask the boss."

## Tips for Writing Effective SOPs

1. **Write for the new hire.** Assume the reader is competent but has zero context about your company. If they need to know where a file lives, tell them the exact path. If they need to log in to a tool, tell them which tool and where to find credentials.

2. **Use numbered steps for procedures.** Bullet points are fine for lists of items, but sequential procedures should always be numbered. The reader needs to know the order.

3. **Be specific about tools and locations.** "Enter the data into the spreadsheet" is not useful. "Open the Client Tracker spreadsheet in Google Drive > Operations > Active Clients and enter the data in the next empty row" is useful.

4. **Include the why, not just the what.** When a step exists for a non-obvious reason, add a brief note explaining it. People follow procedures more reliably when they understand the reasoning. Example: "Send the invoice within 24 hours of project completion (delays beyond 48 hours correlate with a 15% drop in collection rate)."

5. **Add screenshots sparingly.** Screenshots are helpful for complex UI workflows but become maintenance burdens because they break every time the software updates. Use them for genuinely confusing interfaces, not for obvious ones.

6. **Keep procedures under 20 steps.** If a process has more than 20 steps, it is probably two or three processes. Break it up. A long SOP is an unread SOP.

7. **Document exceptions explicitly.** Every process has edge cases. Do not leave people guessing about what to do when things do not go as planned. Add an Exceptions section that covers the most common deviations.

8. **Version and date everything.** When you update an SOP, increment the version number and note what changed. People need to trust that the document they are reading is current.

## Frequently Asked Questions

**Where should we store our SOPs?**
Wherever your team already goes for information. Google Drive, Notion, Confluence, SharePoint, a GitHub repo -- the tool matters less than the habit. Pick one location, make it searchable, and link to SOPs from the places people already look (onboarding checklists, project templates, Slack bookmarks).

**How detailed should SOPs be?**
Detailed enough that a competent person unfamiliar with the process can complete it without asking questions. Not so detailed that it reads like a software manual for basic human tasks. Use judgment. If a step is "open your email," you do not need sub-steps for launching the browser.

**How often should we review SOPs?**
Quarterly for high-frequency, high-impact processes. Annually for everything else. Also review any time the process changes -- new tools, new team structure, new regulations. The style guide has more detail on review cadence.

**Who should write SOPs?**
The person who actually does the work, with editorial support from a manager or ops lead. Do not assign SOP writing to someone who has never performed the process. They will miss critical details.

**What if nobody follows the SOPs?**
That is a management problem, not a documentation problem. SOPs need enforcement. Reference them during training, use them during performance conversations, and update them when they drift from reality. Outdated SOPs are worse than no SOPs because they erode trust in the system.

## License

This starter kit is provided under the MIT License. Use it, modify it, share it. If you find it useful, we would appreciate a link back to [Relay Launch](https://relaylaunch.com).

---

*Built by Relay Launch. We help small businesses design operations that run without the owner in the room. [Learn more about our consulting services.](https://relaylaunch.com)*
