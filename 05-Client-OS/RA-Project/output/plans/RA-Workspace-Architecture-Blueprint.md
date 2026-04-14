# ROLLAND ASSURANCES — WORKSPACE ARCHITECTURE BLUEPRINT
## Lead Generation Ecosystem — Full Project Workspace Initialization
### Version 1.0 | 2026-04-13 | Drafted in Party Mode Session

---

## PURPOSE OF THIS DOCUMENT

This document defines the complete folder structure and workspace architecture for the Rolland Assurances lead generation project — from the first day of research to the fully automated, scaled acquisition machine. Every folder in this structure has a reason, an owner, and a defined role within the ecosystem. Nothing is arbitrary.

This blueprint governs WHERE every piece of work lives: research, strategy, production assets, automation code, performance data, and agent outputs. It is the skeleton on which the entire project is built.

The workspace is organized around the 3 core systems of the ecosystem:

1. **Intelligence System** — the nervous system that feeds the machine
2. **SLM Acquisition Machine** — the operating system that converts strangers into calls
3. **Automation System** — the deployment interface that removes manual execution

Before any system runs, a **Foundation** layer must be established. This is Zone A — no spend, no campaigns, no production until this layer is complete.

---

## ARCHITECTURE OVERVIEW

```
RA-Project/
│
├── 00-foundation/
├── 01-intelligence/
├── 02-slm-machine/
├── 03-automation/
│
├── Ressources/                 (keep — raw source material)
├── output/                     (keep — agent output dump)
├── google-ads-api-developer-assistant/   (keep — API reference submodule)
├── docs/                       (keep — skill and workflow documentation)
├── logs/                       (keep — agent execution logs)
└── Notes/                      (keep — freeform working notes)
```

The top-level numbering (`00`, `01`, `02`, `03`) enforces execution order. You cannot work on `01-intelligence` before `00-foundation` is complete. You cannot deploy `02-slm-machine` before `01-intelligence` has produced its first outputs. You cannot use `03-automation` before `02-slm-machine` is live. The folder names are a reminder of the dependency chain.

---

## 00-FOUNDATION
### Prerequisites — The Hard Gates (Zone A)

**Purpose:** Everything in this folder must exist and be verified before a single euro is spent. The foundation is not optional, not a formality — it is the precondition for the machine to work at all. Missing any Zone A item means campaigns will fail silently, conversions won't be tracked, and optimization will be blind.

**Status logic:** Each item in this folder should have a clear `✅ Done` / `❌ Missing` / `⏳ In Progress` status tracked at the top of its file.

```
00-foundation/
│
├── credentials/
│   ├── google-ads-account.md           (Account ID, MCC link, billing setup)
│   ├── google-ads-api.md               (Developer token, OAuth credentials, customer ID)
│   ├── google-analytics.md             (GA4 property ID, measurement ID)
│   └── README.md                       (Status tracker — all A3–A11 gates)
│
├── tracking/
│   ├── call-conversion-setup.md        (≥60s call = conversion — config instructions)
│   ├── google-number-transfer.md       (Google forwarding number setup)
│   ├── ga4-google-ads-link.md          (GA4 ↔ Google Ads linking steps)
│   ├── gtm-installation.md             (Google Tag Manager — site installation)
│   └── conversion-testing.md           (How to verify tracking is firing correctly)
│
└── legal/
    ├── orias-compliance.md             (ORIAS number — must appear on both landing pages)
    ├── financial-advertiser-verify.md  (Google's financial services verification — 2–7 days)
    └── google-business-profile.md      (GBP creation and verification — recommended)
```

**Zone A Gate Checklist (nothing deploys until all ✅):**

