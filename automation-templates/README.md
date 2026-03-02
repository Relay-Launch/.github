# Relay Launch Automation Templates

**Built by [Relay Launch](https://relaylaunch.com) -- Small business automation, operations, and strategic planning.**

---

## What This Is

This is a curated library of production-ready automation templates built from real client engagements. Every template here started as a solution to a problem we saw repeatedly across the small businesses we work with -- missed follow-ups, manual data entry, onboarding bottlenecks, invoicing headaches.

These are not toy examples. Each workflow has been deployed in live environments, refined based on actual failure modes, and documented so you can adapt it to your stack without starting from scratch.

## Who It's For

- **Small business owners** who know they're wasting time on repetitive tasks but aren't sure where to start automating.
- **Operations managers** looking for tested patterns they can deploy this week, not next quarter.
- **Freelancers and solopreneurs** who need to punch above their weight by automating what a larger team would handle manually.
- **Consultants and agencies** who want a head start on building client automations.

If you have fewer than 50 employees and more than 3 tools in your tech stack, you're in the right place.

## How to Use These Templates

### Quick Start

1. **Browse the templates table below** to find a workflow that matches your use case.
2. **Check the supported platforms** -- each template targets a specific automation platform, but the logic transfers across tools.
3. **Download or copy the workflow file** from the `workflows/` directory.
4. **Import it into your platform** (see platform-specific instructions below).
5. **Configure your credentials** -- every template uses placeholder credentials that you'll swap for your own API keys, OAuth connections, etc.
6. **Test with real data** before turning it on for production traffic.

### Importing into Your Platform

**n8n (self-hosted or cloud):**
1. Open your n8n instance.
2. Go to *Workflows* > *Import from File*.
3. Select the `.json` file.
4. Update all credential nodes with your own connections.
5. Activate the workflow.

**Zapier:**
Use the workflow logic as a blueprint. Zapier doesn't support direct JSON imports, but each template's node structure maps cleanly to Zapier's trigger/action model. Follow the node sequence and recreate it in the Zap editor.

**Make (formerly Integromat):**
Make supports JSON blueprint imports. You may need to adjust the schema slightly -- our templates use n8n's node format, but the `guides/` directory includes translation notes for Make scenarios.

**Power Automate:**
Use the workflow logic as a reference architecture. Power Automate's flow designer can replicate these patterns using its connector library. The node descriptions in each template map to equivalent Power Automate actions.

### Reading the Guides

The `guides/` directory contains decision-making frameworks and checklists we use with our own clients. Start with the **Automation Readiness Checklist** if you're not sure whether a process is ready to automate, and read **Choosing Your Platform** if you haven't committed to a tool yet.

---

## Available Templates

| Template | File | Category | Complexity | Description |
|----------|------|----------|------------|-------------|
| Lead Capture to CRM | [`lead-capture-to-crm.json`](workflows/lead-capture-to-crm.json) | Sales | Medium | Captures form submissions from Typeform/Gravity Forms, enriches the lead, routes to your CRM, and notifies your sales team via Slack and email. |
| Client Onboarding Sequence | [`client-onboarding-sequence.json`](workflows/client-onboarding-sequence.json) | Operations | High | End-to-end onboarding: welcome email, project task creation in your PM tool, intro call scheduling via Calendly, and internal team notification. |
| Invoice Follow-Up | [`invoice-follow-up.json`](workflows/invoice-follow-up.json) | Finance | Medium | Monitors unpaid invoices, sends graduated reminder emails (friendly, firm, final), logs activity, and escalates overdue accounts to your team. |

---

## Supported Platforms

| Platform | Import Support | Best For | Pricing |
|----------|---------------|----------|---------|
| **n8n** | Direct JSON import | Technical teams, self-hosted environments, complex branching logic | Free (self-hosted), from $20/mo (cloud) |
| **Zapier** | Blueprint reference | Non-technical users, quick setup, wide app support | Free tier available, from $19.99/mo |
| **Make** | Adapted JSON import | Visual thinkers, complex data transformations, budget-conscious teams | Free tier available, from $9/mo |
| **Power Automate** | Blueprint reference | Microsoft-heavy environments, enterprise compliance needs | Included with Microsoft 365, from $15/user/mo standalone |

See the full platform comparison in [`guides/choosing-your-platform.md`](guides/choosing-your-platform.md).

---

## Guides

| Guide | Description |
|-------|-------------|
| [Choosing Your Platform](guides/choosing-your-platform.md) | Honest, experience-based comparison of Zapier, Make, n8n, and Power Automate. Includes pricing breakdowns, gotchas, and recommendations by business type. |
| [Automation Readiness Checklist](guides/automation-readiness-checklist.md) | A structured checklist to evaluate whether a process is a good automation candidate. Covers prerequisites, common pitfalls, and a scoring rubric. |

---

## A Note on Customization

These templates are starting points, not finished products. Every business has its own tools, naming conventions, and edge cases. We intentionally keep these templates modular so you can:

- Swap out the CRM (HubSpot, Salesforce, Pipedrive -- the logic is the same).
- Replace the notification channel (Slack, Teams, email, SMS).
- Adjust timing and thresholds (how long before a follow-up? how many retries?).
- Add or remove steps without breaking the core flow.

If you need help adapting a template to your specific setup, that's exactly what we do.

---

## About Relay Launch

[Relay Launch](https://relaylaunch.com) is a business consulting firm that helps small businesses streamline operations through automation, process design, and strategic planning.

We work with businesses that have outgrown their manual processes but aren't ready for (or don't need) enterprise software. Our approach is hands-on: we audit your workflows, identify the highest-impact automation opportunities, build and deploy the solutions, and train your team to maintain them.

**What we do:**
- Workflow automation design and implementation
- Operations audits and process optimization
- Technology stack evaluation and integration
- Strategic planning for growth-stage businesses

**Get in touch:**
- Website: [relaylaunch.com](https://relaylaunch.com)
- Email: hello@relaylaunch.com

---

## License

These templates are provided under the MIT License. Use them, modify them, share them. If they save you time, we'd love to hear about it.

If you want hands-on help implementing these in your business, [reach out to us](https://relaylaunch.com/contact).
