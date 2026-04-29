<p align="center">
  <img src="https://raw.githubusercontent.com/Relay-Launch/.github/main/profile/repo-card.svg" alt="RelayLaunch — AI Due Diligence Platform" width="100%"/>
</p>

<h3 align="center">Every department. One AI.</h3>

<p align="center">
  <em>AI-powered due diligence that produces the actual deliverable — QoE reports, DD memos, risk packages — in hours, not weeks.</em>
</p>

<p align="center">
  <a href="https://relaylaunch.com"><img src="https://img.shields.io/badge/Website-relaylaunch.com-007AFF?style=for-the-badge&logo=globe&logoColor=white" alt="Website"></a>&nbsp;
  <a href="https://deck.relaylaunch.com"><img src="https://img.shields.io/badge/Relay%E2%96%B8Deck-Platform-0F172A?style=for-the-badge&logo=vercel&logoColor=white" alt="Relay Deck"></a>&nbsp;
  <a href="https://github.com/Relay-Launch/councilverse"><img src="https://img.shields.io/badge/CouncilVerse-Open_Source-10B981?style=for-the-badge&logo=github&logoColor=white" alt="CouncilVerse"></a>&nbsp;
  <a href="mailto:hello@relaylaunch.com"><img src="https://img.shields.io/badge/Contact-hello%40relaylaunch.com-6366F1?style=for-the-badge&logo=mail.ru&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Relay-Launch/councilverse?style=social" alt="GitHub stars">&nbsp;
  <img src="https://img.shields.io/npm/dt/@relaylaunch/councilverse-formations?label=npm%20downloads&color=007AFF" alt="npm downloads">&nbsp;
  <img src="https://img.shields.io/badge/models-8%20across%204%20providers-F59E0B" alt="Multi-model">&nbsp;
  <img src="https://img.shields.io/badge/practice%20areas-9-007AFF" alt="9 Practice Areas">&nbsp;
  <img src="https://img.shields.io/badge/veteran--owned-USMC-0F172A" alt="Veteran-owned">
</p>

---

## What We Build

Most AI tools give you a chatbot. We produce the **artifact your firm sends to clients** — the QoE report, the DD memo, the risk package — with full provenance, multi-model reasoning, and audit trails.

**Target ICP:** CPAs, M&A advisors, deal teams, and service businesses that need AI they can trust and verify.

### The Stack

| Product | What It Does | Status |
|:--------|:-------------|:-------|
| **Relay Pulse** | Deployed AI ops system per client — post-visit engagement, wellness scoring, predictive analytics | Production |
| **Relay Deck** | SaaS command center — document analysis, multi-model council debates, deliverable generation | Production |
| **CouncilVerse** | Open-source multi-agent debate engine — formations, voting, scaffolding | MIT Licensed |

---

## How Multi-Model Council Works

We don't trust a single model. Every analysis runs through **heterogeneous council debates** — multiple AI models from different providers arguing from different training data, scored on evidence quality, not headcount.

```
┌─────────────────────────────────────────────────────────────┐
│                    COUNCIL DEBATE ENGINE                     │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Claude   │  │ DeepSeek │  │ GLM-5.1  │  │ MiniMax  │   │
│  │ Sonnet   │  │ V4-Flash │  │ (Zhipu)  │  │ M2.7     │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │             │             │             │           │
│       └─────────────┴──────┬──────┴─────────────┘           │
│                            │                                │
│                   ┌────────▼────────┐                       │
│                   │  Free-MAD       │                       │
│                   │  Weighted       │                       │
│                   │  Synthesis      │                       │
│                   └────────┬────────┘                       │
│                            │                                │
│                   ┌────────▼────────┐                       │
│                   │  VERDICT        │                       │
│                   │  + Dissent      │                       │
│                   │  + Provenance   │                       │
│                   │  + Audit Trail  │                       │
│                   └─────────────────┘                       │
└─────────────────────────────────────────────────────────────┘
```

**Why this matters:** When models from different training corpora agree, confidence is justified. When they disagree, the dissent surfaces risks a single model would miss.

---

## CouncilVerse — Open Source

Multi-agent debate infrastructure. 15 structured formations. Three-valued voting (KEEP / REFUSE / ABSTAIN). Quality-weighted scoring. Provider-agnostic.

```bash
npx create-councilverse my-council
```

<table>
<tr>
<td width="33%">

### [`councilverse-formations`](https://www.npmjs.com/package/@relaylaunch/councilverse-formations)
15 debate formations including Strategy Room (OODA), Tribunal, Risk Council (Monte Carlo), and Due Diligence (M&A).

