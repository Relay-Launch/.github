<h1 align="center">
  <img src="https://raw.githubusercontent.com/Relay-Launch/.github/main/profile/repo-card.svg" alt="RelayLaunch" width="100%"/>
</h1>

<h2 align="center">Get found. Get booked. Keep them.</h2>

<p align="center">
  RelayLaunch helps local service businesses become readable to search engines and AI assistants,<br>
  easier to book, and easier to keep. Every action is owner-approved.
</p>

<p align="center"><em>AI prepares. You approve.</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/Free_scan-31_checks-D97706?style=for-the-badge&logoColor=white" alt="Free scan: 31 checks"/>
  <img src="https://img.shields.io/badge/Engine-Cloudflare_Workers-0F766E?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Cloudflare Workers engine"/>
  <img src="https://img.shields.io/badge/Autonomy-Owner--Approved-F59E0B?style=for-the-badge&logoColor=white" alt="Owner-approved autonomy"/>
  <img src="https://img.shields.io/badge/Veteran--Owned-44403C?style=for-the-badge&logoColor=white" alt="Veteran-owned"/>
</p>

<p align="center">
  <a href="https://relaylaunch.com"><img src="https://img.shields.io/badge/relaylaunch.com-D97706?style=flat-square&logo=googlechrome&logoColor=white" alt="Website"></a>&nbsp;
  <a href="https://relaylaunch.com/scan/ai-visibility/"><img src="https://img.shields.io/badge/Run_the_free_scan-0C0A09?style=flat-square" alt="Run the free scan"></a>&nbsp;
  <a href="https://github.com/Relay-Launch/councilverse"><img src="https://img.shields.io/badge/CouncilVerse-Open_Source-0F766E?style=flat-square&logo=github&logoColor=white" alt="CouncilVerse"></a>&nbsp;
  <a href="https://www.npmjs.com/org/relaylaunch"><img src="https://img.shields.io/badge/npm-@relaylaunch-CB3837?style=flat-square&logo=npm&logoColor=white" alt="npm org"></a>&nbsp;
  <a href="mailto:hello@relaylaunch.com"><img src="https://img.shields.io/badge/hello@relaylaunch.com-44403C?style=flat-square&logo=maildotru&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Relay-Launch/.github/main/profile/approval-loop.svg" alt="Animated RelayLaunch owner-approved loop" width="100%"/>
</p>

---

## What we do

Most owners do not know whether an AI assistant or a search engine can read who they are, where they are, and when they are open. We measure it, fix it on the site they already have, and keep it from drifting back.

1. **See the gap.** The free AI-Readiness scan answers 31 yes-or-no questions about your public site. Your score shows first; one optional email unlocks the itemized fix list.
2. **Fix what it found.** The Get Found Fix Pass works through the 14 get-found checks with you watching. Each one flips, or you are told plainly why it cannot on your platform.
3. **Keep it from drifting.** Site Care re-runs the 14 checks every month and handles small edits, hosting and updates.
4. **Run the loop.** Starter gives you a short Morning Brief whenever something needs an owner decision.

