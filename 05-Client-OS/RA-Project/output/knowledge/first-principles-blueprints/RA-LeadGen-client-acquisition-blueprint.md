# First Principles Blueprint: RA-LeadGen — Small Broker Client Acquisition

**Date:** 2026-04-12
**Deconstruction iterations:** 1 (loop exit: all 6 axioms passed 4-part test)
**Assumptions eliminated:** 6 (Google Ads required, call-only format, call as first contact,
landing page as sole conversion point, SLM/CAI as axioms, 50/50 budget split, ≥60s = qualified)

---

## Problem (Axiomatic Restatement)

> How does an unknown small broker reduce a specific avatar's perceived risk low enough —
> fast enough, cheaply enough — that they initiate contact in a way he can close?

This is NOT "how do we generate phone calls from Google Ads."
The call is one mechanism. Phone-first contact is one convention.
The invariant: **trust must exceed the action threshold before contact happens.**

---

## The 6 Irreducible Axioms

| #   | Axiom                                                                              | Type                  |
| --- | ---------------------------------------------------------------------------------- | --------------------- |
| 1   | Rolland earns revenue only when a qualified conversation happens that he can close | Logical Necessity     |
| 2   | A prospect acts only when perceived benefit > perceived risk                       | Behavioral Law        |
| 3   | Perceived benefit/risk are functions of information transferred before the action  | Cognitive Law         |
| 4   | Rolland can only reach prospects where they actually are                           | Physical Law          |
| 5   | CAC must be less than LTV for the business to survive                              | Mathematical Identity |
| 6   | Two real, externally-validated problems exist (Châtel/Senior, ORIAS/BTP)           | Legal/Empirical Fact  |

## Assumptions Eliminated and Why

| Eliminated Assumption                 | Why It Was Not an Axiom                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Google Ads is required                | One channel among many; Seniors are on YouTube, Artisans in accountant networks. Axiom 4 replaces it.  |
| Phone call as first contact           | Convention. Cold inbound call has maximum perceived risk. First contact can be any low-barrier action. |
| Call-only ad format                   | Eliminates remarketing audiences, removes diagnostic data, assumes maximum trust at zero trust state   |
| Landing page as sole conversion point | One mechanism; WhatsApp, form, referral are equally valid trust-building surfaces                      |
| SLM/CAI as operating axioms           | Frameworks implement axioms — they don't replace them. Good frameworks, wrong classification.          |
| ≥60s call duration = qualified        | Proxy metric contaminated by price-shoppers and wrong numbers. Axiom 1 provides the real definition.   |
| 50/50 budget split                    | Symmetry has no axiomatic basis. Axiom 5 requires economics to work per segment, not equally.          |

---

## Solution         

The axiom-derived solution has two tracks:

**Primary Track (Weeks 1–4):** Restructure the contact architecture.
Google Search captures real intent (Axiom 4). The landing page builds trust before asking
for action (Axioms 2+3). The first conversion event is NOT a call — it is a WhatsApp message
or form submission ("Recevez votre devis en 2h"). Rolland's team responds in under 10 minutes
with a personalized answer to the avatar's specific problem. The CALL is step 3 — outbound
from Rolland, warm, with the avatar's problem already known. The stranger-turned-warm-lead is
now a consultation they requested. Close rate is structurally higher.

**Parallel Track (Month 2+):** Activate referral-source leverage.
Avatars already have trusted intermediaries: BTP artisans rely on accountants (experts-comptables)
and CAPEB; Seniors interact with CARSAT advisors, pharmacists, notaires. These intermediaries
have already built the trust that Rolland spends ad budget to simulate. Three to five referral
partnerships per segment generate pre-qualified, pre-trusted leads at near-zero CPL.

---

## Architecture

