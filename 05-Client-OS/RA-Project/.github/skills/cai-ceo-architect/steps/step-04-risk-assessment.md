# Step 4: Risk Assessment

## Previous Step Check

Verify `stepsCompleted` includes 'step-03-strategic-direction'. If not, redirect to step-03.

## Load Strategic Context

Review the ecosystem priorities and strategic focus areas from previous step.

## Strategic Risk Identification

Systematically identify risks across 5 categories:

### 1. Market Risks

**Questions to ask:**

- Is the target market large enough to support growth goals?
- Are there seasonal fluctuations in demand?
- What if a competitor launches a similar offer?
- What if market conditions change (economy, regulation, technology)?

**Common Market Risks:**

- Market saturation
- Competitive response
- Regulatory changes
- Economic downturn
- Technology disruption

### 2. Execution Risks

**Questions to ask:**

- Do we have the team/skills to execute this strategy?
- What if content production falls behind schedule?
- What if ad creative doesn't resonate?
- What if conversion rates are lower than expected?

**Common Execution Risks:**

- Resource constraints (time, people, budget)
- Quality inconsistency
- Production delays
- Skill gaps
- Technology/platform dependencies

### 3. Financial Risks

**Questions to ask:**

- What if CAC increases beyond projections?
- What if LTV decreases (higher churn)?
- What if payback period extends beyond 12 months?
- What if we run out of budget before achieving profitability?

**Common Financial Risks:**

- CAC inflation
- LTV erosion
- Extended payback periods
- Cash flow constraints
- Budget overruns

### 4. Channel Risks

**Questions to ask:**

- What if our primary acquisition channel changes (algorithm, policy)?
- What if ad costs increase significantly?
- What if organic reach declines?
- What if our account gets suspended/banned?

**Common Channel Risks:**

- Platform algorithm changes
- Ad policy violations
- Account suspensions
- Rising competition (CPM increases)
- Channel saturation

### 5. Strategic Risks

**Questions to ask:**

- What if our positioning doesn't differentiate us?
- What if we're solving a problem people don't care about?
- What if our messaging doesn't resonate?
- What if we're targeting the wrong audience?

**Common Strategic Risks:**

- Poor product-market fit
- Weak value proposition
- Messaging misalignment
- Wrong target audience
- Competitive disadvantage

## Risk Scoring

For each identified risk, score on:

- **Likelihood:** Low (1), Medium (2), High (3)
- **Impact:** Low (1), Medium (2), High (3)
- **Risk Score:** Likelihood × Impact (1-9)

**Priority Levels:**

- High Priority (7-9): Address immediately
- Medium Priority (4-6): Mitigation plan required
- Low Priority (1-3): Monitor

## Mitigation Strategies

For each High and Medium priority risk, define mitigation strategy:

**Mitigation Types:**

1. **Avoid:** Don't pursue the risky action
2. **Reduce:** Take steps to lower likelihood or impact
3. **Transfer:** Use insurance, partnerships, or outsourcing
4. **Accept:** Acknowledge and monitor

**Example Mitigation:**

```
Risk: Ad account suspension (Likelihood: 2, Impact: 3, Score: 6)
Mitigation:
- Reduce: Diversify across 2-3 ad platforms
- Reduce: Follow platform policies strictly, get pre-review
- Transfer: Use agency ad account with backup access
- Accept: Keep 3-month cash reserve for organic-only period
```

## Risk Register

Create a risk register with all identified risks:

| Risk                  | Category  | L   | I   | Score | Priority | Mitigation                             |
| --------------------- | --------- | --- | --- | ----- | -------- | -------------------------------------- |
| CAC inflation         | Financial | 3   | 3   | 9     | High     | Diversify channels, improve conversion |
| Algorithm change      | Channel   | 2   | 3   | 6     | Medium   | Multi-platform strategy                |
| Quality inconsistency | Execution | 2   | 2   | 4     | Medium   | Quality checklists, peer review        |

## Update Output File

Add risk assessment section:

```markdown
## Risk Assessment

### High Priority Risks (Score 7-9)

1. **[Risk Name]** ([Category])
   - Likelihood: [Low/Medium/High]
   - Impact: [Low/Medium/High]
   - Mitigation: [Strategy]

2. **[Risk Name]** ([Category])
   - Likelihood: [Low/Medium/High]
   - Impact: [Low/Medium/High]
   - Mitigation: [Strategy]

### Medium Priority Risks (Score 4-6)

[List with mitigations]

### Low Priority Risks (Score 1-3)

[List for monitoring]

### Risk Monitoring Plan

- Weekly: Review high priority risks
- Monthly: Update risk scores based on new data
- Quarterly: Full risk register review
```

Update frontmatter:

```yaml
stepsCompleted:
  [
    'step-01-init',
    'step-02-business-model-validation',
    'step-03-strategic-direction',
    'step-04-risk-assessment',
  ]
highPriorityRisks: [list of risk names]
riskCount: { total_risks_identified }
```

## Menu

- **[n]** Next step (Resource Allocation)
- **[b]** Back to strategic direction
- **[a]** Add more risks
- **[r]** Revise risk scores
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-05-resource-allocation.md`
