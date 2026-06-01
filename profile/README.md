<h1 align="center">
  <img src="https://raw.githubusercontent.com/Relay-Launch/.github/main/profile/repo-card.svg" alt="RelayLaunch, Every part of your business. One AI." width="100%"/>
</h1>

<h2 align="center">We deploy AI operations systems that <em>run</em> your business,<br>not chatbots that talk about it.</h2>

<p align="center"><strong>Every part of your business. One AI.</strong></p>

<p align="center">
  <strong>Approved Operations:</strong> AI prepares the work and surfaces the decision.<br>
  <strong>You approve.</strong> Multiple models debate, you see the disagreements, then you decide.
</p>

<p align="center">
  <em>AI prepares. You approve.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Models-15_across_7_providers-D97706?style=for-the-badge&logoColor=white" alt="15 models across 7 providers"/>
  <img src="https://img.shields.io/badge/Engine-Cloudflare_Workers-0D9488?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Cloudflare Workers engine"/>
  <img src="https://img.shields.io/badge/Autonomy-Owner--Approved-F59E0B?style=for-the-badge&logoColor=white" alt="Owner-approved autonomy"/>
  <img src="https://img.shields.io/badge/CouncilVerse-Open_Source-10B981?style=for-the-badge&logo=npm&logoColor=white" alt="CouncilVerse open source"/>
  <img src="https://img.shields.io/badge/Veteran--Owned-USMC-44403C?style=for-the-badge&logoColor=white" alt="Veteran-owned"/>
</p>

<p align="center">
  <a href="https://relaylaunch.com"><img src="https://img.shields.io/badge/relaylaunch.com-D97706?style=flat-square&logo=googlechrome&logoColor=white" alt="Website"></a>&nbsp;
  <a href="https://deck.relaylaunch.com"><img src="https://img.shields.io/badge/Relay%E2%96%B8Deck-0C0A09?style=flat-square&logo=vercel&logoColor=white" alt="Relay Deck"></a>&nbsp;
  <a href="https://github.com/Relay-Launch/councilverse"><img src="https://img.shields.io/badge/CouncilVerse-Open_Source-10B981?style=flat-square&logo=github&logoColor=white" alt="CouncilVerse"></a>&nbsp;
  <a href="https://www.npmjs.com/org/relaylaunch"><img src="https://img.shields.io/badge/npm-@relaylaunch-CB3837?style=flat-square&logo=npm&logoColor=white" alt="npm org"></a>&nbsp;
  <a href="mailto:hello@relaylaunch.com"><img src="https://img.shields.io/badge/hello@relaylaunch.com-44403C?style=flat-square&logo=maildotru&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Relay-Launch/.github/main/profile/approval-loop.svg" alt="Animated RelayLaunch owner-approved AI operations loop" width="100%"/>
</p>

---

## Why RelayLaunch Exists

Most "AI for business" is a chat window. You still do the work; the AI just talks about it.

RelayLaunch is the opposite. We deploy a system that **does the operational work in the background** (client follow-up, win-back, slot rescue, reviews, morning briefs) and brings you the finished decision. You approve or skip. That's the whole interaction.

> **The website is the bonus. The deployed AI operations system is the product.**

---

## The Product Stack

| # | Product | What It Does | For Whom |
|:-:|:--------|:-------------|:---------|
| 1 | **Relay Pulse** | Deployed AI ops engine: automated client follow-up, win-back, slot rescue, wellness scoring, review lift, voice AI morning briefs, AI cost metering, timezone-aware scheduling. Runs on Cloudflare Workers. | Service businesses, professional services, startups |
| 2 | **Relay Deck** | SaaS command center: Recovery Board, Action Brief, multi-model council review, eval pipeline, self-healing monitors, state persistence, circuit breakers. | Owners and operators |
| 3 | **CouncilVerse** | Open-source multi-agent council engine: reusable council modes, quality-weighted voting, structured debate. Public on npm. | Developers building AI decision systems |

---

## What Makes This an Ambient Enterprise

The system works in the background, without being asked, and never acts on a money decision without owner approval.

| Capability | What It Does |
|:-----------|:------------|
| **Morning Brief** | Pulse analyzes overnight data, generates a voice briefing, and emails a digest before you open your phone |
| **Owner-Approved Autonomy** | A five-level progressive-autonomy model with approval gates at every level. The owner stays in control of every action that touches money |
| **Multi-Model Council** | Every analysis runs through models from different providers; agreement earns confidence, disagreement surfaces risk |
| **Dissent Surfaced** | When models disagree, you see both sides. No hidden consensus, no buried dissent |
| **Eval Pipeline** | Golden datasets, regression detection, grounding and faithfulness checks, wired into CI so the system grades its own work |
| **Self-Healing Monitor** | Detects drift in specialist accuracy, applies corrections, and logs learning events |
| **Circuit Breakers** | If a model fails or gets expensive, the system degrades gracefully instead of crashing |
| **Smart Model Router** | Routes each query to the cheapest capable model: a frontier model for hard problems, a fast model for routine ones |

---

## Multi-Model Council Architecture

