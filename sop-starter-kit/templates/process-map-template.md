# Process Map: [Process Name]

**Process Owner:** [Name and title]
**Date Created:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]
**Related SOP:** [Link to the detailed SOP for this process]

---

## Overview

<!--
Write 2-3 sentences describing this process at a high level. What does it
accomplish? A process map should be understandable at a glance -- the
overview provides context for someone seeing it for the first time.
-->

[High-level description of the process.]

---

## Process Boundaries

**Start Event:** [What triggers this process, e.g., "Customer submits a support request"]

**End Event:** [What marks the process as complete, e.g., "Customer confirms issue is resolved"]

**Key Inputs:** [What information or materials enter the process]

**Key Outputs:** [What the process produces -- deliverables, decisions, records]

---

## Roles Involved

<!--
List each role that appears in the process map. Use short names that will
fit in the diagram boxes. Map them to full titles here.
-->

| Abbreviation | Full Role Title |
|---|---|
| [MGR] | [Operations Manager] |
| [REP] | [Sales Representative] |
| [FIN] | [Finance / Bookkeeper] |

---

## Process Map

<!--
GUIDE TO BUILDING YOUR PROCESS MAP

Use the symbols below to build your flowchart. Markdown and ASCII art
work well for simple-to-moderate processes. For highly complex processes
with many parallel paths, consider using a diagramming tool (Lucidchart,
Miro, draw.io) and linking to it here.

SYMBOLS:
  ( Start/End )     -- Rounded: terminal points
  [ Action/Step ]   -- Square brackets: tasks or actions
  { Decision? }     -- Curly braces: yes/no or branching decisions
  [[ Sub-process ]] -- Double brackets: reference to another SOP
  (( Document ))    -- Double parens: a document or record is created

ARROWS:
  -->               -- Flow direction
  |                 -- Vertical connector
  v                 -- Downward arrow
  +-- Yes -->       -- Labeled branch
  +-- No  -->       -- Labeled branch

