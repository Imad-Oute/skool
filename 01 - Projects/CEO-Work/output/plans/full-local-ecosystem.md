# Full Local Ecosystem — Solo Operator Setup
**Owner:** Imad
**Goal:** $1k → $100k/month in < 12 months
**Philosophy:** Everything local. Open-source first. Own your data. No subscriptions where avoidable.
**Last Updated:** 2026-04-16

---

## Architecture Overview

Everything runs in two modes:

```
DESKTOP APPS          → Install directly on your machine (no Docker)
DOCKER SERVICES       → Run locally via Docker Compose (server-like processes)
```

When you're ready to scale → same Docker Compose deploys to a VPS. Zero migration.

```
YOUR MACHINE
├── Desktop Apps (always available, no running services)
│   ├── Obsidian          → Second brain + learning system
│   ├── VS Code           → Code editor
│   ├── Anki              → Skill learning via spaced repetition
│   ├── Thunderbird       → Email
│   ├── KeePassXC         → Passwords (lightweight, no Docker)
│   ├── GIMP              → Image editing
│   ├── Inkscape          → Vector design
│   ├── Kdenlive          → Video editing
│   ├── OBS Studio        → Screen recording
│   ├── Calibre           → Book library
│   ├── Zotero            → Research + articles
│   ├── ActivityWatch     → Time tracking
│   └── VLC               → Media player
│
└── Docker Services (run when needed, always-on optional)
    ├── Plane             → Project management
    ├── AppFlowy          → Docs, OKRs, knowledge base
    ├── n8n               → Automation engine
    ├── Supabase          → Database + backend (dev)
    ├── Penpot            → UI/UX design
    ├── Open WebUI        → Local AI chat interface
    ├── Ollama            → Local LLM models
    ├── Invoice Ninja     → Invoicing + finance
    ├── Documenso         → Contracts + e-signatures
    ├── Uptime Kuma       → Service monitoring
    └── Metabase          → Analytics dashboards
```

---

## Part 1 — Agency Operations

### Project & Task Management

```
Plane 🟢 [Docker]
├── Purpose: Manage all client projects, agency tasks, sprints, department work
├── Use for:
│   ├── RA-Project: all tasks, milestones, delivery tracking
│   ├── Construction SaaS: development sprints
│   ├── Agency Internal: systems building tasks
│   └── Department modules: one module per service line
├── URL: localhost:3000
└── Repo: github.com/makeplane/plane
```

### Automation Engine

```
n8n 🟢 [Docker]
├── Purpose: Build and run all automations locally during development
├── Use for:
│   ├── RA-Project lead gen pipeline (7-system automation)
│   ├── Client reporting automations
│   ├── Internal workflow automations
│   └── AI workflow prototyping
├── URL: localhost:5678
└── Repo: github.com/n8n-io/n8n
```

### Database & Backend (SaaS Development)

```
Supabase 🟢 [Docker]
├── Purpose: Local PostgreSQL + Auth + Storage + REST API for all SaaS builds
├── Use for:
│   ├── RA-Project lead database (replace Airtable)
│   ├── Construction company AI SaaS backend
│   └── Any future SaaS product
├── URL: localhost:54323 (Studio UI)
└── Repo: github.com/supabase/supabase
```

### Design (UI/UX + Creatives)

```
Penpot 🟢 [Docker]
├── Purpose: UI design, wireframes, ad creatives, brand assets
├── Use for:
│   ├── Client website mockups
│   ├── Landing page designs
│   ├── Ad creative design
│   └── Agency brand assets
├── URL: localhost:9001
└── Repo: github.com/penpot/penpot
```

### Invoicing & Finance

```
Invoice Ninja 🟢 [Docker]
├── Purpose: Professional invoices, track payments, recurring retainers
├── Use for:
│   ├── Invoice clients (RA-Project, future clients)
│   ├── Track who paid, who owes
│   ├── Recurring monthly retainer invoices
│   └── Basic P&L tracking
├── URL: localhost:8000
└── Repo: github.com/invoiceninja/invoiceninja
```

### Contracts

