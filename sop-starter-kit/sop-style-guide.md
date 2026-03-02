# SOP Style Guide

> How to write SOPs that people actually read, follow, and keep current.

**By Relay▸Launch**

---

## Why a Style Guide?

If ten people write SOPs with ten different formats, you end up with a document library that is hard to navigate, inconsistent to follow, and painful to maintain. This style guide establishes shared conventions so that every SOP in your organization looks, reads, and behaves the same way. Consistency reduces cognitive load for the reader and makes the entire library more trustworthy.

Read this guide before you write your first SOP. Refer back to it when something feels ambiguous.

---

## Tone and Voice

### Write for the Practitioner

Your reader is someone who needs to execute this process. They are competent but may be new to this specific task. Write like you are explaining something to a smart colleague on their first day handling this responsibility.

**Do:** Be direct, specific, and practical.
**Do not:** Be academic, vague, or condescending.

### Be Clear, Not Clever

SOPs are reference documents, not thought leadership. Use plain language. Short sentences. Familiar words. Save the personality for the company blog.

| Instead of this | Write this |
|---|---|
| "Ensure timely execution of the client communication deliverable post-contract finalization." | "Send the welcome email within 24 hours of receiving the signed contract." |
| "Leverage existing templates to facilitate proposal generation." | "Copy the proposal template from `Sales > Templates` and customize it for the client." |
| "Utilize the appropriate channel for stakeholder notification." | "Post a message in the team's Slack channel." |
| "Prior to commencement of the reconciliation workflow..." | "Before you start the reconciliation..." |

### Use Active Voice

Active voice makes it clear who does what. Passive voice hides responsibility.

| Passive (avoid) | Active (use this) |
|---|---|
| "The invoice should be sent." | "The Finance Lead sends the invoice." |
| "The report is reviewed by the Operations Manager." | "The Operations Manager reviews the report." |
| "Errors were identified." | "The Finance Lead identified three errors." |

### Be Specific

Specificity is what separates a useful SOP from a decorative one.

| Vague (useless) | Specific (useful) |
|---|---|
| "Update the system." | "Update the deal stage to 'Proposal Sent' in HubSpot." |
| "Notify the team." | "Post in the #operations Slack channel with the client name and project start date." |
| "File the document." | "Save the signed agreement to `Clients > [Client Name] > Contracts > [Year]`." |
| "Follow up promptly." | "Send a follow-up email within 3 business days." |
| "Get approval." | "Send the proposal to the Managing Director via email for written approval before sharing with the client." |

---

## Formatting Conventions

### File Naming

Use lowercase kebab-case for all SOP file names:

```
employee-onboarding.md
client-intake-process.md
monthly-financial-close.md
vendor-selection-and-approval.md
```

**Rules:**
- All lowercase
- Hyphens between words (not underscores, not spaces)
- No version numbers in the file name (version is tracked inside the document)
- Use `.md` (Markdown) as the file extension
- Name the file after the process, not the department (e.g., `employee-onboarding.md`, not `hr-sop-001.md`)

### SOP Numbering

Every SOP gets a unique identifier. Format: `SOP-[DEPT]-[NNN]`

| Prefix | Department |
|---|---|
| OPS | Operations |
| FIN | Finance |
| HR | Human Resources |
| SAL | Sales / Business Development |
| MKT | Marketing |
| IT | Information Technology |
| CS | Customer Service / Support |
| LGL | Legal / Compliance |
| ADM | Administration |

**Examples:** `SOP-OPS-001`, `SOP-FIN-003`, `SOP-HR-012`, `SOP-SAL-001`

Number sequentially within each department. Do not reuse numbers from retired SOPs -- skip the number and leave a note in the SOP index that the number is retired.

### Document Structure

Every SOP must include the following sections, in this order. Do not rearrange or skip sections. If a section is not applicable (e.g., no definitions are needed), include the section heading and write "Not applicable for this SOP" rather than deleting it. This keeps the structure predictable.

