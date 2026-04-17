# Agency Tools Ecosystem
**Agency:** CEO-Work
**Philosophy:** Open-source first. Self-host where possible. Pay only when there's no viable open-source alternative.
**Last Updated:** 2026-04-16

---

## Reading This Document

Each tool entry follows this format:

```
Tool Name — what it does
├── Type: Open-Source / Proprietary / Freemium
├── Cost: Free / Self-host / Paid
├── Host: Self-hosted / Cloud
└── Why: Why this specific tool for this specific job
```

Legend:
- 🟢 Open-source + free / self-hostable
- 🟡 Freemium (free tier sufficient for early stage)
- 🔴 Proprietary (no good open-source alternative exists)
- ⭐ Priority — set this up first

---

## Layer 0 — Infrastructure (The Foundation Everything Runs On)

Before any tool works, you need the infrastructure layer.

### VPS / Server Hosting

```
Hetzner Cloud ⭐
├── Type: Proprietary (infrastructure)
├── Cost: ~€5–20/month (CAX11: 2 vCPU ARM, 4GB RAM = €4.15/mo)
├── Host: Cloud (their data centers, EU-based)
└── Why: Cheapest reliable VPS in Europe. Most self-hosted tools run on one
         Hetzner box. German infrastructure = GDPR-safe. Way cheaper than AWS/DO.

Alternative: OVHcloud (French, similar pricing), Contabo (cheaper, less reliable)
```

### Self-Hosting Platform

```
Coolify 🟢⭐
├── Type: Open-source
├── Cost: Free (self-hosted on your Hetzner VPS)
├── Host: Self-hosted
└── Why: Open-source Heroku/Railway/Vercel alternative. One dashboard to deploy
         ALL your self-hosted apps (n8n, Plane, Supabase, etc.) with one click.
         Handles SSL, domains, deployments, databases automatically.
         Replaces needing to manually configure Nginx/Docker for each service.

Repo: github.com/coollabsio/coolify
```

### Domain & DNS

```
Cloudflare 🟡
├── Type: Proprietary (free tier)
├── Cost: Free for DNS + CDN + DDoS protection
├── Host: Cloud
└── Why: Best DNS + CDN for free. Protects all your domains and speeds up
         all client sites. The free tier covers everything you need for years.
```

### SSL Certificates

```
Let's Encrypt 🟢
├── Type: Open-source
├── Cost: Free
├── Host: Handled by Coolify automatically
└── Why: Free SSL for all domains. Coolify handles auto-renewal.
         Zero manual work needed.
```

### Email (Transactional — for system alerts, notifications)

```
Resend 🟡
├── Type: Proprietary (free tier)
├── Cost: Free up to 3,000 emails/month
├── Host: Cloud
└── Why: Best deliverability for transactional emails (system alerts, client
         notifications, invoice delivery). Simple API, n8n integration.

Alternative open-source: Postal (self-hosted), but complex to maintain
```

### Email (Business — your @youragency.com inbox)

```
Proton Mail 🟡
├── Type: Freemium (privacy-focused, partial open-source)
├── Cost: Free (1 custom domain on paid plan: €4/month)
├── Host: Cloud (Swiss servers)
└── Why: Privacy-first, end-to-end encrypted. GDPR-compliant.
         Better than Google Workspace for a privacy-conscious agency.

Alternative: Migadu (€4/month, unlimited domains/users, excellent for agencies)
```

---

## Layer 1 — CEO & Leadership Tools

### OKR & Strategy Tracking

```
AppFlowy 🟢⭐
├── Type: Open-source (Notion alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Your command center. OKRs, strategic docs, meeting notes, knowledge base.
         Open-source Notion — same blocks/database concept, fully self-owned.
         Everything that would go in Notion lives here.

Repo: github.com/AppFlowy-IO/AppFlowy
```

### CEO Dashboard / KPI Tracking

