# Step 3: 3-Layer Diagnosis

**Objective:** Identify exactly where each asset is failing or succeeding using the Hook → Retention → Reward framework.

## Instructions

### 1. Previous Step Check

Verify `stepsCompleted` includes `2`. If not, redirect to step-02.

### 2. The 3-Layer Diagnosis Framework

Every piece of content or ad fails at one of three layers. Identify the failure layer before recommending any fix.

```
Layer 1: HOOK (Did they stop?)
  Signal: Impressions vs. Engagement / CTR
  Question: "Did the hook stop the scroll or get the click?"
  Metric: CTR, Engagement Rate (first line/frame)

Layer 2: RETENTION (Did they stay?)
  Signal: Avg. View Duration / Read Depth / Time on Page
  Question: "Did the content hold their attention all the way through?"
  Metric: Completion rate, saves, full reads

Layer 3: REWARD (Did they act?)
  Signal: Clicks, Leads, DMs, Conversions
  Question: "Did the payoff reward their attention with value?"
  Metric: CTR on CTA, leads generated, conversions
```

**Diagnosis Rule:**

- If impressions are HIGH but engagement/CTR is LOW → **Hook failure**
- If CTR is HIGH but conversion/lead rate is LOW → **Retention failure** (they clicked but didn't convert) OR **Reward failure** (bad landing page/offer)
- If everything is high but sales are low → **Reward failure** (wrong audience or weak offer)

### 3. Diagnose Each Asset

For each content asset:

```
Asset: [Name]
─────────────────────────
Layer 1 — HOOK Analysis:
  Impressions: {count}
  Engagement Rate: {%} (benchmark: 1-3%)
  First-line CTR (if measurable): {%}
  Hook Diagnosis: [PASS / WEAK / FAIL]

  If FAIL/WEAK: Root cause?
  - [ ] Hook headline was unclear or generic
  - [ ] No pattern interrupt (looked like every other post)
  - [ ] Wrong hook style for this audience
  - [ ] Poor visual/thumbnail
  - [ ] Posted at wrong time

Layer 2 — RETENTION Analysis:
  Avg. View Duration / Read Depth: {%}
  Comments (signal of full consumption): {count}
  Saves (signal of high value): {count}
  Retention Diagnosis: [PASS / WEAK / FAIL]

  If FAIL/WEAK: Root cause?
  - [ ] Content didn't deliver on the hook's promise
  - [ ] Too long / too dense (poor value-per-second)
  - [ ] No retention mechanics (no loops, lists, stories)
  - [ ] Structure was confusing
  - [ ] Audience wasn't the right fit

Layer 3 — REWARD Analysis:
  Clicks / CTA conversions: {count}
  Leads generated: {count}
  CTR on CTA: {%}
  Reward Diagnosis: [PASS / WEAK / FAIL]

  If FAIL/WEAK: Root cause?
  - [ ] CTA was weak, unclear, or missing
  - [ ] Offer wasn't valuable enough for the ask
  - [ ] Landing page didn't match the content promise
  - [ ] Asked too soon (Give:Ask ratio imbalance)
  - [ ] Wrong conversion mechanism for audience stage

PRIMARY FAILURE LAYER: [Hook / Retention / Reward / None — All Green]
```

For each ad campaign:

```
Campaign: [Name]
─────────────────────────
Layer 1 — HOOK Analysis (Ad Creative):
  CTR: {%} (benchmark: 0.3-1.5%)
  Impressions: {count}
  Hook Diagnosis: [PASS / WEAK / FAIL]

  If FAIL/WEAK: Root cause?
  - [ ] Headline doesn't call out the right audience
  - [ ] No clear value proposition in first frame/line
  - [ ] Creative looks like an ad (no pattern interrupt)
  - [ ] Wrong targeting — shown to wrong people
  - [ ] Fatigue — ad has been running too long

Layer 2 — RETENTION Analysis (Landing Page):
  Lead page conversion rate: {%} (benchmark: 10-30% for lead gen)
  Time on landing page: {time}
  Retention Diagnosis: [PASS / WEAK / FAIL]

  If FAIL/WEAK: Root cause?
  - [ ] Landing page doesn't match ad's promise
  - [ ] Too much friction (too many form fields)
  - [ ] Trust signals missing (testimonials, logos)
  - [ ] Page loads too slowly
  - [ ] Offer isn't compelling enough

Layer 3 — REWARD Analysis (Lead → Customer):
  Lead-to-customer conversion rate: {%}
  CAC: ${amount}
  LTGP:CAC: {ratio}:1
  Reward Diagnosis: [PASS / WEAK / FAIL]

  If FAIL/WEAK: Root cause?
  - [ ] Lead quality is low (wrong audience at top)
  - [ ] Sales process is the bottleneck
  - [ ] Offer pricing doesn't align with audience's willingness to pay
  - [ ] Follow-up sequence is weak
  - [ ] Wrong traffic temperature (too cold for the ask)

PRIMARY FAILURE LAYER: [Hook / Retention / Reward / None — All Green]
```

### 4. Portfolio Diagnosis Summary

After diagnosing all assets, identify patterns:

```
Portfolio Patterns:
- Most common failure layer: [Hook / Retention / Reward]
- % of assets with Hook failures: {%}
- % of assets with Retention failures: {%}
- % of assets with Reward failures: {%}

System-Level Diagnosis:
[Are failures concentrated in one layer? If so, this points to a systemic issue]

Example:
"8 out of 10 content pieces have Hook failures → The team needs to improve
headline and opening line quality. This is a top-of-funnel attention problem,
not a content quality problem."
```

### 5. Winners Analysis

For top-performing assets, document WHY they worked:

```
Top Performer: [Name]
Reason It Worked:
- Hook: [What made it stop-the-scroll?]
- Retention: [What kept attention?]
- Reward: [What drove the action?]

Repeatable Pattern: [What can be templated and repeated?]
```

### 6. Update Output File

Add diagnosis section:

```markdown
## 3-Layer Diagnosis

### Content Assets Diagnosis

| Asset  | Hook           | Retention      | Reward         | Primary Failure | Root Cause |
| ------ | -------------- | -------------- | -------------- | --------------- | ---------- |
| [name] | PASS/WEAK/FAIL | PASS/WEAK/FAIL | PASS/WEAK/FAIL | [Layer]         | [Reason]   |

### Ad Campaigns Diagnosis

| Campaign | Hook (CTR)     | Retention (CVR) | Reward (LTGP:CAC) | Primary Failure | Root Cause |
| -------- | -------------- | --------------- | ----------------- | --------------- | ---------- |
| [name]   | PASS/WEAK/FAIL | PASS/WEAK/FAIL  | PASS/WEAK/FAIL    | [Layer]         | [Reason]   |

### Portfolio Patterns

**Most Common Failure Layer:** {layer}
**System Diagnosis:** {diagnosis}

### Winners: What Worked

**Top Content:** {name}

- Hook: {what worked}
- Retention: {what worked}
- Reward: {what worked}
- Template for reuse: {pattern}

**Top Campaign:** {name}

- Hook: {what worked}
- Retention: {what worked}
- Reward: {what worked}
- Template for reuse: {pattern}
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3]
primaryFailureLayer: [hook/retention/reward/none]
hookFailures: { count }
retentionFailures: { count }
rewardFailures: { count }
topPerformer: { name }
```

### 7. Present Menu

```
✓ Step 3 Complete: Diagnosis done
  Primary failure layer: {layer}
  Hook failures: {count}
  Retention failures: {count}
  Reward failures: {count}

[C] Continue to Iteration Directives
[R] Re-diagnose an asset
[X] Exit workflow
```

Wait for user selection.

### 8. Handle Selection

- **If [C]**: Update frontmatter, load `./step-04-iteration-directives.md`
- **If [R]**: Re-run diagnosis for a specific asset, then return to menu
- **If [X]**: Exit with "Workflow paused. Run this skill again to resume."

---

**END OF STEP 3**
