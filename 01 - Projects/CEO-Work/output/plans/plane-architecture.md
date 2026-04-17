# Plane Architecture — Agency Operating System
**Owner:** Imad
**Version:** v1 (solo operator, 1 active client)
**Last Updated:** 2026-04-16

---

## Overview

Plane is the single source of truth for all agency work. Every task that matters lives here. If it's not in Plane, it doesn't exist.

```
WORKSPACE: [Agency Name]
├── PROJECT: RA-Project (RollandAssurance) ← active client
├── PROJECT: Agency-OS (Internal Operations) ← infrastructure + CEO systems
├── PROJECT: BD-Pipeline (Business Development) ← activate Month 2
└── PROJECT: Construction-SaaS (AI SaaS) ← activate Month 4-8
```

---

# PART 1 — WORKSPACE SETUP

## Workspace Settings

```
Workspace name:     [Your Agency Name]
Workspace URL:      localhost:3000/[agency-slug]
Role:               Owner (you)
Members:            Just you at v1
```

---

# PART 2 — STATES (Workflow)

**Apply this state set to ALL projects. Consistent workflow across everything.**

```
STATE SET: Agency Standard

┌─────────────┬────────────────────────────────────────────────────────┐
│ State       │ Meaning                                                │
├─────────────┼────────────────────────────────────────────────────────┤
│ 📋 Backlog  │ Captured but not scheduled — will be done, not now    │
│ 📌 Todo     │ Scheduled — this week or this cycle                   │
│ ⚡ In Progress │ Actively working on it right now                  │
│ 🔍 In Review   │ Done by you — needs QA pass or client review      │
│ ✅ Done     │ Shipped, approved, complete                           │
│ ❌ Cancelled│ Won't do — scope change or no longer relevant         │
└─────────────┴────────────────────────────────────────────────────────┘

Default state for new issues: Backlog
"Done" is the only terminal state that counts.
```

---

# PART 3 — LABELS

**Labels tag issues by department and type. Apply globally across all projects.**

## Department Labels (what area the work belongs to)

```
Label           Color       Use for
──────────────────────────────────────────────────────────────────
[ads]           🔴 Red      Google Ads setup, optimization, reporting
[content]       🟢 Green    Blog articles, copy, editorial calendar
[seo]           🟡 Yellow   Technical SEO, keyword research, rankings
[webdev]        🔵 Blue     Code, website builds, deployments
[design]        🟣 Purple   Wireframes, mockups, brand assets
[analytics]     🟠 Orange   Tracking setup, dashboards, reporting
[ai-automation] ⚫ Black    n8n workflows, AI SaaS features, scripts
[ops]           ⚪ Grey     Internal systems, infrastructure, admin
```

## Type Labels (what kind of task it is)

```
Label           Use for
──────────────────────────────────────────────────────────────────
[deliverable]   Work that ships to the client
[qa]            Quality assurance pass before client delivery
[strategy]      Planning, research, decision-making tasks
[admin]         Invoices, contracts, comms, scheduling
[setup]         One-time configuration or installation tasks
[blocker]       Something blocking another task — resolve first
```

---

# PART 4 — PROJECTS

---

## PROJECT 1: RA-Project (RollandAssurance)

**Status:** Active — primary mission
**Goal:** Get RollandAssurance generating qualified insurance leads from digital channels
**Client:** RollandAssurance (insurance broker)
**Start date:** 2026-04-16
**Target completion:** 2026-06-30 (first delivery cycle)

### Project Description
```
Mission: Website live + Google Ads running + content flowing + SEO in motion.
Success = client says "we're getting leads."
This is the only project that matters until this is delivered.
```

### Modules (department tracks within RA-Project)

