# API Integration 101: A Guide for Business Owners

*By Relay▸Launch — written for the people who sign off on integration projects, not the people who build them.*

---

## Who This Is For

You run a business. You use software — probably a CRM, a payment processor, an email tool, a spreadsheet, a project management app, and half a dozen others. And at some point, someone on your team (or a consultant like us) said the words "API integration" to you.

This guide explains what that means, why it matters, how much it typically costs, and how to make good decisions about when to build, when to buy, and when to leave well enough alone.

No code. No jargon without explanation. Just the mental model you need to evaluate integration work with confidence.

---

## What Is an API?

**API** stands for **Application Programming Interface**. That doesn't help much, so here's a better way to think about it:

An API is a **structured way for two pieces of software to talk to each other**.

Think of it like a restaurant. You (the customer) don't walk into the kitchen and cook your own food. Instead, you use a menu (the API documentation), place an order through your server (the API request), and receive your meal (the API response). The kitchen does its thing behind closed doors.

When Stripe processes a payment, it doesn't call you on the phone to tell you. It sends that information through its API. When you want to look up a contact in HubSpot, your software asks HubSpot's API and gets a structured response back.

**The key idea**: APIs let software systems share data and trigger actions in each other without human involvement.

### A Concrete Example

Without an API integration:
1. A customer pays you on Stripe
2. Someone on your team notices the payment
3. They manually copy the customer info into your CRM
4. They manually send a Slack message to the team
5. They manually update the spreadsheet

With an API integration:
1. A customer pays you on Stripe
2. Everything else happens automatically in under a second

That's what we're talking about. Eliminating the manual steps between your tools.

---

## How Integrations Actually Work

Every integration follows the same basic pattern, no matter how complex:

### The Three-Step Pattern

1. **Trigger** — Something happens that starts the process. A payment comes in. A form is submitted. A clock hits 9:00 AM.

2. **Process** — Your integration code receives the trigger, reads the data, transforms it if needed, applies business rules, and decides what to do.

3. **Action** — The integration sends data to another system. Creates a CRM contact. Sends a Slack message. Updates a spreadsheet row.

That's it. Every integration — from a simple Zapier connection to a million-dollar enterprise middleware platform — follows this pattern. The difference is in how much processing happens in the middle and how reliably it runs.

### Webhooks: The "Don't Call Us, We'll Call You" Pattern

Most modern integrations are triggered by **webhooks**. A webhook is when one system sends an automatic notification to another system the moment something happens.

Instead of constantly asking Stripe "did anyone pay yet? how about now? now?" (which is called **polling** and is wasteful), you give Stripe a URL and say "send a message to this address every time someone pays." Stripe pushes the data to you in real time.

Webhooks are the backbone of real-time integrations. Almost every major SaaS tool supports them: Stripe, Shopify, HubSpot, GitHub, Typeform, Calendly, and hundreds more.

### Scheduled Syncs: The "Check Every So Often" Pattern

Not everything needs to happen in real time. Some integrations run on a schedule:

- Sync your CRM contacts to a spreadsheet every 30 minutes
- Generate a revenue report every morning at 8 AM
- Archive completed projects every Sunday night

These are typically simpler to build and maintain than real-time integrations, and for many use cases, "every 15 minutes" is plenty fast enough.

---

## Authentication: How Systems Prove Who They Are

When your integration talks to Stripe or HubSpot, those services need to know it's actually you (and not a random stranger) making the request. This is **authentication**.

There are a few common patterns:

### API Keys

The simplest approach. You get a secret key from the service (like a very long password), and your integration includes it with every request.

**Example**: Stripe gives you a key like `sk_live_abc123...`. Your code sends this key with every request to prove it's authorized.

**Security note**: API keys should be treated like passwords. Never put them in emails, Slack messages, or public code repositories.

### OAuth

A more sophisticated system where your integration asks for permission to act on behalf of a user, and the service grants a temporary token.

