# Step 3: Strategic Direction

## Previous Step Check

Verify `stepsCompleted` includes 'step-02-business-model-validation'. If not, redirect to step-02.

## Load Business Model Status

Review the LTGP:CAC ratio and business model verdict from previous step.

## Strategic Priority Setting

Based on the business model status, help the user set strategic priorities for the next 6-12 months.

### The 4 CAI Ecosystems Framework

Present the 4 ecosystems and ask the user to prioritize:

**Ecosystem 1: Make Content (Free Content Accumulation)**

- Goal: Asset accumulation, authority building
- Time to results: 3-6 months (compounding)
- Investment: Low monetary, high time
- Best for: Building long-term trust, organic reach

**Ecosystem 2: Monetize Content (The Commercials)**

- Goal: Convert goodwill to revenue
- Time to results: 1-3 months
- Investment: Low monetary, medium time
- Best for: Extracting value from existing audience

**Ecosystem 3: Make Ads (The House Advantage)**

- Goal: Guaranteed reach via capital
- Time to results: Immediate (2-4 weeks)
- Investment: Medium to high monetary
- Best for: Predictable lead flow, market testing

**Ecosystem 4: Scale Ads (The Money Printer)**

- Goal: Fiscal expansion
- Time to results: Ongoing (once profitable)
- Investment: High monetary
- Best for: Aggressive growth when unit economics work

### Priority Recommendation Based on Business Model

**If LTGP:CAC < 3:1 (Risk Status):**

```
Recommended Priority Order:
1. Ecosystem 1 (Make Content) - Build foundation
2. Ecosystem 2 (Monetize) - Extract value from content
3. HOLD on Ecosystem 3 & 4 - Don't scale what doesn't work

Rationale: Fix unit economics before spending on ads.
```

**If LTGP:CAC 3:1-5:1 (Caution Status):**

```
Recommended Priority Order:
1. Ecosystem 1 (Make Content) - Build organic foundation
2. Ecosystem 3 (Make Ads) - Small budget tests ($500-2k/month)
3. Ecosystem 2 (Monetize) - Balance give and ask
4. HOLD on Ecosystem 4 - Don't scale yet

Rationale: Build organic while testing paid at small scale.
```

**If LTGP:CAC > 5:1 (Green Light):**

```
Recommended Priority Order:
1. Ecosystem 3 (Make Ads) - Aggressive testing
2. Ecosystem 4 (Scale Ads) - Scale what works
3. Ecosystem 1 (Make Content) - Long-term compounding
4. Ecosystem 2 (Monetize) - Optimize conversion

Rationale: Your economics justify aggressive paid acquisition.
```

## User Priority Selection

Ask the user:

1. Do you agree with the recommended priority order?
2. If not, what would you change and why?
3. What is your primary constraint? (Time, money, expertise, or market readiness)
4. What is your risk tolerance? (Conservative, moderate, aggressive)

## Strategic Focus Areas

Based on priorities, define 3-5 strategic focus areas for the next quarter:

**Example for LTGP:CAC > 5:1:**

1. Launch 5 ad campaigns per month (testing creative variations)
2. Produce 10 free content pieces per month (organic foundation)
3. Develop 2 high-converting landing pages
4. Build email nurture sequence (5-7 emails)
5. Monitor LTGP:CAC weekly, scale winners aggressively

**Example for LTGP:CAC 3:1-5:1:**

1. Produce 15 free content pieces per month (build authority)
2. Launch 2 small ad tests ($500 each) to validate messaging
3. Monitor CAC closely, pause if exceeds $X
4. Build organic distribution (LinkedIn, email list, partnerships)
5. Improve conversion rates on existing traffic

## Update Output File

Add strategic direction section:

```markdown
## Strategic Direction

### Ecosystem Priority Order

1. [Ecosystem name] - [Rationale]
2. [Ecosystem name] - [Rationale]
3. [Ecosystem name] - [Rationale]
4. [Ecosystem name] - [Rationale]

### Strategic Focus Areas (Next Quarter)

1. [Focus area 1]
2. [Focus area 2]
3. [Focus area 3]
4. [Focus area 4]
5. [Focus area 5]

### Constraints & Risk Tolerance

- Primary constraint: [Time/Money/Expertise/Market]
- Risk tolerance: [Conservative/Moderate/Aggressive]
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02-business-model-validation', 'step-03-strategic-direction']
ecosystemPriority: ['ecosystem-1', 'ecosystem-3', ...]
riskTolerance: [conservative/moderate/aggressive]
```

## Menu

- **[n]** Next step (Risk Assessment)
- **[b]** Back to business model validation
- **[r]** Revise strategic priorities
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-04-risk-assessment.md`