```
MODULE 1: Website
Status: ⚠️ In Progress
Goal: Live, fast, SEO-ready, conversion-optimized site
Owner: Imad
Completion gate: All 12 QA checks pass + client approval + live on domain

MODULE 2: Paid Ads
Status: ❌ Not Started — blocked by Website (tracking requires live site)
Goal: Google Ads campaign generating leads at target CPL
Owner: Imad
Completion gate: Campaigns live + conversion tracking verified + first week monitored

MODULE 3: Content & SEO
Status: ❌ Not Started
Goal: 4+ articles published, targeting keywords with buyer intent
Owner: Imad
Completion gate: Articles published, indexed in GSC, ranking movement visible in 30 days

MODULE 4: Analytics & Reporting
Status: ❌ Not Started — blocked by Website + Ads
Goal: GA4 + GSC + Looker Studio dashboard live, client has visibility
Owner: Imad
Completion gate: Dashboard live, client can view anytime, weekly auto-report running

MODULE 5: Client Communication
Status: ✅ Active (ongoing)
Goal: Client always knows what's happening, zero uncertainty
Owner: Imad
Completion gate: Never closes — ongoing for the life of the engagement
```

### Cycles (2-week sprints)

```
CYCLE 1: Foundation  [2026-04-16 → 2026-04-30]
Goal: Website QA complete + launched on domain
Key issues:
  → Complete all open website issues (list below)
  → Domain configured + SSL active
  → GA4 + GTM installed + tracking verified
  → First Friday client update sent

CYCLE 2: Ads Launch  [2026-05-01 → 2026-05-15]
Goal: Google Ads live + tracking confirmed
Key issues:
  → Campaign setup complete (all QA checks pass)
  → Conversion tracking fires correctly (tested)
  → First 7 days monitored daily
  → Looker Studio dashboard live for client

CYCLE 3: Content Start  [2026-05-16 → 2026-05-31]
Goal: First 2 articles live + SEO audit done
Key issues:
  → Technical SEO audit complete (Screaming Frog)
  → 2 articles written, QA'd, published
  → GSC connected + articles submitted for indexing
  → Keyword matrix documented in Obsidian

CYCLE 4: Optimization  [2026-06-01 → 2026-06-30]
Goal: Ads optimized + 2 more articles + monthly report delivered
Key issues:
  → Ads optimization (search term report, bid adjustments)
  → 2 more articles live
  → First full monthly report delivered
  → Client satisfaction check: are they seeing leads?
```

### Issue Bank — RA-Project Website Module

All known website issues, ready to assign to Cycle 1:

```
WEBSITE ISSUES (Cycle 1)
─────────────────────────────────────────────────────
[ ] [webdev] Final page copy added — all placeholder text replaced
[ ] [webdev] All images optimized (WebP, < 200KB, alt text)
[ ] [webdev] Contact form tested — email received on submission
[ ] [webdev] Mobile: tested on iOS + Android (all pages)
[ ] [webdev] Browsers: Chrome, Firefox, Safari, Edge
[ ] [webdev] Core Web Vitals: LCP < 2.5s, CLS < 0.1 (all green)
[ ] [webdev] SSL active, no mixed content warnings
[ ] [webdev] Sitemap.xml at /sitemap.xml
[ ] [webdev] robots.txt configured
[ ] [webdev] 404 page exists and styled
[ ] [webdev] Domain configured + DNS propagated
[ ] [seo] Title tags + meta descriptions on all pages (< 60 + < 160 chars)
[ ] [seo] H1 on every page, keyword-targeted
[ ] [seo] GA4 property created + tracking code installed
[ ] [analytics] GTM container installed on site
[ ] [analytics] GA4 ↔ GTM connected + pageview tag firing
[ ] [analytics] GSC property created + site verified
[ ] [analytics] GSC sitemap submitted
[ ] [ads] Conversion action created in Google Ads
[ ] [ads] Conversion tag deployed via GTM
[ ] [ads] Test conversion fires correctly (mandatory before Cycle 2)
[ ] [admin] First Friday update sent to client
```

### Issue Bank — RA-Project Paid Ads Module

