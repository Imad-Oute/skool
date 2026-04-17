# Step 2: Metrics Collection

## Previous Step Check

Verify `stepsCompleted` includes 'step-01-init'. If not, redirect to step-01.

## Load Review Context

Review the time period and purpose from step-01.

## Key Metrics to Collect

### 1. Lead Generation Metrics

**Ask the user to provide:**

- Total leads generated: {count}
- Lead sources breakdown:
  - Organic content: {count} leads
  - Paid ads: {count} leads
  - Other channels: {count} leads

### 2. Spend Metrics

**Ask the user to provide:**

- Total ad spend: ${amount}
- Spend by platform:
  - Facebook/Instagram: ${amount}
  - LinkedIn: ${amount}
  - Google: ${amount}
  - Other: ${amount}
- Content production costs: ${amount} (optional)
- Tool/software costs: ${amount}

### 3. Revenue Metrics

**Ask the user to provide:**

- Revenue generated from acquired leads: ${amount}
- Average deal size: ${amount}
- Number of closed customers: {count}
- Gross margin percentage: {percentage}%

### 4. Customer Lifetime Metrics

**Ask the user to provide:**

- Average customer lifetime: {months} months
- Churn rate (if applicable): {percentage}% per month
- Repeat purchase rate: {percentage}% (if applicable)
- Upsell/cross-sell rate: {percentage}% (if applicable)

### 5. Conversion Metrics

**Ask the user to provide:**

- Lead-to-customer conversion rate: {percentage}%
- Time to conversion (sales cycle): {days} days
- Current pipeline value: ${amount}

## Calculate Derived Metrics

### Cost Per Lead (CPL)

```
CPL = Total Ad Spend / Total Leads
    = ${spend} / {leads}
    = ${cpl}
```

### Customer Acquisition Cost (CAC)

```
CAC = Total Spend / Customers Acquired
    = ${total_spend} / {customers}
    = ${cac}

OR (if leads not yet converted):
Projected CAC = CPL / Lead-to-Customer Rate
              = ${cpl} / {conversion_rate}%
              = ${projected_cac}
```

### Lifetime Gross Profit (LTGP)

```
LTGP = Average Deal Size × Gross Margin % × (Lifetime Months / 12)
     = ${deal_size} × {margin}% × ({lifetime} / 12)
     = ${ltgp}
```

### Payback Period

```
Monthly Profit = (Deal Size / Lifetime Months) × Gross Margin %
               = (${deal_size} / {lifetime}) × {margin}%
               = ${monthly_profit}

Payback Period = CAC / Monthly Profit
               = ${cac} / ${monthly_profit}
               = {months} months
```

## Metrics Dashboard

Create a visual summary:

```
┌─────────────────────────────────────────┐
│         GROWTH METRICS DASHBOARD        │
├─────────────────────────────────────────┤
│ Period: {review_period}                 │
│                                         │
│ LEAD GENERATION                         │
│ • Total Leads: {count}                  │
│ • Cost Per Lead: ${cpl}                 │
│                                         │
│ CUSTOMER ACQUISITION                    │
│ • Customers: {count}                    │
│ • CAC: ${cac}                          │
│ • Conversion Rate: {percentage}%        │
│                                         │
│ PROFITABILITY                           │
│ • Revenue: ${revenue}                   │
│ • Average Deal: ${deal_size}           │
│ • LTGP: ${ltgp}                        │
│ • LTGP:CAC: {ratio}:1                  │
│                                         │
│ EFFICIENCY                              │
│ • Payback Period: {months} months      │
│ • Gross Margin: {percentage}%          │
│ • Total Spend: ${spend}                │
└─────────────────────────────────────────┘
```

## Data Quality Check

Validate the collected data:

- [ ] All required fields provided
- [ ] Numbers are reasonable (no obvious errors)
- [ ] Dates/periods match
- [ ] Calculations add up

**If data is incomplete or questionable:**
→ Flag for user review before proceeding

## Update Output File

```markdown
## Performance Metrics ({review_period})

### Lead Generation

- Total leads: {count}
- Organic: {count}
- Paid: {count}
- Cost per lead: ${cpl}

### Customer Acquisition

- Customers acquired: {count}
- Customer Acquisition Cost: ${cac}
- Conversion rate: {percentage}%
- Sales cycle: {days} days

### Revenue & Profitability

- Revenue generated: ${revenue}
- Average deal size: ${deal_size}
- Gross margin: {percentage}%
- Lifetime Gross Profit: ${ltgp}

### Financial Ratios

- LTGP:CAC: {ratio}:1
- Payback period: {months} months
- Total spend: ${spend}

### Customer Lifetime

- Average lifetime: {months} months
- Churn rate: {percentage}%
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02-metrics-collection']
totalLeads: { count }
totalSpend: { amount }
cac: { amount }
ltgp: { amount }
ltgpCacRatio: { ratio }
```

## Menu

- **[n]** Next step (Unit Economics Analysis)
- **[b]** Back to initialization
- **[e]** Edit/correct metrics
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-03-unit-economics.md`