| Gate | Item | Blocking? |
|------|------|-----------|
| A3 | Google Ads account created | YES |
| A4 | Financial services advertiser verification approved | YES — 2–7 days |
| A5 | Call conversion tracking (≥60s) activated | YES |
| A6 | Google Number Transfer enabled | YES |
| A7 | GA4 ↔ Google Ads linked | YES |
| A8 | Google Tag Manager installed on site | YES |
| A9 | Google Business Profile created + verified | Recommended |
| A10 | ORIAS number on both landing pages | Legal requirement |
| A11 | Real phone number in create_rolland_campaigns.py | YES |

**Owner:** Rolland (A3, A4, A9, A10) + Technical/Dev (A5, A6, A7, A8, A11)

---

## 01-INTELLIGENCE
### The Nervous System — Runs Continuously, Feeds the Entire Machine

**Purpose:** The Intelligence System is the only system in the ecosystem that runs before the machine starts AND after it starts. It has two distinct sub-systems with different inputs, different processing logic, and different outputs. They must never be confused with each other — they solve different problems.

**Critical distinction:**
- **SS1 (Market)** = What is the market doing? Informs WHAT to say and WHO to target.
- **SS2 (Performance)** = What are WE doing? Informs WHAT to change and HOW to optimize.

Confusing these two produces the most common mistake in paid acquisition: changing targeting when the problem is the landing page, or rewriting copy when the problem is the bid strategy.

```
01-intelligence/
│
├── SS1-market/
│   ├── avatars/
│   │   ├── avatar-A-senior.md          (Le Retraité Surpayé — full psychological profile)
│   │   ├── avatar-B-btp.md             (L'Artisan BTP Bloqué — full psychological profile)
│   │   └── avatar-research-log.md      (Verbatim quotes from forums, communities, reviews)
│   │
│   ├── competitors/
│   │   ├── serp-audit-senior.md        (Who is advertising on our Senior keywords?)
│   │   ├── serp-audit-decennale.md     (Who is advertising on our Décennale keywords?)
│   │   ├── competitor-ad-angles.md     (What headlines, descriptions, CTAs are they using?)
│   │   ├── competitor-lp-audit.md      (Three Tens audit of competitor landing pages)
│   │   └── competitive-gaps.md         (Angles they are NOT covering = our opportunity)
│   │
│   ├── keywords/
│   │   ├── intent-map-senior.md        (Commercial / informational / navigational split)
│   │   ├── intent-map-decennale.md     (Same — BTP segment)
│   │   ├── volume-analysis.md          (Monthly search volume per keyword group)
│   │   ├── negative-keywords-master.md (Master negative keyword library — maintained)
│   │   └── keyword-research-log.md     (Raw keyword data, Keyword Planner exports)
│   │
│   └── seasonality/
│       ├── chatel-window-calendar.md   (Nov–Jan rate increase notification window)
│       ├── btp-peaks-calendar.md       (BTP contract seasons, construction activity peaks)
│       └── annual-campaign-calendar.md (Full year — when to push, when to reduce, when to test)
│
└── SS2-performance/
    ├── directives/
    │   └── YYYY-MM-DD-directive.md     (Weekly optimization directive — naming convention)
    │
    ├── diagnostics/
    │   └── YYYY-MM-DD-diagnostic.md    (3-layer diagnostic report — Hook / Body / CTA)
    │
    └── kpi/
        ├── weekly-kpi-log.md           (Rolling weekly KPI tracker — all campaigns)
        └── monthly-audit-log.md        (Monthly financial audit — Felix's domain)
```

### SS1 — Market Intelligence (External)

**Cadence:** Deep research at launch → Quarterly refresh → Triggered review when CPL degrades or new competitor appears.

**Owner:** Analyst (keyword research, intent mapping, avatar language) + CEO (competitive gaps, offer positioning)

**Output feeds:** Avatar profiles → ad copy angles → keyword strategy → offer positioning → competitive gap exploitation

### SS2 — Performance Feedback Loop (Internal)

**Cadence:** Daily check (first 30 days) → Weekly review → Monthly deep audit