```
PAID ADS ISSUES (Cycle 2)
─────────────────────────────────────────────────────
[ ] [ads] [strategy] Competitor audit (SpyFu) — top 3 competitors, their keywords + copy
[ ] [ads] [strategy] Keyword research done (Google Keyword Planner + GSC)
[ ] [ads] [strategy] Campaign structure designed (campaigns, ad groups, keywords)
[ ] [ads] [strategy] Ad copy written — 3+ headlines + 2+ descriptions per ad group
[ ] [ads] [deliverable] Campaign built in Google Ads (paused — QA before live)
[ ] [ads] [deliverable] Negative keyword list — minimum 50 keywords added
[ ] [ads] [deliverable] Ad extensions set (sitelinks, callouts, call)
[ ] [ads] [deliverable] Budget cap set + bidding strategy configured
[ ] [ads] [deliverable] Geographic targeting confirmed with client
[ ] [qa] All 7 QA gate items pass (see Paid Ads department pipeline)
[ ] [ads] [deliverable] Campaigns set LIVE
[ ] [ads] First 4 hours monitored manually after launch
[ ] [analytics] Looker Studio dashboard created — GA4 + Google Ads connected
[ ] [analytics] Dashboard shared with client
```

---

## PROJECT 2: Agency-OS (Internal Operations)

**Status:** Active — runs in parallel with client work
**Goal:** Build and maintain the agency's internal operating system
**Cadence:** Rolling (no fixed cycles — use modules to organize)

### Modules

```
MODULE 1: Infrastructure Setup
Goal: Docker stack running, all v1 tools configured
Owner: Imad
One-time setup — close when done

MODULE 2: CEO OS
Goal: CEO rhythm active (daily + weekly review systems running)
Owner: Imad
Ongoing — never closes

MODULE 3: Finance
Goal: Invoice Ninja configured, all billing current
Owner: Imad
Ongoing — weekly review

MODULE 4: Department Buildout
Goal: Department pipelines and QA gates documented (in Obsidian)
Owner: Imad
Monthly — update as processes are proven
```

### Issue Bank — Infrastructure Setup Module

```
INFRASTRUCTURE ISSUES
─────────────────────────────────────────────────────
[ ] [ops] [setup] Clone/create agency-infra GitHub repo
[ ] [ops] [setup] Write v1 docker-compose.yml (Plane + Invoice Ninja only)
[ ] [ops] [setup] Write .env.example + create .env
[ ] [ops] [setup] docker compose up — Plane running at localhost:3000
[ ] [ops] [setup] Plane: create workspace + all 4 projects
[ ] [ops] [setup] Plane: configure states for all projects
[ ] [ops] [setup] Plane: create all department + type labels
[ ] [ops] [setup] Plane: import all RA-Project issues from this doc
[ ] [ops] [setup] Invoice Ninja running at localhost:8000
[ ] [ops] [setup] Invoice Ninja: configure company details + logo
[ ] [ops] [setup] Invoice Ninja: create RollandAssurance client record
[ ] [ops] [setup] Invoice Ninja: send/record deposit invoice
[ ] [ops] [setup] KeePassXC: create .kdbx with all agency categories
[ ] [ops] [setup] KeePassXC: migrate all credentials into correct groups
[ ] [ops] [setup] Obsidian: set up vault structure (see blueprint Part 2)
[ ] [ops] [setup] GitHub: create private agency-infra repo + push
```

### Issue Bank — CEO OS Module

```
CEO OS ISSUES
─────────────────────────────────────────────────────
[ ] [ops] Set up Obsidian daily note template (MITs + review fields)
[ ] [ops] Set up Obsidian weekly note template (CEO Weekly Review agenda)
[ ] [ops] First CEO Weekly Review written (this Sunday)
[ ] [ops] Daily rhythm locked in — first full day following schedule
[ ] [ops] Anki deck created — first cards for current skill track
[ ] [ops] OKRs set for Q2 2026 (April → June)
```

### Issue Bank — Finance Module

