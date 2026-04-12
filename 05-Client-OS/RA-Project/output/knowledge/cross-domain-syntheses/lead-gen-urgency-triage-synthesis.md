# Cross-Domain Synthesis: RA Lead Gen — Urgency-Tiered Acquisition Architecture

**Skill:** mgi-cross-domain-synthesizer  
**Source Domain:** Emergency Medicine / Advanced Trauma Life Support (ATLS)  
**Problem Domain:** Rolland Assurances Lead Gen Ecosystem (RA-LeadGen-Ecosystem-Map-v2.md)  
**Date:** 2026-04-12  
**Synthesis Level:** Level 3 — Structural Isomorphism  

---

## Core Insight — One Sentence

> The RA ecosystem correctly segments by intent but does not triage — it routes all urgency levels through the same acquisition architecture, which means the highest-value, shortest-window prospects (BTP D1, Senior S3 Châtel) are systematically under-served by a system optimized for the average.

---

## Source Domain: Emergency Medicine / ATLS

### Core Mechanism

```
Chief complaint → Primary survey (90s, standardized) → Triage classification
→ Architecturally differentiated care pathway → Pathway-specific resources
→ Outcome monitoring → Re-triage if status changes
```

### Key Principles

1. **Urgency is a signal, not a fixed property** — it can change; re-triage is continuous
2. **Red patients don't get Yellow treatment faster** — they get an architecturally different system
3. **Resources are finite** — scarcity makes triage necessary; without it the high-urgency cases deteriorate in the queue
4. **Under-triage is more lethal than over-triage** — the cost of missing a Red is higher than the cost of over-treating a Yellow
5. **The pathway determines the protocol** — same treatment team but completely different sequences, tools, and timelines per tier

### Triage Categories

| Tier | Label | Condition | Resource Allocation |
|---|---|---|---|
| Red | Immediate | Life-threatening; window measured in minutes | Trauma bay, attending physician, full team, max resources |
| Yellow | Delayed | Serious but stable; window measured in hours | Medical ward, monitored queue, appropriate protocol |
| Green | Minimal | Self-limiting; no acute intervention needed | Self-care instructions or scheduled appointment |
| Black | Expectant | Unsurvivable without extreme resource consumption | Comfort care only; do not divert from Red/Yellow |

---

## Problem Domain: RA Lead Gen Ecosystem

### The Structural Flaw

The ecosystem map (v2) has four campaign intent groups for BTP:

- **D1: Urgence attestation** — "J'ai un chantier qui attend" — conversion window: TODAY
- **D2: Création / première décennale** — conversion window: days
- **D3: Changement assureur / prix** — conversion window: days to weeks
- **D4: Profils complexes / refusés ailleurs** — conversion window: days to weeks

And three for Senior:

- **S1: Changement de mutuelle** — conversion window: 2–6 weeks
- **S2: Urgence soins / remboursements** — conversion window: days to weeks
- **S3: Hausse cotisation / résiliation Châtel** — conversion window: TODAY (during Châtel window Nov-Jan) or weeks (outside it)

**The current system routes D1 and D4 through the same campaign, same budget pool, same bid strategy framework, same ad format options.** This is triage labeling without triage pathway differentiation. Every intent group goes to the same ward after being correctly labeled Red or Yellow.

### Problem Profile

```
Core challenge:       Heterogeneous urgency demand + fixed budget constraint
Mechanism missing:    Signal-based urgency classification → differentiated acquisition architecture
Resource constraint:  €68.20/day total — insufficient for max bids across all intents simultaneously
Urgency variance:     D1 (hours) vs D4 (weeks) = 100x+ conversion window difference
Current solution:     Segment by intent, vary message, same architecture — inadequate
```

---

## Structural Mapping