1. **Title** -- Clear, descriptive name of the process
2. **Metadata Table** -- SOP number, version, dates, owner, approver, department
3. **Purpose** -- Why this SOP exists (2-4 sentences)
4. **Scope** -- Who it applies to, what triggers it, what is excluded
5. **Roles & Responsibilities** -- Every role involved and what they do
6. **Prerequisites** -- What must be true before the process begins
7. **Procedure** -- The numbered steps, organized into phases
8. **Exceptions** -- Known situations where the standard process does not apply
9. **Definitions & Acronyms** -- Specialized terms used in the document
10. **Related Documents** -- Links to connected SOPs, templates, and policies
11. **Revision History** -- Chronological log of every change

### Metadata Table Format

Use this exact format at the top of every SOP, directly below the title:

```markdown
| Field | Details |
|---|---|
| **SOP Number** | SOP-DEPT-NNN |
| **Version** | X.Y |
| **Effective Date** | YYYY-MM-DD |
| **Last Reviewed** | YYYY-MM-DD |
| **Owner** | [Full Name, Title] |
| **Approved By** | [Full Name, Title] |
| **Department** | [Department Name] |
```

### Writing Steps

**Numbered lists** for sequential steps (order matters -- the reader must do Step 3 before Step 4):

```markdown
1. Open the client's file in the shared drive.
2. Review the signed agreement for the payment schedule.
3. Generate the invoice in QuickBooks using the details from the agreement.
```

**Bullet lists** for non-sequential items (order does not matter -- these can be done in any order):

```markdown
- Monitor, keyboard, and mouse
- Building access badge
- Welcome kit (company swag, notebook, pen)
```

**Checkboxes** for items that must be verified or confirmed:

```markdown
- [ ] I-9 is complete and filed
- [ ] All tax forms are submitted
- [ ] Benefits enrollment is finalized or waived in writing
```

**Step writing rules:**
- Start every step with an action verb: Open, Navigate, Send, Review, Create, Update, Verify, Calculate, Confirm, Schedule, Download, Enter, Record
- One action per step. If a step contains "and," consider whether it should be two separate steps.
- Include the specific tool, system, or location: "Open QuickBooks" not "Open the accounting software" (unless you genuinely support multiple options)
- Include the expected timeframe when it matters: "within 24 business hours," "by end of day," "before the 10th of the month"
- If a step requires a decision, write both paths clearly using sub-steps

**Decision points:**

```markdown
7. Review the expense report for policy compliance.
   - **If approved:** Record the expense in QuickBooks and queue the reimbursement.
   - **If rejected:** Notify the employee with a specific explanation of which items
     were rejected and why. The employee may revise and resubmit.
```

### Text Formatting

| Element | Format | Example |
|---|---|---|
| Role names | **Bold** | **Operations Manager** |
| Tool/system names | **Bold** | **QuickBooks**, **Slack**, **HubSpot** |
| Critical actions or warnings | **Bold** | **Do not skip this step.** |
| File paths and system values | `Code` | `Finance > Monthly Close > 2025 > January` |
| Notes or clarifications | *Italics* | *This step is only required for accrual-basis accounting.* |
| Definitions inline | Parenthetical | DSO (Days Sales Outstanding -- how quickly clients pay) |

**Horizontal rules** (`---`) between major sections for visual separation.

**Tables** for structured reference information (roles, metrics, definitions, exception lists).

### Phases and Sub-sections

For procedures with more than 8-10 steps, organize the steps into phases. Each phase gets:

- A descriptive name (e.g., "Phase 3: Reconciliation")
- The responsible role
- The expected timeline

```markdown
### Phase 2: Transaction Processing (Days 1-3 of new month)

**Responsible:** Finance Lead
**Timeline:** Complete by end of business Day 3.

6. Import and categorize all bank transactions...
7. Import and categorize all credit card transactions...
```

Phases make long SOPs scannable. A reader who is already familiar with Phases 1-3 can jump directly to Phase 4 without scrolling through steps they know.

---

## Versioning

### Version Numbers