```
FINANCE ISSUES
─────────────────────────────────────────────────────
[ ] [admin] Invoice Ninja: deposit invoice created + sent (RollandAssurance)
[ ] [admin] Invoice Ninja: recurring monthly retainer configured (if applicable)
[ ] [admin] Obsidian P&L tracker created (MRR, expenses, net)
[ ] [admin] Weekly finance review cadence added to calendar
```

---

## PROJECT 3: BD-Pipeline (Business Development)

**Status:** INACTIVE — activate Month 2 after RA-Project first delivery
**Goal:** Build a steady flow of new qualified clients
**Activate trigger:** RollandAssurance is getting leads → you have a case study → you can sell

### When activated, this project tracks:

```
MODULE 1: Outreach
Issues = individual outreach sequences per prospect

MODULE 2: Active Deals
Issues = deals in pipeline (Prospect → Contacted → Qualified → Proposal → Closed)
Labels = pipeline stage
One issue per deal, updated as it moves

MODULE 3: Proposals
Issues = proposals in flight
Description = proposal link + client context

MODULE 4: Won Clients
Archive of won deals → becomes the top of RA-Project or new client project
```

### Issue Labels for BD (add when activating)

```
[prospect]     → Identified, not contacted
[contacted]    → Outreach sent, awaiting reply
[qualified]    → Discovery call done, budget confirmed
[proposal]     → Proposal sent
[negotiation]  → Back and forth on scope/price
[won]          → Closed → create new client project
[lost]         → Not now → add follow-up date
```

---

## PROJECT 4: Construction-SaaS

**Status:** INACTIVE — activate Month 4-8
**Goal:** Build and deliver the AI SaaS product for the construction company CEO
**Activate trigger:** RA-Project systematized → bandwidth exists → SaaS client ready

### When activated:

```
MODULE 1: Discovery & Architecture
MODULE 2: Core Build (2-week dev sprints)
MODULE 3: Integration & Testing
MODULE 4: Client Delivery & Handoff
MODULE 5: Maintenance (post-launch)
```

---

# PART 5 — DAILY WORKFLOW IN PLANE

```
MORNING (5 min, after CEO daily planning in Obsidian)
────────────────────────────────────────────────────────
1. Open Plane → RA-Project
2. Filter: "My Issues" + "Due Today" or "In Progress"
3. Identify your 3 MITs from the list
4. Write them in Obsidian daily note
5. Start working — update issue to "In Progress" when you start

DURING WORK
────────────────────────────────────────────────────────
- Move issues to "In Progress" when you start
- Move to "In Review" when your work is done, before QA
- Move to "Done" after QA passes + client approval (if applicable)
- Add comments to issues if context is needed later

EVENING (3 min, end of work day)
────────────────────────────────────────────────────────
1. Confirm issues you completed → status = Done
2. Review tomorrow's "Due" issues — are they realistic?
3. If something is blocked → add [blocker] label + describe what's blocking

FRIDAY (15 min, before client update)
────────────────────────────────────────────────────────
1. Open RA-Project → current cycle
2. What shipped this week? → include in client update
3. What's next week? → include in client update
4. Adjust next week's issues: priorities, due dates
5. Send client update (email template in Obsidian)
```

---

# PART 6 — CYCLE RHYTHM

```
CYCLE STRUCTURE
────────────────────────────────────────────────────────
Duration:       2 weeks (Monday → Sunday)
Planning:       Monday morning, 20 min
Review:         Sunday evening, 15 min (part of CEO Weekly Review)

PLANNING SESSION (Monday)
1. What is the cycle goal? (one sentence — what does "winning" this cycle look like?)
2. What issues from Backlog move to Todo for this cycle?
3. Are current In Progress issues realistic to finish?
4. Add due dates to everything in Todo

REVIEW SESSION (Sunday — part of CEO Weekly Review)
1. Cycle completion: how many issues Done vs. planned?
2. What blocked progress? (note in Obsidian)
3. What carries over to next cycle?
4. Start planning next cycle (takes 10 min after review)

HEALTHY CYCLE METRICS
├── > 70% of planned issues Done = good cycle
├── < 50% = something was wrong — diagnose before next cycle
└── > 90% = you under-loaded — push harder next cycle
```