```
Documenso 🟢 [Docker]
├── Purpose: E-signature for client contracts
├── Use for:
│   ├── Service agreements with clients
│   ├── NDA when needed
│   └── Any document needing legal sign-off
├── URL: localhost:3001
└── Repo: github.com/documenso/documenso
```

### Analytics

```
Metabase 🟢 [Docker]
├── Purpose: Visual dashboards connected to Supabase/PostgreSQL
├── Use for:
│   ├── Agency KPI dashboard (revenue, clients, deliverables)
│   ├── Client campaign data visualization
│   └── RA-Project lead gen pipeline stats
├── URL: localhost:3002
└── Repo: github.com/metabase/metabase
```

### Monitoring

```
Uptime Kuma 🟢 [Docker]
├── Purpose: Monitor all local Docker services + any deployed client work
├── Use for:
│   ├── Know immediately if any local service crashes
│   ├── Monitor client websites (ping monitoring)
│   └── Monitor deployed automations
├── URL: localhost:3003
└── Repo: github.com/louislam/uptime-kuma
```

---

## Part 2 — Knowledge & Learning System

This is the most important part for a 20-year-old going from zero to elite.
Your knowledge system IS your competitive advantage compounding over time.

### Second Brain (Primary Knowledge Base)

```
Obsidian 🟢 [Desktop App]
├── Purpose: Your external brain. Everything you learn, think, plan lives here.
├── Use for:
│   ├── LEARNING NOTES: Summaries from every book, course, video watched
│   ├── SKILL MAPS: What you know, what you're learning, what's next
│   ├── CEO JOURNAL: Daily/weekly reflections, decisions, lessons
│   ├── MEETING NOTES: Every client call, every important conversation
│   ├── IDEAS: Capture every business idea, product idea, content idea
│   ├── RESEARCH: Deep dives on any topic (competitors, markets, tech)
│   └── SYSTEMS DOCS: Agency playbooks, processes, what works
├── Storage: Local markdown files (sync via Git if needed)
├── Key Plugins:
│   ├── Dataview (query your notes like a database)
│   ├── Calendar (daily notes, weekly reviews)
│   ├── Tasks (inline task management)
│   ├── Templater (templates for note types)
│   └── Omnisearch (find anything instantly)
└── Download: obsidian.md
```

### Spaced Repetition (Skill Mastery)

```
Anki 🟢 [Desktop App]
├── Purpose: Lock in knowledge permanently. Learn once, retain forever.
├── Use for:
│   ├── Google Ads concepts, bidding strategies, optimization rules
│   ├── SEO principles, algorithm updates, ranking factors
│   ├── AI/ML concepts (for building AI SaaS)
│   ├── Business fundamentals (pricing, margins, positioning)
│   ├── Code patterns (Python, JavaScript, SQL)
│   ├── Sales scripts, objection handling
│   └── Any concept worth remembering from books/courses
├── Method: After every learning session → create 5–10 Anki cards
│           Review cards daily (10–15 min/morning)
└── Download: apps.ankiweb.net
```

### Research Management

```
Zotero 🟢 [Desktop App]
├── Purpose: Organize research, articles, PDFs, web pages
├── Use for:
│   ├── Save and annotate industry research
│   ├── Competitor analysis documents
│   ├── Technical papers for AI/automation work
│   ├── Marketing research and case studies
│   └── Any article worth reading later
├── Browser extension: captures articles in one click
└── Repo: github.com/zotero/zotero
```

### Book Library

```
Calibre 🟢 [Desktop App]
├── Purpose: Manage your entire ebook library
├── Use for:
│   ├── Store and organize all ebooks (business, tech, mindset)
│   ├── Convert formats as needed
│   └── Read on device or desktop
└── Repo: github.com/kovidgoyal/calibre
```

### AppFlowy (Team/Agency Docs)

```
AppFlowy 🟢 [Docker]
├── Purpose: Structured docs — agency playbooks, templates, OKRs
├── Use for:
│   ├── OKRs and quarterly goals
│   ├── Department playbooks (how you do each service)
│   ├── Client onboarding templates
│   ├── Proposal templates, brief templates, report templates
│   └── Case studies as you build them
├── Note: Obsidian = thinking + learning. AppFlowy = structured agency docs.
├── URL: localhost:3004
└── Repo: github.com/AppFlowy-IO/AppFlowy
```

