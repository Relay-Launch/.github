<h1 align="center">
  <img src="https://raw.githubusercontent.com/Relay-Launch/.github/main/profile/repo-card.svg" alt="RelayLaunch" width="100%"/>
</h1>

<h2 align="center">We deploy AI operations systems that run your business &mdash;<br>not chatbots that talk about it.</h2>

<p align="center">
  <strong>Approved Operations:</strong> AI prepares the work and surfaces the decision &mdash; you approve. Multiple models debate; you see the disagreements.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Models-15_across_7_providers-D97706?style=for-the-badge&logo=brain&logoColor=white" alt="15 Models"/>
  <img src="https://img.shields.io/badge/Rooms-10_Business_Domains-0D9488?style=for-the-badge&logo=building&logoColor=white" alt="10 Rooms"/>
  <img src="https://img.shields.io/badge/Council_Modes-17-F59E0B?style=for-the-badge&logo=robot&logoColor=white" alt="17 Council Modes"/>
  <img src="https://img.shields.io/badge/Tested-CI_suites_across_repos-10B981?style=for-the-badge&logo=check-circle&logoColor=white" alt="CI test suites"/>
  <img src="https://img.shields.io/badge/Veteran--Owned-USMC-09090B?style=for-the-badge&logo=shield&logoColor=white" alt="Veteran-Owned"/>
</p>

<p align="center">
  <a href="https://relaylaunch.com"><img src="https://img.shields.io/badge/relaylaunch.com-D97706?style=flat-square&logo=globe&logoColor=white" alt="Website"></a>&nbsp;&nbsp;
  <a href="https://deck.relaylaunch.com"><img src="https://img.shields.io/badge/Relay%E2%96%B8Deck-09090B?style=flat-square&logo=vercel&logoColor=white" alt="Relay Deck"></a>&nbsp;&nbsp;
  <a href="https://github.com/Relay-Launch/councilverse"><img src="https://img.shields.io/badge/CouncilVerse-Open_Source-10B981?style=flat-square&logo=github&logoColor=white" alt="CouncilVerse"></a>&nbsp;&nbsp;
  <a href="mailto:hello@relaylaunch.com"><img src="https://img.shields.io/badge/hello%40relaylaunch.com-3F3F46?style=flat-square&logo=mail.ru&logoColor=white" alt="Email"></a>
</p>

---

## The Product Stack

We don't sell websites. We deploy **complete AI operations systems** for founders, startups, and growing businesses.

| # | Product | What It Does | For Whom |
|:-:|:--------|:-------------|:---------|
| 1 | **Relay Pulse** | Deployed AI ops engine -- automated client follow-up, wellness scoring, win-back campaigns, voice AI morning briefs, AI cost metering, timezone-aware scheduling | Service businesses, professional services, startups |
| 2 | **Relay Deck** | SaaS command center -- 10 Rooms, 17 Council Modes, eval pipeline, self-healing monitors, Ghost Teams, circuit breakers, state persistence | Business owners and operators |
| 3 | **CouncilVerse** | Open-source multi-agent debate engine -- 17 council modes, three-valued voting, quality-weighted scoring | Developers building AI decision systems |

> **The website is the bonus. The AI system is the product.**

---

## What Makes This an Ambient Enterprise

The system works in the background, without being asked:

| Capability | What It Does |
|:-----------|:------------|
| **Morning Brief** | Pulse analyzes overnight data, generates a voice briefing, emails a digest before you check your phone |
| **Ghost Teams** | Autonomous background agents quietly evaluate your business decisions and surface risks you missed |
| **Self-Healing Monitor** | Detects drift in specialist accuracy, auto-applies corrections, logs learning events |
| **Circuit Breakers** | If a model fails or gets expensive, the system degrades gracefully -- never crashes |
| **Dissent Digest** | When AI models disagree, you see both sides. No hidden consensus, no buried dissent |
| **Eval Pipeline** | PGR scoring, golden datasets, regression detection -- the system grades its own work |
| **Cryptographic Signing** | Every verdict is Ed25519-signed with full provenance chain. Tamper-proof audit trail |
| **Smart Model Router** | Routes queries to the cheapest capable model. Claude Opus for hard problems, DeepSeek for routine ones |