| Domain A Element | Function | Domain B Equivalent | Confidence |
|---|---|---|---|
| Chief complaint + vital signs | Initial urgency signal | Search keyword + query modifier ("urgence", "rapidement", "attestation", "aujourd'hui") | **Strong** |
| Primary survey (ABCDE, 90s) | Rapid standardized classification | Keyword list → Intent tier assignment at campaign design | **Strong** |
| Red triage (Immediate) | Maximum resources, today | D1 BTP + S3 Senior during Châtel window (Nov-Jan) | **Strong** |
| Yellow triage (Delayed) | Appropriate care, standard queue | D2-D4 BTP + S1-S2 Senior (all year) + S3 outside Châtel | **Strong** |
| Green triage (Minimal) | Exclude from acute resources | Informational queries — negative keyword list | **Strong** |
| Trauma bay (limited, expensive) | High-resource pathway for Red | Call-Only ad + max bid + zero landing page friction + 4-hour callback SLA | **Strong** |
| Medical ward (larger, slower) | Standard pathway for Yellow | Text ad → landing page → Three Tens → CTA → call | **Strong** |
| Re-triage (continuous) | Status change → pathway change | Weekly keyword review: promote Yellow→Red if urgency signals appear | **Moderate** |
| Finite hospital capacity | Forces triage discipline | €68.20/day total budget — scarcity makes allocation decisions consequential | **Strong** |
| ICU admission criteria | Criteria-triggered escalation | Felix Gate 2: CPL < target × 0.8 → budget escalation to that tier | **Strong** |

### Residual Gaps (No Domain A Equivalent)

**Seasonal triage pressure (Châtel window Nov-Jan):**
No ER equivalent of predictable seasonal surges that change a search intent's urgency tier.
→ **Novel solution:** Seasonal triage calendar. S3 keywords reclassify to Red during Nov 1 – Jan 31, revert to Yellow on Feb 1. Implemented as scheduled campaign type switch or bid rule.

**Two products with structurally different urgency-tier distributions:**
BTP is inherently Red-majority (most searches are urgency-driven). Senior is inherently Yellow-majority.
→ **Confirmed insight:** BTP and Senior are not the same machine with different messages. They are different urgency-tier distributions requiring different default resource postures.

---

## Transferable Pattern

```
PATTERN NAME:           Urgency-Tiered Acquisition Architecture (UTAA)

DOMAIN OF ORIGIN:       Emergency Medicine / Advanced Trauma Life Support

CORE MECHANISM:         Search intent signal → urgency classification → architecturally 
                        differentiated acquisition pathway → independent budget and 
                        format allocation per tier → tier-specific success metrics → 
                        re-triage feedback loop

APPLICATION CONDITION:  When:
  (a) multiple intent signals co-exist with materially different conversion windows
  (b) budget is constrained enough that blanket treatment wastes high-urgency demand
  (c) the platform supports independent campaign structures (Google Ads does)

INAPPLICABILITY:        When all intents have equivalent urgency profiles, or when 
                        budget is effectively unlimited

NOVEL INSIGHT:          The RA ecosystem's CPL diagnostic (3-Layer: Hook → Body → CTA) 
                        identifies WHERE a campaign fails but not WHICH campaign 
                        architecture caused the failure. A D1 keyword in a shared 
                        BTP campaign that underperforms is not a hook problem — 
                        it's an architecture problem. No amount of copy iteration 
                        fixes the structural error of routing a Red patient to a 
                        Yellow ward.

FALSIFIABLE PREDICTION: If BTP-RED is split into a standalone call-only campaign with 
                        priority budget allocation, CPL for D1 intent should decrease 
                        within 30 days, and call volume per euro should increase relative 
                        to the D2-D4 Yellow group. If not, the urgency classification 
                        was wrong — run re-triage.
```

---

## Implementation Blueprint

### Component Design

