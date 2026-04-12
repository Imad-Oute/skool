# ROLLAND ASSURANCES — LEAD GEN DEPARTMENT
## Master Ecosystem Map
### Documented: 2026-04-12 | Party Mode Session

---

## CONTEXT & SITUATION

**Client:** Rolland Assurances — rollandassurances.com
**Goal:** Generate qualified leads (calls + form submissions) to two landing pages:
- `https://rollandassurances.com/landing/sante-senior` — Mutuelle Santé, Seniors 55+
- `https://rollandassurances.com/landing/garantie-decennale` — Assurance Décennale, Artisans BTP

**Budget:** 1,500€/month (Google Ads)
**Previous campaigns:** Ran but results were unsatisfactory — root cause diagnosis pending

**The core atom of this entire department:**
> Someone has a problem (health costs in retirement / no insurance certificate for a job site). They search Google. They see your ad. They call. Rolland closes the deal.

Everything — the API script, the SLM framework, the CAI ecosystem — is infrastructure built to make that atom happen more often, more cheaply, more reliably. Every decision made in this department should be testable against one question: **does this help more qualified people call Rolland?** If the answer isn't immediately yes — it waits.

---

## THE THREE PILLARS

The department is built on three pillars that work together as one machine:

1. **Pillar 1 — Paid Traffic Engine** (Short-Term, Immediate): Google Ads System
2. **Pillar 2 — Content & Organic Engine** (Mid-Term, Authority): CAI System (Hormozi)
3. **Pillar 3 — Persuasion Layer** (Governs ALL copy & messaging): SLM System (Belfort)

These are connected by a continuous **Intelligence Loop** that feeds performance data back into all three pillars.

---

## FULL ECOSYSTEM MAP

```
╔══════════════════════════════════════════════════════════════════╗
║              ROLLAND ASSURANCES — LEAD GEN MACHINE              ║
║                    Goal: Qualified Calls & Leads                 ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  THE TWO OFFERS (Non-Negotiable Foundation)                      ║
║  ┌─────────────────────┐   ┌──────────────────────────┐         ║
║  │  MUTUELLE SANTÉ      │   │  GARANTIE DÉCENNALE       │         ║
║  │  Seniors 55+         │   │  Artisans BTP             │         ║
║  │  /landing/sante-     │   │  /landing/garantie-       │         ║
║  │  senior              │   │  decennale                │         ║
║  └─────────────────────┘   └──────────────────────────┘         ║
║                    ↑                   ↑                         ║
║              All traffic flows to these two pages                ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  PILLAR 1 — PAID TRAFFIC ENGINE (Short-Term, Immediate)          ║
║  ┌──────────────────────────────────────────────────────────┐    ║
║  │  GOOGLE ADS SYSTEM                                        │    ║
║  │                                                           │    ║
║  │  ┌──────────────────┐    ┌──────────────────┐            │    ║
║  │  │ Campaign SENIOR   │    │ Campaign DÉCENNALE│            │    ║
║  │  │ Call-Only Ads     │    │ Call-Only Ads     │            │    ║
║  │  │ 750€/month        │    │ 750€/month        │            │    ║
║  │  │ S1/S2/S3 groups   │    │ D1/D2/D3/D4 groups│            │    ║
║  │  └──────────────────┘    └──────────────────┘            │    ║
║  │                                                           │    ║
║  │  AUTOMATION LAYER                                         │    ║
║  │  └── create_rolland_campaigns.py (Google Ads API)         │    ║
║  │       → Creates campaigns via CLI                         │    ║
║  │       → Pushes ads, keywords, ad groups                   │    ║
║  │       → Future: reads performance, auto-optimizes         │    ║
║  │                                                           │    ║
║  │  PERFORMANCE TRACKING                                     │    ║
║  │  └── Google Ads Dashboard                                 │    ║
║  │  └── GA4 linked                                           │    ║
║  │  └── Call conversion tracking (≥60s)                      │    ║
║  └──────────────────────────────────────────────────────────┘    ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  PILLAR 2 — CONTENT & ORGANIC ENGINE (Mid-Term, Authority)       ║
║  ┌──────────────────────────────────────────────────────────┐    ║
║  │  CAI SYSTEM (Hormozi — Client Acquisition Intelligence)   │    ║
║  │                                                           │    ║
║  │  ATTRACT LAYER                                            │    ║
║  │  ├── cai-content-architect (Coda)                         │    ║
║  │  │    → 5-Category Topic Matrix for each offer            │    ║
║  │  │    → Content mapped to funnel stages                   │    ║
║  │  └── cai-hook-engineer (Aura)                             │    ║
║  │       → High-CTR hooks for ads + organic content          │    ║
║  │                                                           │    ║
║  │  CONVERT LAYER                                            │    ║
║  │  ├── Landing page optimization (SLM-informed)             │    ║
║  │  └── Lead magnet / nurture sequences (future)             │    ║
║  │                                                           │    ║
║  │  OPTIMIZE LAYER                                           │    ║
║  │  ├── cai-feedback-loop-tracker (Trace)                    │    ║
║  │  ├── cai-growth-controller (Felix)                        │    ║
║  │  └── cai-compliance-auditor (Vera)                        │    ║
║  └──────────────────────────────────────────────────────────┘    ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  PILLAR 3 — PERSUASION LAYER (Governs ALL copy & messaging)      ║
║  ┌──────────────────────────────────────────────────────────┐    ║
║  │  SLM SYSTEM (Belfort — Straight-Line Marketing)           │    ║
║  │                                                           │    ║
║  │  APPLIES TO:                                              │    ║
║  │  ├── Ad copy (hooks, headlines, descriptions)             │    ║
║  │  ├── Landing page structure (Three Tens framework)        │    ║
║  │  ├── CTA timing (action threshold logic)                  │    ║
║  │  └── Future: email sequences, retargeting                 │    ║
║  │                                                           │    ║
║  │  KEY PRINCIPLES IN USE:                                   │    ║
║  │  ├── Three Tens: Product + Person + Company trust         │    ║
║  │  ├── Pain threshold → Action threshold sequence           │    ║
║  │  └── 4-Second Rule: Sharp / Enthusiastic / Expert         │    ║
║  └──────────────────────────────────────────────────────────┘    ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  INTELLIGENCE LOOP (Runs continuously, feeds all pillars)        ║
║  ┌──────────────────────────────────────────────────────────┐    ║
║  │  DATA IN                        DATA OUT                  │    ║
║  │  ├── Google Ads performance  →  Campaign adjustments      │    ║
║  │  ├── Call quality / duration →  Keyword pruning           │    ║
║  │  ├── CTR by ad / hook        →  Copy iteration            │    ║
║  │  ├── CPL vs target           →  Budget reallocation       │    ║
║  │  └── Competitor search terms →  Keyword expansion         │    ║
║  └──────────────────────────────────────────────────────────┘    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## LAYER ARCHITECTURE EXPLAINED

### The Relationship Between the Three Pillars

The three pillars are not independent — they feed each other in a specific sequence:

```
PILLAR 3 (SLM Persuasion)
       ↓ governs all messaging