**Example**: When you connect Google Sheets to another app, Google shows you a screen asking "Do you want to allow this app to access your spreadsheets?" That's OAuth.

OAuth is more secure because tokens can be limited in scope (read-only vs. read-write) and expire automatically.

### Webhook Signatures

When a service sends you a webhook, you need to verify it's really from that service and not someone impersonating it. Services sign their webhooks with a shared secret, and your code verifies the signature before processing.

**Why this matters**: Without signature verification, anyone who discovers your webhook URL could send fake events to your system. You'd process fake payments, create fake contacts, or trigger fake notifications.

---

## Common Integration Patterns

Over years of building integrations for small businesses, we see the same patterns again and again:

### 1. Notification Routing

**What it does**: When something happens in System A, send a formatted notification to System B.

**Examples**:
- Stripe payment → Slack message
- New form submission → Email to sales team
- Server error → PagerDuty alert

**Complexity**: Low. This is the simplest type of integration and a great place to start.

### 2. Data Sync

**What it does**: Keep data consistent between two systems, either in real time or on a schedule.

**Examples**:
- CRM contacts → Google Sheet
- Shopify orders → Accounting software
- HR system → Payroll system

**Complexity**: Medium. The tricky part is handling conflicts (what if data was changed in both places?) and updates vs. new records.

### 3. Workflow Automation

**What it does**: When a trigger occurs, execute a multi-step process with business logic.

**Examples**:
- Form submission → Validate → Enrich with company data → Score the lead → Route to correct sales pipeline
- New customer signup → Create accounts in three systems → Send welcome sequence → Notify account manager

**Complexity**: Medium to high. The more business rules and branching logic involved, the more complex it gets.

### 4. Aggregation & Reporting

**What it does**: Pull data from multiple sources, compute metrics, and deliver a report.

**Examples**:
- Stripe + CRM + Support tickets → Weekly business dashboard email
- Multiple ad platforms → Unified marketing report
- Sales data → Automated forecasting

**Complexity**: Medium. The hard part is usually getting clean data from multiple sources that structure things differently.

---

## Build vs. Buy: Making the Right Choice

This is the most important decision in any integration project. Here's a framework:

### Buy (Use a No-Code Tool)

**Tools**: Zapier, Make (Integromat), Workato, Tray.io

**Choose this when**:
- The integration is straightforward (trigger → action, minimal logic)
- Both systems are popular and well-supported by the platform
- Volume is low (under a few thousand events per month)
- You want non-technical team members to be able to modify it
- You need it working this week, not this month

**Typical cost**: $20–$100/month for Zapier/Make. Enterprise platforms run $500–$2,000/month.

**Limitations**:
- Complex business logic is hard to express in a visual builder
- Costs scale with volume — high-volume integrations get expensive fast
- You're dependent on the platform (if Zapier goes down, your integration goes down)
- Debugging is harder than reading code
- Some APIs aren't supported or are only partially supported

### Build (Write Custom Code)

**Choose this when**:
- The logic is complex (scoring, routing, conditional branching)
- Volume is high (thousands of events per day)
- You need full control over error handling and retry behavior
- The integration is core to your business operations
- You want to own the infrastructure and not pay per-task fees
- The APIs involved aren't well-supported by no-code platforms

**Typical cost**: $2,000–$15,000 one-time development, plus $5–$50/month hosting.

**Limitations**:
- Requires a developer to build and maintain
- Takes longer to set up initially
- You're responsible for monitoring and fixing issues

### The Hybrid Approach

Many businesses start with Zapier for quick wins, then migrate critical integrations to custom code as they grow. This is a perfectly valid strategy. Use no-code tools to validate that an integration is actually useful before investing in custom development.

---

## What to Look for in an Integration Partner

If you're hiring someone to build integrations for your business, here's what separates good work from bad work:

### Green Flags

