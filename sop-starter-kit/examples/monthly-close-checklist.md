# Monthly Financial Close Process

| Field | Details |
|---|---|
| **SOP Number** | SOP-FIN-001 |
| **Version** | 2.0 |
| **Effective Date** | 2025-08-01 |
| **Last Reviewed** | 2026-01-15 |
| **Owner** | Angela Okafor, Finance Lead |
| **Approved By** | Marcus Rivera, Managing Director |
| **Department** | Finance |

---

## Purpose

This procedure defines the standard process for closing the company's financial books at the end of each month. A consistent, thorough month-end close ensures that financial records are accurate, complete, and available on a predictable schedule. Business decisions should be based on real numbers, not estimates or gut feelings. This process produces the financial reports, reconciliations, and metrics that leadership needs to manage the business effectively.

---

## Scope

**Applies to:** All monthly financial closing activities for the company, including revenue recognition, expense categorization, bank and credit card reconciliation, accounts receivable and payable review, and financial reporting.

**Timeline:** The close period spans from the last 3 business days of the current month through the 10th business day of the following month. The books should be locked by the 10th.

**Triggers:** The close process begins automatically on the third-to-last business day of every month. The Finance Lead initiates Phase 1 without needing to be prompted.

**Exclusions:** Year-end close and annual financial statements require additional procedures documented in SOP-FIN-002 (Annual Close and Tax Preparation). Audit preparation is covered in SOP-FIN-003.

---

## Roles & Responsibilities

| Role | Responsibility |
|---|---|
| **Finance Lead / Bookkeeper** | Executes the close process end-to-end. Performs reconciliations, enters adjustments, generates reports, and prepares the month-end summary. |
| **Operations Manager** | Reviews financial reports, flags discrepancies, asks questions, and approves the final numbers before the period is locked. |
| **Managing Director** | Receives and reviews the month-end financial summary. Participates in the financial review meeting. Makes strategic decisions based on the data. |
| **Department Leads** | Submit all expense reports and receipts by the stated deadline. Review and confirm charges allocated to their department. Flag any missing or incorrect items. |
| **All Employees** | Submit personal expense reports and receipts by the monthly deadline. |

---

## Prerequisites

- [ ] Accounting software (QuickBooks Online) is current and accessible
- [ ] Bank feeds and credit card feeds are connected and syncing daily
- [ ] All employees and department leads know the expense submission deadline (communicated at the start of each month and reinforced with the pre-close reminder)
- [ ] Chart of accounts is up to date and reviewed within the last 6 months
- [ ] Budget for the current fiscal year has been entered into the accounting system for variance reporting
- [ ] Prior month's close is fully completed and that period is locked

---

## Procedure

### Phase 1: Pre-Close Preparation (Last 3 business days of the month)

**Responsible:** Finance Lead
**Timeline:** Complete before the last business day of the month.

1. **Send the pre-close reminder to all employees.** Email and Slack message (use the "Month-End Reminder" template in `Finance > Templates > Month-End Reminder.md`). Include:
   - Expense report submission deadline: last business day of the month, 5:00 PM local time
   - What to submit: all receipts, mileage logs, and reimbursement requests for expenses incurred during the month
   - Where to submit: expense reporting system (Expensify) or the shared expense submission form
   - Reminder that late submissions will be pushed to the following month

2. **Verify all client invoices for the month have been issued.** Review the project management tool (Asana) and any active engagement agreements to confirm:
   - All milestone-based invoices that are due have been generated and sent
   - All retainer invoices for the month have been generated and sent
   - Any time-and-materials invoices are calculated and sent based on approved time logs
   - Cross-reference the invoice register in QuickBooks with the list of active engagements

3. **Confirm all vendor bills have been received and entered.** Review the accounts payable queue:
   - Check the company email for any outstanding vendor invoices
   - Log into vendor portals for recurring services (hosting, software subscriptions, insurance, etc.) and download statements
   - Enter any bills that have been received but not yet recorded in QuickBooks
   - For expected bills that have not arrived, contact the vendor or accrue the estimated amount (see Step 12)