PILLAR 2 (CAI Content)        PILLAR 1 (Google Ads)
       ↓ builds authority             ↓ drives immediate traffic
              ↘                      ↙
         THE TWO LANDING PAGES
         (conversion point)
              ↓
         INTELLIGENCE LOOP
         (performance data feeds back into all pillars)
```

**Critical insight:** The three pillars are not three separate workstreams. They are one machine at different time horizons:
- **Google Ads** = immediate lead flow (weeks 1–8)
- **CAI Content** = compounding authority (month 2+)
- **SLM Persuasion** = the quality layer that improves every other pillar's conversion rate

---

## WORK BREAKDOWN STRUCTURE

```
DEPARTMENT WORK BREAKDOWN
─────────────────────────────────────────────────────────

ZONE A — FOUNDATION (Must exist before anything else works)
  A1. Offers validated (✅ Done — 2 landing pages exist)
  A2. Google Ads account setup + tech checklist
      └── Conversion tracking, call tracking, GA4 link
  A3. Campaign structure created and live
      └── create_rolland_campaigns.py → deployed

ZONE B — PAID TRAFFIC (Primary lead source, weeks 1-8)
  B1. Campaign SENIOR live + monitoring
  B2. Campaign DÉCENNALE live + monitoring
  B3. Weekly data review (CTR, CPL, call duration)
  B4. Optimization cycles (negative keywords, bid adjustments)
  B5. API script expansion (auto-reporting, auto-optimization)

ZONE C — PERSUASION LAYER (Improves conversion at every stage)
  C1. SLM audit of both landing pages (Three Tens check)
  C2. SLM-informed ad copy rewrite (current hooks)
  C3. SLM hook testing matrix (A/B test 4 angles per offer)

ZONE D — CONTENT ENGINE (Month 2+, compounds over time)
  D1. 5-Category Topic Matrix per offer (Coda leads)
  D2. Hook library for each category (Aura leads)
  D3. Content calendar — 2 offers × 5 categories
  D4. Distribution strategy (LinkedIn, YouTube, Meta)

