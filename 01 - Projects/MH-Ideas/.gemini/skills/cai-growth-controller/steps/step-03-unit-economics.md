# Step 3: Unit Economics Analysis

## Previous Step Check

Verify `stepsCompleted` includes 'step-02-metrics-collection'. If not, redirect to step-02.

## Load Financial Metrics

Review collected metrics:

- CAC: ${cac}
- LTGP: ${ltgp}
- Revenue: ${revenue}
- Spend: ${spend}

## The LTGP:CAC Framework

The single most important metric for scaling decisions.

### What It Means

```
LTGP:CAC Ratio = Lifetime Gross Profit / Customer Acquisition Cost

This answers: "For every $1 spent acquiring a customer,
              how much gross profit do we make?"
```

### Interpretation Bands

**9:1 or higher - EXCEPTIONAL**

```
Status: 🟢 Elite Performance
Signal: You have massive pricing power or extremely efficient acquisition
Action: Scale aggressively, you're leaving money on the table if you don't
Risk: Market opportunity may not last, competition will notice
```

**7:1 to 8:9 - EXCELLENT**

```
Status: 🟢 Green Light for Scaling
Signal: Very healthy economics, strong moat
Action: Invest heavily in acquisition, scale confidently
Risk: Monitor for CAC inflation as you scale
```

**5:1 to 6:9 - VERY GOOD**

```
Status: 🟢 Safe to Scale
Signal: Solid economics, sustainable growth
Action: Measured scaling, increase budget 2-3x per cycle
Risk: Watch payback period, maintain quality
```

**3:1 to 4:9 - VIABLE**

```
Status: 🟡 Proceed with Caution
Signal: Economics work but margins are tight
Action: Small to moderate scaling, test carefully
Risk: Any CAC increase makes it unprofitable
```

**2:1 to 2:9 - MARGINAL**

```
Status: 🟠 High Risk
Signal: Barely profitable, very fragile
Action: Focus on improving LTV or reducing CAC first
Risk: Most channels will be unprofitable here
```

**Below 2:1 - UNPROFITABLE**

```
Status: 🔴 Do Not Scale
Signal: Losing money on every customer
Action: STOP paid acquisition, fix the model
Risk: Scaling will accelerate losses
```

### Your Status

```
LTGP: ${ltgp}
CAC: ${cac}
Ratio: {ratio}:1

Status: {status}
Band: {band}
```

## Payback Period Analysis

How long does it take to recover the CAC?

### Calculation

```
Monthly Profit per Customer = (Deal Size / Lifetime Months) × Gross Margin %
Payback Period = CAC / Monthly Profit

Your Numbers:
Monthly Profit = (${deal_size} / {lifetime}) × {margin}%
               = ${monthly_profit}

Payback = ${cac} / ${monthly_profit}
        = {payback_months} months
```

### Interpretation

**0-6 months - EXCELLENT**

- Fast cash recovery
- Low working capital needs
- Can scale aggressively

**6-12 months - GOOD**

- Standard for most B2B
- Manageable cash flow
- Moderate scaling pace

**12-18 months - CAUTION**

- Requires significant working capital
- Slow scaling recommended
- Monitor cash closely

**18+ months - RISKY**

- Heavy capital requirements
- Churn risk high
- Not suitable for most businesses

**Your Payback:** {months} months ({status})

## Break-Even Analysis

How many months until you're profitable overall?

```
Total Invested: ${total_spend}
Monthly Profit from Cohort: ${monthly_cohort_profit}

Break-Even Point = Total Invested / Monthly Profit
                 = ${total_spend} / ${monthly_profit}
                 = {breakeven_months} months
```

## Profitability Diagnosis

Based on unit economics, diagnose the current state:

### Scenario 1: LTGP:CAC > 5:1, Payback < 12 months

```
✅ DIAGNOSIS: Healthy Growth Machine

Strengths:
- Strong unit economics
- Fast payback
- Safe to scale

Recommendation:
→ Increase ad budget 3-5x
→ Expand to new channels
→ Test higher-funnel strategies
```

### Scenario 2: LTGP:CAC 3:1-5:1, Payback < 12 months

```
✅ DIAGNOSIS: Viable with Optimization Opportunity

Strengths:
- Economics work
- Reasonable payback

Weaknesses:
- Margins could be better

Recommendation:
→ Scale cautiously (2x budget increases)
→ Focus on improving LTV (upsells, retention)
→ Optimize CAC (better targeting, creative)
```

### Scenario 3: LTGP:CAC < 3:1 OR Payback > 12 months

```
⚠️ DIAGNOSIS: Needs Structural Improvement

Problems:
- Tight margins or slow payback
- High scaling risk

Recommendation:
→ PAUSE scaling
→ Fix unit economics first:
  - Increase prices
  - Reduce CAC (better targeting)
  - Improve conversion rates
  - Extend customer lifetime
→ Re-run this analysis after improvements
```

## Update Output File

```markdown
## Unit Economics Analysis

### LTGP:CAC Ratio: {ratio}:1

**Status:** {band}
**Assessment:** {assessment}

### Ratio Breakdown

- Lifetime Gross Profit: ${ltgp}
- Customer Acquisition Cost: ${cac}
- Ratio: {ratio}:1

**Interpretation:** {interpretation}

### Payback Period: {months} months

**Status:** {status}
**Cash Flow Impact:** {impact}

### Break-Even Analysis

- Total invested: ${spend}
- Monthly cohort profit: ${profit}
- Break-even in: {months} months

### Diagnosis: {diagnosis_title}

{diagnosis_details}

### Recommendation

{scaling_recommendation}
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02-metrics-collection', 'step-03-unit-economics']
ltgpCacRatio: { ratio }
economicsStatus: [excellent/good/viable/marginal/unprofitable]
paybackMonths: { months }
scalingRecommendation: [scale-aggressively/scale-cautiously/pause-and-fix]
```

## Menu

- **[n]** Next step (Scaling Readiness)
- **[b]** Back to metrics collection
- **[w]** What-if scenarios (adjust numbers)
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-04-scaling-readiness.md`
