# 02-SLM-MACHINE
## The Operating System — The Complete Acquisition Machine

---

## PURPOSE

The SLM Acquisition Machine is the core of everything. It is the system that governs how Rolland Assurances attracts, persuades, and converts strangers into qualified phone calls. It is not a collection of tactics — it is one unified machine with four layers, each governing a specific function.

**The machine has exactly one purpose:**
> Convert strangers with a problem into qualified phone calls for Rolland Assurances, at a cost that makes the business profitable and scalable.

Every file in this folder exists to serve that purpose. If it doesn't move someone closer to a phone call, it doesn't belong here.

---

## THE CRITICAL DISTINCTION: THIS FOLDER vs `output/`

This is the most important rule about this folder:

| `output/` | `02-slm-machine/` |
|-----------|-------------------|
| Raw agent drafts — work in progress | Approved, finalized production assets |
| Iterations welcome — messy by design | Stable — only updated after review |
| Where CAI agents write first | Where approved work lands after sign-off |
| Not referenced by live campaigns | Referenced directly by live campaigns |

**The workflow:**
Agent produces draft → lands in `output/` → reviewed and approved → moved/copied to `02-slm-machine/` → deployed to live campaigns or landing pages.

Nothing goes live from `output/` directly. Everything must pass through this folder first.

---

## THE 4-LAYER ARCHITECTURE

```
LAYER 4 — META-RULES
  Strategic governing principles — set once, never violated
  Lives in: persuasion-core/ (as framework documentation)
      ↓ governs all layers below

LAYER 1 — PERSUASION CORE
  The psychology layer — governs ALL messaging across the machine
  Lives in: persuasion-core/
      ↓ executes through

LAYER 2 — EXECUTION ENGINE
  Where the actual work happens — 5 sub-systems
  Lives in: traffic/ + content/ + funnels/ + conversion/ + looping/
      ↓ powered by

LAYER 3 — INTELLIGENCE LOOP
  = The 01-intelligence/ folder — feeds everything continuously
```

---

## FOLDER STRUCTURE

```
02-slm-machine/
│
├── persuasion-core/            Layer 1 + Layer 4 — psychology and meta-rules
│   └── three-tens-audits/      Audit results for each landing page
│
├── traffic/                    Layer 2A — Google Ads campaign structure
│   ├── senior/                 Campaign SENIOR — Mutuelle Santé (750€/month)
│   └── decennale/              Campaign DÉCENNALE — Garantie BTP (750€/month)
│
├── content/                    Layer 2B — All ad and organic content production
│   ├── hooks/                  Hook library per avatar and pain point
│   │   ├── senior/
│   │   └── decennale/
│   ├── ads/                    Finalized ad copy — headlines and descriptions
│   │   ├── senior/
│   │   └── decennale/
│   └── organic/                5-Category Topic Matrix outputs (Month 2+)
│
├── funnels/                    Layer 2C — Landing page copy
│   ├── senior/                 /landing/sante-senior
│   └── decennale/              /landing/garantie-decennale
│
├── conversion/                 Layer 2D — Call scripts and close protocols
└── looping/                    Layer 2E — Retargeting, RLSA, email (Month 2–3+)
```

---

## SUBFOLDERS IN DETAIL

### `persuasion-core/`
The psychological foundation that governs every word written anywhere in the machine. No copy is written, no landing page built, no ad deployed without satisfying these frameworks.

**Three Tens Framework** — the 3 certainties every prospect must feel before calling:
1. **1st Ten (Product)** — "This is the best solution for my problem"
2. **2nd Ten (Person)** — "I trust Rolland — he is on my side"
3. **3rd Ten (Company)** — "Rolland Assurances is legitimate and established"

**Threshold System** — two psychological barriers that must be crossed before any CTA:
- **Pain Threshold** — the prospect's felt problem must be amplified to the point where NOT acting is more painful than acting
- **Action Threshold** — the barrier to calling must be lowered until the effort feels near-zero

**Straight-Line Structure** — the sequence applied to landing pages and call scripts:
Open → Rapport → Intelligence Gathering → Presentation → Objection Handling → Close

**`three-tens-audits/`** — after every landing page version, an audit is run here to confirm all three tens are present and strong.

### `traffic/`
The Google Ads campaign structure — what lives in the account, how it's organized, what settings are used.