```
Metabase 🟢
├── Type: Open-source
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Connect to your Supabase/PostgreSQL database and build visual
         dashboards. Agency KPIs (MRR, active clients, deliverables, margins)
         all in one place. SQL-powered but has a visual query builder.

Repo: github.com/metabase/metabase
```

### Calendar & Scheduling (for client calls, BD meetings)

```
Cal.com 🟢⭐
├── Type: Open-source (Calendly alternative)
├── Cost: Free (self-hosted or cloud free tier)
├── Host: Self-hosted or cal.com cloud
└── Why: Share your calendar link with prospects. They book directly.
         No back-and-forth email chains. Integrates with Google Calendar.
         Open-source Calendly — exactly the same UX.

Repo: github.com/calcom/cal.com
```

---

## Layer 2 — Revenue Engine Tools

### CRM (Sales Pipeline + Client Relationships)

```
Twenty 🟢⭐
├── Type: Open-source (modern CRM)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Best open-source CRM right now. Clean UI, modern design, built on
         top of a proper data model. Manages prospects, clients, deals,
         contacts. Think Salesforce/HubSpot but open-source and beautiful.
         Integrates with email to auto-log client conversations.

Repo: github.com/twentyhq/twenty
Alternative: Formbricks for lead capture forms
```

### Proposals

```
Docmost 🟢
├── Type: Open-source (Notion/Confluence alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Use for client-facing proposal documents. Clean, collaborative,
         shareable with a link. Better than AppFlowy for client-facing docs
         because of its cleaner public sharing UX.
         AppFlowy = internal. Docmost = client-facing.

Repo: github.com/docmost/docmost

Alternative: Just use a well-designed Notion-style doc in AppFlowy and export to PDF
```

### E-Signature / Contracts

```
Documenso 🟢⭐
├── Type: Open-source (DocuSign alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Full e-signature workflow. Upload your contract PDF → set signature
         fields → send to client → legally binding e-signature. Open-source
         DocuSign. No per-document fees.

Repo: github.com/documenso/documenso

Alternative: Docuseal 🟢 (github.com/docuseal/docuseal) — simpler, also free
```

### Invoicing & Finance

```
Invoice Ninja 🟢⭐
├── Type: Open-source
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Full invoicing system. Create invoices, send to clients, track
         payment status, recurring invoices for retainers, expense tracking,
         basic P&L. Connects to Stripe for online payment.
         Open-source Wave/FreshBooks.

Repo: github.com/invoiceninja/invoiceninja

Alternative: Crater 🟢 (github.com/crater-invoice/crater) — simpler
```

### Client Portal

```
Docmost 🟢 (same as proposals)
├── Use for: Shared workspace per client
├── What goes in: Project status, deliverables, reports, meeting notes
└── Client gets: Read access to their workspace, can leave comments

Structure per client:
├── [Client Name] Workspace
│   ├── Project Overview (what we're building + timeline)
│   ├── Deliverables (files, links to live work)
│   ├── Weekly Updates (running log)
│   ├── Reports (monthly performance reports)
│   └── Resources (access credentials, brand assets)
```

### Forms (Lead capture, client questionnaires, briefs)

```
Formbricks 🟢
├── Type: Open-source (Typeform alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Beautiful forms for: client onboarding questionnaires, project briefs,
         feedback surveys, NPS surveys. Embed on your agency website.
         Open-source Typeform.

Repo: github.com/formbricks/formbricks
```

---

## Layer 3 — Service Department Tools

### Department: Paid Ads