| Component | Domain A Analogue | Function | Implementation |
|---|---|---|---|
| **Urgency Signal Classifier** | Primary Survey (ABCDE) | Reads keyword → assigns Red/Yellow/Green | Keyword list: urgency-signal terms isolated into separate match type lists during campaign build |
| **BTP-RED Campaign** | Trauma Bay | Captures highest-intent BTP searchers; zero friction | Call-Only ads only, max bid (8-12€ CPC), Mon-Fri 07:00-19:30, no landing page, direct to phone |
| **BTP-YELLOW Campaign** | Medical Ward | Processes consideration-mode BTP through full persuasion arc | Text ads → /garantie-decennale, Three Tens architecture, Target CPA after 30 conversions |
| **Senior-YELLOW Campaign** | Medical Ward | Processes Senior searchers who need trust-building | Text ads → /sante-senior, Three Tens + Threshold, retargeting pool feeds |
| **Senior-RED Seasonal Mode** | Code-Red surge protocol | Châtel window (Nov-Jan): S3 urgency spikes to Red | S3 keywords switched to call-only format OR +80% bid modifier, Nov 1 – Jan 31 |
| **Red Callback SLA** | Trauma bay response standard | Red-code inbound answered within 4 hours | Operational agreement with Rolland: Red inbound = priority queue |
| **Re-triage Gate** | Continuous vital sign monitoring | Weekly keyword promotion/demotion between Red/Yellow | Trace reviews: Yellow keywords with call rate > 40% + avg duration > 120s → Red candidate |

### Interface Design

```
[Search Query]
    ↓
[Urgency Classifier — keyword list check]
    │
    ├── URGENCY SIGNAL PRESENT (D1 BTP + S3 Nov-Jan)
    │       ↓
    │   [BTP-RED Campaign — Call-Only]
    │       → Direct Call → Conversion System
    │       → 4-hour callback SLA (Rolland operational)
    │       → KPI: calls/day, CPL < 55€ Red tier
    │
    ├── BTP, NO URGENCY SIGNAL (D2-D4)
    │       ↓
    │   [BTP-YELLOW Campaign — Text Ads]
    │       → /garantie-decennale → Three Tens → CTA → Call
    │       → Non-convert → BTP-YELLOW RLSA Pool → Looping System
    │       → KPI: CPL < 55€ Yellow tier, call rate > 40%
    │
    ├── SENIOR QUERY (S1-S2, S3 outside Nov-Jan)
    │       ↓
    │   [Senior-YELLOW Campaign — Text Ads]
    │       → /sante-senior → Three Tens + Threshold → CTA → Call
    │       → Non-convert → Senior RLSA Pool → Looping System
    │       → KPI: CPL < 35€, call rate > 35%, call duration > 90s
    │
    └── INFORMATIONAL (no commercial intent)
            → Negative keyword list — excluded from paid

[Performance Data — Trace Weekly]
    ↓
[Re-triage Gate]
    → Red CPL > target × 1.5 → re-examine urgency classification for that keyword set
    → Yellow keyword: call rate > 40% + duration > 120s → promote to Red candidate
    → Date = Nov 1 → activate Senior-RED seasonal mode
    → Date = Feb 1 → deactivate, revert S3 to Yellow

[Conversion System Output — Rolland → Felix Monthly]
    → Close rate per tier → financial audit, tier-level LTGP:CAC
    → Lost deal reasons per tier → avatar profile updates (Analyst)
    → Tier CPL trend → scaling gate decisions per tier, not blended
```

### Critical Path

```
STEP 1 — Pre-launch, this week (BLOCKING)
  Audit all keywords in create_rolland_campaigns.py
  → Identify which contain urgency signals: ["urgence", "rapidement", "aujourd'hui", 
    "attestation immédiate", "refusé ailleurs", "besoin rapide", "chantier qui attend"]
  → Separate into: BTP-RED keyword list | BTP-YELLOW keyword list | Negative list
  ENABLES: campaign structure decision before first euro spent

STEP 2 — Week 1 Launch
  Build BTP-RED as standalone call-only campaign (€350-400/month)
  Build BTP-YELLOW as separate standard campaign (€350-400/month)
  Each with independent bid strategy, independent CPL target, independent KPI tracking
  ENABLES: no urgency tier contaminating the other's optimization signal

STEP 3 — Month 1
  BTP-RED hits 30 calls → switch to Target CPA (calls)
  BTP-YELLOW hits 30 conversions → switch to Target CPA
  ENABLES: algorithm calibrated per tier independently — not averaged across mixed urgencies

STEP 4 — Month 2, before November
  Build Senior-RED seasonal protocol
  → S3 keyword list ready for call-only switch or bid-boost (+80%) on Nov 1
  → Rolland briefed: Nov-Jan is Code Red season for Senior — response time is critical
  ENABLES: Châtel window captured with correct architecture, not missed on generic Yellow setup

STEP 5 — Ongoing (Trace weekly)
  Re-triage gate active
  → Weekly promotion/demotion of keywords between Red and Yellow based on observed call behavior
  ENABLES: living triage system that self-corrects, rather than static taxonomy locked at launch
```

