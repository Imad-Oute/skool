# Step 5: Scaling Plan

## Previous Step Check

Verify `stepsCompleted` includes 'step-04-scaling-readiness'. If not, redirect to step-04.

## Load Readiness Context

Review from previous step:

- Readiness score: {percentage}%
- Scaling verdict: {verdict}
- Current monthly budget: ${current_budget}
- LTGP:CAC ratio: {ratio}:1

## Define the Scaling Budget

### Current Baseline

Ask the user to confirm current spend:

- Current monthly ad spend: ${amount}
- Current monthly content production cost: ${amount}
- Total current acquisition budget: ${total}

### The Track → Invest → Print Framework

**Phase 1: Track (Testing)**

- Budget: $500 - $2,000/month
- Goal: Establish baseline metrics, find winning creative/copy
- Duration: 30-60 days
- Success criteria: LTGP:CAC ≥ 3:1 consistently

**Phase 2: Invest (Scaling)**

- Budget: $2,000 - $10,000/month
- Goal: Scale winning campaigns, increase volume
- Duration: 60-90 days
- Success criteria: LTGP:CAC maintained ≥ 3:1 at higher volume

**Phase 3: Print (Aggressive Scaling)**

- Budget: $10,000+/month
- Goal: Maximum market penetration with profitable economics
- Duration: Ongoing while metrics hold
- Success criteria: LTGP:CAC ≥ 5:1 and growing

### Determine Current Phase

Based on readiness assessment and current budget, identify phase:

```
Current Budget: ${current_budget}/month
LTGP:CAC: {ratio}:1
Current Phase: [Track/Invest/Print]
```

## Budget Scaling Model

### Conservative Scaling (Recommended for LTGP:CAC 3:1-5:1)

```
Month 1: ${current} → ${current × 1.5} (50% increase)
Month 2: Evaluate → if LTGP:CAC holds, increase to ${current × 2.25}
Month 3: Evaluate → if still profitable, increase to ${current × 3.4}

Rule: Never increase more than 2x in a single month
```

### Aggressive Scaling (For LTGP:CAC > 5:1)

```
Month 1: ${current} → ${current × 2} (2x increase)
Month 2: Evaluate → if LTGP:CAC holds, increase to ${current × 4}
Month 3: Evaluate → if still profitable, increase to ${current × 6-8}

Rule: Double budget monthly while metrics hold
```

### Optimization Mode (For LTGP:CAC < 3:1)

```
Month 1: Maintain current budget, focus on CRO and creative testing
Month 2: If metrics improve to 3:1, begin conservative scaling
Goal: Fix economics BEFORE increasing spend
```

## The Scaling Budget

Based on readiness verdict, define the scaling plan:

### Recommended Budget Allocation

**Total Monthly Budget: ${total_budget}**

| Category           | Budget    | Percentage | Purpose                 |
| ------------------ | --------- | ---------- | ----------------------- |
| Paid Ads           | ${amount} | {%}%       | Predictable lead flow   |
| Content Production | ${amount} | {%}%       | Organic foundation      |
| Landing Pages/CRO  | ${amount} | {%}%       | Conversion optimization |
| Tools/Software     | ${amount} | {%}%       | Infrastructure          |
| Buffer/Testing     | ${amount} | {%}%       | New channel tests       |

### Platform Budget Split

For paid ads, allocate by platform based on performance:

```
Primary Channel (best LTGP:CAC): ${amount} ({%}%)
Secondary Channel (testing): ${amount} ({%}%)
New Platform Test: ${amount} ({%}%)
```

## Financial Guardrails

Define automatic stop-loss triggers:

### Hard Stops (Automatic Pause)

- LTGP:CAC drops below 2:1 for 2 consecutive weeks → PAUSE ALL PAID ADS
- CPL increases > 50% from baseline → PAUSE and audit
- Monthly spend exceeds budget cap → STOP
- ROAS (if measurable) drops below 2x → PAUSE

### Soft Alerts (Review Required)

- LTGP:CAC drops from target by 20% → Review required
- Lead volume drops > 30% week-over-week → Investigate
- CAC increases > 25% from baseline → Strategic review

### Review Cadence

- **Weekly:** Check CPL, leads generated, ad spend vs. budget
- **Monthly:** Full LTGP:CAC calculation, readiness re-score
- **Quarterly:** Strategic direction review, phase assessment

## Scaling Timeline

Create a 90-day scaling roadmap:

```
Month 1 Goals:
- Budget: ${month1_budget}
- Target leads: {count}
- Target CAC: ${amount}
- Actions: {list key actions}

Month 2 Goals:
- Budget: ${month2_budget} (if Month 1 metrics hold)
- Target leads: {count}
- Target CAC: ${amount}
- Decision point: Scale further or optimize

Month 3 Goals:
- Budget: ${month3_budget} (if Month 2 metrics hold)
- Target leads: {count}
- Target CAC: ${amount}
- Decision point: Enter next phase or maintain
```

## Update Output File

Add scaling plan section:

```markdown
## Scaling Plan

### Current Phase: {track/invest/print}

**Budget Starting Point:** ${current_budget}/month
**Recommended Next Budget:** ${next_budget}/month

### 90-Day Scaling Roadmap

| Month   | Budget    | Target Leads | Target CAC | Decision Point |
| ------- | --------- | ------------ | ---------- | -------------- |
| Month 1 | ${budget} | {count}      | ${cac}     | {criteria}     |
| Month 2 | ${budget} | {count}      | ${cac}     | {criteria}     |
| Month 3 | ${budget} | {count}      | ${cac}     | {criteria}     |

### Budget Allocation (Month 1)

- Paid Ads: ${amount} ({%}%)
- Content: ${amount} ({%}%)
- CRO/LPs: ${amount} ({%}%)
- Tools: ${amount} ({%}%)
- Buffer: ${amount} ({%}%)

### Financial Guardrails

**Hard Stops:**

1. LTGP:CAC < 2:1 for 2 weeks → PAUSE
2. CPL > 50% above baseline → PAUSE and audit
3. Monthly spend > ${cap} → STOP

**Soft Alerts:**

1. LTGP:CAC drops 20% → Review
2. Lead volume drops 30% → Investigate
```

Update frontmatter:

```yaml
stepsCompleted:
  [
    'step-01-init',
    'step-02-metrics-collection',
    'step-03-unit-economics',
    'step-04-scaling-readiness',
    'step-05-scaling-plan',
  ]
currentPhase: { track/invest/print }
month1Budget: { amount }
month2Budget: { amount }
month3Budget: { amount }
scalingStrategy: [conservative/aggressive/optimize]
```

## Menu

- **[n]** Next step (Finalize Growth Plan)
- **[b]** Back to scaling readiness
- **[r]** Revise budget allocations
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-06-finalize.md`

---

**END OF STEP 5**