### Component Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ACQUISITION ARCHITECTURE                          │
│                    First Principles Edition                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [1] INTENT CAPTURE          [6] REFERRAL TRACK (Month 2+)          │
│  Google Search Ads            Accountants + CARSAT + Pharmacies      │
│  (commercial intent only)     (pre-trusted intermediaries)          │
│        ↓                               ↓                            │
│  [2] TRUST INTERFACE          ↓ (skip 1-3, leads arrive warm)       │
│  Landing Page                         ↓                             │
│  (face, ORIAS, testimonials,          ↓                             │
│   specific problem, credentials)      ↓                             │
│        ↓                              ↓                             │
│  [3] LOW-BARRIER FIRST CONTACT        ↓                             │
│  WhatsApp button + 2-field form       ↓                             │
│  "Recevez votre devis en 2h"          ↓                             │
│        ↓                              ↓                             │
│  ──────────────────────────────────────                             │
│                      ↓                                              │
│  [4] WARM CALL PROTOCOL                                             │
│  Rolland team — outbound, 10-min SLA                                │
│  Opens with: "I saw your question about X — here's the answer"      │
│  NOT: "You clicked our ad"                                          │
│                      ↓                                              │
│  [5] CLOSE + FEEDBACK                                               │
│  Contract OR Lost-deal record (with reason)                         │
│  Weekly: close rate + lost reasons → feed upstream optimization     │
└─────────────────────────────────────────────────────────────────────┘
```

### Dependency Map

```
[1] Intent Capture      → requires → [2] Landing Page to receive traffic
[2] Trust Interface     → requires → [3] First Contact to capture intent
[3] First Contact       → requires → [4] Warm Call to close the loop
[4] Warm Call           → requires → [5] Feedback to track and improve
[5] Feedback            → feeds    → [1][2][3] upstream optimization

[6] Referral Track      → independent of [1][2][3]
                        → feeds directly into [4] Warm Call