**Owner:** Trace (weekly directive, 3-layer diagnostic, negative keyword expansion) + Felix (monthly financial audit, scaling decisions)

**Output feeds:** Weekly Optimization Directive with exactly 4 verdicts:
1. What to **kill** (pause ads, keywords, or groups)
2. What to **keep** (leave unchanged, let data accumulate)
3. What to **scale** (increase budget or bid — requires Felix gate approval)
4. What to **test next** (new angle, new keyword, new ad variant)

### Naming Convention for SS2 Files

All directive and diagnostic files use the format `YYYY-MM-DD-[type].md`:
- `2026-05-05-directive.md`
- `2026-05-05-diagnostic-senior-ctr.md`

This is non-negotiable. When you have 52 weekly directives, chronological sort is the only thing that keeps it readable.

---

## 02-SLM-MACHINE
### The Operating System — 4 Layers, One Purpose

**Purpose:** The SLM Acquisition Machine is the complete system that governs how Rolland Assurances attracts, persuades, and converts. This folder contains the finalized, approved production assets that are actually deployed — not drafts. Drafts live in `output/`. Everything in `02-slm-machine/` has passed review and is either live or ready to deploy.

**The single purpose of this machine:**
> Convert strangers with a problem into qualified phone calls for Rolland Assurances, at a cost that makes the business profitable and scalable.

```
02-slm-machine/
│
├── persuasion-core/
│   ├── three-tens-framework.md         (Three Tens applied to RA — Product/Person/Company)
│   ├── threshold-system.md             (Pain Threshold + Action Threshold protocols)
│   ├── straight-line-structure.md      (SLP applied to landing pages and call scripts)
│   └── three-tens-audits/
│       ├── audit-sante-senior-lp.md    (Three Tens audit of /landing/sante-senior)
│       └── audit-decennale-lp.md       (Three Tens audit of /landing/garantie-decennale)
│
├── traffic/
│   ├── campaign-structure-overview.md  (Full campaign architecture — settings, budgets, schedule)
│   ├── senior/
│   │   ├── S1-changement-mutuelle.md   (Ad group — keywords, match types, bids)
│   │   ├── S2-urgence-soins.md         (Ad group — keywords, match types, bids)
│   │   └── S3-hausse-chatel.md         (Ad group — keywords, match types, bids)
│   └── decennale/
│       ├── D1-urgence-attestation.md   (Ad group — highest intent — keywords, bids)
│       ├── D2-creation-premiere.md     (Ad group — keywords, match types, bids)
│       ├── D3-changement-prix.md       (Ad group — keywords, match types, bids)
│       └── D4-profils-complexes.md     (Ad group — keywords, match types, bids)
│
├── content/
│   ├── hooks/
│   │   ├── senior/
│   │   │   ├── hook-library-senior.md  (All approved hooks for Avatar A, organized by pain point)
│   │   │   └── ctr-log-senior.md       (Hook performance tracking — CTR per hook)
│   │   └── decennale/
│   │       ├── hook-library-decennale.md  (All approved hooks for Avatar B, organized by pain point)
│   │       └── ctr-log-decennale.md       (Hook performance tracking — CTR per hook)
│   │
│   ├── ads/
│   │   ├── senior/
│   │   │   ├── headlines-senior-v1.md  (4 angles × 3 headline variants = 12 headlines)
│   │   │   └── descriptions-senior.md  (Approved description copy)
│   │   └── decennale/
│   │       ├── headlines-decennale-v1.md
│   │       └── descriptions-decennale.md
│   │
│   └── organic/
│       ├── content-strategy-senior.md  (5-Category Matrix for Senior segment — Month 2+)
│       ├── content-strategy-decennale.md (5-Category Matrix for Décennale — Month 2+)
│       └── content-calendar.md         (Production calendar — both segments, all categories)
│
├── funnels/
│   ├── senior/
│   │   ├── lp-copy-sante-senior.md     (Full landing page copy — SLP structure)
│   │   └── lp-audit-sante-senior.md    (Three Tens + Threshold audit results)
│   └── decennale/
│       ├── lp-copy-decennale.md        (Full landing page copy — SLP structure)
│       └── lp-audit-decennale.md       (Three Tens + Threshold audit results)
│
├── conversion/
│   ├── call-script-senior.md           (SLP call script for Senior leads)
│   ├── call-script-decennale.md        (SLP call script for Décennale leads)
│   ├── objection-handling.md           (Common objections + SLP responses per avatar)
│   └── close-rate-tracker.md           (Close rate per segment — feeds SS2 performance loop)
│
└── looping/
    ├── rlsa-strategy.md                (RLSA audience setup — Month 2+)
    ├── retargeting-campaign.md         (Display retargeting structure — Month 2+)
    └── email-nurture-sequence.md       (SLP-structured email sequence — Month 3+)
```