We don't trust a single model. Every analysis runs through a **heterogeneous council** of 15 cloud models across 7 independent providers (Anthropic, DeepSeek, xAI, Zhipu AI, MiniMax, Perplexity, Google), with optional local Ollama inference, routed through a single LiteLLM gateway. Models trained on different corpora argue from different priors, and the verdict is scored on evidence quality, not headcount.

```
                  INPUT  ·  Business decision / analysis request
                                     │
            ┌────────────────────────┼────────────────────────┐
            │                        │                         │
      ┌─────▼──────┐          ┌──────▼──────┐          ┌───────▼──────┐
      │  Anthropic │          │   DeepSeek  │          │   Zhipu AI   │
      │  Opus      │          │   V4-Flash  │          │   GLM-5.1    │
      │  Sonnet    │          │   V4-Pro    │          │   + MiniMax  │
      │  Haiku     │          │             │          │     M2.7     │
      └─────┬──────┘          └──────┬──────┘          └───────┬──────┘
            │                        │                         │
            │              ┌─────────▼─────────┐               │
            │              │  xAI Grok 4.x     │               │
            │              │  Perplexity Sonar │               │
            │              │  Google Gemini    │               │
            │              │  Ollama (local)   │               │
            │              └─────────┬─────────┘               │
            └────────────────────────┼────────────────────────┘
                                     │
                       ┌─────────────▼─────────────┐
                       │   LiteLLM GATEWAY ROUTER   │
                       │   cheapest capable model   │
                       └─────────────┬─────────────┘
                                     │
                       ┌─────────────▼─────────────┐
                       │      COUNCIL DEBATE        │
                       │   · Position papers        │
                       │   · Cross-examination      │
                       │   · Evidence scoring       │
                       │   · Dissent capture        │
                       └─────────────┬─────────────┘
                                     │
                       ┌─────────────▼─────────────┐
                       │          VERDICT           │
                       │   · Confidence score       │
                       │   · Majority opinion       │
                       │   · Dissenting views       │
                       │   · Reasoning traces       │
                       │   · Owner approval gate    │
                       └────────────────────────────┘
```

**When models from different training corpora agree, confidence is justified. When they disagree, the dissent surfaces a risk a single model would have buried.**

---

## The Engine Behind the Product

RelayLaunch isn't assembled by hand. It's built and operated by a coordinated AI engineering harness, and that harness *is* the company's edge.

### Four AI agents, one synchronized sprint

**Claude Code · GitHub Copilot · Gemini CLI · Codex** run in synchronized sprints against shared handoff docs, with a trust-but-verify step where each agent's strongest output is re-checked before it ships. Parallel build, sequential ship, one source of truth.

### The infrastructure spine

A self-hosted Docker Compose stack of ~27 containers gives the harness a full local operations layer:

| Layer | Stack |
|:------|:------|
| **Model gateway** | LiteLLM routing 15 cloud models across 7 providers, plus local Ollama on GPU |
| **Vectors / RAG** | Qdrant + pgvector for retrieval and precedent search |
| **Observability** | Langfuse (LLM traces) + Prometheus + Grafana + Loki |
| **Edge proxy** | Traefik reverse proxy across services |
| **Automation** | n8n workflow engine |
| **Eval harness** | Golden datasets + regression detection + grounding/faithfulness checks, wired into CI |

### Deployment fabric

| Plane | Stack |
|:------|:------|
| **Execution engine** | Cloudflare Workers, multi-tenant: per-tenant D1 / KV / R2 / Queues, 40+ migrations |
| **Data + auth** | Supabase Postgres with Row-Level Security |
| **Governance** | AI incident-response playbook + escalation matrix; IBM 6-pillar + EU AI Act mapping |

---

## SaaS Pricing

| Tier | Price | Seats | What You Get |
|:-----|:------|:-----:|:-------------|
| **Free Ops Scan** | $0 | n/a | Instant AI operations audit for your business |
| **Pilot (Outcome)** | $0 + $20 / recovered booking (cap $149/mo) | 1 | 30-day outcome-based pilot. You pay for results |
| **Starter** | $149/mo | 1 | Top 3 daily actions, lapsed-client recovery, basic slot filling |
| **Pro** | $299/mo | 1 | Full platform access, all integrations |
| **Team** | $999/mo | 5 | Multi-seat, month-to-month |
| **Enterprise** | $3,000/mo | Unlimited | SSO, audit trails, dedicated support |
| **Concierge** | $1,500 one-time | n/a | Forensic operations analysis, delivered in 7 days |

<p align="center">
  <a href="https://relaylaunch.com"><strong>Start with a Free Ops Scan &rarr;</strong></a>
</p>

---

## CouncilVerse, Open Source