- Start every new SOP at version **1.0**
- **Minor updates** (typos, clarification, adding a note, correcting a link): increment the minor version: 1.0 to 1.1, 1.1 to 1.2, etc.
- **Major updates** (new steps added, steps removed, process changed, tools changed, roles changed): increment the major version: 1.x to 2.0, 2.x to 3.0, etc.

| Change Type | Version Bump | Example |
|---|---|---|
| Fix a typo in Step 4 | Minor (1.0 to 1.1) | Corrected "Quickbooks" to "QuickBooks" |
| Add a clarifying note to an existing step | Minor (1.1 to 1.2) | Added note about holiday scheduling |
| Rewrite the reconciliation phase | Major (1.2 to 2.0) | Restructured Phase 4 with new reconciliation steps |
| Change the accounting software from Xero to QuickBooks | Major (2.0 to 3.0) | Replaced all Xero references with QuickBooks |
| Add a new role to the process | Major | Added Account Manager role and handoff step |

### Revision History

Every change, no matter how small, gets logged in the Revision History table at the bottom of the document. Never delete old entries -- the history is an audit trail.

```markdown
| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2025-01-15 | Sarah Chen | Initial version |
| 1.1 | 2025-03-22 | Sarah Chen | Corrected payroll system name in Step 6 |
| 2.0 | 2025-09-01 | Sarah Chen | Added Phase 3 (Adjustments). Updated tool references after QuickBooks migration. |
```

### Effective Date vs. Last Reviewed Date

- **Effective Date:** The date this version of the SOP went into effect. Update this only when a new version is published.
- **Last Reviewed Date:** The date someone reviewed the SOP and confirmed it is still accurate. Update this even if no changes were made. A review with no changes means the SOP was reviewed and confirmed current.

---

## Review Cadence

SOPs are living documents. An outdated SOP is worse than no SOP because people follow the wrong instructions with confidence.

### Recommended Review Frequencies

| SOP Category | Review Frequency | Rationale |
|---|---|---|
| Core daily operations (processes executed every day) | Every 6 months | High-frequency processes drift quickly. Catch changes before they become ingrained habits. |
| Regular processes (weekly or monthly cadence) | Annually | These change less often but should still be validated yearly. |
| Compliance and regulatory procedures | When regulations change, minimum annually | Regulatory changes can happen anytime. Subscribe to relevant update sources. |
| Newly created SOPs | 30 days after initial publication, then standard cadence | The first version always has gaps. An early review catches them while the process is fresh. |
| SOPs for processes that recently changed tools or systems | 30 days after the change, then standard cadence | Tool migrations always surface undocumented steps. |

### How to Conduct a Review

1. **The SOP owner initiates the review.** Set calendar reminders when the SOP is published. Do not rely on memory.
2. **Read the SOP end-to-end.** Do not skim. Read every step.
3. **Walk the process.** If possible, observe someone executing the procedure or execute it yourself. Compare reality to documentation.
4. **Check for:**
   - Steps that are no longer performed
   - Steps that are performed but not documented
   - Tools or systems that have changed
   - Role titles or responsibilities that have shifted
   - Links or file paths that are broken
   - Prerequisites that are no longer relevant or new ones that should be added
5. **Update the SOP** if changes are needed. Follow the versioning rules above.
6. **If no changes are needed,** update the "Last Reviewed" date in the metadata table. This confirms the SOP was reviewed and is current.
7. **Notify the team** if the update includes substantive changes to the procedure. A Slack message or email noting what changed and why is sufficient.

### Triggers for an Unscheduled Review

Do not wait for the scheduled review if any of the following occur:

- A tool or system used in the process is replaced or significantly updated
- A role involved in the process is restructured or eliminated
- A compliance or regulatory requirement changes
- An incident or error occurs that the SOP should have prevented
- Multiple people report confusion about the same step
- A new team member follows the SOP and gets stuck (this is a signal, not a complaint)

---

## Naming Standards for Common Elements

### Templates and Supporting Documents

SOPs often reference templates, forms, and supporting documents. Use this naming convention:

```
[SOP Number]-[Letter]: [Document Name]
```