### Folder Ownership by Agent

| Folder | Primary Owner | Supporting |
|--------|--------------|------------|
| `persuasion-core/` | CEO | Coda, Analyst |
| `traffic/` | Dev (deployment) | CEO, Felix |
| `content/hooks/` | Aura | Trace (CTR tracking) |
| `content/ads/` | Aura | Coda, Vera (compliance) |
| `content/organic/` | Coda | Aura |
| `funnels/` | Coda + Aura | CEO (Three Tens audit) |
| `conversion/` | Rolland | CEO (SLP framework) |
| `looping/` | CEO + Aura | Coda |

### The `output/` vs `02-slm-machine/` Distinction

This is critical to understand and must never be confused:

| `output/` | `02-slm-machine/` |
|-----------|-------------------|
| Raw agent drafts and brainstorm dumps | Approved, finalized production assets |
| Work in progress — iterations welcome | Stable — only updated after review |
| Where CAI agents write first | Where approved work lands after sign-off |
| Disorganized by nature | Organized by deployment purpose |
| Not referenced by campaigns | Referenced directly by live campaigns |

**The workflow:** Agent produces draft → lands in `output/` → reviewed → approved → copied/moved to `02-slm-machine/` → deployed.

### Layer Logic Reminder

```
Layer 4 — Meta-Rules      (strategic guardrails — lives in persuasion-core/)
    ↓ governs
Layer 1 — Persuasion Core (psychology — Three Tens, Threshold, SLP)
    ↓ executes through
Layer 2 — Execution Engine (traffic + content + funnels + conversion + looping)
    ↓ powered by
Layer 3 — Intelligence    (= 01-intelligence/ — feeds all layers continuously)
```

---

## 03-AUTOMATION
### The Deployment Interface — Google Ads API

**Purpose:** The automation system sits between the Execution Engine and the live Google Ads account. It is NOT a standalone system — it is the CLI that pushes the SLM machine live, pulls performance data back, and eventually automates optimization decisions that are currently made manually.

**Position in ecosystem:** A tool inside Layer 2 (Traffic System). It accelerates deployment and reporting. It does not define strategy — it executes it.

```
03-automation/
│
├── v1-deployment/
│   ├── create_rolland_campaigns.py     (moved from Ressources/ — campaign creation script)
│   ├── campaign-config.yaml            (campaign parameters — phone number, budgets, bids)
│   ├── deployment-log.md               (record of each deployment — date, changes, result)
│   └── README.md                       (how to run the script, prerequisites, troubleshooting)
│
├── v2-reporting/                       (Planned — Month 1)
│   ├── performance-report.py           (pulls CPL, CTR, call volume from Google Ads API)
│   ├── alarm-detection.py              (flags CPL > target, CTR < 3%, zero impressions)
│   ├── report-config.yaml              (thresholds, alert targets, report schedule)
│   └── README.md
│
└── v3-advanced/                        (Future — Month 3+)
    ├── auto-bid-rules.py               (auto-adjusts bids based on performance rules)
    ├── negative-keyword-expander.py    (adds negatives from search term report automatically)
    ├── ab-test-manager.py              (A/B test rotation management)
    └── README.md
```

