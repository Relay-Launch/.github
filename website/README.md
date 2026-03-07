# relaylaunch.com

Company website for **RelayLaunch LLC** — built with Astro 6 + Tailwind CSS 4, deployed on Cloudflare Pages.

## Stack

| Layer | Tech | Cost |
|---|---|---|
| Framework | Astro 5+ | — |
| Styling | Tailwind CSS 4 | — |
| Hosting | Cloudflare Pages | **$0/mo** |
| CI/CD | GitHub Actions | **$0/mo** |

## Pages

| Route | File | Description |
|---|---|---|
| `/` | `src/pages/index.astro` | Home — hero, stats, services, HRC teaser, founder |
| `/services` | `src/pages/services.astro` | Signal / Blueprint / Relay / Sustain with pricing |
| `/about` | `src/pages/about.astro` | Victor's background, credentials, company mission |
| `/contact` | `src/pages/contact.astro` | GitHub Issues intake, process walkthrough, FAQ |
| `/case-studies/hrc` | `src/pages/case-studies/hrc.astro` | HRC full case study ($342→$51/mo) |

## Local Dev

```bash
npm install
npm run dev       # starts at http://localhost:4321
npm run build     # output to dist/
npm run preview   # preview the built site
```

## Cloudflare Pages Setup

1. Log in to [Cloudflare Pages](https://pages.cloudflare.com)
2. **Create a project** → Connect to Git → Select `Relay-Launch/relaylaunch-website`
3. Build settings:
   - **Framework preset**: Astro
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
4. Deploy → point `relaylaunch.com` DNS to the Pages domain

## Project Structure

```
website/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   ├── Nav.astro          # Sticky nav with active state detection
│   │   └── Footer.astro       # Service + company links
│   ├── layouts/
│   │   └── Layout.astro       # Base layout: SEO, OG tags, schema.org
│   ├── pages/
│   │   ├── index.astro
│   │   ├── services.astro
│   │   ├── about.astro
│   │   ├── contact.astro
│   │   └── case-studies/
│   │       └── hrc.astro
│   └── styles/
│       └── global.css         # Tailwind 4 + design system tokens
├── astro.config.mjs
└── package.json
```