4. **Verify payroll has been processed and recorded.** Confirm:
   - All payroll runs for the month are complete in Gusto
   - Payroll journal entries have synced to QuickBooks (if automatic) or have been entered manually
   - Employer tax liabilities are recorded
   - Any payroll adjustments (bonuses, corrections, retroactive changes) are reflected

5. **Review open purchase orders and commitments.** Check for any approved purchases that have been received but not yet invoiced. If goods or services were received this month, accrue the expense even if the bill has not arrived.

---

### Phase 2: Transaction Processing and Categorization (Days 1-3 of the new month)

**Responsible:** Finance Lead
**Timeline:** Complete by the end of business Day 3.

6. **Import and categorize all bank transactions.** In QuickBooks:
   - Download or sync all transactions from every bank account through the last day of the prior month
   - Categorize each transaction to the correct account in the chart of accounts
   - Match transactions to existing invoices, bills, or transfers where applicable
   - Investigate and resolve any unmatched or unfamiliar transactions (contact the card holder or check bank records)
   - Clear the bank feed queue entirely -- zero uncategorized bank transactions remaining

7. **Import and categorize all credit card transactions.** For each company credit card:
   - Download or sync all transactions through the statement closing date
   - Match each transaction to a receipt (Expensify auto-matches, but verify)
   - Categorize each transaction to the correct expense account
   - Flag any transactions missing receipts and follow up with the card holder
   - Clear the credit card feed queue entirely -- zero uncategorized credit card transactions remaining

8. **Process employee expense reports.** For each submitted report:
   - Verify all receipts are attached and legible
   - Confirm each expense complies with the company expense policy (see `Company > Policies > Expense Policy.pdf`)
   - Approve or reject line items (notify the employee of any rejections with an explanation)
   - Record approved expenses in QuickBooks under the correct categories
   - Queue approved reimbursements for payment (next scheduled payment run)

9. **Record revenue correctly.** Review all revenue transactions for the month:
   - Cash-basis revenue: confirm all payments received are recorded and categorized as income in the correct revenue account
   - If the company uses accrual accounting: recognize revenue for work delivered during the month, regardless of when payment was received. Ensure deferred revenue (payments received for future work) is properly recorded as a liability, not income
   - Reconcile total monthly revenue against the invoice register and payment receipts

10. **Process intercompany transactions and owner draws/contributions (if applicable).** Record any:
    - Owner draws or distributions
    - Owner contributions or loans to the business
    - Transfers between business entities (if the company has multiple entities)
    - Ensure these are recorded in the correct equity or liability accounts, not as expenses or income

11. **Review the "Uncategorized" and "Ask My Accountant" accounts.** These accounts must be at zero before proceeding. Every transaction must be categorized. If you are unsure about a transaction, research it now -- do not leave it for later. Common culprits:
    - Bank fees that did not auto-categorize
    - Refunds or credits that need to be matched to the original transaction
    - Transfers between accounts that were recorded as expenses

---

### Phase 3: Adjustments and Accruals (Days 3-4 of the new month)

**Responsible:** Finance Lead
**Timeline:** Complete by end of business Day 4.

12. **Record accrued expenses.** Enter journal entries for expenses that were incurred during the month but have not yet been billed. Common accruals for small businesses:
    - Professional services fees (legal, accounting) if the invoice has not arrived
    - Contractor invoices for work completed but not yet billed
    - Utility bills (if the billing cycle does not align with the calendar month)
    - Interest on loans or lines of credit

    Use the memo field to note "Month-end accrual -- [description]" so these are easy to identify and reverse.