---

## Multi-Model Council Architecture

We don't trust a single model. Every analysis runs through **heterogeneous council debates** -- 15 models from 7 independent providers (Anthropic, DeepSeek, xAI, Zhipu AI, MiniMax, Perplexity, Google) plus local Ollama, arguing from different training data, scored on evidence quality.

```
                           INPUT: Business Decision / Analysis Request
                                          |
                    +---------------------+---------------------+
                    |                     |                     |
              +-----v-----+        +-----v-----+        +-----v-----+
              |  Anthropic |        |  DeepSeek  |        |  Zhipu AI  |
              |            |        |            |        |  + MiniMax |
              | +--------+ |        | +--------+ |        | +--------+ |
              | | Opus   | |        | |V4-Flash| |        | | GLM-5.1| |
              | +--------+ |        | +--------+ |        | +--------+ |
              | | Sonnet | |        | +--------+ |        | +--------+ |
              | +--------+ |        | |V4-Pro  | |        | | M2.7   | |
              | | Haiku  | |        | +--------+ |        | +--------+ |
              | +--------+ |        +-----+------+        +-----+------+
              +-----+------+              |                      |
                    |            +--------+--------+             |
                    |            |  Perplexity +   |             |
                    |            |  Ollama (Local) |             |
                    |            +--------+--------+             |
                    +---------------------+---------------------+
                                          |
                               +----------v----------+
                               |   FREE-MAD ENGINE    |
                               |                      |
                               |  - Position Papers   |
                               |  - Cross-Exam        |
                               |  - Evidence Scoring  |
                               |  - Dissent Capture   |
                               +----------+----------+
                                          |
                               +----------v----------+
                               |      VERDICT         |
                               |                      |
                               |  Confidence Score    |
                               |  Majority Opinion    |
                               |  Dissenting Views    |
                               |  Reasoning Traces    |
                               |  Ed25519 Signature   |
                               |  Full Audit Trail    |
                               +---------------------+
```

**When models from different training corpora agree, confidence is justified. When they disagree, the dissent surfaces risks a single model would miss.**

---

## SaaS Pricing

| Tier | Price | Seats | What You Get |
|:-----|:------|:-----:|:-------------|
| **Free Ops Scan** | $0 | -- | Instant AI operations audit for your business |
| **Pilot (Outcome)** | $0 + $20 / recovered booking (cap $149/mo) | 1 | 30-day outcome-based pilot |
| **Starter** | $149/mo | 1 | Top 3 daily actions, lapsed-client recovery, basic slot filling |
| **Pro** | $299/mo | 1 | Full platform access, 48-hour trial |
| **Team** | $999/mo | 5 | Multi-seat, priority support, month-to-month |
| **Enterprise** | $3,000/mo | Unlimited | SSO, audit trails, dedicated support |
| **Concierge** | $1,500 one-time | -- | Forensic analysis delivered in 7 days |

<p align="center">
  <a href="https://relaylaunch.com"><strong>Start with a Free Ops Scan &rarr;</strong></a>
</p>

---

## CouncilVerse -- Open Source

Multi-agent debate infrastructure for developers. MIT Licensed.

```bash
npx create-councilverse my-council
```

<table>
<tr>
<td width="33%">

### [`councilverse-formations`](https://www.npmjs.com/package/@relaylaunch/councilverse-formations)
17 structured council modes: Strategy Room (OODA), Tribunal, Risk Council (Monte Carlo), Due Diligence (M&A).

</td>
<td width="33%">

### [`councilverse-voting`](https://www.npmjs.com/package/@relaylaunch/councilverse-voting)
Three-valued voting (KEEP / REFUSE / ABSTAIN) with quality-weighted scoring. Evidence over headcount.

</td>
<td width="33%">

### [`create-councilverse`](https://www.npmjs.com/package/create-councilverse)
Working council scaffold in 60 seconds. TypeScript configured. Drop in an API key and run.

</td>
</tr>
</table>