[See all 31 checks &rarr;](https://relaylaunch.com/scan/checks/)

---

## Pricing

Flat by design: no required setup fee, no usage meter, no annual lock, cancel anytime.

| Rung | Price | What you get |
|:-----|:------|:-------------|
| **AI-Readiness Score** | $0 | 31 checks on your public site. Score first, email optional |
| **Get Found Fix Pass** | $350 one-time | The 14 get-found checks fixed on your existing site, with you watching. Nothing renews |
| **Site Care** | $149/mo | Upkeep for a site we built or fixed: hosting, SSL, uptime watch, up to 4 small edits a month, the 14 checks re-run monthly |
| **Starter** | $199/mo | Owner-approved loop: get found, get booked, review lift, and a portable record of every approved action |
| **Team** | $999/mo | 5 seats, month-to-month |
| **Enterprise** | $3,000/mo | Unlimited seats, SSO, audit trails |
| **Full Onboarding** | $5,995 one-time | Optional founder-led launch: a template-led Cloudflare website (up to 5 core pages), schema, analytics, and standard Relay workflows |

**Proof status:** no verified client outcomes are published yet. Samples stay labeled Sample, and we do not promise rankings, placement, or traffic.

<p align="center">
  <a href="https://relaylaunch.com/scan/ai-visibility/"><strong>Run the free scan &rarr;</strong></a>
</p>

---

## The product

| Product | What it does |
|:--------|:-------------|
| **Relay Deck** | The owner's command center: Morning Brief, approvals, and the record of every approved action |
| **Relay Pulse** | The operations engine on Cloudflare Workers that prepares the work behind the brief |
| **CouncilVerse** | Open-source multi-agent review engine we use to check our own work (below) |

---

## How it's built

RelayLaunch is built and operated by a small fleet of AI seats, each with one job, and a founder who approves what ships.

| Seat | Job |
|:-----|:----|
| **Claude** | Builds code, keeps the rules, records what was measured |
| **Gemini** | Research, design specs, and visual checks of what ships |
| **Hermes** | Runs scheduled work on our own hardware: health probes, research fetches, nightly checks |
| **Odysseus** | A workspace on local models for planning and drafts |

Underneath: a self-hosted stack with a LiteLLM model gateway over local Ollama models and cloud providers, Qdrant for retrieval, Langfuse for traces, n8n for automation, and Prometheus/Grafana for monitoring. The website runs on Cloudflare Workers; Relay Deck runs on Railway with Supabase.

---

## CouncilVerse, open source

Multi-agent review infrastructure for developers. Published on [npm under `@relaylaunch`](https://www.npmjs.com/org/relaylaunch).

```bash
npx create-councilverse my-council
```

<table>
<tr>
<td width="33%" valign="top">

### [`councilverse-formations`](https://www.npmjs.com/package/@relaylaunch/councilverse-formations)
Structured council modes: Strategy Room (OODA), Tribunal, Risk Council, Due Diligence, and more.

</td>
<td width="33%" valign="top">

### [`councilverse-voting`](https://www.npmjs.com/package/@relaylaunch/councilverse-voting)
Quality-weighted voting (KEEP / REFUSE / ABSTAIN). Evidence over headcount.

</td>
<td width="33%" valign="top">

### [`create-councilverse`](https://www.npmjs.com/package/create-councilverse)
A working council scaffold. TypeScript configured. Drop in an API key and run.

</td>
</tr>
</table>

---

## Open-source resources

| Resource | What's inside |
|:---------|:-------------|
| [**CouncilVerse**](https://github.com/Relay-Launch/councilverse) | Multi-agent review engine, npm packages, MIT licensed |
| [**automation-templates**](https://github.com/Relay-Launch/.github/tree/main/automation-templates) | n8n workflows and self-host playbooks |
| [**integration-cookbook**](https://github.com/Relay-Launch/.github/tree/main/integration-cookbook) | API recipes for Stripe, Slack, HubSpot, Sheets |
| [**business-audit-framework**](https://github.com/Relay-Launch/.github/tree/main/business-audit-framework) | 8-area diagnostic, scoring rubric, priority matrix |
| [**kpi-dashboard-templates**](https://github.com/Relay-Launch/.github/tree/main/kpi-dashboard-templates) | KPI selection guide and dashboard specs |
| [**sop-starter-kit**](https://github.com/Relay-Launch/.github/tree/main/sop-starter-kit) | Process documentation templates and style guide |

---

## Founder

**Victor David Medina**, veteran founder, Watertown, MA. Builds RelayLaunch solo with the AI fleet above, on the rule that AI prepares the work and the owner approves it.

---

<p align="center">
  <a href="https://relaylaunch.com"><strong>relaylaunch.com</strong></a>&nbsp;&nbsp;&middot;&nbsp;&nbsp;
  <a href="https://relaylaunch.com/scan/ai-visibility/"><strong>Free scan</strong></a>&nbsp;&nbsp;&middot;&nbsp;&nbsp;
  <a href="https://github.com/Relay-Launch/councilverse"><strong>CouncilVerse</strong></a>&nbsp;&nbsp;&middot;&nbsp;&nbsp;
  <a href="mailto:hello@relaylaunch.com"><strong>hello@relaylaunch.com</strong></a>
</p>

<p align="center">
  <sub><strong>RelayLaunch LLC</strong> &middot; Veteran-Owned &middot; Watertown, MA</sub>
</p>