**Campaign SENIOR — Mutuelle Santé Sénior** (`senior/`)
Budget: 750€/month | Daily: 34.10€
- `S1-changement-mutuelle/` — Intent: switching insurance provider
- `S2-urgence-soins/` — Intent: not enough reimbursements, prescription costs
- `S3-hausse-chatel/` — Intent: received rate increase letter (Loi Châtel window — peak season)

**Campaign DÉCENNALE — Garantie Décennale BTP** (`decennale/`)
Budget: 750€/month | Daily: 34.10€
- `D1-urgence-attestation/` — Intent: needs certificate NOW, job site waiting (highest intent)
- `D2-creation-premiere/` — Intent: new business, first policy
- `D3-changement-prix/` — Intent: switching insurer or finding better price
- `D4-profils-complexes/` — Intent: refused elsewhere, complex profile

**Global settings for both campaigns:**
- Search Network Only (no Display)
- Call-Only Ads format
- Ad schedule: Mon–Fri 09:00–18:30
- Device bids: Mobile +40%, Tablet -30%
- Conversion tracking: Calls ≥60s = 1 conversion

### `content/`
All production content — what gets seen by prospects. Split into paid (hooks + ads) and organic (Month 2+).

**`hooks/`** — The hook is the only thing that exists before attention is earned. Hooks live here organized by avatar and pain point. Each hook has a tested CTR logged next to it. Only hooks that have proven CTR > target graduate to the main hook library.

- `senior/hook-library-senior.md` — Approved hooks for Avatar A, by pain point
- `decennale/hook-library-decennale.md` — Approved hooks for Avatar B, by pain point
- CTR logs sit next to each library — performance is tracked from day 1

**`ads/`** — Finalized, approved ad copy.
- Headlines: 4 angles × 2 offers = 8 headline sets. 3 variants per set = 24 headlines minimum.
- Descriptions: Supporting copy that builds the Three Tens and lowers the action threshold.

**`organic/`** — Activated Month 2+. Content calendar and 5-Category Topic Matrix outputs.
The 5 categories: Educate / Inspire / Relate / Entertain / Convert
One matrix per segment (Senior + Décennale). All content maps to a pipeline stage.

### `funnels/`
The two landing pages that are the **only conversion points** in the entire ecosystem. All traffic flows to one of these two URLs. Nothing else matters until someone calls.

- `/landing/sante-senior` — Senior segment
- `/landing/garantie-decennale` — Décennale segment

Each page must satisfy the full SLP structure:
Hook (≤4 seconds) → Pain Amplification → Solution Presentation (Three Tens) → Proof → Objection Handling → CTA (only after both thresholds are crossed)

### `conversion/`
What happens on the call — Rolland's domain. This folder contains:
- Call scripts structured on the Straight Line (Open → Intelligence Gathering → Presentation → Objection Handling → Close)
- Objection handling library per avatar (common objections + SLP responses)
- Close rate tracker — feeds directly back to SS2 performance loop

### `looping/`
How we re-engage people who didn't convert on first touch. Activated Month 2–3+:
- **RLSA** — bid higher when previous visitors search again
- **Display Retargeting** — show ads to people who visited landing pages but didn't call
- **Email Nurture** — requires lead capture form — SLP-structured sequence that builds Three Tens over time

---

## AGENT OWNERSHIP

| Folder | Primary Owner | Supporting |
|--------|--------------|------------|
| `persuasion-core/` | CEO | Coda, Analyst |
| `traffic/` | Dev (deployment) | CEO, Felix |
| `content/hooks/` | Aura | Trace (CTR tracking) |
| `content/ads/` | Aura | Coda, Vera (compliance check) |
| `content/organic/` | Coda | Aura |
| `funnels/` | Coda + Aura | CEO (Three Tens audit) |
| `conversion/` | Rolland | CEO (SLP framework) |
| `looping/` | CEO + Aura | Coda |

---

## FINANCIAL MODEL

| Segment | Monthly Budget | CPL Target Ph.1 | CPL Target Ph.2 | Commission/Deal |
|---------|---------------|-----------------|-----------------|-----------------|
| Senior Mutuelle | 750€ | <35€ | <22€ | 180–220€/year |
| BTP Décennale | 750€ | <55€ | <35€ | 250–350€/year |

LTGP:CAC must exceed 3x before any scaling decision. Felix approves all scale moves.