---

# PART 7 — SETUP SEQUENCE (Day 1)

Run this in order. Estimated time: 2-3 hours.

```
HOUR 1: Docker + Plane
──────────────────────────────────────────────────────
[ ] 1. Create agency-infra folder + GitHub repo
[ ] 2. Write docker-compose.yml (Plane + Invoice Ninja only)
[ ] 3. Write .env.example → copy to .env → fill values
[ ] 4. docker compose up -d
[ ] 5. Open localhost:3000 → create Plane workspace
[ ] 6. Set workspace name + slug

HOUR 2: Plane Configuration
──────────────────────────────────────────────────────
[ ] 7. Create all 4 projects (RA-Project, Agency-OS, BD-Pipeline, Construction-SaaS)
[ ] 8. Configure states for each project (use Agency Standard set)
[ ] 9. Create all department labels (8 labels)
[ ] 10. Create all type labels (6 labels)
[ ] 11. Set BD-Pipeline and Construction-SaaS to inactive/archived

HOUR 3: Issue Import + First Cycle
──────────────────────────────────────────────────────
[ ] 12. RA-Project → Website Module: create all issues from bank above
[ ] 13. Assign all issues: you
[ ] 14. Set due dates: end of Cycle 1 (2026-04-30)
[ ] 15. Create Cycle 1: Foundation [2026-04-16 → 2026-04-30]
[ ] 16. Add all website issues to Cycle 1
[ ] 17. Agency-OS → Infrastructure Module: create all setup issues
[ ] 18. Mark today's 3 MITs as "In Progress"
[ ] 19. Write today's MITs in Obsidian → start working
```

---

# PART 8 — PLANE ISSUE NAMING CONVENTION

```
FORMAT: [DEPT] [ACTION] — [WHAT]

Examples:
  [ads] Setup — Google Ads conversion tracking via GTM
  [webdev] Fix — mobile layout breaks on iPhone SE
  [seo] Write — keyword matrix for insurance broker keywords
  [analytics] Create — Looker Studio dashboard for RA-Project
  [admin] Send — Friday client update Week 1
  [ops] Configure — Plane workspace states and labels

RULES
├── Always start with department label in brackets
├── Use action verbs: Setup / Create / Write / Fix / Review / Send / Configure / Test
├── Description field: context + what "Done" looks like (acceptance criteria)
└── Due date: always set one — "no due date" = won't get done
```

---

# PART 9 — ISSUE DESCRIPTION TEMPLATE

Use this for any issue that takes > 1 hour:

```markdown
## Context
[Why does this task exist? What happens if it's not done?]

## What needs to be done
[Specific steps, not vague instructions]

## Done when
[Exact acceptance criteria — how do you know it's complete?]

## Blockers
[Anything that needs to happen first, or anything that could block progress]

## Notes
[Any relevant links, docs, or context]
```

---

# PART 10 — PLANE AS CEO DASHBOARD

Every Monday morning, this is your 5-minute agency health check:

```
OPEN: RA-Project → Current Cycle
CHECK:
├── Issues "In Progress" → is this the right priority?
├── Issues "Due Today/This Week" → are they on track?
├── Issues "In Review" → what needs QA before it can ship?
└── Cycle progress bar → are we on track to hit the cycle goal?

RED FLAGS (investigate immediately if you see these):
├── 0 issues "In Progress" → something is wrong with your workflow
├── 5+ issues "In Progress" simultaneously → too many things open, pick 1
├── Any issue "In Progress" for > 3 days → it's stuck, diagnose it
└── Cycle < 50% done with 5 days left → reprioritize, cut scope
```
