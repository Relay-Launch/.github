# Process Map: [Process Name]

<!--
  ABOUT THIS TEMPLATE

  A process map is a visual representation of a workflow. It shows who does what,
  in what order, and where decisions branch the process into different paths.

  Use a process map when:
  - A process involves handoffs between multiple people or teams
  - There are decision points that change the flow
  - You need to identify bottlenecks or redundant steps
  - A linear numbered list does not adequately capture the process

  This template uses ASCII/text-based diagrams that render in any Markdown viewer.
  For more complex maps, consider using a dedicated tool (Lucidchart, Miro, draw.io)
  and embedding or linking the output.
-->

| Field | Details |
|---|---|
| **Process Name** | [Name of the process] |
| **SOP Reference** | [Link to the related SOP, if one exists] |
| **Owner** | [Name and title] |
| **Last Updated** | [YYYY-MM-DD] |
| **Version** | [1.0] |

---

## Diagram Conventions

Before reading or creating a process map, understand these symbols:

```
  Standard Symbols (ASCII Representation)
  ========================================

  [ Start / End ]       Rounded box or brackets -- marks the beginning or end of the process

  | Action Step |       Rectangle -- a task or action someone performs

  < Decision? >         Diamond (angle brackets) -- a yes/no or branching question

  (( Subprocess ))      Double parentheses -- a step that has its own separate SOP or process map

  [Document]            A document or artifact produced or consumed by the step

  ------>               Arrow -- shows direction of flow

  - - - - >             Dashed arrow -- optional or conditional path
```

---

## Swimlane Map

<!--
  A swimlane map organizes steps by WHO performs them. Each "lane" represents
  a role or department. This makes handoffs visible at a glance.

  Adapt the lane names below to match the roles in your process.
-->

```
ROLE / DEPT        PROCESS FLOW
=============================================================================

                   [ Start: Trigger Event ]
                              |
                              v
[Role A]           | Step 1: Description |
                              |
                              v
                        < Decision? >
                       /             \
                     YES              NO
                      |                |
                      v                v
[Role B]     | Step 2a: Path A |    | Step 2b: Path B |
                      |                |
                      v                v
                      +-------+--------+
                              |
                              v
[Role C]           | Step 3: Description |
                              |
                              v
                   (( Subprocess: Name ))
                              |
                              v
[Role A]           | Step 4: Description |
                              |
                              v
                        < Approved? >
                       /             \
                     YES              NO
                      |                |
                      v                v
              | Step 5: Proceed |   | Step 5b: Revise |
                      |                |
                      v                +----> (loops back to Step 3)
                   [ End ]
```

---

## Example: Customer Support Ticket Resolution

Below is a completed process map to demonstrate the format. Replace this with your own process.

### Overview

This map shows how a customer support ticket moves from submission to resolution, including escalation paths.

### Swimlane Diagram

```
ROLE                PROCESS FLOW
=============================================================================

                    [ Start: Customer submits support ticket ]
                                   |
                                   v
[Support Rep]       | 1. Review ticket and categorize |
                    |    (Bug / Feature Request / How-To / Billing) |
                                   |
                                   v
                             < Can resolve
                              within 15 min? >
                            /                \
                          YES                 NO
                           |                   |
                           v                   v
[Support Rep]    | 2a. Resolve and     | 2b. Assign priority |
                 |     reply to         |     (P1/P2/P3) and  |
                 |     customer |       |     escalate |
                           |                   |
                           v                   v
                    [ Skip to          < Priority
                      Step 6 ]           level? >
                                      /     |      \
                                    P1      P2      P3
                                     |      |       |
                                     v      v       v
[Support Lead]              | 3a. Assign   | 3b. Add to
                            |  to senior   |  sprint backlog |
                            |  rep, notify |       |
                            |  customer    |       v
                            |  within 1hr |  (( Standard Dev
                                     |        Workflow ))
                                     v             |
[Senior Rep /               | 4. Investigate       |
 Engineering]               |    and diagnose |     |
                                     |              |
                                     v              |
                              < Needs code           |
                                fix? >               |
                             /          \            |
                           YES           NO          |
                            |             |          |
                            v             v          |
                     (( Dev Release  | 5. Apply      |
                        Workflow ))  | config or     |
                            |        | workaround |  |
                            |             |          |
                            v             v          |
                            +------+------+          |
                                   |                 |
                                   v                 |
[Support Rep]       | 6. Send resolution to customer |
                    |    with explanation |           |
                                   |                 |
                                   v                 |
                            < Customer               |
                              confirmed              |
                              resolved? >            |
                           /              \          |
                         YES               NO        |
                          |                 |        |
                          v                 v        |
                   | 7. Close       | 7b. Reopen     |
                   |    ticket |    |     and return  |
                          |         |     to Step 4 | |
                          v                          |
                   | 8. Log resolution               |
                   |    in knowledge base |           |
                          |                          |
                          v                          |
                   [ End: Ticket resolved ]          |
                                                     |
                                   (P3 items resolved in future sprint,
                                    customer notified per release notes)
```

### Key Metrics to Track

| Metric | Target | Measured At |
|---|---|---|
| First response time | Under 2 hours (business hours) | Step 1 to customer notification |
| Resolution time (P1) | Under 4 hours | Start to Step 6 |
| Resolution time (P2) | Under 24 hours | Start to Step 6 |
| First-contact resolution rate | Above 40% | Step 2a vs. total tickets |
| Reopen rate | Below 10% | Step 7b vs. Step 7 |

---

## Blank Process Map

Copy the structure below to map your own process.

```
ROLE                PROCESS FLOW
=============================================================================

                    [ Start: _________________________________ ]
                                   |
                                   v
[___________]       | 1. _________________________________________ |
                                   |
                                   v
                             < __________________ ? >
                            /                       \
                          YES                        NO
                           |                          |
                           v                          v
[___________]    | 2a. ___________________ |  | 2b. ___________________ |
                           |                          |
                           v                          v
                           +------------+-------------+
                                        |
                                        v
[___________]       | 3. _________________________________________ |
                                        |
                                        v
[___________]       | 4. _________________________________________ |
                                        |
                                        v
                             < __________________ ? >
                            /                       \
                          YES                        NO
                           |                          |
                           v                          v
                    | 5a. _____________ |     | 5b. _____________ |
                           |                          |
                           v                          |
                    [ End: ____________ ]              |
                                                      v
                                              (loops back to Step __)
```

---

## Tips for Process Mapping

1. **Start with the trigger.** Every process begins with an event: a customer calls, a date arrives, someone clicks a button. Name it explicitly.

2. **End with the outcome.** What is the deliverable or end state? "Invoice sent," "Employee active in payroll," "Ticket closed." Be specific.

3. **Limit decision points.** If your map has more than four or five decision diamonds, the process may be too complex. Consider breaking it into subprocesses.

4. **Show handoffs clearly.** The swimlane format exists specifically to highlight when work moves from one person or team to another. Every handoff is a potential failure point -- make them visible.

5. **Include time expectations.** Where steps have deadlines or SLAs, note them. This turns the map from a description into a performance tool.

6. **Validate with the people who do the work.** The person drawing the map and the person performing the process often have different mental models. Walk through the map together step by step.

7. **Keep it current.** A process map that does not match reality is worse than no map at all. Update it whenever the process changes and include a version date.

8. **Use subprocesses for complexity.** If a single step on your map could itself be a 10-step procedure, represent it as a subprocess `(( Name ))` and link to a separate map or SOP.

---

*Template provided by [Relay Launch](https://relaylaunch.com) | SOP Starter Kit*