Multi-agent debate infrastructure for developers. Published on [npm under `@relaylaunch`](https://www.npmjs.com/org/relaylaunch).

```bash
npx create-councilverse my-council
```

<table>
<tr>
<td width="33%" valign="top">

### [`councilverse-formations`](https://www.npmjs.com/package/@relaylaunch/councilverse-formations)
Structured council modes: Strategy Room (OODA), Tribunal, Risk Council, Due Diligence, and more. Capability packs, not templates.

</td>
<td width="33%" valign="top">

### [`councilverse-voting`](https://www.npmjs.com/package/@relaylaunch/councilverse-voting)
Quality-weighted voting (KEEP / REFUSE / ABSTAIN). Evidence over headcount, so the loudest model doesn't win.

</td>
<td width="33%" valign="top">

### [`create-councilverse`](https://www.npmjs.com/package/create-councilverse)
A working council scaffold in 60 seconds. TypeScript configured. Drop in an API key and run.

</td>
</tr>
</table>

<p align="center">
  <a href="https://github.com/Relay-Launch/councilverse"><img src="https://img.shields.io/github/stars/Relay-Launch/councilverse?style=social" alt="GitHub stars"></a>&nbsp;
  <a href="https://www.npmjs.com/package/@relaylaunch/councilverse-formations"><img src="https://img.shields.io/npm/dt/@relaylaunch/councilverse-formations?label=npm%20downloads&color=D97706" alt="npm downloads"></a>
</p>

---

<details>
<summary><strong>Platform capabilities (click to expand)</strong></summary>
<br>

| Feature | Description |
|:--------|:------------|
| **Multi-Model Councils** | 15 models from 7 providers debate each analysis |
| **Business Rooms** | Marketing, Operations, Client Retention, Finance, HR, Legal, Strategy, Content, Sales, Support |
| **Council Modes** | Strategy Room (OODA), Tribunal, Risk Council, Due Diligence, Round Robin, Adversarial, and more |
| **Morning Brief** | AI-generated daily digest with voice narration, email delivery, and an approval workflow |
| **Owner-Approved Autonomy** | Five-level progressive-autonomy model with approval gates on every money-touching action |
| **Self-Healing Monitor** | Detects specialist drift, corrects, and logs learning events |
| **Eval Pipeline** | Golden datasets, regression detection, grounding/faithfulness checks, wired into CI |
| **Circuit Breakers** | Graceful degradation when models fail or costs spike |
| **Precedent Search** | Semantic search over past verdicts (Qdrant + pgvector) |
| **Smart Model Router** | Routes to the cheapest capable model via the LiteLLM gateway |
| **Feedback Flywheel** | Accept / Edit / Reject tunes the system to your preferences |
| **A2A + MCP Protocols** | Agent-to-Agent and Model Context Protocol bridges |
| **BYOK** | Bring your own API keys, control model spend |
| **Governance Mapping** | IBM 6-pillar + EU AI Act mapping, incident-response playbook, escalation matrix |

</details>

<details>
<summary><strong>Technical architecture (click to expand)</strong></summary>
<br>

```
Frontend        Next.js 16 + React 19 + Tailwind CSS 4 + Vercel
Backend         Supabase (Postgres + Auth + Row-Level Security + pgvector)
AI routing      LiteLLM gateway · 15 cloud models · 7 providers · + local Ollama
Ops engine      Cloudflare Workers + Hono · per-tenant D1 / KV / Queues / R2 · 40+ migrations
Vectors / RAG   Qdrant + pgvector
Eval harness    Golden datasets + regression detection + grounding/faithfulness · CI-wired
Observability   Langfuse traces + Prometheus + Grafana + Loki
Automation      n8n
Website         Astro 6 + Tailwind 4.2 + Cloudflare Pages
Infra spine     Docker Compose · ~27 containers (Traefik, LiteLLM, Langfuse, Qdrant, Ollama GPU, n8n …)
Build harness   Claude Code + GitHub Copilot + Gemini CLI + Codex, synchronized w/ trust-but-verify
```

</details>

---

## Open-Source Resources

| Resource | What's Inside |
|:---------|:-------------|
| [**CouncilVerse**](https://github.com/Relay-Launch/councilverse) | Multi-agent debate engine, npm packages, MIT licensed |
| [**automation-templates**](https://github.com/Relay-Launch/.github/tree/main/automation-templates) | Production n8n workflows and self-host playbooks |
| [**integration-cookbook**](https://github.com/Relay-Launch/.github/tree/main/integration-cookbook) | API recipes for Stripe, Slack, HubSpot, Sheets |
| [**business-audit-framework**](https://github.com/Relay-Launch/.github/tree/main/business-audit-framework) | 8-area diagnostic, scoring rubric, priority matrix |
| [**kpi-dashboard-templates**](https://github.com/Relay-Launch/.github/tree/main/kpi-dashboard-templates) | KPI selection guide and dashboard specs |
| [**sop-starter-kit**](https://github.com/Relay-Launch/.github/tree/main/sop-starter-kit) | Process documentation templates and style guide |

---

## Founder

**Victor David Medina**, veteran founder, Watertown, MA.

Eight years of enterprise operations. Cloud and platform infrastructure (Cloudflare Workers, AWS, Terraform). Full-stack AI systems: multi-model councils, owner-approved autonomy, self-healing monitors, CI-wired evals. Builds with a four-agent engineering harness (Claude Code, GitHub Copilot, Gemini CLI, Codex) running synchronized sprints with a trust-but-verify gate.

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