</td>
<td width="33%">

### [`councilverse-voting`](https://www.npmjs.com/package/@relaylaunch/councilverse-voting)
Three-valued voting with quality-weighted scoring. Arguments scored on evidence, structure, and specificity.

</td>
<td width="33%">

### [`create-councilverse`](https://www.npmjs.com/package/create-councilverse)
Working council scaffold in 60 seconds. TypeScript configured. Drop in an API key and run.

</td>
</tr>
</table>

**[Source on GitHub](https://github.com/Relay-Launch/councilverse)** · MIT Licensed

---

## Platform Capabilities

<details>
<summary><strong>Relay Deck — Production Features (click to expand)</strong></summary>

| Feature | Description |
|:--------|:------------|
| **Multi-Model Councils** | 8 models from 4 providers debate each analysis |
| **Deliverable Engine** | Generates QoE reports, DD memos, risk packages as PDF |
| **Verdict Library** | Persistent, searchable archive of council decisions |
| **Precedent Search** | Semantic search over past verdicts (pgvector) |
| **Reasoning Traces** | Full audit trail per verdict (Langfuse) |
| **Feedback Flywheel** | Accept/Edit/Reject trains the system on your preferences |
| **Embeddable Widgets** | Iframe verdict cards for reports and dashboards |
| **A2A + MCP Protocols** | Google Agent-to-Agent and Model Context Protocol bridges |
| **HMAC-Signed Verdicts** | Cryptographic provenance for every decision |
| **BYOK** | Bring your own API keys, control model spend |
| **EU AI Act Ready** | JSON-LD transparency manifests |

</details>

<details>
<summary><strong>Technical Architecture (click to expand)</strong></summary>

```
Frontend       Next.js 16 · React 19 · Tailwind CSS 4 · Vercel
Backend        Supabase (Postgres + Auth + RLS + pgvector)
AI Routing     LiteLLM gateway · 8 models · 4 providers
Telemetry      Langfuse Cloud · structured reasoning traces
PDF Engine     @react-pdf/renderer · 6 report templates
Protocols      A2A JSON-RPC · MCP · HMAC-SHA256 signing
Infra          Docker Compose (21 containers) · Cloudflare · GitHub Actions
```

</details>

---

## SaaS Pricing

| Tier | Price | What You Get |
|:-----|:------|:-------------|
| **Free Ops Scan** | $0 | Instant AI operations audit |
| **Pro** | $299/mo | Full platform, 1 seat, 48-hour trial |
| **Team** | $999/mo | 5 seats, priority support |
| **Enterprise** | $3,000/mo | Unlimited seats, SSO, audit trails |
| **Concierge** | $1,500 one-time | Forensic analysis delivered in 7 days |

---

## Open-Source Resources

| Resource | What's Inside |
|:---------|:-------------|
| [**CouncilVerse**](https://github.com/Relay-Launch/councilverse) | Multi-agent debate engine, 3 npm packages, MIT |
| [**automation-templates**](https://github.com/Relay-Launch/.github/tree/main/automation-templates) | Production n8n workflows and self-host playbooks |
| [**integration-cookbook**](https://github.com/Relay-Launch/.github/tree/main/integration-cookbook) | Python API recipes for Stripe, Slack, HubSpot, Sheets |
| [**business-audit-framework**](https://github.com/Relay-Launch/.github/tree/main/business-audit-framework) | 8-area diagnostic, scoring rubric, priority matrix |
| [**kpi-dashboard-templates**](https://github.com/Relay-Launch/.github/tree/main/kpi-dashboard-templates) | KPI selection guide and dashboard specs |
| [**sop-starter-kit**](https://github.com/Relay-Launch/.github/tree/main/sop-starter-kit) | Process documentation templates and style guide |

---

## Founder

**Victor David Medina** — USMC Sergeant (E-5), Watertown MA. Building AI systems that do the work, not just talk about it.

8 years enterprise operations. Cloud/DevOps (AWS, Terraform, Cloudflare). Full-stack AI (Claude Code, multi-agent harnesses, MCP, A2A). Solo founder with AI leverage.

<p align="center">
  <a href="https://relaylaunch.com"><strong>relaylaunch.com</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://deck.relaylaunch.com"><strong>Try Relay Deck</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Relay-Launch/councilverse"><strong>CouncilVerse</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="mailto:hello@relaylaunch.com"><strong>hello@relaylaunch.com</strong></a>
</p>

<p align="center">
  <sub><strong>RelayLaunch</strong> · Veteran-Owned · Watertown, MA</sub><br>
  <sub>Every department. One AI.</sub>
</p>