```
Google Ads — Campaign Management 🔴
├── Type: Proprietary (no open-source alternative for ad platforms)
├── Cost: Free platform, you pay for ad spend
└── Why: Required. This is where campaigns live.

Google Ads API 🔴
├── Type: Proprietary API (free to use)
├── Cost: Free (developer token required)
└── Why: You've already built create_rolland_campaigns.py around this.

Google Analytics 4 🔴
├── Type: Proprietary (free)
├── Cost: Free
└── Why: Client website analytics. Required for conversion tracking.

Google Tag Manager 🔴
├── Type: Proprietary (free)
├── Cost: Free
└── Why: Tracking deployment without touching client's code for every change.

Google Looker Studio 🔴
├── Type: Proprietary (free)
├── Cost: Free
└── Why: Client-facing reporting dashboards. Connects to Google Ads + GA4 directly.
         Best free option. No open-source alternative matches it for ad reporting.

Plausible Analytics 🟢 (for your own sites + privacy-focused clients)
├── Type: Open-source (Google Analytics alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: GDPR-compliant, cookie-free analytics. Use for agency website + clients
         who want privacy-friendly tracking.

Repo: github.com/plausible/analytics

Competitor Research:
SpyFu / SimilarWeb 🔴 — no good open-source alternative
└── Use free tiers for competitor ad intelligence
```

---

### Department: Content & SEO

```
Ahrefs / Semrush 🔴
├── Type: Proprietary
├── Cost: ~€100–200/month
└── Why: No open-source alternative with comparable keyword + backlink data.
         This is a necessary paid tool. Start with Ahrefs Starter (~€29/month).

Google Search Console 🔴
├── Type: Proprietary (free)
├── Cost: Free
└── Why: Real rank tracking from Google. Required. Free.

Screaming Frog SEO Spider 🔴
├── Type: Proprietary (free up to 500 URLs)
├── Cost: Free tier sufficient for most projects
└── Why: Technical SEO audits. Crawls sites, finds broken links, missing tags,
         duplicate content. The free tier covers most client sites.

SurferSEO / Clearscope 🔴 (content optimization)
├── Type: Proprietary
├── Cost: ~€49–89/month
└── Why: On-page SEO optimization scoring. Use free alternatives first:
         - Google's own NLP API (free tier)
         - Manually reference top 10 ranking pages

WordPress / Webflow (CMS) — depends on client's existing setup
└── Open-source CMS alternative: Ghost 🟢 (github.com/TryGhost/Ghost)
    Perfect for blog-heavy clients who want speed + simplicity.

AI Writing Assistant:
Ollama 🟢 (run local LLMs for content drafting)
├── Type: Open-source
├── Cost: Free (runs on your machine)
├── Host: Local or VPS
└── Why: Run Mistral/Llama locally for content drafts, brief generation,
         meta description writing. No per-token costs. Privacy-safe.

Repo: github.com/ollama/ollama
```

---

### Department: Web Development

```
Figma 🔴 (design)
├── Type: Proprietary (free tier)
├── Cost: Free for 3 projects
└── Why: Industry standard for web design. Clients expect Figma files.

Penpot 🟢 (open-source Figma alternative)
├── Type: Open-source
├── Cost: Free (self-hosted or cloud)
├── Host: Self-hosted via Coolify
└── Why: Full Figma alternative. SVG-native, browser-based.
         Use for internal projects. Use Figma when client collaboration requires it.

Repo: github.com/penpot/penpot

VS Code 🟢
├── Type: Open-source (Microsoft, MIT license core)
├── Cost: Free
└── Why: Primary code editor. Enough said.

Next.js 🟢 (frontend framework)
├── Type: Open-source
├── Cost: Free
└── Why: Best React framework for agency web builds. Fast, SEO-friendly, deployable everywhere.

Repo: github.com/vercel/next.js

Astro 🟢 (static/content sites)
├── Type: Open-source
├── Cost: Free
└── Why: Best choice for content-heavy, SEO-focused sites (blogs, landing pages).
         Ships zero JavaScript by default. Core Web Vitals green out of the box.

Repo: github.com/withastro/astro

Webflow 🔴 (no-code option for non-dev clients)
├── Type: Proprietary
├── Cost: ~€14–23/month per site
└── Why: When client wants to edit their own site without touching code.

WordPress 🟢 (existing client sites)
├── Type: Open-source
├── Cost: Free (hosting costs only)
└── Why: Most clients already have WordPress. Know it.

Coolify 🟢 (deployment)
├── Already listed in Layer 0
└── Why: Deploy all client sites from one dashboard. Git push → auto-deploy.

GitHub 🟡
├── Type: Proprietary free tier (Git is open-source)
├── Cost: Free for public/private repos
└── Why: Version control for all client projects. Gitea 🟢 if you want self-hosted.

Gitea 🟢 (self-hosted GitHub alternative)
├── Type: Open-source
├── Cost: Free (self-hosted)
└── Repo: github.com/go-gitea/gitea

PageSpeed Insights / Lighthouse 🔴 (free)
└── Performance testing. Required. Free.
```