---

## Part 3 — AI & Intelligence Layer

### Local AI (Your Personal AI Stack)

```
Ollama 🟢 [Docker]
├── Purpose: Run AI models locally. Zero API costs for dev and daily use.
├── Models to run:
│   ├── mistral (fast, general purpose — daily assistant)
│   ├── llama3 (strongest open-source reasoning)
│   ├── codellama (code generation + review)
│   └── nomic-embed-text (embeddings for RAG)
├── URL: localhost:11434 (API)
└── Repo: github.com/ollama/ollama

Open WebUI 🟢 [Docker]
├── Purpose: Beautiful ChatGPT-like interface for your local Ollama models
├── Use for:
│   ├── Daily AI assistance (brainstorming, writing, research)
│   ├── Code review and debugging
│   ├── Draft client emails, proposals, reports
│   ├── Summarize articles and research
│   └── Build and test prompts for n8n workflows
├── URL: localhost:8080
└── Repo: github.com/open-webui/open-webui
```

---

## Part 4 — Personal Productivity

### Time Awareness

```
ActivityWatch 🟢 [Desktop App]
├── Purpose: Automatic time tracking. Know exactly where your hours go.
├── Use for:
│   ├── See how many hours actually went to deep work vs. distraction
│   ├── Track time per client project
│   ├── Identify your most productive hours
│   └── Hold yourself accountable (data doesn't lie)
├── It runs in the background — you install it and forget it
└── Repo: github.com/ActivityWatch/activitywatch
```

### Focus & Deep Work

```
Pomatez 🟢 [Desktop App]
├── Purpose: Pomodoro timer — structured deep work sessions
├── Use for:
│   ├── 90-minute deep work blocks (CEO standard)
│   ├── Break reminders (protect your energy)
│   └── Session logging
└── Repo: github.com/zidoro/pomatez
```

### Habit Tracking

```
Loop Habit Tracker 🟢 [Mobile] or Habitica 🟢 [Web/Mobile]
├── Purpose: Build and track elite daily habits
├── Habits to track:
│   ├── Morning standup (15 min — what are my 3 MITs today?)
│   ├── Deep work blocks completed
│   ├── Anki review done
│   ├── CEO weekly review (Sunday)
│   ├── Physical exercise
│   ├── Reading (30 min/day minimum)
│   └── Evening reflection (what did I ship today?)
└── Loop: github.com/iSoron/uhabits
```

### Password Management

```
KeePassXC 🟢 [Desktop App]
├── Purpose: Offline password manager — zero cloud, zero breach risk
├── Use for: Every login, every API key, every credential
├── Storage: Local encrypted .kdbx file (back up to external drive)
└── Repo: github.com/keepassxreboot/keepassxc
```

---

## Part 5 — Creative & Content Tools

### Screen Recording (Client Deliveries + Learning)

```
OBS Studio 🟢 [Desktop App]
├── Purpose: Screen recording for client walkthroughs, personal recordings
├── Use for:
│   ├── Record Loom-style client update videos
│   ├── Record tutorial content if you build a personal brand
│   └── Capture important demos
└── Repo: github.com/obsproject/obs-studio
```

### Image Editing

```
GIMP 🟢 [Desktop App]
├── Purpose: Raster image editing (Photoshop alternative)
└── Repo: github.com/GNOME/gimp

Inkscape 🟢 [Desktop App]
├── Purpose: Vector graphics (Illustrator alternative)
└── Repo: gitlab.com/inkscape/inkscape
```

### Video Editing

```
Kdenlive 🟢 [Desktop App]
├── Purpose: Video editing for ad content, agency content, personal brand
└── Repo: invent.kde.org/multimedia/kdenlive
```

---

## Part 6 — Communication & Email

### Email Client

```
Thunderbird 🟢 [Desktop App]
├── Purpose: Manage all email accounts in one place
├── Use for:
│   ├── Agency email (youragency.com)
│   ├── Personal email
│   └── Client communication (threaded per client)
└── mozilla.org/thunderbird
```

### Video Calls (Client Meetings)