- **They ask about your business processes before talking about technology.** The integration should serve the workflow, not the other way around.
- **They use environment variables for configuration.** API keys should never be hardcoded in the source files.
- **They include error handling and logging.** Things will go wrong. Good integrations log what happened so you can diagnose issues.
- **They handle retries gracefully.** Webhooks sometimes fail. Networks are unreliable. Good code accounts for this.
- **They document everything.** Six months from now, someone needs to understand how this works.
- **They set up monitoring.** You should know when an integration breaks, not discover it when a customer complains.

### Red Flags

- **"It works on my machine."** If they can't deploy it to production reliably, it's not done.
- **No error handling.** If the integration crashes silently on unexpected input, you'll lose data.
- **Hardcoded credentials.** This is a security incident waiting to happen.
- **No logging.** When something goes wrong (and it will), you'll be flying blind.
- **"We'll figure out the edge cases later."** Edge cases are where integrations break. They should be figured out now.

---

## Common Pitfalls

These are the problems we see most often when businesses set up integrations:

### 1. Not Handling Duplicates

Webhooks can fire more than once. If your integration creates a new CRM contact every time a webhook fires, you'll end up with duplicates. Good integrations check whether a record already exists before creating a new one.

### 2. Ignoring Rate Limits

APIs limit how many requests you can make per second/minute/hour. If your integration ignores these limits, requests will start failing. Good integrations respect rate limits and queue requests when needed.

### 3. Not Verifying Webhook Signatures

Without verification, anyone who discovers your webhook URL can send fake data to your system. Always verify that webhooks are actually coming from the service they claim to be from.

### 4. Tight Coupling

If your integration is so tightly wired to a specific tool that switching CRMs means rewriting everything, that's a problem. Good integrations use abstraction layers that make it relatively easy to swap out one service for another.

### 5. No Monitoring

An integration that fails silently is worse than no integration at all, because you think the work is being done when it isn't. Set up alerts for failures.

---

## Key Terms Glossary

| Term | Plain-English Meaning |
|------|----------------------|
| **API** | A structured way for two software systems to communicate |
| **Webhook** | An automatic notification sent from one system to another when something happens |
| **Endpoint** | A specific URL that accepts API requests (like a mailing address for data) |
| **Payload** | The actual data sent in an API request or webhook |
| **Authentication** | How a system proves its identity (usually with API keys or tokens) |
| **Rate Limit** | The maximum number of requests an API allows in a time period |
| **Polling** | Repeatedly checking a system for new data (less efficient than webhooks) |
| **Idempotency** | The property that processing the same event twice produces the same result as processing it once |
| **Middleware** | Software that sits between two systems and translates between them |
| **ETL** | Extract, Transform, Load — pulling data from one system, reshaping it, and putting it in another |
| **REST API** | The most common API style; uses standard HTTP methods (GET, POST, PUT, DELETE) |
| **JSON** | The most common data format for APIs; a structured text format that's easy for both humans and machines to read |

---

## Next Steps

If you're a Relay▸Launch client:
- **Quick audit**: We'll review your current tool stack and identify the highest-impact integration opportunities.
- **Proof of concept**: We'll build one integration to demonstrate value before committing to a larger project.
- **Full implementation**: We'll build, deploy, and monitor your complete integration suite.

If you're exploring on your own:
1. **Map your tools.** List every SaaS product your business uses and how data flows between them.
2. **Find the manual steps.** Where is a human copying data from one system to another? That's your first integration candidate.
3. **Start small.** Pick the simplest, highest-frequency manual task and automate it. Build confidence before tackling complex workflows.
4. **Check this cookbook.** The [recipes in this repository](../recipes/) are production-ready starting points for the most common integrations.

---

*Questions? Reach out to [Relay▸Launch](https://github.com/Relay-Launch/.github/issues/new?template=project-request.yml). We help small businesses automate the work that shouldn't require a human.*