SWIM LANES:
  Use headers (### Role Name) to show which role is responsible
  for each section of the process.

TIPS:
  - Keep it to one page if possible
  - Read the map out loud to check flow logic
  - Every decision must have at least two exits
  - Every path must reach an end point (no dead ends)
  - Number steps to match the detailed SOP procedure section
-->

```
                        ( START )
                            |
                            v
                  +-------------------+
                  | 1. [First action] |
                  +-------------------+
                            |
                            v
                  +-------------------+
                  | 2. [Second action]|
                  +-------------------+
                            |
                            v
                   { Decision point? }
                    /              \
                 Yes                No
                  /                  \
                 v                    v
      +----------------+    +------------------+
      | 3a. [Action if |    | 3b. [Action if   |
      |     yes]       |    |     no]          |
      +----------------+    +------------------+
                  \                  /
                   \                /
                    v              v
                  +-------------------+
                  | 4. [Next action]  |
                  +-------------------+
                            |
                            v
                  +-------------------+
                  | 5. [Final action] |
                  +-------------------+
                            |
                            v
                        ( END )
```

---

## Detailed Step Reference

<!--
This table maps each numbered step in the process map to additional
detail. It bridges the visual diagram with the full SOP.
-->

| Step | Action | Responsible | System/Tool | Notes |
|---|---|---|---|---|
| 1 | [Description] | [Role] | [Tool] | [Any notes] |
| 2 | [Description] | [Role] | [Tool] | [Any notes] |
| 3a | [Description] | [Role] | [Tool] | [If yes branch] |
| 3b | [Description] | [Role] | [Tool] | [If no branch] |
| 4 | [Description] | [Role] | [Tool] | [Any notes] |
| 5 | [Description] | [Role] | [Tool] | [Any notes] |

---

## Decision Point Details

<!--
For each decision in the process map, document the criteria clearly.
Ambiguous decision points are the #1 cause of process breakdowns.
-->

### Decision: [Decision point name]

- **Question:** [Exact question being evaluated]
- **Yes criteria:** [What conditions lead to "Yes"]
- **No criteria:** [What conditions lead to "No"]
- **Who decides:** [Role with authority to make this call]
- **Escalation:** [What to do if the answer is unclear]

---

## Handoff Points

<!--
Handoffs -- where work transfers from one person or team to another --
are where most process failures occur. Document each one explicitly.
-->

| From | To | What Is Handed Off | How | SLA |
|---|---|---|---|---|
| [Role] | [Role] | [Deliverable or information] | [Email, system notification, etc.] | [Expected timeframe] |
| [Role] | [Role] | [Deliverable or information] | [How] | [Expected timeframe] |

---

## Metrics & KPIs

<!--
Define how you will measure whether this process is working well.
Without metrics, you cannot identify bottlenecks or justify improvements.
-->

| Metric | Target | How Measured | Review Frequency |
|---|---|---|---|
| [e.g., Total cycle time] | [e.g., < 3 business days] | [e.g., Timestamps in CRM] | [e.g., Monthly] |
| [e.g., Error rate] | [e.g., < 2%] | [e.g., QA review log] | [e.g., Weekly] |

---

---

# Sample Process Map: Customer Support Ticket Resolution

Below is a completed example to illustrate how the template works in practice.

## Overview

This process covers the lifecycle of a customer support ticket from initial submission through resolution and closure. It ensures every ticket is triaged, assigned, resolved, and documented consistently.

## Process Boundaries

**Start Event:** Customer submits a support request (email, form, or phone)

**End Event:** Ticket is marked "Closed" in the help desk system after customer confirmation

**Key Inputs:** Customer contact info, issue description, account details

**Key Outputs:** Resolved issue, updated knowledge base (if applicable), closed ticket record

## Roles Involved

| Abbreviation | Full Role Title |
|---|---|
| CSR | Customer Service Representative |
| TL | Team Lead / Support Manager |
| SPEC | Subject Matter Specialist |

## Process Map

```
                          ( TICKET RECEIVED )
                                  |
                                  v
                      +------------------------+
                      | 1. CSR logs ticket in  |
                      |    help desk system     |
                      +------------------------+
                                  |
                                  v
                      +------------------------+
                      | 2. CSR reviews issue   |
                      |    and categorizes      |
                      +------------------------+
                                  |
                                  v
                        { Can CSR resolve? }
                         /              \
                      Yes                No
                       /                  \
                      v                    v
          +------------------+   +------------------------+
          | 3a. CSR resolves |   | 3b. CSR escalates to   |
          |     the issue    |   |     TL for assignment   |
          +------------------+   +------------------------+
                      |                    |
                      |                    v
                      |          +------------------------+
                      |          | 4. TL assigns to SPEC  |
                      |          +------------------------+
                      |                    |
                      |                    v
                      |          +------------------------+
                      |          | 5. SPEC investigates   |
                      |          |    and resolves         |
                      |          +------------------------+
                      |                    |
                      v                    v
                      +------------------------+
                      | 6. CSR notifies        |
                      |    customer of          |
                      |    resolution            |
                      +------------------------+
                                  |
                                  v
                     { Customer confirms fix? }
                         /              \
                      Yes                No
                       /                  \
                      v                    v
          +------------------+   +------------------------+
          | 7a. CSR closes   |   | 7b. Reopen ticket,     |
          |     ticket       |   |     return to Step 2    |
          +------------------+   +------------------------+
                      |
                      v
              ( TICKET CLOSED )
```

## Decision Point Details

### Decision: Can CSR resolve?

- **Question:** Does the CSR have the knowledge and access to resolve this issue without specialist help?
- **Yes criteria:** Issue matches a known solution in the knowledge base, or CSR has handled this type of issue before and has the required system access.
- **No criteria:** Issue is technical, involves system configuration, requires elevated permissions, or is not documented in the knowledge base.
- **Who decides:** CSR (with TL available for guidance)
- **Escalation:** If unsure, escalate. It is better to escalate unnecessarily than to provide an incorrect resolution.

### Decision: Customer confirms fix?

- **Question:** Has the customer confirmed that the issue is resolved to their satisfaction?
- **Yes criteria:** Customer replies confirming resolution, or 48 hours pass with no response after resolution notification.
- **No criteria:** Customer reports the issue persists or a new related issue has surfaced.
- **Who decides:** CSR based on customer response
- **Escalation:** If the ticket is reopened more than twice, TL reviews the ticket directly.

---

*Use this template to map your own processes. Start simple, refine with your team, and link the finished map to its corresponding SOP.*