```
Jitsi Meet 🟡 [Browser — no install]
├── Purpose: Client calls, no account needed
├── Use: meet.jit.si → create room → share link
└── Zero setup. Free forever.
```

---

## Part 7 — Development Environment

### Code Editor

```
VS Code 🟢 [Desktop App]
├── Extensions (install these):
│   ├── GitLens (git history inline)
│   ├── Docker (manage containers)
│   ├── Prettier (code formatting)
│   ├── ESLint (JavaScript linting)
│   ├── Python (Python support)
│   ├── Tailwind CSS IntelliSense
│   ├── REST Client (test APIs without Postman)
│   └── GitHub Copilot (if budget allows — massive productivity boost)
└── code.visualstudio.com
```

### Version Control

```
Git + GitHub 🟢
├── GitHub org structure:
│   ├── agency-infra/ → Docker Compose for all local services
│   ├── ra-project/ → RA-Project client work
│   ├── construction-saas/ → AI SaaS client project
│   └── agency-website/ → Your own agency website
└── Git CLI or GitHub Desktop (your choice)
```

### Local Dev Infrastructure

```
Docker Desktop 🟢
├── Purpose: Run all Docker services locally
├── Manages: All the Docker services in this document
└── docker.com/products/docker-desktop
```

---

## Part 8 — Skills Learning Roadmap

**The skills you need to master — sequenced by revenue stage:**

### Stage 1: $0 → $10k/month (Now — Month 3)
*Master the skills that deliver results for current clients*

```
PAID ADS (Google Ads)
├── Google Ads fundamentals (search campaigns, bidding, quality score)
├── Google Ads API (you've started — finish it)
├── Conversion tracking + GA4
└── Campaign optimization (what to change and when)
Resources: Google Skillshop (free), YouTube, do + document

SEO & CONTENT
├── On-page SEO fundamentals
├── Technical SEO basics (Core Web Vitals, indexing)
├── Keyword research methodology
└── Content strategy for lead generation
Resources: Ahrefs Academy (free), Moz Beginner's Guide

WEB PERFORMANCE
├── Core Web Vitals optimization
├── Next.js / Astro (if not already solid)
└── Technical SEO implementation
Resources: web.dev (Google's free resource)

CEO / LEADERSHIP (while building)
├── "The Hard Thing About Hard Things" — Ben Horowitz
├── "Zero to One" — Peter Thiel
├── "High Output Management" — Andy Grove (most important management book)
└── "$100M Offers" — Alex Hormozi (positioning + pricing)
```

### Stage 2: $10k → $50k/month (Month 3–8)
*Add the skills that unlock scale*

```
AI & AUTOMATION (your premium track)
├── n8n mastery (advanced workflows, error handling, APIs)
├── Python for AI (LangChain, OpenAI API, Claude API)
├── Supabase + PostgreSQL (database design for SaaS)
├── FastAPI (Python backend for AI services)
└── Prompt engineering (production-grade prompts)
Resources: n8n docs, FastAPI docs, LangChain docs, build projects

SALES & BD
├── Cold email that converts (Alex Berman framework)
├── Discovery call framework (SPIN Selling)
├── Proposal writing
└── Negotiation basics
Resources: "SPIN Selling" — Neil Rackham

BUSINESS FUNDAMENTALS
├── Unit economics (CAC, LTV, margins)
├── Pricing strategy (value-based pricing)
├── Cash flow management
└── Hiring (when, who, how)
Resources: "Profit First" — Mike Michalowicz, "Built to Sell" — John Warrillow
```

### Stage 3: $50k → $100k/month (Month 8–12)
*The leverage layer*

```
SYSTEMS & SCALE
├── SOPs and documentation (how to delegate)
├── Hiring and onboarding
├── Management frameworks
└── Agency positioning and premium pricing

ADVANCED AI
├── Fine-tuning models
├── RAG systems (retrieval-augmented generation)
├── Multi-agent systems
└── Production AI deployment

PERSONAL BRAND (optional but powerful)
├── Content creation on LinkedIn/X
├── Build in public (document the journey)
└── Speaking / thought leadership
```

---

## Part 9 — CEO Operating System (Personal)

### Daily Rhythm

