# System Audit Report: Agency Master Blueprint

**Date:** 2026-04-16
**System type:** Technical Architecture + Business Process (hybrid)
**Lenses applied:** Waste, Complexity, Abstraction Bloat
**Audit passes:** 3

---

## System Health Assessment

**Overall verdict:** Premature Over-Engineering — requires scope reduction before first use

**Primary entropy source:** The blueprint was designed for a scaled agency and then applied to a 1-person, 1-client operation. Every tool and department is architecturally correct — but 70% of it belongs in v2 or v3. Activating it in full at v1 will recreate the exact productivity death loop the system was designed to escape.

---

## Findings by Lens

### Lens 1: Waste Audit

| Finding | Severity | Root Cause | Recommendation |
| --- | --- | --- | --- |
| Metabase requires live data pipelines to produce dashboards — nothing to connect at v1 | HIGH | No clients, no MRR data, no pipeline | Defer to Month 3+ |
| AppFlowy duplicates Obsidian — both manage docs/knowledge for the same person | HIGH | Over-engineered knowledge layer | Eliminate AppFlowy from v1; Obsidian handles everything |
| Documenso (e-signing) for 1 client who can sign a PDF by email | HIGH | Treating 1-client agency as enterprise | Defer — PDF + email works until Month 4+ |
| Uptime Kuma monitors production services — nothing deployed to monitor | HIGH | Nothing in production at v1 | Defer until VPS/production exists |
| n8n automation — processes don't exist yet, nothing repeatable to automate | MEDIUM | Automating work before it's manual-proven | Defer to Month 2-3, after first delivery cycle |
| Penpot (Docker + PostgreSQL + assets) vs. Figma free tier (zero setup) | MEDIUM | NIH bias toward local-first even when costly | Defer Penpot; use Figma free or skip design tools at v1 |
| Ollama + Open WebUI — AI chat locally, not required for client delivery | LOW | Nice-to-have infrastructure | Defer to Phase 2 |

### Lens 2: Complexity Audit

| Finding                                                    | Severity | Root Cause                                              | Recommendation                           |
| ---------------------------------------------------------- | -------- | ------------------------------------------------------- | ---------------------------------------- |
| 15+ Docker containers with 5 separate PostgreSQL instances | HIGH     | Each tool picked independently without counting DB cost | Strip to 3-4 containers max for v1       |
| Setup time 2-4 days before anything is stable and usable   | HIGH     | Complexity of inter-service dependencies                | v1 Docker = Plane only (1 tool, 1 job)   |
| Any container failure = debugging before you can work      | MEDIUM   | No clear critical path — all services treated as equal  | Separate must-run from nice-to-run       |
| .env.example with 40+ variables for v1                     | MEDIUM   | All services configured together                        | Reduce to 10-15 variables for Plane only |

### Lens 3: Abstraction Audit

| Finding | Severity | Root Cause | Recommendation |
| --- | --- | --- | --- |
| 6 departments fully documented when 2 are active right now | MEDIUM | Future-proof design applied immediately | KEEP the docs (right structure), defer the tools |
| Department 5 (Creative & Design) merged with Web Dev "at solo stage" — exists but doesn't | MEDIUM | Documentation bloat for inactive department | Mark as inactive in blueprint |
| Department 6 (Analytics) requires n8n automation — which isn't in v1 | MEDIUM | Cross-dependency between deferred tools | Simplify Dept 6 to: GSC + GA4 + Looker Studio only at v1 |
| 24-step client journey documented for acquisition that hasn't started | LOW | Correct to have — useful reference | Keep, but activate Phase 1 (delivery) first |

---

## Top Entropy Sources

1. **Docker Services Layer** — 15+ containers for 1-person operation kills setup velocity and creates daily maintenance burden — Impact: HIGH
2. **AppFlowy + Obsidian duplication** — Two knowledge systems for one person is guaranteed neglect of one, polluted workflow in both — Impact: HIGH
3. **Tools requiring data that doesn't exist** (Metabase, n8n, Uptime Kuma) — Zero-value infrastructure that costs real setup time — Impact: HIGH

---

## Optimization Directive

### Phase 1 — v1 Stack (activate NOW, this week)

**Docker (run locally — agency-infra repo):**
- [x] **Plane** — project + task management (Plane-web + Plane-api + Plane-db + Plane-redis = 4 containers, 1 purpose)
- [x] **Invoice Ninja** — invoicing from day 1 (Invoice-ninja + Invoice-ninja-db = 2 containers)