ZONE E — INTELLIGENCE & OPTIMIZATION (Ongoing)
  E1. Weekly feedback loop review (Trace leads)
  E2. Monthly financial audit (Felix leads)
  E3. Quarterly ecosystem audit (CEO leads)
```

---

## BUILD SEQUENCE

The correct order of operations — do not skip ahead:

| Phase | Zone | What | Why |
|-------|------|------|-----|
| Phase 0 | A | Foundation: tech setup + tracking | Can't measure without this |
| Phase 1 | B | Launch paid campaigns, collect data | Validates the offer before anything else |
| Phase 1 | C | Apply SLM to ads + landing pages | Improves conversion while collecting data |
| Phase 2 | B | Optimize campaigns with real data | Kill losers, scale winners |
| Phase 2 | E | Intelligence loop running | Weekly review cadence established |
| Phase 3 | D | Content engine activated | Compounds on top of proven paid system |
| Phase 3 | B5 | API script expanded | Automate what's been validated manually |

---

## FINANCIAL MODEL

### Budget Allocation

| Campaign | Budget/Month | Budget/Day | Active Days |
|----------|-------------|------------|-------------|
| Senior — Mutuelle Santé | 750€ | 34,10€ | Mon–Fri only |
| BTP — Décennale | 750€ | 34,10€ | Mon–Fri only |
| **TOTAL** | **1,500€** | **68,20€** | — |

### CPL Targets (Cost Per Qualified Lead)

| Segment | CPL Target | Qualified = | Commission/Deal | LTV (3 ans) |
|---------|-----------|-------------|-----------------|-------------|
| Senior Mutuelle | < 35€ | Call ≥ 60 seconds | 180–220€/an | 540–660€ |
| BTP Décennale | < 55€ | Call ≥ 60 seconds | 250–350€/an | 750–1,050€ |

### Felix's Financial Rule
> LTGP:CAC must exceed 3x before any scaling decision. Every dollar spent is a hypothesis — validate before multiplying. Scaling a losing campaign faster is not growth, it's accelerated destruction.

### Scaling Decision Framework

| Condition | Action |
|-----------|--------|
| Segment CPL < target × 0.8 | Increase budget 20–30% |
| Segment CPL > target × 1.5 | Investigate queries, reduce spend |
| Group with 0 conversions in 30 days | Pause and revise keywords |
| ≥ 30 conversions on a campaign | Switch to Target CPA bidding |
| Segment A CPA < 30€ | Increase Senior budget 20–30% |
| Segment B CPA < 45€ | Increase Décennale budget 20–30% |

---

## DIAGNOSTIC FRAMEWORK (3-Layer Autopsy)

When results are poor, run this before making any change:

### Layer 1 — Hook Failure
- CTR < 3% → The ad never earned attention
- Action: Revise headlines using SLM 4-Second Rule

### Layer 2 — Body Failure
- CTR decent but no conversions on landing page
- The Three Tens (Product / Person / Company) are not satisfied
- Action: SLM audit of landing page

### Layer 3 — CTA Failure
- People reach the CTA but don't call/submit
- Action threshold not cleared — too much friction, not enough urgency
- Action: Rewrite CTA section, add urgency, reduce friction

---

## CAMPAIGN STRUCTURE REFERENCE

### Campaign 1 — Senior Mutuelle Santé

```
[RA] Senior - Mutuelle Santé - Call Only
├── S1: Changement de mutuelle
│     Keywords: mutuelle santé senior, changer mutuelle 60 ans...
├── S2: Urgence soins / remboursements
│     Keywords: mutuelle dentaire senior, reste à charge retraité...
└── S3: Hausse cotisation / résiliation Châtel
      Keywords: résiliation mutuelle hausse tarif, loi Châtel...
```

**Ad angles (4 per campaign):**
- A1: Conseil Expert ("Courtier Indépendant — Conseils 55+")
- A2: Économies ("Votre Mutuelle Coûte Trop Cher ?")
- A3: Reste à charge / Dentaire ("Réduisez votre reste à charge")
- A4: Résiliation / Changement ("Loi Châtel — Changez Sans Frais")

### Campaign 2 — BTP Assurance Décennale

```
[RA] BTP - Décennale - Call Only
├── D1: Urgence attestation (highest intent)
│     Keywords: assurance décennale urgent, attestation en 24h...
├── D2: Création / première décennale
│     Keywords: décennale artisan, auto entrepreneur bâtiment...
├── D3: Changement assureur / prix
│     Keywords: changer assurance décennale, décennale moins chère...
└── D4: Profils complexes / refusés
      Keywords: décennale refusée, sinistre antérieur...