### Automation Roadmap

```
CURRENT STATE — v1 (create_rolland_campaigns.py)
├── Creates campaigns, ad groups, keywords, ads via CLI
├── Pushes complete campaign structure in one command
└── Status: Built. Needs: credentials + real phone number to deploy.

NEXT STATE — v2 (Month 1 priority)
├── Reads performance data from Google Ads API
├── Generates weekly performance report (CPL, CTR, call volume)
├── Flags alarm signals automatically (CPL > target, CTR < 3%)
└── Proposed: auto-pauses underperforming ad groups after threshold breach

FUTURE STATE — v3 (Month 3+)
├── Auto-adjusts bids based on performance rules
├── Adds negative keywords from search term report automatically
└── A/B test rotation management
```

**Owner:** Dev for all v1/v2/v3 implementation. Felix + CEO for threshold and rule definition.

---

## EXISTING STRUCTURE — WHAT STAYS

### `Ressources/`

**Keep as-is.** This is the raw source material library — documents, PDFs, frameworks that inform the work but are not production outputs.

```
Ressources/
├── CLICK-TO-CALL-GoogleAds-RollandAssurances.md   (Google Ads click-to-call reference)
├── Rolland_Assurances_Strategy_Report.pdf          (original strategy document)
└── Straight-Line-Marketing/
    └── SLM-Ecosystem-Map.md                        (SLM framework reference)
```

**Note:** `create_rolland_campaigns.py` moves FROM here TO `03-automation/v1-deployment/`. Everything else stays.

### `output/`

**Keep and maintain.** This is the agent output dump — where CAI agents write first-draft outputs before review. It is intentionally less structured because creative work is non-linear.

```
output/
├── plans/          (ecosystem maps, strategic plans, blueprints)
├── ads/            (first-draft ad copy from Aura — pre-approval)
├── content/        (first-draft content from Coda — pre-approval)
├── reports/        (performance reports, audits — raw from Trace and Felix)
└── knowledge/
    ├── audits/
    ├── cross-domain-syntheses/
    ├── first-principles-blueprints/
    └── stress-tests/
```

### `google-ads-api-developer-assistant/`

**Keep as-is.** This is a Git submodule — the official Google Ads API developer assistant toolkit. It serves as the reference library for building and debugging the automation scripts in `03-automation/`. Do not modify files in this folder.

### `docs/`

**Keep as-is.** Contains CAI skill index, workflow maps, and getting-started guides for the agent system.

### `logs/`

**Keep as-is.** Agent execution logs (mgi-adversarial-designer, mgi-first-principles, mgi-system-auditor). Auto-generated — do not manually edit.

### `Notes/`

**Keep as-is.** Freeform working notes — the scratch pad. Anything that doesn't fit elsewhere lands here first.

---

## WHAT MOVES

| Current Location | New Location | Reason |
|-----------------|-------------|--------|
| `credentials/` (root) | `00-foundation/credentials/` | Belongs in foundation layer |
| `Ressources/create_rolland_campaigns.py` | `03-automation/v1-deployment/` | It's automation code, not a resource |

---

## EXECUTION ORDER PROTOCOL

The folder numbering is the execution protocol. Work flows in this order:

```
00-foundation  →  All Zone A gates complete
      ↓
01-intelligence/SS1-market  →  Research before spend (Zone B)
      ↓
02-slm-machine/persuasion-core  →  Frameworks locked before copy is written
      ↓
02-slm-machine/traffic  +  02-slm-machine/content  →  Parallel (Zone C + Zone D)
      ↓
03-automation/v1-deployment  →  Deploy when everything above is ready (Zone C)
      ↓
01-intelligence/SS2-performance  →  Activates after launch (Zone E — ongoing)
      ↓
03-automation/v2-reporting  →  Automate what's working manually (Zone F)
      ↓
02-slm-machine/looping  +  03-automation/v3-advanced  →  Scale and loop (Zone G)
```