---

### Department: AI & Automation

```
n8n 🟢⭐
├── Type: Open-source (Make.com / Zapier alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Your primary automation engine. Visual workflow builder, 400+ integrations,
         full code nodes (JavaScript/Python), self-hostable, no per-operation costs.
         You've already started with n8n blueprints. This stays.

Repo: github.com/n8n-io/n8n

Activepieces 🟢 (n8n alternative)
├── Type: Open-source
├── Cost: Free (self-hosted)
└── Why: Cleaner UI than n8n. Use as backup/alternative for simpler workflows.

Repo: github.com/activepieces/activepieces

Ollama 🟢 (local LLMs)
├── Already listed above
└── Why: Run AI models locally on your VPS. No API costs for internal workflows.

OpenAI API 🔴
├── Type: Proprietary
├── Cost: Pay per token
└── Why: GPT-4o for production AI features in client SaaS products.
         Use when output quality justifies the cost.

Claude API (Anthropic) 🔴
├── Type: Proprietary
├── Cost: Pay per token
└── Why: Best reasoning model for complex agentic workflows. Use Claude 3.5 Sonnet
         for your premium AI SaaS builds.

Supabase 🟢⭐
├── Type: Open-source (Firebase alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: PostgreSQL database + REST API + Auth + Storage + Realtime — all in one.
         Backend infrastructure for all AI SaaS projects. Open-source Firebase.

Repo: github.com/supabase/supabase

FastAPI 🟢 (Python backend)
├── Type: Open-source
├── Cost: Free
└── Why: Build AI service backends in Python. Fast, async, auto-generates API docs.

Repo: github.com/tiangolo/fastapi

Docker 🟢
├── Type: Open-source
├── Cost: Free
└── Why: Containerize all deployments. Consistent environments.

Python 🟢
└── Primary language for: automation scripts, data processing, AI integrations.
```

---

### Department: Creative & Design

```
Penpot 🟢
├── Already listed in Web Dev
└── Why: UI design, ad creatives, brand assets.

GIMP 🟢 (image editing)
├── Type: Open-source (Photoshop alternative)
├── Cost: Free
└── Repo: github.com/GNOME/gimp

Inkscape 🟢 (vector graphics)
├── Type: Open-source (Illustrator alternative)
├── Cost: Free
└── Repo: gitlab.com/inkscape/inkscape

Kdenlive 🟢 (video editing — for ad video content)
├── Type: Open-source
├── Cost: Free
└── Repo: invent.kde.org/multimedia/kdenlive

Canva 🔴 (quick social assets)
├── Type: Proprietary (free tier)
├── Cost: Free tier sufficient
└── Why: Fastest for quick social media graphics. Use free tier.

Unsplash / Pexels 🟡 (stock photos)
├── Type: Free (licensed for commercial use)
└── Why: Free high-quality stock photos. Use before paying for stock.
```

---

### Department: Analytics & Intelligence