```

---

## Critical Path

### Phase 1 — Foundation Redesign (Week 1–2, before any paid spend)

- [ ] Add WhatsApp Business button to both landing pages (free, 2-hour setup)
- [ ] Add "devis en 2h" form: name + phone + one-line problem description (2 fields max)
- [ ] Define 10-minute response SLA; assign to specific person on Rolland's team
- [ ] Create outbound warm call script (problem-first opening, not ad-reference opening)
- [ ] Switch Google Ads targeting: call-only → search ads with landing page destination
- [ ] Track form submissions + WhatsApp initiations as PRIMARY conversions in GA4
- [ ] Track inbound calls as SECONDARY conversion (not eliminated, just demoted)
- [ ] Qualified lead redefined: Rolland-confirmed within 24h (not ≥60s duration proxy)

### Phase 2 — Micro-Validation Sprint (Weeks 2–3, 400€ max)

- [ ] Run D1 ad group only (Urgence attestation, 20€/day × 14 days)
- [ ] Measure THREE diagnostic layers:
  - Click → form/WhatsApp initiation rate (Component 2 quality)
  - Form → warm call completed rate (Component 3+4 quality)
  - Warm call → close rate (Component 4+5 quality)
- [ ] Gate: if form rate >15% AND close rate >20% → proceed to full launch
- [ ] Gate fail: diagnose which layer broke before committing 1,500€/month

### Phase 3 — Full Launch (Week 4, post-validation)

- [ ] Both campaigns live with revised CPL targets (Senior <55€, BTP <80€ — new account reality)
- [ ] Seasonal budget: BTP 65% / Senior 35% until November
- [ ] Weekly: Rolland submits call log (mandatory — close rate data required for Felix)

### Phase 4 — Referral Track Activation (Month 2)

- [ ] Identify first 3 BTP accountants in Rolland's geographic zone
  (Method: ask current BTP clients "who does your accounting?")
- [ ] Identify first 2 Senior intermediaries (CARSAT advisor or pharmacist in zone)
- [ ] Create one-page referral brief: who Rolland helps + what happens when you refer
- [ ] Activate informally: "Send me your client, I handle everything, I'll update you"
- [ ] Create dedicated landing page URL per referral source (/from/[partner-name])
  for attribution and thank-you personalization
- [ ] Track: referred leads close rate vs paid leads close rate
- [ ] Month 3 decision: if referral close rate >2× paid → expand referral, reduce paid spend

---

## Implementation Requirements

**For Phase 1 (immediate, low cost):**
- WhatsApp Business account for Rolland Assurances (free)
- Landing page edit capability (2-4 hours dev time)
- Rolland commits to 10-minute response SLA during ad hours
- 1 person designated as "first response" for form/WhatsApp

**For Phase 4 (referral track, medium effort):**
- Rolland's time: ~3 hours/week for relationship-building conversations
- Simple CRM or spreadsheet to track referral source per lead
- Personalized landing page URLs per partner (one URL parameter change)

**What the plan does NOT need to change:**
- Google Ads as the primary paid channel (still the best high-intent source)
- SLM and CAI as production frameworks (still valid implementation tools)
- Avatar definitions (Axiom 6 confirms they are real)
- Budget total (1,500€/month remains the resource limit)
- Agent structure (CAI agents serve the architecture, not vice versa)

---

## Validation: Axiom Compliance

| Axiom | Satisfied by |
|-------|-------------|
| 1: Conversation before revenue | Component 4 (Warm Call) — now outbound from Rolland with context |
| 2: Benefit > Risk before action | Component 2 (trust-building LP) + Component 3 (low-barrier first contact) |
| 3: Information transfer changes decision | LP delivers ORIAS, credentials, face, testimonials before any ask; referral transfers pre-existing trust |
| 4: Reach avatars where they are | Component 1 (Google search intent) + Component 6 (accountants/CARSAT already with avatars) |
| 5: CAC < LTV | Warm call close rate 2-3× cold call → better economics at same CPL; referral track near-zero CPL |
| 6: Two real avatar problems exist | Validated by Châtel law (Senior) and ORIAS regulation (BTP) — unchanged |

---

## The One Structural Insight This Analysis Produces

> **The current plan is built backwards.**
>
> It assumes the phone call is the trust-building mechanism.
> First principles says trust must be built BEFORE contact.
>
> A stranger receiving a cold inbound call is at maximum perceived risk.
> They don't know Rolland. They don't know his credentials. They have no social proof.
> They are deciding whether to give personal financial information to a voice they've
> never encountered. This is the hardest possible moment to close.
>
> The fix is not better ad copy. It is architectural:
> **move trust-building earlier in the sequence, and move the call to after trust exists.**
>
> Form/WhatsApp first. Personalized response in 10 minutes. Outbound warm call.
> "I saw your question about [specific problem] — here's exactly what I'd do."
>
> That call opens with Rolland already knowing the avatar's problem.
> The avatar already received a useful response.
> Perceived risk has dropped. Perceived benefit has risen.
> The conversation starts in a fundamentally different place.

---

## Residual Assumptions (Acknowledged, Not Resolved)

| Assumption                                                    | Status                                                                               | How to Test                                        |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------- |
| WhatsApp form rate > inbound call rate from same landing page | Unvalidated                                                                          | A/B test during micro-sprint                       |
| Accountants will refer clients without a financial incentive  | Unvalidated                                                                          | 3 conversations in Month 2 will confirm or deny    |
| Rolland's team can maintain 10-min response SLA               | Unvalidated                                                                          | Must be confirmed before Phase 1 launch            |
| Warm call close rate > cold call close rate                   | Directionally true per behavioral economics but unvalidated for this specific market | Compare Phase 1 data vs historical call close rate |

---

*Blueprint by: Thinker 🧠 + Engineer ⚙️ + Architect 🏛️*
*First Principles session: 2026-04-12 | Iterations: 1*
*Input: RA-LeadGen-Ecosystem-Map-v2.md*
*Output: Trust-First Acquisition Architecture with Referral Parallel Track*