---

## Budget Reallocation Implication

Current model: €750 BTP (blended) + €750 Senior (blended)

**Triage-aligned model:**

| Campaign | Tier | Monthly Budget | Rationale |
|---|---|---|---|
| BTP-RED (D1 urgence) | Red | €400 | Highest conversion probability, shortest window, priority resource |
| BTP-YELLOW (D2-D4) | Yellow | €350 | Longer window, sustains lower spend, feeds retargeting pool |
| Senior-YELLOW (S1-S2 + S3 off-season) | Yellow | €600 | Majority of Senior searches; needs landing page + Three Tens time |
| Senior-RED seasonal (S3 Nov-Jan only) | Red (seasonal) | €150 (Nov-Jan surge) | Reallocated from Senior-YELLOW during Châtel window |

*Total: €1,500/month — same budget, different allocation logic.*

---

## Expected Behavior

When correctly implemented, observe:

1. **BTP-RED CPL decreases** vs. the blended BTP CPL from v1 (call-only removes landing page drop-off; max bid wins the auction before comparison shopping occurs)
2. **BTP-YELLOW CPL stabilizes independently** — no longer averaged with high-urgency D1 noise; optimization converges faster
3. **Senior Châtel window generates disproportionate call volume Nov-Jan** — the seasonal Red mode captures the highest-intent window that previously ran at standard Yellow bids
4. **Close rate correlation by tier** — Rolland should see higher close rates on Red-code inbound (self-selected by urgency signal) vs. Yellow (consideration mode, lower close rate but higher LTV potential)
5. **3-Layer Diagnostic becomes tier-specific** — Hook failures in BTP-RED mean different things than hook failures in Senior-YELLOW; same CTR metric, different root causes

---

## Validation Criteria

| Criterion | How to Measure | Pass Threshold |
|---|---|---|
| BTP-RED CPL vs. prior blended BTP CPL | Compare 30-day post-split CPL | BTP-RED CPL ≤ blended historic CPL |
| Call volume per euro on BTP-RED | Calls ÷ spend, tracked per week | Higher than BTP-YELLOW rate |
| Senior Châtel surge captured | Call volume Nov vs. Oct | ≥ 2x call volume during Red season |
| Re-triage accuracy | % of promoted keywords that improve after Red treatment | > 60% of promoted keywords show CPL decrease |
| Tier-specific close rate | Rolland reports close rate tagged by campaign source | Red > Yellow close rate (confirms urgency signal is real) |

---

## Competitive Advantage Assessment

**Why no Google Ads practitioner finds this from within the domain:**
- Platform UI organizes thinking as campaigns → ad groups → ads. Urgency triage crosses this hierarchy and is invisible within it.
- Google Ads best practice: segment by intent, optimize bids per group. This is segmentation — not triage. Segmentation labels. Triage allocates.
- SLM thinking operates at the persuasion layer — assumes same conversion architecture for all, varied by message. Resource allocation under urgency scarcity is outside SLM's frame.

**What this unlocks:**
- Within the same €1,500/month budget, priority concentration on Red-code prospects captures the highest-ROI demand first — before daily budget is consumed by lower-urgency impression volume
- Tier-specific optimization signals allow Google's algorithm to calibrate independently per urgency class — rather than being confused by mixed-urgency signals averaging each other out
- The Châtel seasonal architecture is a structural moat: competitors who don't model the urgency tier shift during Nov-Jan are running Yellow systems against a prospect base that has turned Red

---

*Synthesis saved: output/knowledge/cross-domain-syntheses/lead-gen-urgency-triage-synthesis.md*  
*Source document: output/plans/RA-LeadGen-Ecosystem-Map-v2.md*  
*Pattern: Urgency-Tiered Acquisition Architecture (UTAA)*  
*Agents: Brainstormer 💡 | Analyst 📊 | Engineer ⚙️*