---

## NAMING CONVENTIONS

Consistent naming across the entire workspace prevents confusion and makes agent handoffs clean.

| File Type | Convention | Example |
|-----------|-----------|---------|
| Weekly directives | `YYYY-MM-DD-directive.md` | `2026-05-05-directive.md` |
| Diagnostics | `YYYY-MM-DD-diagnostic-[topic].md` | `2026-05-12-diagnostic-senior-ctr.md` |
| KPI snapshots | `YYYY-MM-DD-kpi-[period].md` | `2026-05-31-kpi-monthly.md` |
| Ad copy versions | `[segment]-[type]-v[N].md` | `senior-headlines-v2.md` |
| Audit files | `audit-[subject]-[date].md` | `audit-sante-senior-lp-2026-04.md` |
| Hook libraries | `hook-library-[segment].md` | `hook-library-decennale.md` |

---

## WORK BREAKDOWN STRUCTURE — FOLDER MAPPING

Each WBS Zone from the Ecosystem Map maps directly to a workspace folder:

| WBS Zone | Workspace Folder | Cadence |
|----------|-----------------|---------|
| Zone A — Foundation | `00-foundation/` | Once (before launch) |
| Zone B — Market Intelligence | `01-intelligence/SS1-market/` | Launch + Quarterly |
| Zone C — Campaign Execution | `02-slm-machine/traffic/` + `03-automation/v1-deployment/` | Week 1 |
| Zone D — Ad Production | `02-slm-machine/content/` | Week 1–2, then ongoing |
| Zone E — Performance Loop | `01-intelligence/SS2-performance/` | Weekly, from day 1 post-launch |
| Zone F — Automation Expansion | `03-automation/v2-reporting/` + `v3-advanced/` | Month 1–3 |
| Zone G — Looping System | `02-slm-machine/looping/` | Month 2–3 |

---

## FINANCIAL GUARDRAILS — FELIX'S SCALING GATES

These gates are documented here because they govern which workspace folders get activated in sequence. No folder is activated early.

```
GATE 1 — Validation Gate
  Condition: ≥30 conversions on a campaign
  Action: Switch from "Maximize Conversions" to "Target CPA" bidding
  Unlocks: Felix's scaling analysis in SS2-performance/

GATE 2 — Scaling Gate
  Condition: CPL < target × 0.8 consistently over 2 weeks
  Action: Increase budget 20–30%
  Unlocks: Budget increase directive in SS2-performance/directives/

GATE 3 — Kill Gate
  Condition: CPL > target × 1.5 after 30 days
  Action: Pause group → run 3-layer diagnostic → revise or kill
  Activates: SS2-performance/diagnostics/ + Trace-led investigation

GATE 4 — Profitability Gate
  Condition: LTGP:CAC > 3x before any significant scale
  Formula: (Commission × Close Rate × LTV multiplier) ÷ CPL > 3
  Unlocks: 03-automation/v3-advanced/ and 02-slm-machine/looping/
```

**CPL Targets:**
- Senior Mutuelle: < 35€ (Phase 1) → < 22€ (Phase 2)
- BTP Décennale: < 55€ (Phase 1) → < 35€ (Phase 2)

---

## STATUS TRACKING PROTOCOL

Each major folder should contain a `README.md` or `_status.md` file with:
- Current status (Not Started / In Progress / Complete)
- Owner
- Blocking dependencies
- Last updated date

This allows any agent or team member to open any folder and immediately understand what state it's in without reading every file inside it.

---

*This document supersedes any prior informal notes on workspace structure. When in doubt about where something belongs, consult this blueprint. When this blueprint is wrong or incomplete, update it here — not in your head.*
