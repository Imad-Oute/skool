# Step 4: Scaling Readiness Assessment

## Previous Step Check

Verify `stepsCompleted` includes 'step-03-unit-economics'. If not, redirect to step-03.

## Load Unit Economics Context

Review from previous step:

- LTGP:CAC ratio: {ratio}:1
- Payback period: {months} months
- Scaling recommendation: {recommendation}

## The Scaling Readiness Checklist

Before increasing budget, validate readiness across 5 dimensions:

### Dimension 1: Financial Readiness

Score each item (0 = No, 1 = Partial, 2 = Yes):

- [ ] LTGP:CAC ratio ≥ 3:1 (Minimum viable)
- [ ] Payback period ≤ 12 months
- [ ] Positive unit economics confirmed over 60+ days (not a fluke)
- [ ] Cash reserves to fund 2-3x budget increase for 90 days
- [ ] Revenue from acquisition reinvestable into more acquisition

**Financial Readiness Score: {score}/10**

### Dimension 2: Data Confidence

Score each item (0 = No, 1 = Partial, 2 = Yes):

- [ ] ≥ 20 customers acquired (statistically meaningful sample)
- [ ] Consistent results across 3+ ad creatives/content pieces
- [ ] Lead source attribution is accurate (tracking working)
- [ ] Conversion rate is stable (not volatile week-to-week)
- [ ] Metrics have been consistent for ≥ 30 days

**Data Confidence Score: {score}/10**

### Dimension 3: Operations Capacity

Score each item (0 = No, 1 = Partial, 2 = Yes):

- [ ] Content production can scale (templates, systems, team)
- [ ] Ad management can handle more campaigns
- [ ] Lead handling process works at current volume
- [ ] Sales/conversion process won't break with more leads
- [ ] Reporting and tracking can scale

**Operations Score: {score}/10**

### Dimension 4: Market Opportunity

Score each item (0 = No, 1 = Partial, 2 = Yes):

- [ ] Target market is large enough to absorb more spend
- [ ] Current channels have remaining scale headroom
- [ ] CPM/CPL has not significantly increased (market not saturated)
- [ ] No major competitive threats emerging
- [ ] Seasonal timing is favorable

**Market Score: {score}/10**

### Dimension 5: Risk Controls

Score each item (0 = No, 1 = Partial, 2 = Yes):

- [ ] Stop-loss trigger defined (e.g., "Pause if LTGP:CAC drops below 2:1")
- [ ] Weekly financial review scheduled
- [ ] Budget caps set in all ad platforms
- [ ] Backup channels identified if primary fails
- [ ] Team aligned on scaling plan

**Risk Control Score: {score}/10**

## Scaling Readiness Score

Calculate overall readiness:

```
Total Score = Financial + Data + Operations + Market + Risk Controls
            = {f} + {d} + {o} + {m} + {r}
            = {total}/50

Percentage = {total}/50 × 100 = {percentage}%
```

**Readiness Levels:**

- 80-100% → ✅ READY TO SCALE — All systems go
- 60-79% → ⚠️ CONDITIONALLY READY — Address gaps before scaling
- 40-59% → 🟡 NOT READY — Fix critical gaps first
- < 40% → 🔴 DO NOT SCALE — Fundamental issues must be resolved

## Readiness Verdict

Based on the score, provide verdict:

**If READY (80-100%):**

```
✅ SCALING VERDICT: GREEN LIGHT

Your operations are ready for budget increases.
Key Strengths:
- [Top 3 reasons they're ready]

Recommended Scale-Up:
- Immediate: Increase budget by 2x
- Month 2: Evaluate and increase by 1.5-2x if metrics hold
- Month 3: Consider 3-5x from original if still profitable
```

**If CONDITIONALLY READY (60-79%):**

```
⚠️ SCALING VERDICT: PROCEED WITH CAUTION

You can scale, but address these gaps first:
- [List gaps with scores < 1.5 average]

Recommended Scale-Up:
- Modest: Increase budget by 1.5x only
- Resolve identified gaps within 30 days
- Re-assess before further scaling
```

**If NOT READY (< 60%):**

```
🔴 SCALING VERDICT: NOT YET

Critical gaps must be resolved before scaling:
- [List all dimensions with score < 6/10]

Action Required:
- DO NOT increase budget
- Fix identified gaps in next 30 days
- Re-run Growth Controller after fixes
```

## Update Output File

Add scaling readiness section:

```markdown
## Scaling Readiness Assessment

### Overall Readiness Score: {percentage}%

**Verdict:** [READY/CONDITIONALLY READY/NOT READY]

### Dimension Scores

| Dimension           | Score          | Status        |
| ------------------- | -------------- | ------------- |
| Financial Readiness | {score}/10     | {status}      |
| Data Confidence     | {score}/10     | {status}      |
| Operations Capacity | {score}/10     | {status}      |
| Market Opportunity  | {score}/10     | {status}      |
| Risk Controls       | {score}/10     | {status}      |
| **Total**           | **{total}/50** | **{verdict}** |

### Critical Gaps (Score < 6/10)

{list of gaps or "None — all dimensions strong"}

### Scaling Recommendation

{recommendation_text}
```

Update frontmatter:

```yaml
stepsCompleted:
  [
    'step-01-init',
    'step-02-metrics-collection',
    'step-03-unit-economics',
    'step-04-scaling-readiness',
  ]
readinessScore: { percentage }
scalingVerdict: [ready/conditional/not-ready]
```

## Menu

- **[n]** Next step (Scaling Plan)
- **[b]** Back to unit economics
- **[r]** Re-score readiness dimensions
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-05-scaling-plan.md`

---

**END OF STEP 4**