```
Metabase 🟢⭐
├── Already listed in Layer 1
└── Why: Agency-wide analytics dashboard. Connect all data sources.

Google Looker Studio 🔴 (client dashboards)
├── Already listed in Paid Ads
└── Why: Client-facing performance dashboards. Free, connects to everything Google.

Plausible Analytics 🟢
├── Already listed in Paid Ads
└── Why: Privacy-friendly web analytics for your agency site + privacy-conscious clients.

PostHog 🟢 (product analytics for SaaS clients)
├── Type: Open-source (Mixpanel/Amplitude alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Full product analytics for AI SaaS builds — event tracking, funnels,
         session recordings, feature flags. Open-source Mixpanel.

Repo: github.com/PostHog/posthog

Grafana 🟢 (technical monitoring dashboards)
├── Type: Open-source
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Real-time monitoring dashboards for AI SaaS systems. Connects to
         n8n metrics, server health, API response times, error rates.
         More technical than Metabase — use for operational monitoring.

Repo: github.com/grafana/grafana
```

---

## Layer 4 — Operations Tools

### Project Management

```
Plane 🟢⭐
├── Type: Open-source (Linear/Jira alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Issues, cycles (sprints), modules (projects), pages (docs).
         One workspace for everything. Department-level modules per client.
         The operating backbone of your agency. Agreed on this already.

Repo: github.com/makeplane/plane
```

### Internal Communication

```
Mattermost 🟢⭐
├── Type: Open-source (Slack alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Full Slack clone. Channels, DMs, threads, file sharing, integrations.
         Own your data. No per-user costs ever. Works with n8n for bot notifications.

Repo: github.com/mattermost/mattermost

Alternative: Rocket.Chat 🟢 (heavier, more features, also open-source)
Note: If you prefer staying on Slack free tier — it's fine for 2 people.
      Switch to Mattermost when team grows or data ownership matters.
```

### Video Calls

```
Jitsi Meet 🟢
├── Type: Open-source (Zoom alternative)
├── Cost: Free (use meet.jit.si or self-host)
├── Host: Cloud (free) or self-hosted
└── Why: No account needed. Share a link. Full video/audio/screen share.
         Use for: internal calls, client calls, demos.
         meet.jit.si is free forever, no installation needed.

Repo: github.com/jitsi/jitsi-meet
```

### Screen Recording / Async Video (Loom alternative)

```
Cap 🟢
├── Type: Open-source (Loom alternative)
├── Cost: Free
├── Host: Cloud (open-source)
└── Why: Record screen + camera. Share link. Client watches async.
         Use for: client update walkthroughs, QA recordings, onboarding videos.

Repo: github.com/CapSoftware/Cap

Alternative: OBS Studio 🟢 (more control, steeper learning curve)
```

### Knowledge Management

```
AppFlowy 🟢⭐
├── Already listed in Layer 1
└── Structure:
    ├── Agency Playbooks (how we do each service)
    ├── Templates Library (proposals, briefs, reports, emails)
    ├── What Works (ad copy, campaign structures, content formats)
    ├── Case Studies (problem → solution → results per client)
    └── Learning Log (books, courses, experiments)
```

### QA Management

```
Plane 🟢 (same tool as project management)
└── Use: QA checklists as issue templates per department.
    When work is "Ready for QA" → assign to reviewer → checklist completed → approved/rejected.
```

### Password & Secrets Management

```
Vaultwarden 🟢⭐
├── Type: Open-source (self-hosted Bitwarden-compatible server)
├── Cost: Free (self-hosted on your Hetzner VPS)
├── Host: Self-hosted via Coolify
└── Why: Full Bitwarden experience (browser extension, mobile app, desktop app)
         but self-hosted. You own ALL your passwords and credentials.
         Bitwarden clients connect to your Vaultwarden server.
         This is how you secure every tool, every client account, every API key.

Repo: github.com/dani-garcia/vaultwarden
```

### Contracts & E-Signatures

```
Documenso 🟢⭐
├── Already listed in Layer 2
└── Why: All client contracts signed here. Zero per-document fees.
```

### Invoicing & Finance

```
Invoice Ninja 🟢⭐
├── Already listed in Layer 2
└── Why: Invoicing, recurring retainers, expense tracking, basic P&L.
```