```
06:00 — Wake + Physical (30 min exercise minimum)
06:30 — Anki review (15 min — lock in yesterday's learning)
06:45 — CEO Morning Review (15 min):
         → What are my 3 MITs today?
         → What's the #1 thing that moves the needle?
         → Write it down in Obsidian daily note
07:00 — Deep Work Block 1 (90–120 min — hardest MIT first)
09:00 — Break (15 min — Pomatez enforces this)
09:15 — Deep Work Block 2 (90 min)
11:00 — Client communication + email (30 min — batch, not constant)
11:30 — Deep Work Block 3 (90 min)
13:00 — Lunch + real break (no screen if possible)
14:00 — Deep Work Block 4 (90 min — second hardest work)
15:30 — Learning Block (60 min — book, course, or skill practice)
16:30 — Admin (invoices, planning, research — low-cognitive tasks)
17:30 — Evening Review (15 min in Obsidian):
         → What did I ship today?
         → Did I hit my MITs?
         → What's tomorrow's #1 priority?
18:00 — Done. Protect evenings for recovery.
```

### Weekly Rhythm

```
MONDAY: Weekly planning (30 min) — set 3 MITs for the week
MON–FRI: Daily rhythm above
FRIDAY: Weekly review (30 min) — what shipped, what didn't, why
SATURDAY: Learning deep dive (2–3 hours — master one concept deeply)
SUNDAY: CEO review (30 min) — OKR check, next week direction, Obsidian weekly note
```

### Obsidian Vault Structure

```
vault/
├── 00-Inbox/           → capture everything fast, sort later
├── 01-Daily/           → daily notes (linked to calendar)
├── 02-Weekly/          → weekly reviews
├── 03-Projects/        → one note per active project
│   ├── RA-Project/
│   └── Construction-SaaS/
├── 04-Areas/           → ongoing areas of responsibility
│   ├── Agency-CEO/     → leadership, strategy, decisions
│   ├── Skills/         → what you're learning
│   └── Finance/        → personal + business financial tracking
├── 05-Resources/       → reference material
│   ├── Books/          → one note per book (summary + key ideas)
│   ├── Courses/        → notes from courses
│   └── Research/       → industry knowledge
├── 06-Archive/         → completed projects, old notes
└── Templates/          → note templates
    ├── Daily-Note.md
    ├── Weekly-Review.md
    ├── Book-Summary.md
    ├── Project.md
    └── Meeting-Note.md
```

---

## Part 10 — Docker Compose Architecture

All Docker services in one `docker-compose.yml` in your `agency-infra` GitHub repo.

### Repository Structure

```
agency-infra/
├── docker-compose.yml        → all services
├── docker-compose.override.yml → local dev overrides (gitignored)
├── .env.example              → all required env vars (committed)
├── .env                      → actual secrets (gitignored)
├── configs/
│   ├── plane/
│   ├── n8n/
│   ├── supabase/
│   ├── penpot/
│   └── nginx/
│       └── nginx.conf        → local reverse proxy
├── data/                     → all volumes (gitignored)
└── README.md                 → how to start everything
```

### Services Map

```yaml
# docker-compose.yml (structure)
services:

  # ── REVERSE PROXY ──────────────────────────────────
  nginx:                        # routes *.localhost to each service
    ports: 80

  # ── PROJECT MANAGEMENT ─────────────────────────────
  plane-web:     localhost/plane
  plane-api:     (internal)
  plane-worker:  (internal)
  plane-db:      PostgreSQL (internal)
  plane-redis:   Redis (internal)

  # ── DOCS & KNOWLEDGE ───────────────────────────────
  appflowy:      localhost/appflowy
  appflowy-db:   PostgreSQL (internal)

  # ── AUTOMATION ─────────────────────────────────────
  n8n:           localhost/n8n

  # ── DATABASE / BACKEND ─────────────────────────────
  supabase-db:         PostgreSQL
  supabase-studio:     localhost/supabase
  supabase-auth:       (internal)
  supabase-rest:       (internal)
  supabase-storage:    (internal)

  # ── DESIGN ─────────────────────────────────────────
  penpot-frontend:   localhost/penpot
  penpot-backend:    (internal)
  penpot-exporter:   (internal)
  penpot-db:         PostgreSQL (internal)
  penpot-redis:      Redis (internal)

  # ── LOCAL AI ───────────────────────────────────────
  ollama:          localhost:11434 (API)
  open-webui:      localhost/ai

  # ── BUSINESS ───────────────────────────────────────
  invoice-ninja:   localhost/invoices
  invoice-db:      MySQL (internal)

  documenso:       localhost/contracts
  documenso-db:    PostgreSQL (internal)

  # ── ANALYTICS ──────────────────────────────────────
  metabase:        localhost/analytics
  metabase-db:     PostgreSQL (internal)

  # ── MONITORING ─────────────────────────────────────
  uptime-kuma:     localhost/status
```

