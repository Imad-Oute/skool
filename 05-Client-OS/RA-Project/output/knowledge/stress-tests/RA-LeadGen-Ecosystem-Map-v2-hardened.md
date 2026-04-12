# Hardened Plan: RA-LeadGen-Ecosystem-Map-v2

**Date:** 2026-04-12
**Adversarial iterations:** 1
**Attacks analyzed:** 14 | **Critical:** 6 | **Accepted risk:** 2

---

## Original Plan (Summary)

Rolland Assurances Lead Gen Machine — a Google Ads system built on the SLM framework
targeting two verticals (Senior Mutuelle Santé + BTP Garantie Décennale) at 1,500€/month,
converting search intent into qualified phone calls via two landing pages and a Call-Only
ad format, managed through a Python Google Ads API script and 10 CAI agents.

---

## What Changed

| Element | Original | Hardened Version | Why |
|---------|---------|-----------------|-----|
| Launch sequence | Zone A → Zone C (immediate full launch) | Zone A → Phase 0.5 Micro-Sprint → Zone C | Budget-volume death spiral: 34€/day is too thin to validate. Spend 400€ to confirm real CPCs before committing 1,500€/month |
| Phase 1 CPL targets | Senior <35€, BTP <55€ | Senior <55€, BTP <80€ | New account CPC penalty (QS 3–5 vs established accounts at 7–10) means paying 2× for same position. Original targets were benchmarked to established accounts, not a new account |
| Qualified lead definition | Call duration ≥60s | Call duration ≥60s AND Rolland-confirmed within 24h | Duration is a proxy. Price-shoppers and wrong numbers contaminate close rate data |
| Close layer | Described, assigned to Rolland, no tracking | Zone A item A12: Close Layer Protocol with SLA, call log, circuit breaker | The entire financial model depends on close rate. It was listed as Open Question #6 — unacceptable for a production plan |
| Budget split | 50/50 year-round | BTP 65% / Senior 35% (April–Oct), reverse Nov–Jan | Senior peak demand is the Châtel window (Nov–Jan). Launching April with equal budget ignores seasonal demand asymmetry |
| Legal/compliance | Vera covers blueprint adherence + ORIAS | Vera + Zone A item A13: RGPD, ACPR, Google financial services policy | GDPR/RGPD layer was entirely absent. French insurance advertising has specific legal requirements that are launch-blocking |
| Agent authority | 10 agents with overlapping mandates | Single decision authority table (see below) | Diffusion of responsibility when KPIs degrade. No tiebreaker = paralysis |
| Phase 2 CPL targets | Unchanged | Senior <22€, BTP <35€ (unchanged) | Phase 2 targets remain as-is — once account is established, original benchmarks are valid |

---

## Hardened Structure

### Phase 0 — Foundation (Week 0, pre-spend)

All Zone A items. Two additions:

**A12 — Close Layer Protocol** *(blocking before any spend)*
- Call response SLA: <10 minutes during ad hours (Mon–Fri 09:00–18:30)
- Backup call handler defined if Rolland is unavailable
- Call log started (shared sheet): Date | Duration | Qualified (Y/N) | Status | Lost reason
- Qualified lead definition locked: ≥60s AND Rolland-confirmed within 24h
- Weekly data input from Rolland to Trace is mandatory (non-optional)

**A13 — Legal Compliance Checklist** *(blocking before any spend)*
- RGPD: Consent disclosure for call data on landing pages
- ACPR: Insurance advertising disclosure requirements verified for both products
- Google financial services policy: France-specific restrictions confirmed
- ORIAS number visible on both landing pages AND in all ad copy
- Vera signs off before first ad goes live

**Start A4 (financial services verification) on Day 1** — not "Week 0." This is a 2–7 day process at minimum and must begin immediately.

---

### Phase 0.5 — Micro-Validation Sprint *(NEW — 2 weeks, 400€ max)*

**Purpose:** Validate critical assumptions before committing 1,500€/month.