### HR / Team (when you hire)

```
Planka 🟢
├── Type: Open-source (Trello-like board)
├── Cost: Free (self-hosted)
└── Why: Simple kanban boards for hiring pipeline, onboarding new team members.

Repo: github.com/plankanban/planka
```

### Email Marketing / Newsletter (agency's own content marketing)

```
Listmonk 🟢
├── Type: Open-source (Mailchimp alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Send newsletters, cold email sequences, client digest emails.
         No per-subscriber fees. Own your list. GDPR-compliant.

Repo: github.com/knadh/listmonk
```

### Social Media Management (agency's own presence)

```
Postiz 🟢
├── Type: Open-source (Buffer/Hootsuite alternative)
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Schedule posts across LinkedIn, X, Instagram from one dashboard.
         Build agency brand on social without paying Buffer/Hootsuite fees.

Repo: github.com/gitroomhq/postiz-app
```

### Security — Uptime Monitoring

```
Uptime Kuma 🟢⭐
├── Type: Open-source
├── Cost: Free (self-hosted)
├── Host: Self-hosted via Coolify
└── Why: Monitor uptime of ALL your deployed services (n8n, Supabase, client sites,
         your own tools). Alerts via email/Slack/Telegram when anything goes down.
         Set this up once and it watches everything.

Repo: github.com/louislam/uptime-kuma
```

### Backup System

```
Restic 🟢
├── Type: Open-source
├── Cost: Free (+ storage cost)
└── Why: Encrypted backups of all self-hosted data (databases, files, configs).
         Backup to Backblaze B2 (cheapest S3-compatible storage: ~$0.006/GB/month).
         Run automated daily backups via cron.

Repo: github.com/restic/restic
Storage: Backblaze B2 (not open-source but cheapest option, ~€2–5/month)
```

---

## Layer 5 — Agency Brand & Positioning Tools

### Agency Website

```
Astro 🟢 + Coolify deployment
├── Already listed in Web Dev dept
└── Why: Build your own agency site in Astro. Fast, SEO-optimized, showcases work.
         Deploy on Coolify. Custom domain on Cloudflare.
         Your agency website is your 24/7 sales pitch.
```

### Portfolio / Case Studies

```
AppFlowy or Docmost
└── Internal: AppFlowy for drafting case studies
    Public: Published as pages on your agency website
```

---

## Full Stack Summary

### Open-Source Tools (Self-Hosted on Hetzner via Coolify)

| Tool | Category | Replaces |
|------|----------|---------|
| Coolify | Infrastructure | Heroku, Railway, Render |
| Plane | Project Management | Linear, Jira, Asana |
| Mattermost | Communication | Slack |
| Twenty | CRM | HubSpot, Salesforce |
| AppFlowy | Knowledge + OKRs | Notion |
| Docmost | Client Portals + Proposals | Notion, Confluence |
| Vaultwarden | Password Manager | 1Password, LastPass |
| Documenso | E-Signatures | DocuSign, PandaDoc |
| Invoice Ninja | Invoicing + Finance | Wave, FreshBooks |
| n8n | Automation | Make.com, Zapier |
| Supabase | Database + Backend | Firebase, Airtable at scale |
| Activepieces | Automation (backup) | Make.com |
| Formbricks | Forms | Typeform, JotForm |
| Cal.com | Scheduling | Calendly |
| Metabase | Analytics Dashboards | Tableau, Grafana (business) |
| Grafana | Technical Monitoring | Datadog |
| PostHog | Product Analytics | Mixpanel, Amplitude |
| Plausible | Web Analytics | Google Analytics |
| Listmonk | Email Marketing | Mailchimp, Brevo |
| Postiz | Social Media | Buffer, Hootsuite |
| Uptime Kuma | Uptime Monitoring | Better Uptime, Pingdom |
| Jitsi Meet | Video Calls | Zoom, Google Meet |
| Cap | Screen Recording | Loom |
| Penpot | UI Design | Figma (for internal use) |
| Gitea | Git Hosting | GitHub (self-hosted) |
| Ghost | Blog/CMS | WordPress (for new client sites) |
| Ollama | Local AI | OpenAI API (for dev/drafts) |

