# Step 2: Business Model Validation

## Previous Step Check

Verify `stepsCompleted` includes 'step-01-init'. If not, redirect to step-01-init.md.

## Load Business Context

Read the strategic plan output file to review:

- Core offering and revenue model
- Current revenue and CAC
- Target customer profile
- Growth targets

## Unit Economics Analysis

### 1. LTGP:CAC Ratio Calculation

Calculate the Lifetime Gross Profit to Customer Acquisition Cost ratio:

**Formula:**

```
LTGP = (Average Deal Size × Gross Margin %) × (Average Customer Lifetime in months / 12)
LTGP:CAC Ratio = LTGP / CAC

Minimum Viable: 3:1
Healthy: 5:1+
Excellent: 7:1+
```

**Questions to ask:**

- What is the average deal size?
- What is the gross margin percentage?
- What is the average customer lifetime (months)?
- What is the current CAC?

**Calculate and present:**

```
LTGP = ${average_deal_size} × {gross_margin}% × ({lifetime_months} / 12)
     = ${ltgp_value}

LTGP:CAC = ${ltgp_value} / ${cac}
         = {ratio}:1

Status: [Excellent/Healthy/Viable/WARNING]
```

### 2. Payback Period

Calculate how long it takes to recover CAC:

**Formula:**

```
Monthly Profit per Customer = (Deal Size / Lifetime Months) × Gross Margin %
Payback Period = CAC / Monthly Profit per Customer
```

**Target:** 12 months or less for healthy businesses

### 3. Give:Ask Ratio Validation

For content-based acquisition strategies, validate the 3.5:1 Give:Ask ratio:

- Count of free value content pieces planned
- Count of direct ask/commercial pieces planned
- Ratio: Should be at least 3.5 free for every 1 ask

## Business Model Verdict

Based on the calculations above, provide strategic guidance:

**If LTGP:CAC < 3:1:**

```
⚠️ STRATEGIC RISK: Unit economics are not viable for scaling.

Recommendation:
- PAUSE paid acquisition until CAC improves OR LTV increases
- Focus on organic/free channels only
- Prioritize improving conversion rates and retention
- Revisit this workflow when metrics improve
```

**If LTGP:CAC 3:1 to 5:1:**

```
✅ PROCEED WITH CAUTION: Unit economics are viable but tight.

Recommendation:
- Start with small budget tests ($500-$2000/month)
- Monitor metrics weekly
- Focus on high-intent, bottom-of-funnel acquisition
- Build organic foundation in parallel
```

**If LTGP:CAC > 5:1:**

```
✅ GREEN LIGHT: Excellent unit economics for scaling.

Recommendation:
- Aggressive acquisition investment is justified
- Can support longer payback periods
- Can invest in top-of-funnel brand building
- Ready for scaling phases
```

## Update Output File

Add business model validation section:

```markdown
## Business Model Validation

### Unit Economics

- **LTGP:** ${ltgp_value}
- **CAC:** ${cac}
- **LTGP:CAC Ratio:** {ratio}:1
- **Status:** [Verdict]
- **Payback Period:** {months} months

### Strategic Recommendation

[Recommendation based on ratio]

### Give:Ask Ratio

- Free content planned: {count}
- Ask content planned: {count}
- Ratio: {ratio}:1
- Status: [COMPLIANT/NEEDS ADJUSTMENT]
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02-business-model-validation']
ltgpCacRatio: { ratio }
businessModelStatus: [viable/caution/risk]
```

## Menu

- **[n]** Next step (Strategic Direction)
- **[b]** Back to initialization
- **[r]** Recalculate with different inputs
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-03-strategic-direction.md`