**Desktop apps (install once, no Docker needed):**
- [x] Obsidian — knowledge, daily notes, CEO OS, everything
- [x] KeePassXC — credential security
- [x] VS Code — code editor
- [x] Anki — skill compounding
- [x] Thunderbird — email

**External tools (zero setup beyond account creation):**
- [x] GitHub — code + version control
- [x] Google Ads + GA4 + GTM + GSC + Looker Studio — client delivery stack (free, required)
- [x] Ahrefs Starter (€29/mo) — only subscribe when actively doing SEO work

**v1 Docker Compose: 6 containers total. Everything works on Day 1.**

---

### Phase 2 — Month 2-3 (after first client delivered)

Activate when: RollandAssurance is getting leads and the first delivery cycle is complete.

- [ ] **n8n** — automate what you've already done manually at least 3x
- [ ] **AppFlowy** — REPLACE with enhanced Obsidian structure OR activate only for polished playbook docs (one system, not two)
- [ ] **Penpot** — activate if doing regular UI/UX design work (not for 1-2 sites/year)

---

### Phase 3 — Month 4-8 (AI SaaS project activation)

Activate when: Construction SaaS project is starting.

- [ ] **Supabase** (via Supabase CLI, per-project) — database for SaaS builds
- [ ] **Ollama + Open WebUI** — local AI for SaaS development and prompt engineering
- [ ] **Metabase** — connect to Supabase for agency internal dashboards

---

### Phase 4 — Month 8+ (when team grows beyond solo)

- [ ] **Documenso** — e-signing when client volume makes PDF workflow annoying
- [ ] **Uptime Kuma** — monitoring when you have a production server with clients depending on uptime

---

### Eliminated (not deferred — dropped entirely from all phases)

| Item | Reason |
| --- | --- |
| Vaultwarden | KeePassXC solves the same problem locally without a server. Two credential tools = security risk, not improvement. |
| Formbricks | Client briefs can be Google Forms or a Notion form. Formbricks adds a Docker service for a use case that doesn't need one. |
| Cal.com | Until you're booking 5+ calls/week, Google Calendar + direct scheduling works. |
| Separate Penpot PostgreSQL | Folded into Plane's DB if Penpot ever activated — or Penpot uses its own SQLite. Don't run a DB just for design. |

---

## v1 Final Tool Stack (Complete Reference)

```
DOCKER (agency-infra repo)
├── Plane           → Project & task management   [localhost:3000]
│   ├── plane-db    → PostgreSQL for Plane
│   └── plane-redis → Redis for Plane
└── Invoice Ninja   → Invoicing + finance         [localhost:8000]
    └── invoice-db  → MySQL for Invoice Ninja

DESKTOP (install, no containers)
├── Obsidian        → CEO OS, knowledge, daily notes
├── KeePassXC       → Credentials + secrets
├── VS Code         → Code editor
├── Anki            → Daily skill compounding
└── Thunderbird     → Email client

EXTERNAL (account creation only)
├── GitHub          → Code + version control (free)
├── Google Ads      → Client campaign management (free to use)
├── Google Analytics 4 → Conversion tracking (free)
├── Google Tag Manager → Tag deployment (free)
├── Google Search Console → SEO data (free)
├── Google Looker Studio  → Client dashboards (free)
└── Ahrefs Starter  → SEO research (€29/mo — subscribe when needed)

TOTAL DOCKER CONTAINERS: 6
TOTAL MONTHLY COST: €0 until SEO work begins, then €29/mo
SETUP TIME: Half a day, not 4 days
```

---

## Expected Outcomes

After executing this directive:

- **Setup time:** 4 days → 4-6 hours (Day 1 operational)
- **Daily maintenance burden:** 15+ containers → 6 containers (60% reduction)
- **Cognitive load:** "What tool do I use for this?" → one clear answer per function
- **First-day paralysis risk:** Eliminated — Plane is running in 30 minutes
- **Path to v2:** Each deferred tool has a clear activation trigger (not a date, a condition)
- **Revenue risk eliminated:** No more "I need to set up infrastructure before I can work" — the work IS the infrastructure for v1

**The directive:** Run Plane + Invoice Ninja in Docker. Run everything else as desktop apps or external tools. Build the machine that gets the RA-Project delivering leads. The rest of the blueprint is correct — it's just not for today.
