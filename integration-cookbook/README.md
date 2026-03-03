# Relay▸Launch Integration Cookbook

Production-ready integration recipes for small businesses. Copy, configure, deploy.

---

## What This Is

The Integration Cookbook is a collection of standalone Python scripts that connect the tools your business already uses — Stripe, HubSpot, Google Sheets, Slack, email — into automated workflows. Each recipe solves a specific, common problem that small businesses face when their tools don't talk to each other.

These aren't toy examples. Every recipe includes proper error handling, logging, environment variable configuration, and is structured for real deployment. They're designed to run on a $5/month VPS, a Heroku dyno, or a serverless function.

Built and maintained by [Relay▸Launch](https://relaylaunch.com), a business consulting firm specializing in automation, operations, and strategic planning for small businesses.

---

## Available Recipes

| Recipe | What It Does | Key Integrations |
|--------|-------------|------------------|
| [Stripe to Slack Notifications](recipes/stripe-to-slack-notifications.py) | Sends formatted Slack messages when payments succeed, fail, or new subscriptions start | Stripe, Slack |
| [HubSpot to Sheets Sync](recipes/hubspot-to-sheets-sync.py) | Syncs your HubSpot CRM contacts to a Google Sheet on a schedule | HubSpot, Google Sheets |
| [Form to CRM Router](recipes/form-to-crm-router.py) | Receives form submissions, validates and enriches the data, then routes leads to the right CRM pipeline | Webhooks, HubSpot |
| [Email Report Generator](recipes/email-report-generator.py) | Aggregates data from CSV or database, builds a formatted HTML report, and emails it on schedule | CSV/SQLite, SMTP |

---

## Utilities

Shared modules that the recipes build on. You can use these independently in your own integrations.

| Utility | Purpose |
|---------|---------|
| [Webhook Handler](utils/webhook_handler.py) | Reusable Flask-based webhook receiver with signature verification, retry handling, and structured logging |
| [API Client](utils/api_client.py) | Base HTTP client class with rate limiting, automatic retries, and response caching — extend it for any REST API |

---

## Guides

| Guide | Audience |
|-------|----------|
| [API Integration 101](guides/api-integration-101.md) | Business owners and non-technical stakeholders who want to understand what integrations are, how they work, and when to build vs. buy |

---

## Prerequisites

### Runtime

- **Python 3.8+** (tested on 3.8, 3.9, 3.10, 3.11, 3.12)
- `pip` for package management
- A Linux/macOS environment for production (Windows works for development)

### API Keys & Credentials

Each recipe documents its own requirements at the top of the file. Here's the full list across all recipes:

| Service | What You Need | Where to Get It |
|---------|--------------|-----------------|
| Stripe | Secret key + webhook signing secret | [Stripe Dashboard → Developers](https://dashboard.stripe.com/apikeys) |
| Slack | Bot token or incoming webhook URL | [Slack API → Your Apps](https://api.slack.com/apps) |
| HubSpot | Private app access token | [HubSpot → Settings → Integrations → Private Apps](https://app.hubspot.com/private-apps/) |
| Google Sheets | Service account JSON credentials | [Google Cloud Console → IAM & Admin → Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) |
| SMTP | Host, port, username, password | Your email provider (Gmail, SendGrid, Mailgun, etc.) |

### Environment Variables

Every recipe reads its configuration from environment variables. No hardcoded secrets, ever. Copy the example below to a `.env` file and fill in your values:

```bash
# Stripe
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Slack
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T.../B.../...
SLACK_BOT_TOKEN=xoxb-...
SLACK_CHANNEL=#payments

# HubSpot
HUBSPOT_ACCESS_TOKEN=pat-na1-...

# Google Sheets
GOOGLE_SHEETS_CREDENTIALS_FILE=credentials.json
GOOGLE_SHEET_ID=1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms

# SMTP
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM=reports@yourcompany.com
SMTP_TO=team@yourcompany.com

# General
LOG_LEVEL=INFO
FLASK_PORT=5000
```

---

## Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/your-org/integration-cookbook.git
cd integration-cookbook
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
# Edit .env with your actual API keys and configuration
```

### 3. Run a Recipe

```bash
# Webhook-based recipes (Stripe notifications, form router)
python recipes/stripe-to-slack-notifications.py

# Scheduled recipes (HubSpot sync, email reports)
python recipes/hubspot-to-sheets-sync.py

# Or run on a cron schedule
# Every 30 minutes:
# */30 * * * * cd /path/to/integration-cookbook && /path/to/venv/bin/python recipes/hubspot-to-sheets-sync.py
```

---

## Project Structure

```
integration-cookbook/
├── README.md                 # You are here
├── requirements.txt          # All Python dependencies
├── recipes/
│   ├── stripe-to-slack-notifications.py   # Stripe → Slack payment alerts
│   ├── hubspot-to-sheets-sync.py          # HubSpot → Google Sheets sync
│   ├── form-to-crm-router.py             # Form → CRM lead routing
│   └── email-report-generator.py          # Data → HTML email reports
├── utils/
│   ├── webhook_handler.py    # Reusable webhook receiver
│   └── api_client.py         # Reusable API client base class
└── guides/
    └── api-integration-101.md # Non-technical integration guide
```

---

## Deployment Options

These recipes are designed to be deployed however makes sense for your business:

| Method | Best For | Cost |
|--------|----------|------|
| **Cron job on a VPS** | Scheduled sync scripts | $5–10/month |
| **Heroku** | Webhook listeners that need to stay online | Free–$7/month |
| **Railway / Render** | Modern alternative to Heroku | Free tier available |
| **AWS Lambda** | High-volume webhooks, pay-per-use | Pennies/month for most small businesses |
| **Docker** | Consistent environments, easy scaling | Depends on host |

---

## Customization

Every recipe is designed to be forked and modified. Common customizations:

- **Change notification format** — Edit the message templates in the Slack/email recipes
- **Add new webhook event types** — Extend the event handler dictionaries
- **Swap CRM providers** — Replace the HubSpot API calls with your CRM's API
- **Add database storage** — Replace CSV reads with SQLAlchemy queries
- **Chain recipes together** — Use the webhook handler utility to pipe one recipe's output into another

---

## Contributing

Found a bug? Have a recipe idea? We welcome contributions.

1. Fork the repository
2. Create a feature branch (`git checkout -b recipe/new-integration`)
3. Write your recipe following the existing patterns (docstrings, env vars, error handling, logging)
4. Submit a pull request

---

## Support

- **Documentation issues**: Open a GitHub issue
- **Implementation help**: [Contact Relay▸Launch](https://relaylaunch.com/contact) for consulting
- **Custom integrations**: We build bespoke automation for small businesses — [learn more](https://relaylaunch.com/services)

---

## License

MIT License. Use these recipes however you want. Attribution appreciated but not required.

Built with care by [Relay▸Launch](https://relaylaunch.com).