**Structure:**
- Run ONE ad group only: D1 (Urgence attestation — highest intent, least competition)
- Budget: 20€/day × 14 days = 280€ maximum
- Landing page: /landing/garantie-decennale only

**Measure:**
| Metric | Gate (proceed if) | Kill signal |
|--------|-------------------|-------------|
| Real CPC | <8€ average | >12€ average |
| CTR | >5% | <2% |
| Call rate from click | >20% | <10% |
| Phase 0.5 CPL | <80€ | >120€ |
| Rolland call log | >5 confirmed qualified calls | 0 calls answered |

**Decision logic:**
- All gates passed → proceed to Phase 1 full launch, both campaigns
- 1–2 gates failed → diagnose, fix, re-run sprint before committing full budget
- Multiple gates failed → run 3-layer diagnostic before any spend; do not "try anyway"

---

### Phase 1 — Launch (Week 3–4, after Phase 0.5)

Both campaigns live. Revised targets:

**Revised Phase 1 CPL Targets (new-account benchmarks):**
| Segment | Phase 1 CPL Target | Phase 2 CPL Target |
|---------|-------------------|-------------------|
| Senior Mutuelle | <55€ | <22€ |
| BTP Décennale | <80€ | <35€ |

**Revised Budget Allocation (seasonal):**

*April–October (BTP priority):*
| Segment | Monthly Budget | Daily Budget |
|---------|---------------|-------------|
| BTP Décennale | 975€ | 44.30€ |
| Senior Mutuelle | 525€ | 23.90€ |

*November–January (Senior peak — Châtel window):*
| Segment | Monthly Budget | Daily Budget |
|---------|---------------|-------------|
| Senior Mutuelle | 975€ | 44.30€ |
| BTP Décennale | 525€ | 23.90€ |

---

### Phase 1 — Learn (Weeks 2–4 post-launch)

Daily monitoring as planned. **Added:**
- Close layer check: Rolland submits call log weekly (mandatory, not optional)
- Close rate circuit breaker: if <10% confirmed close rate for 2 consecutive weeks
  → pause all campaigns → CEO + Rolland diagnostic before resuming

---

### Agent Decision Authority Table *(Replaces committee ambiguity)*

| Domain | Decision Authority | Escalation |
|--------|------------------|------------|
| Ad copy, hooks, headlines | Aura | CEO if Aura + Coda disagree |
| Budget allocation, scaling | Felix | CEO if Felix + Trace disagree |
| Weekly optimization directive | Trace | Felix for financial impact calls |
| Legal/compliance gate | Vera | Hard stop — no workaround |
| Keyword strategy | Analyst | Trace for bid decisions |
| System architecture | CEO | Final authority on meta-rules |

One agent owns each domain. Others advise but do not block.

---

## Monitoring & Circuit Breakers

| Signal | Threshold | Who | Action |
|--------|-----------|-----|--------|
| Phase 0.5 CPL > 120€ | After 7 days | Felix | Pause sprint, diagnose before continuing |
| CTR < 2% | Week 1 | Trace → Aura | Rewrite all headlines immediately |
| Call rate < 10% from click | Week 1 | Trace → CEO + Coda | Emergency landing page audit |
| Confirmed close rate < 10% | 2 consecutive weeks | Felix → Rolland | Pause spend, close layer diagnostic |
| CPC > 12€ BTP / >9€ Senior | Ongoing | Trace | Shift to long-tail, add exact match, reduce max bid |
| Zero impressions | Day 1 post-launch | Trace | Check campaign status, bids, verification status |
| Account policy warning | Any time | Vera | Immediate escalation to CEO; prepare documentation |
| Phase 1 CPL > 80€ Senior / >120€ BTP | After 30 days | Felix | Kill Gate — pause, full diagnostic |

---

## Pre-Execution Validation Checklist

