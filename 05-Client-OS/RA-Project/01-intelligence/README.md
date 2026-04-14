# 01-INTELLIGENCE
## The Nervous System — Runs Before Launch and Continuously After

---

## PURPOSE

The Intelligence System is the only system in the ecosystem that is **always running**. It feeds the machine before it starts (shaping what to say, who to target, what keywords to buy) and continuously after it starts (telling you what to change, what to kill, what to scale).

It is not a research dump. Every output from this folder must produce a **decision or a directive** — something that changes an input to the machine. Intelligence that doesn't change behavior is just overhead.

---

## THE CRITICAL DISTINCTION

This folder contains two sub-systems that solve fundamentally different problems. They must never be confused:

|                         | SS1 — Market Intelligence                                       | SS2 — Performance Feedback                                   |
| ----------------------- | --------------------------------------------------------------- | ------------------------------------------------------------ |
| **Question it answers** | What is the market doing?                                       | What are WE doing?                                           |
| **Data source**         | External (competitors, search data, forums)                     | Internal (our own Google Ads account)                        |
| **Feeds**               | Avatar profiles, keyword strategy, ad angles, offer positioning | Weekly directive, budget decisions, kill/keep/scale verdicts |
| **Cadence**             | Launch + Quarterly + Triggered                                  | Daily (first 30 days) → Weekly → Monthly                     |
| **Owner**               | Analyst + CEO                                                   | Trace + Felix                                                |

Confusing these two is the most common optimization mistake in paid acquisition: changing the ad copy when the problem is the bid strategy, or rewriting the landing page when the problem is keyword intent.

---

## FOLDER STRUCTURE

```
01-intelligence/
│
├── SS1-market/                     External — study the market before spending
│   ├── avatars/                    Psychological profiles of the two target customers
│   ├── competitors/                Who else is advertising, what they say, where they're weak
│   ├── keywords/                   What people search, what intent it signals, what to exclude
│   └── seasonality/                When demand peaks, when to push budget, when to pull back
│
└── SS2-performance/                Internal — study our own campaigns after spending
    ├── directives/                 Weekly optimization directive (kill/keep/scale/test)
    ├── diagnostics/                3-layer diagnostic reports (Hook / Body / CTA failure)
    └── kpi/                        Rolling KPI log — weekly and monthly performance snapshots
```

---

## SS1 — MARKET INTELLIGENCE (External)

### What happens here
Before spending a single euro, SS1 answers: who exactly is searching, what are they afraid of, what language do they use, who else is competing for them, and where are the gaps we can exploit.

### Subfolders

**`avatars/`**
The two psychological profiles that govern ALL messaging decisions across the entire ecosystem:
- `avatar-A-senior.md` — Le Retraité Surpayé (Senior 55+, fixed income, rate increase letter in hand)
- `avatar-B-btp.md` — L'Artisan BTP Bloqué (Self-employed contractor, job site waiting, needs attestation fast)
- `avatar-research-log.md` — Verbatim quotes pulled from forums (Que Choisir, forum-assurance.com, BTP communities). Raw language the avatars actually use — copied directly into headlines.

**`competitors/`**
- `serp-audit-senior.md` — Who is advertising on our Senior keywords? What are their headlines?
- `serp-audit-decennale.md` — Same for Décennale segment
- `competitor-ad-angles.md` — What angles are competitors using? What are they NOT covering? (gaps = our opportunity)
- `competitor-lp-audit.md` — Three Tens audit of competitor landing pages (Product/Person/Company trust)
- `competitive-gaps.md` — The angles nobody is covering — this is where we win

**`keywords/`**
- `intent-map-senior.md` — Commercial vs informational vs navigational split for Senior keywords
- `intent-map-decennale.md` — Same for Décennale
- `volume-analysis.md` — Monthly search volume per keyword group
- `negative-keywords-master.md` — Master negative keyword library. Maintained and expanded weekly.
- `keyword-research-log.md` — Raw keyword data and Keyword Planner exports

**`seasonality/`**
- `chatel-window-calendar.md` — The Nov–Jan rate increase notification window (Loi Châtel). Peak demand for Senior segment.
- `btp-peaks-calendar.md` — BTP contract seasons and construction activity peaks
- `annual-campaign-calendar.md` — Full year view: when to increase budget, when to test new angles, when to reduce spend

### Cadence
- **Deep research** at launch (before any spend)
- **Quarterly refresh** — market shifts, new competitors appear, avatar language evolves
- **Triggered review** when CPL degrades significantly or a new competitor enters the auction

---

## SS2 — PERFORMANCE FEEDBACK LOOP (Internal)

### What happens here
After campaigns go live, SS2 answers: what's working, what's broken, and what exact change will move the needle. It does not guess — it diagnoses layer by layer and issues a directive.

### The 3-Layer Diagnostic Framework

Before changing anything, Trace runs the diagnostic to identify WHERE the breakdown is. Changing the wrong layer wastes money.

```
LAYER 1 — HOOK FAILURE
  Signal:   CTR < 3%
  Cause:    Headlines not stopping the avatar, not triggering the pain
  Fix:      Rewrite headlines — Aura leads with SLM 4-Second Rule
  
LAYER 2 — BODY FAILURE
  Signal:   CTR decent (>5%) but call rate low (<20%)
  Cause:    Landing page not satisfying Three Tens — trust not built
  Fix:      SLM audit of landing page — CEO + Coda
  
LAYER 3 — CTA FAILURE
  Signal:   Landing page engagement decent but no calls
  Cause:    Action threshold not cleared — too much friction
  Fix:      Rewrite CTA section — Aura + SLM Threshold system
```

### Subfolders

**`directives/`**
Weekly optimization directives. One file per week.
**Naming convention: `YYYY-MM-DD-directive.md`** — non-negotiable.

Each directive contains exactly 4 verdicts:
1. **Kill** — pause this (ads, keywords, or groups)
2. **Keep** — leave unchanged, let data accumulate
3. **Scale** — increase budget or bid (requires Felix gate approval)
4. **Test Next** — new angle, new keyword, new ad variant to run next week

**`diagnostics/`**
3-layer diagnostic reports — triggered when KPIs drop below alarm thresholds.
**Naming convention: `YYYY-MM-DD-diagnostic-[topic].md`**
Example: `2026-05-12-diagnostic-senior-ctr.md`

**`kpi/`**
- `weekly-kpi-log.md` — Rolling tracker. All campaigns. Every week post-launch.
- `monthly-audit-log.md` — Monthly financial audit. Felix's domain. CPL, LTGP:CAC, ROI.

### KPI Targets & Alarm Thresholds

| KPI | Senior Target | Décennale Target | Alarm |
|-----|--------------|-----------------|-------|
| CTR | >8% | >10% | <3% |
| Call Rate from Click | >35% | >40% | <20% |
| Avg Call Duration | >90s | >120s | <60s |
| CPL (Qualified Call) | <35€ | <55€ | >52€ / >82€ |
| Close Rate | >15% | >20% | <10% |

---

## EXECUTION ORDER

SS1 activates **before launch** (Zone B in the WBS).
SS2 activates **after launch** (Zone E — day 1 post-deployment, runs forever).