### Necessary Proprietary Tools (No Good Open-Source Alternative)

| Tool | Category | Cost | Why Necessary |
|------|----------|------|--------------|
| Google Ads | Paid Ads Platform | Free (pay ad spend) | The ad platform. Can't avoid it. |
| Google Analytics 4 | Web Analytics (client) | Free | Client conversion tracking |
| Google Tag Manager | Tag Management | Free | Tracking deployment |
| Google Search Console | SEO Monitoring | Free | Real ranking data from Google |
| Google Looker Studio | Client Reporting | Free | Best free client dashboards |
| Cloudflare | DNS + CDN | Free | Best free DNS/CDN |
| Figma | Design (client collab) | Free (3 projects) | Client collaboration requires it |
| Ahrefs Starter | SEO Research | ~€29/month | No open-source keyword data |
| Resend | Transactional Email | Free (3k/month) | Email deliverability |
| Hetzner VPS | Server Hosting | ~€5–20/month | Everything runs on this |
| Backblaze B2 | Backup Storage | ~€2–5/month | Cheapest encrypted backup storage |

### Tools You Already Use (From RA-Project)

| Tool | Status | Notes |
|------|--------|-------|
| n8n | ⚠️ Blueprint only | Deploy via Coolify on Hetzner |
| Google Ads API | ⚠️ Script built | Needs foundation gates cleared |
| Airtable | ⚠️ In architecture | Replace with Supabase at scale |
| Python | ✅ Active | Keep using for automation + AI |
| GitHub | ✅ Assumed active | Keep (or self-host with Gitea) |

---

## Estimated Monthly Infrastructure Cost

| Item | Cost/month |
|------|-----------|
| Hetzner VPS (CAX21: 4 vCPU ARM, 8GB RAM) | ~€8 |
| Cloudflare (DNS + CDN) | Free |
| Resend (transactional email) | Free |
| Proton Mail or Migadu (business email) | €4 |
| Ahrefs Starter (SEO) | €29 |
| Backblaze B2 (backup storage) | ~€2 |
| **Total** | **~€43/month** |

Everything else (Plane, Mattermost, AppFlowy, n8n, Supabase, Twenty, Vaultwarden, Cal.com, Listmonk, Postiz, Uptime Kuma, Metabase, Grafana, PostHog, Penpot, Formbricks, Documenso, Invoice Ninja, Jitsi) runs **free on your Hetzner VPS**.

---

## Setup Priority Order

### Week 1 — Core Operations (set these up first)
1. ⭐ Hetzner VPS + Coolify (the foundation everything else runs on)
2. ⭐ Vaultwarden (secure all passwords immediately)
3. ⭐ Plane (project management — start tracking work today)
4. ⭐ Mattermost or Slack free (communication)
5. ⭐ AppFlowy (OKRs, knowledge base, team docs)
6. ⭐ Uptime Kuma (monitor everything you deploy)

### Week 2 — Client Delivery
7. Twenty CRM (track RA-Project + prospect pipeline)
8. Documenso (get contracts signed properly)
9. Invoice Ninja (send professional invoices)
10. Cal.com (share booking link for client calls)
11. Docmost (build RA-Project client portal)

### Week 3 — Automation & Analytics
12. n8n (deploy on Coolify — needed for RA lead gen)
13. Supabase (database for RA lead gen system)
14. Metabase (connect to Supabase for agency dashboard)
15. Plausible (add to agency website)

### Month 2+ — Growth Tools
16. Listmonk (outbound email sequences for BD)
17. Postiz (agency social media presence)
18. PostHog (add to AI SaaS projects)
19. Grafana (monitoring for deployed AI systems)
20. Penpot (design work)