- [ ] A4: Financial services advertiser verification STARTED on Day 1 (not deferred)
- [ ] A12: Call response SLA defined and backup handler confirmed
- [ ] A12: Call log template created and shared with Rolland
- [ ] A12: Rolland confirms weekly data input commitment
- [ ] A13: Vera has completed RGPD consent review on both landing pages
- [ ] A13: ACPR advertising disclosure requirements confirmed for both products
- [ ] A13: ORIAS number visible on both landing pages AND in script ad copy
- [ ] A13: Google financial services policy confirmed for insurance products in France
- [ ] Phase 0.5: D1 ad group built, 20€/day budget set, call tracking confirmed working
- [ ] Phase 0.5: All gate metrics defined and tracking before first euro spent
- [ ] Open Question #1: Previous campaign data reviewed and CPL benchmarks updated
- [ ] Open Question #4: Real phone number in create_rolland_campaigns.py
- [ ] Agent authority table communicated to all operators

---

## Residual Risks (Accepted)

| Risk | Likelihood | Mitigation | Why Accepted |
|------|-----------|-----------|-------------|
| Google Ads account suspension | M | Vera daily health check, escalation protocol defined | No structural workaround exists for Google policy action. Mitigation is monitoring + fast response |
| Comparison platform CPC competition | M | Long-tail keyword focus, exact match priority, Quality Score improvement over time | New account disadvantage is temporary. Quality Score improves with data. Accepted with Phase 0.5 gate |
| Cultural transfer gap (US SLM → French market) | M | French avatar language validation step added to all copy review | Framework provides structure; French forum language research (B4) provides cultural calibration. Risk decreases after first iteration |
| Châtel window missed for Year 1 Senior peak | H | Seasonal budget rebalancing partially compensates | April launch means first Châtel peak is Nov 2026. Accepted — cannot change calendar |

---

## Attack Log

| # | Attack | Source | Severity | Resolution |
|---|--------|--------|---------|-----------|
| 1 | Budget-volume death spiral: 34€/day insufficient for 30-conv threshold | Inversionist | H | Fixed — Phase 0.5 micro-sprint gates full commitment |
| 2 | New account CPC penalty (QS 3–5 vs established 7–10) | Inversionist | H | Fixed — Phase 1 CPL targets revised to new-account benchmarks |
| 3 | Close layer accountability gap — leads die silently | Inversionist | H | Fixed — Zone A item A12: Close Layer Protocol + circuit breaker |
| 4 | GDPR/RGPD + ACPR compliance absent | Critic | H | Fixed — Zone A item A13 + Vera mandate expanded |
| 5 | Landing page conversion rate unknown before budget commit | Inversionist | H | Fixed — Phase 0.5 measures call rate before full launch |
| 6 | Seasonal budget asymmetry (Châtel window mismatch) | Inversionist | M | Fixed — seasonal budget rebalancing Apr–Oct vs Nov–Jan |
| 7 | Call duration ≥60s as contaminated proxy metric | Critic | M | Fixed — qualified lead redefined as Rolland-confirmed |
| 8 | CAI agent committee paralysis (10 agents, no tiebreaker) | Inversionist | M | Fixed — single decision authority table per domain |
| 9 | Cultural transfer risk (US frameworks → French market) | Critic | M | Accepted with mitigation — B4 avatar language research is mandatory |
| 10 | Google Ads account suspension (no fallback) | Inversionist | H | Accepted — monitoring + escalation protocol; no structural fix available |
| 11 | Comparison platform CPC competition | Inversionist | H | Accepted — Quality Score improves over time; Phase 0.5 gates entry |
| 12 | Second-order: scaling destroys the CPL that triggered scaling | Inversionist | M | Deferred — Felix's scaling gates (Gate 2) already address this; confirmed valid |
| 13 | Planning fallacy: Zone A timeline unrealistic | Critic | M | Fixed — A4 starts Day 1; Phase 0.5 adds buffer |
| 14 | Authority bias on SLM/CAI frameworks | Critic | M | Accepted with mitigation — B4 avatar research provides French-market grounding |

---

*Hardened by: Inversionist 🔄 + Critic 🎯 + Architect 🏛️*
*Adversarial session: 2026-04-12 | Iterations: 1 | Loop exit: all categories covered*
*Supersedes stress-test of: RA-LeadGen-Ecosystem-Map-v2.md*