```

**Ad angles (4 per campaign):**
- B1: Urgence Attestation ("Attestation en 24h")
- B2: Obligation Légale ("Loi Spinetta — 10+ Assureurs Comparés")
- B3: Profils Difficiles ("Décennale Refusée Ailleurs ? Tous Profils Acceptés")
- B4: Prix / Économies ("Décennale Moins Chère — Courtier Indépendant")

---

## TECH STACK & TOOLS

| Tool | Purpose | Status |
|------|---------|--------|
| Google Ads | Paid traffic platform | Setup required |
| Google Analytics 4 | Web analytics + conversion import | Setup required |
| Google Tag Manager | Tag deployment on site | Setup required |
| Google Business Profile | Local presence + LSA eligibility | Setup required |
| `create_rolland_campaigns.py` | Google Ads API CLI automation | Built, needs credentials |
| CAI Agent System | Content creation + optimization agents | Installed |
| SLM Ecosystem | Persuasion framework reference | Documented |

### Tech Checklist (Must complete before any spend)

- [ ] Google Ads account created + financial services advertiser verification
- [ ] Google Number Call Transfer activated (Conversion tracking)
- [ ] Conversion event "Appel ≥ 60 secondes" created
- [ ] Google Ads ↔ GA4 linked (import conversions)
- [ ] Call extensions configured on all campaigns
- [ ] Google Business Profile created and verified
- [ ] Google Tag Manager installed on rollandassurances.com
- [ ] ORIAS number visible on both landing pages (regulatory requirement)

---

## COMPLIANCE NOTES

- **Google Ads category:** "Crédit, logement et assurance" — requires financial services advertiser certification (2–7 business days)
- **ORIAS number** must appear on both landing pages
- **RGPD:** Any form/data collection requires up-to-date privacy policy
- **Ad copy rules:** Cannot promise "meilleur prix garanti" without justification

---

## KPIs TO TRACK WEEKLY

| KPI | Senior Target | Décennale Target |
|-----|--------------|-----------------|
| Impressions | > 500/week | > 300/week |
| CTR | > 8% | > 10% |
| Call rate from click | > 35% | > 40% |
| Avg call duration | > 90 seconds | > 120 seconds |
| CPL (qualified call) | < 35€ | < 55€ |
| Close rate | > 15% | > 20% |

### Alarm Signals (investigate immediately)

| Signal | Interpretation | Action |
|--------|---------------|--------|
| CTR < 3% | Ads not relevant or bids too low | Revise headlines, raise bid |
| >60% calls < 60s | Poor prospect quality or wrong number | Check number, revise keywords |
| CPC > 8€ (Senior) | Intense competition | Add long-tail keywords |
| CPC > 12€ (Décennale) | Bid too aggressive | Adjust max bid or switch to Target CPA |
| Zero impressions | Bid too low or config error | Check status, raise bid |

---

## TIMELINE & MILESTONES

| Period | Expected |
|--------|---------|
| Week 0 | Tech setup complete, zero spend |
| Week 1 | Both campaigns live, first impressions |
| Week 2–3 | Enough data to optimize ads |
| Month 1 | 30–80 qualified calls, first contracts |
| Month 2 | Target CPA bidding activated, CPL dropping |
| Month 3 | ROI stabilized, most profitable segment identified |
| Month 4–6 | Scale winner, reduce loser, content engine activated |

---

## RESOURCES IN THIS PROJECT

| File | What It Contains |
|------|-----------------|
| `Ressources/CLICK-TO-CALL-GoogleAds-RollandAssurances.md` | Full Google Ads strategy: campaigns, keywords, ads, projections |
| `Ressources/Straight-Line-Marketing/SLM-Ecosystem-Map.md` | Jordan Belfort SLM full system map |
| `Ressources/create_rolland_campaigns.py` | Google Ads API script to deploy campaigns via CLI |
| `Ressources/Rolland_Assurances_Strategy_Report.pdf` | Strategy report |

---

## OPEN QUESTIONS (To resolve before execution)

1. **What data exists from previous campaigns?** CTR, impressions, call count, call duration — needed for Layer 1/2/3 diagnostic
2. **Which tech checklist items are actually complete?** Conversion tracking, call transfer number, GA4 link
3. **Is the Google Ads account certified** for financial services advertising?
4. **What is Rolland's actual phone number?** The script uses `+33100000000` as placeholder
5. **What are the current landing pages' conversion rates?** Needed to know if the problem is traffic or page

---

*Document generated in Party Mode session — 2026-04-12*
*Agents involved: CEO (Strategic Architect), Coda (Content Architect), Trace (Feedback Loop Tracker), Felix (Growth Controller), Thinker (First Principles Deconstructor)*