**Examples:**
- HR-001-A: Role-Specific Training Plan Template
- HR-001-B: Welcome Email Template
- FIN-001-A: Month-End Reminder Template
- SAL-001-A: Proposal Template

### File Storage Paths

Always use the full path when referencing file locations in an SOP. Use the `>` character to denote folder hierarchy:

```
Finance > Monthly Close > 2025 > January > Bank Reconciliation
HR > Active Onboarding > Onboarding - Smith, Jane - 2025-09-15.xlsx
Sales > Templates > Proposal Template - Current.docx
```

Do not use system-specific path separators (/ or \) -- `>` is platform-neutral and readable.

### Pipeline Stages and Status Values

When referring to CRM stages, ticket statuses, or workflow states, use the exact name as it appears in the system, formatted in quotes:

```
Update the deal stage to "Proposal Sent" in HubSpot.
Move the ticket to "Awaiting Customer Response" in the help desk.
```

---

## Common Mistakes to Avoid

### 1. Writing for yourself instead of the reader

You know the process. The reader does not. Spell out what seems obvious. Define acronyms. Include links to tools and resources. If you find yourself thinking "everyone knows this" -- write it down anyway.

### 2. Using vague time references

"Soon," "promptly," "in a timely manner," and "as needed" are meaningless in an SOP. Use specific timeframes: "within 24 business hours," "by the 10th of the month," "before the end of the business day."

### 3. Skipping the exceptions section

Every process has edge cases. If you do not document them, people will either guess (inconsistently) or interrupt someone to ask (inefficiently). Write down the exceptions you know about and add new ones as they come up.

### 4. Making SOPs too long

If an SOP is longer than 5-6 printed pages, consider splitting it into multiple SOPs that reference each other. A 20-page SOP will not be read, maintained, or followed. Break large processes into logical sub-processes, each with its own SOP.

### 5. Failing to assign an owner

An SOP without an owner is an SOP that will not be maintained. Every SOP needs one person (by role, not by name, in case of turnover) who is responsible for keeping it current and initiating reviews.

### 6. Including screenshots that will break

Screenshots of software interfaces go stale quickly. If you include screenshots, accept that you are committing to updating them every time the software changes. Consider whether a text description is more maintainable: "Click the gear icon in the top-right corner, then select 'Account Settings'" ages better than a screenshot that is outdated after the next UI update.

### 7. Writing "see above" or "as previously mentioned"

SOPs are reference documents, not narratives. People jump to specific sections. If a step needs information from an earlier section, restate it briefly or link to the specific section. Do not make the reader hunt.

### 8. Documenting aspirational processes

Write the SOP for the process as it is actually performed today. If you want to document a future improved process, label it clearly as a draft or target state. Mixing "how it works now" with "how we wish it worked" creates confusion.

---

## Quick Reference Checklist

Use this checklist when reviewing an SOP before publishing:

- [ ] Title is clear and descriptive
- [ ] Metadata table is complete (SOP number, version, dates, owner, approver, department)
- [ ] Purpose explains why the SOP exists in 2-4 sentences
- [ ] Scope defines who it applies to, what triggers it, and what is excluded
- [ ] All roles involved are listed with their responsibilities
- [ ] Prerequisites are documented (or marked "None")
- [ ] Steps are numbered, start with action verbs, and specify one action each
- [ ] Steps include specific tool names, file paths, and timeframes
- [ ] Decision points have all branches documented
- [ ] Exceptions are listed with modified procedures and approval authority
- [ ] Definitions section covers any specialized terms or acronyms
- [ ] Related documents are linked
- [ ] Revision history includes the current version entry
- [ ] The SOP has been tested by someone who did not write it
- [ ] A review date is set and a calendar reminder is in place
- [ ] The file name follows kebab-case convention
- [ ] Text formatting follows this style guide (bold for roles/tools, code for paths, etc.)

---

*Part of the [Relay▸Launch SOP Starter Kit](README.md). Questions or suggestions? Open an issue or see [CONTRIBUTING.md](../CONTRIBUTING.md).*