### Local URL Map (via nginx reverse proxy)

| Service | Local URL | Purpose |
|---------|----------|---------|
| Plane | localhost/plane | Project management |
| AppFlowy | localhost/appflowy | Docs + OKRs |
| n8n | localhost/n8n | Automation |
| Supabase Studio | localhost/supabase | Database UI |
| Penpot | localhost/penpot | Design |
| Open WebUI | localhost/ai | Local AI chat |
| Invoice Ninja | localhost/invoices | Billing |
| Documenso | localhost/contracts | E-signatures |
| Metabase | localhost/analytics | Dashboards |
| Uptime Kuma | localhost/status | Monitoring |

---

## Part 11 — Full Tool Inventory

### Docker Services (run via docker-compose.yml)

| Tool | Category | Image | Priority |
|------|----------|-------|----------|
| Plane | Project Management | makeplane/plane | P0 |
| n8n | Automation | n8nio/n8n | P0 |
| Open WebUI | AI Interface | ghcr.io/open-webui/open-webui | P0 |
| Ollama | Local LLMs | ollama/ollama | P0 |
| AppFlowy | Docs + Knowledge | appflowyio/appflowy_cloud | P1 |
| Supabase | Database + Backend | supabase/supabase | P1 |
| Penpot | Design | penpotapp/frontend | P1 |
| Invoice Ninja | Invoicing | invoiceninja/invoiceninja | P1 |
| Documenso | Contracts | documenso/documenso | P1 |
| Uptime Kuma | Monitoring | louislam/uptime-kuma | P1 |
| Metabase | Analytics | metabase/metabase | P2 |

### Desktop Apps (install directly)

| Tool | Category | Priority |
|------|----------|----------|
| Obsidian | Second Brain | P0 |
| VS Code | Code Editor | P0 |
| KeePassXC | Passwords | P0 |
| ActivityWatch | Time Tracking | P0 |
| Anki | Learning/Memory | P0 |
| Docker Desktop | Infrastructure | P0 |
| Thunderbird | Email | P1 |
| GIMP | Image Editing | P1 |
| Inkscape | Vector Design | P1 |
| OBS Studio | Screen Recording | P1 |
| Pomatez | Focus/Pomodoro | P1 |
| Calibre | Book Library | P2 |
| Zotero | Research | P2 |
| Kdenlive | Video Editing | P2 |

---

## Setup Sequence (Build Order)

### Day 1 — Foundation
1. Install Docker Desktop
2. Install Obsidian → set up vault structure
3. Install KeePassXC → move all passwords here
4. Install ActivityWatch → starts tracking immediately
5. Install VS Code + extensions
6. Install Anki → create first deck

### Day 2 — Core Agency Stack
7. Clone `agency-infra` repo
8. Set up `docker-compose.yml` with: Plane + n8n + Ollama + Open WebUI
9. Configure nginx reverse proxy
10. Set up `.env` from `.env.example`
11. `docker compose up -d`
12. Set up Plane: create RA-Project, departments, first sprint

### Day 3 — Business Tools
13. Add Invoice Ninja + Documenso to compose
14. Set up first invoice template in Invoice Ninja
15. Upload contract template to Documenso
16. Add Uptime Kuma → monitor all running services

### Week 2 — Design + Data
17. Add Penpot to compose
18. Add Supabase to compose
19. Add AppFlowy to compose → migrate architecture docs here
20. Add Metabase → connect to Supabase

### Month 2+ — As Needed
- Add services only when the problem exists
- Don't run services you're not using (CPU/RAM cost on local machine)