<p align="center">
  <a href="https://github.com/Relay-Launch/councilverse"><img src="https://img.shields.io/github/stars/Relay-Launch/councilverse?style=social" alt="GitHub stars"></a>&nbsp;&nbsp;
  <a href="https://www.npmjs.com/package/@relaylaunch/councilverse-formations"><img src="https://img.shields.io/npm/dt/@relaylaunch/councilverse-formations?label=npm%20downloads&color=D97706" alt="npm downloads"></a>
</p>

---

<details>
<summary><strong>Platform Capabilities (click to expand)</strong></summary>
<br>

| Feature | Description |
|:--------|:------------|
| **Multi-Model Councils** | 15 models from 7 providers debate each analysis |
| **10 Business Rooms** | Marketing, Operations, Client Retention, Finance, HR, Legal, Strategy, Content, Sales, Support |
| **17 Council Modes** | Strategy Room (OODA), Tribunal, Risk Council, Due Diligence, Round Robin, Adversarial, and more |
| **Morning Brief** | AI-generated daily digest with voice narration, email delivery, and approval workflow |
| **Ghost Teams** | Autonomous background agents that quietly evaluate decisions and surface risks |
| **Self-Healing Monitor** | Detects specialist drift, auto-corrects, logs learning events |
| **Eval Pipeline** | PGR scoring, golden datasets, regression detection -- the system grades itself |
| **Circuit Breakers** | Graceful degradation when models fail or costs spike |
| **Precedent Search** | Semantic search over past verdicts (pgvector) |
| **Ed25519 Signed Verdicts** | Cryptographic provenance for every decision |
| **Smart Model Router** | Routes to cheapest capable model (80% cost reduction) |
| **Feedback Flywheel** | Accept/Edit/Reject trains the system on your preferences |
| **Deliverable Engine** | QoE reports, DD memos, risk packages as PDF |
| **A2A + MCP Protocols** | Google Agent-to-Agent and Model Context Protocol bridges |
| **BYOK** | Bring your own API keys, control model spend |
| **EU AI Act Ready** | JSON-LD transparency manifests, bias detection, constitutional checks |

</details>

<details>
<summary><strong>Technical Architecture (click to expand)</strong></summary>
<br>

```
Frontend       Next.js 16 + React 19 + Tailwind CSS 4 + Vercel
Backend        Supabase (Postgres + Auth + RLS + pgvector)
AI Routing     LiteLLM gateway + 15 models + 7 providers
Ops Engine     Cloudflare Workers + Hono + D1/KV/Queues/R2
Voice AI       Kokoro TTS + R2 storage + HMAC presigned URLs
Telemetry      Langfuse + structured reasoning traces
PDF Engine     @react-pdf/renderer + 6 report templates
Protocols      A2A JSON-RPC + MCP + Ed25519 signing
Website        Astro 6 + Tailwind 4.2 + Cloudflare Pages
Infra          Docker Compose (27 containers) + GitHub Actions CI
Testing        CI test suites across 4 repos (Vitest + Wrangler)
```

</details>

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

**Victor David Medina** -- veteran founder, Watertown, MA.

8 years enterprise operations. Cloud infrastructure (AWS, Terraform, Cloudflare Workers). Full-stack AI systems (multi-model councils, autonomous agents, self-healing monitors). Building with Claude Code, GitHub Copilot, Gemini CLI, and Codex -- four AI tools working as a coordinated engineering team.

Building AI systems that do the work, not just talk about it.

---

<p align="center">
  <a href="https://relaylaunch.com"><strong>relaylaunch.com</strong></a>&nbsp;&nbsp;&middot;&nbsp;&nbsp;
  <a href="https://deck.relaylaunch.com"><strong>Try Relay Deck</strong></a>&nbsp;&nbsp;&middot;&nbsp;&nbsp;
  <a href="https://github.com/Relay-Launch/councilverse"><strong>CouncilVerse</strong></a>&nbsp;&nbsp;&middot;&nbsp;&nbsp;
  <a href="mailto:hello@relaylaunch.com"><strong>hello@relaylaunch.com</strong></a>
</p>

<p align="center">
  <sub><strong>RelayLaunch LLC</strong> &middot; Veteran-Owned &middot; Watertown, MA</sub><br>
  <sub><em>Every part of your business. One AI.</em></sub>
</p>