13. **Record prepaid expense amortization.** If the company has prepaid expenses (annual insurance premiums, annual software licenses paid upfront, prepaid rent), record the monthly amortization entry:
    - Debit the relevant expense account (e.g., Insurance Expense)
    - Credit the prepaid asset account (e.g., Prepaid Insurance)
    - Amount = total prepaid / number of months covered

14. **Record depreciation.** If the company owns fixed assets (equipment, vehicles, furniture, leasehold improvements):
    - Calculate or verify the monthly depreciation amount for each asset (straight-line or per your accountant's schedule)
    - Debit Depreciation Expense
    - Credit Accumulated Depreciation
    - Maintain the fixed asset register with current book values (`Finance > Assets > Fixed Asset Register.xlsx`)

15. **Record deferred revenue adjustments.** If clients pay upfront for multi-month engagements:
    - Calculate the revenue earned this month based on work delivered or time elapsed
    - Debit Deferred Revenue (liability)
    - Credit the appropriate Revenue account
    - The remaining balance in Deferred Revenue should represent work not yet delivered

16. **Review and reverse prior month accruals (if applicable).** If last month's accruals have now been replaced by actual invoices, reverse the accrual entries and record the actual amounts. This prevents double-counting.

---

### Phase 4: Reconciliation (Days 4-6 of the new month)

**Responsible:** Finance Lead
**Timeline:** Complete by end of business Day 6.

17. **Reconcile each bank account.** For every bank account the company holds:
    - Download the official bank statement for the month from the bank's website
    - In QuickBooks, run the reconciliation tool for the account
    - Match each transaction on the bank statement to the corresponding entry in QuickBooks
    - Investigate and resolve any discrepancies:
      - Outstanding checks (issued but not yet cashed) -- confirm they are still valid
      - Deposits in transit (recorded in QuickBooks but not yet on the bank statement) -- confirm they cleared in the following month
      - Bank fees or interest that were not auto-imported
    - The reconciled balance must match the bank statement balance exactly. A difference of even $0.01 must be investigated and resolved.
    - Save a copy of the reconciliation report and the bank statement to `Finance > Monthly Close > [Year] > [Month] > Bank Reconciliation`

18. **Reconcile each credit card account.** For every company credit card:
    - Download the credit card statement for the month
    - Reconcile in QuickBooks: match each statement transaction to the recorded entry
    - Resolve any discrepancies (pending charges, disputed transactions, returns/credits)
    - The reconciled balance must match the credit card statement balance exactly
    - Save the reconciliation report and statement to `Finance > Monthly Close > [Year] > [Month] > Credit Card Reconciliation`

19. **Review Accounts Receivable (AR).** Generate the AR Aging Report in QuickBooks. Review:
    - **Current (0-30 days):** No action needed. Confirm invoices are accurate.
    - **31-60 days overdue:** Send a friendly payment reminder email to each client. Use the "Payment Reminder - Friendly" template.
    - **61-90 days overdue:** Send a firmer reminder. The BDL or Account Manager should follow up with a phone call. Escalate to the Operations Manager.
    - **Over 90 days overdue:** Escalate to the Managing Director. Evaluate whether to engage a collections process, negotiate a payment plan, or write off the receivable. Any write-off requires Managing Director approval.
    - Document all collection actions in the CRM and the AR tracking log.
    - Update the AR Aging Report and save to `Finance > Monthly Close > [Year] > [Month] > AR Aging`

20. **Review Accounts Payable (AP).** Generate the AP Aging Report in QuickBooks. Review:
    - Confirm all bills due within the next 30 days are scheduled for payment
    - Identify any early payment discounts available and capture them if cash flow allows
    - Flag any disputed bills and document the dispute status
    - Confirm no bills have been double-entered or double-paid
    - Save the AP Aging Report to `Finance > Monthly Close > [Year] > [Month] > AP Aging`

21. **Reconcile payroll.** Compare the payroll register from Gusto to the payroll entries in QuickBooks:
    - Gross wages should match
    - Employer tax liabilities (FICA, FUTA, SUTA) should match
    - Benefits deductions and employer contributions should match
    - Net pay (total disbursements) should match the bank transactions
    - Resolve any discrepancies before proceeding

22. **Reconcile sales tax (if applicable).** If the company collects sales tax:
    - Verify that sales tax collected matches the sales tax liability in QuickBooks
    - Confirm the filing deadline for the current period
    - If filing is due, prepare and submit the sales tax return
    - Record the payment when filed

---

### Phase 5: Financial Reporting and Analysis (Days 6-8 of the new month)

**Responsible:** Finance Lead
**Timeline:** Reports ready for review by end of business Day 8.

23. **Generate the Profit & Loss Statement (Income Statement) for the month.** In QuickBooks, run the P&L for the month. Also generate:
    - P&L: Budget vs. Actual for the month (flag any line item variance greater than 10% or $500, whichever is larger)
    - P&L: Current month vs. same month prior year (year-over-year comparison)
    - P&L: Year-to-date

24. **Generate the Balance Sheet as of month-end.** Review for:
    - Assets = Liabilities + Equity (this must balance; if it does not, there is an error in the books)
    - Any unusual or unexpected account balances (negative balances in asset accounts, unexpected liability balances)
    - Cash and cash equivalent balances match the reconciled bank balances
    - AR and AP balances match the aging reports generated in Phase 4

25. **Generate the Cash Flow Statement (or prepare a cash flow summary).** At minimum, document:
    - Beginning cash balance (1st of the month)
    - Cash inflows: client payments received, other income
    - Cash outflows: payroll, vendor payments, rent, loan payments, owner draws, other
    - Ending cash balance (last day of the month)
    - Net cash change for the month

26. **Calculate key financial metrics.** Update the KPI dashboard or tracking spreadsheet (`Finance > KPIs > Monthly KPI Tracker.xlsx`):

    | Metric | How to Calculate | Why It Matters |
    |---|---|---|
    | Monthly revenue | Total income from all revenue accounts | Top-line growth tracking |
    | Monthly expenses | Total of all expense accounts | Spending discipline |
    | Gross profit margin | (Revenue - COGS) / Revenue | Profitability of services before overhead |
    | Net profit margin | Net income / Revenue | Bottom-line profitability |
    | Operating expense ratio | Total operating expenses / Revenue | Overhead efficiency |
    | Cash on hand | Ending cash balance across all accounts | Liquidity and runway |
    | Cash runway | Cash on hand / Average monthly operating expenses | How many months the business can operate at current spending |
    | Accounts receivable days (DSO) | (AR balance / Revenue) x 30 | How quickly clients are paying |
    | Accounts payable days (DPO) | (AP balance / COGS) x 30 | How quickly the company is paying vendors |
    | Revenue per employee | Monthly revenue / Number of FTEs | Productivity and scaling efficiency |
    | Monthly recurring revenue (MRR) | Sum of all active retainer/subscription amounts | Revenue predictability |

27. **Prepare the month-end financial summary.** Write a 1-page narrative (not just numbers) that covers:
    - Revenue: total, vs. budget, vs. prior month, vs. same month last year. What drove the result?
    - Expenses: total, any notable increases or one-time costs, progress against budget
    - Cash position: healthy or concerning? Any upcoming large outlays to plan for?
    - AR status: any collections concerns?
    - Key wins or concerns: new client revenue, lost client impact, unexpected expenses, trends to watch
    - Action items: specific recommendations based on the numbers (e.g., "AR over 60 days has increased to $12,400 -- recommend the Account Manager contact Client X and Client Y this week")

    Save the summary to `Finance > Monthly Close > [Year] > [Month] > Month-End Summary - [Month Year].pdf`

---

### Phase 6: Review, Approval, and Period Lock (Days 8-10 of the new month)

**Responsible:** Finance Lead, Operations Manager, Managing Director
**Timeline:** Complete by end of business Day 10. The period must be locked by this date.

28. **Schedule and conduct the monthly financial review meeting (30-45 minutes).** Attendees: Finance Lead, Operations Manager, Managing Director. Agenda:
    - Finance Lead walks through the P&L, highlighting variances to budget and prior periods (10 min)
    - Review the Balance Sheet for any unusual items (5 min)
    - Review cash position and runway (5 min)
    - Review AR aging and any collection concerns (5 min)
    - Discuss the key metrics and trends from the KPI dashboard (5 min)
    - Discuss action items: what needs to change based on these numbers? (10 min)

29. **Document action items from the review meeting.** Finance Lead records decisions and action items in the meeting notes. Assign owners and due dates. Store meeting notes in `Finance > Monthly Close > [Year] > [Month] > Review Meeting Notes - [Month Year].md`

30. **Make any corrections identified during the review.** If the review meeting surfaces errors, missing entries, or reclassifications, the Finance Lead makes the adjustments and updates the affected reports. Note all post-review adjustments in the revision log.

31. **Obtain sign-off.** Operations Manager and Managing Director confirm (via email or a shared sign-off document) that they have reviewed and approved the month-end financials. This confirmation is filed with the close package.

32. **Lock the accounting period.** In QuickBooks, close the month:
    - Go to Settings > Account and Settings > Advanced > Close the books
    - Set the closing date to the last day of the month being closed
    - Set a closing date password (shared only with the Finance Lead and Managing Director)
    - This prevents anyone from accidentally modifying transactions in the closed period

33. **File the complete close package.** Save all supporting documents to `Finance > Monthly Close > [Year] > [Month]`:
    - Bank statements and reconciliation reports
    - Credit card statements and reconciliation reports
    - AR Aging Report
    - AP Aging Report
    - Payroll reconciliation
    - Profit & Loss Statement (all versions: monthly, budget vs. actual, YoY, YTD)
    - Balance Sheet
    - Cash Flow Statement or summary
    - KPI dashboard (updated)
    - Month-End Financial Summary narrative
    - Review meeting notes with action items
    - Sign-off confirmation

34. **Update the financial dashboard.** If the company maintains a shared KPI dashboard (Google Sheets, Notion, or a BI tool), update it with the finalized numbers so that all stakeholders have access to current data without needing to request reports.

35. **Set the reminder for next month.** Confirm the calendar reminder for next month's pre-close phase is set. If there are holidays in the upcoming close window, adjust the timeline accordingly (see Exceptions).

---

## Monthly Close Calendar Summary

| Phase | Timing | Key Deliverables |
|---|---|---|
| Phase 1: Pre-Close | Last 3 business days of month | Reminders sent, invoices issued, bills entered, payroll verified |
| Phase 2: Transaction Processing | Days 1-3 of new month | All transactions categorized, expenses processed, revenue recorded |
| Phase 3: Adjustments | Days 3-4 of new month | Accruals, amortization, depreciation, deferred revenue entries |
| Phase 4: Reconciliation | Days 4-6 of new month | Bank, credit card, AR, AP, and payroll reconciled |
| Phase 5: Reporting | Days 6-8 of new month | P&L, Balance Sheet, Cash Flow, KPIs, narrative summary |
| Phase 6: Review & Lock | Days 8-10 of new month | Management review, corrections, sign-off, period locked, documents filed |

---

## Exceptions

| Exception | Condition | Modified Procedure | Approved By |
|---|---|---|---|
| **Year-end close** | December close (or fiscal year-end) | Requires additional steps: annual adjustments, year-end accruals, tax provision estimate, 1099 preparation, audit prep. Follow SOP-FIN-002 in addition to this SOP. Extend the close window by 5 additional business days. | Managing Director |
| **Holiday in the close window** | A company holiday or bank holiday falls within the Day 1-10 close period | Start Phase 1 one business day earlier for each holiday. Communicate the adjusted timeline to all employees with the pre-close reminder. | Finance Lead |
| **Accounting software migration** | The company is transitioning to a new accounting system | The first close on the new system may require 3-5 extra business days. Run a parallel close on the old system for the first month to validate accuracy. Requires Operations Manager oversight. | Operations Manager |
| **Significant one-time event** | A major, unusual transaction occurred during the month (e.g., large asset purchase, legal settlement, insurance claim, M&A activity) | Consult with the external accountant or CPA before recording the transaction. Document the accounting treatment and rationale. Include a detailed note in the month-end summary. | Managing Director |
| **Finance Lead absence** | The Finance Lead is unavailable during the close period | The Operations Manager executes the close using this SOP. The Finance Lead provides a handoff briefing before their absence, noting any in-progress items or known issues. External accountant is on standby for questions. | Operations Manager |

---

## Definitions & Acronyms

| Term | Definition |
|---|---|
| **P&L** | Profit and Loss Statement, also called the Income Statement. Shows revenue, expenses, and net income for a period. |
| **Balance Sheet** | A financial statement showing the company's assets, liabilities, and equity at a specific point in time. Must always balance (Assets = Liabilities + Equity). |
| **AR** | Accounts Receivable -- money owed to the company by clients for delivered services or products. |
| **AP** | Accounts Payable -- money the company owes to vendors and suppliers. |
| **DSO** | Days Sales Outstanding -- a measure of how quickly the company collects payment. Lower is better. Calculated as (AR balance / Revenue) x 30. |
| **DPO** | Days Payable Outstanding -- a measure of how quickly the company pays its vendors. |
| **MRR** | Monthly Recurring Revenue -- the predictable, repeating revenue from active retainers or subscription agreements. |
| **COGS** | Cost of Goods Sold -- the direct costs attributable to delivering services or producing goods. For a consulting firm, this typically includes contractor costs and direct labor. |
| **Accrual** | An accounting entry that recognizes an expense or revenue in the period it was incurred or earned, regardless of when cash changes hands. |
| **Deferred Revenue** | A liability representing cash received from clients for services not yet delivered. Recognized as revenue when the work is performed. |
| **Reconciliation** | The process of comparing two sets of records (e.g., bank statement vs. accounting software) to verify they agree. |
| **Close the Books** | The process of finalizing all financial transactions for a period, generating reports, and locking the period to prevent further changes. |

---

## Related Documents

- SOP-FIN-002: Annual Close and Tax Preparation
- SOP-FIN-003: Audit Preparation
- Company Expense Policy (`Company > Policies > Expense Policy.pdf`)
- Chart of Accounts (`Finance > Chart of Accounts - Current.pdf`)
- Budget vs. Actual Template (`Finance > Templates > Budget vs Actual.xlsx`)
- Fixed Asset Register (`Finance > Assets > Fixed Asset Register.xlsx`)
- Monthly KPI Tracker (`Finance > KPIs > Monthly KPI Tracker.xlsx`)
- Month-End Reminder Template (`Finance > Templates > Month-End Reminder.md`)
- Payment Reminder Email Templates (`Finance > Templates > Payment Reminders`)
- KPI Dashboard Templates (see `../kpi-dashboard-templates/`)

---

## Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2025-01-15 | Angela Okafor | Initial version with basic 5-phase close process |
| 1.1 | 2025-05-01 | Angela Okafor | Added payroll reconciliation step. Added sales tax reconciliation. Expanded KPI section. |
| 2.0 | 2025-08-01 | Angela Okafor | Major revision: added Phase 3 (Adjustments and Accruals) as a separate phase. Added detailed reconciliation procedures. Expanded reporting section with narrative summary requirement. Added Finance Lead absence exception. Added file storage paths for close package. |

---

*This SOP is due for review on 2026-08-01. The Finance Lead is responsible for initiating the review process. Part of the [Relay▸Launch SOP Starter Kit](../README.md).*
