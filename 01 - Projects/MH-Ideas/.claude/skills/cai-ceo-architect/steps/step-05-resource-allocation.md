# Step 5: Resource Allocation

## Previous Step Check

Verify `stepsCompleted` includes 'step-04-risk-assessment'. If not, redirect to step-04.

## Load Strategic Context

Review:

- Ecosystem priorities (step-03)
- Risk assessment (step-04)
- Business model status (step-02)

## Resource Categories

Identify available resources across 4 categories:

### 1. Budget Allocation

**Ask the user:**

- What is the total monthly budget for client acquisition?
- How much can be allocated to each ecosystem?
- What is the minimum viable budget for testing?
- What is the maximum risk capital (can afford to lose)?

**Budget Allocation Framework:**

**If Total Budget < $2,000/month:**

```
Recommended Allocation:
- 70% Ecosystem 1 (Free Content) - Time investment
- 20% Ecosystem 3 (Paid Ads) - Small tests ($400)
- 10% Buffer/Tools

Rationale: Build organic foundation, test paid at minimal scale
```

**If Total Budget $2,000-$10,000/month:**

```
Recommended Allocation:
- 40% Ecosystem 1 (Free Content) - Time + some paid distribution
- 40% Ecosystem 3 (Paid Ads) - Serious testing
- 10% Ecosystem 2 (Monetize) - Conversion optimization
- 10% Buffer/Tools

Rationale: Balanced approach, sufficient capital to test paid seriously
```

**If Total Budget > $10,000/month:**

```
Recommended Allocation:
- 50% Ecosystem 3 (Paid Ads) - Aggressive testing & scaling
- 20% Ecosystem 1 (Free Content) - Long-term asset building
- 15% Ecosystem 4 (Scale Ads) - Scale proven winners
- 10% Ecosystem 2 (Monetize) - Conversion optimization
- 5% Buffer/Tools

Rationale: Capital sufficient for aggressive paid acquisition
```

### 2. Time Allocation

**Ask the user:**

- How many hours per week can be dedicated to CAI?
- How is time split between strategy, creation, and execution?
- What tasks can be delegated or automated?

**Time Framework:**

```
For 10 hours/week available:
- 20% Strategy (CEO Architect, planning) - 2 hours
- 50% Creation (Content, Ads, Landing Pages) - 5 hours
- 20% Execution (Publishing, Campaign Management) - 2 hours
- 10% Analysis (Feedback Loop, Optimization) - 1 hour
```

### 3. Team & Skills

**Ask the user:**

- Who is on the team? (Solo, small team, agency support?)
- What skills are in-house vs need to be hired/outsourced?
- What is the skill proficiency level? (Beginner, intermediate, expert)

**Skill Categories Needed:**

- Content creation (writing, video, design)
- Ad campaign management (Facebook, LinkedIn, Google)
- Analytics & optimization
- Strategy & planning
- Technical (website, funnels, tools)

**Resource Matrix:**

| Skill           | In-House | Proficiency  | Gap      | Solution           |
| --------------- | -------- | ------------ | -------- | ------------------ |
| Content Writing | Yes      | Intermediate | Minor    | Training/templates |
| Ad Management   | No       | N/A          | Major    | Hire freelancer    |
| Analytics       | Yes      | Beginner     | Moderate | Tools + training   |

### 4. Tools & Infrastructure

**Ask the user:**

- What tools are currently in use?
- What additional tools are needed?
- What is the budget for tools/software?

**Essential CAI Tools:**

- Content creation (Canva, Adobe, video editor)
- Ad platforms (Facebook Ads Manager, LinkedIn Campaign Manager)
- Analytics (Google Analytics, ad platform analytics)
- CRM/Email (HubSpot, Mailchimp, ActiveCampaign)
- Landing pages (Unbounce, Leadpages, Webflow)
- Project management (Notion, Asana, Trello)

## Scaling Plan

Based on resource allocation, create a scaling timeline:

### Month 1-3 (Foundation)

**Focus:** Build foundation with current resources

- Weekly content output: [X pieces]
- Monthly ad spend: [$X]
- Expected leads: [X]
- Team: [Current team only]

### Month 4-6 (Validation)

**Focus:** Validate what works, optimize

- Weekly content output: [X pieces]
- Monthly ad spend: [$X - increased if ROI positive]
- Expected leads: [X]
- Team: [Consider first hire if profitable]

### Month 7-12 (Scaling)

**Focus:** Scale what works aggressively

- Weekly content output: [X pieces]
- Monthly ad spend: [$X - scale if LTGP:CAC holds]
- Expected leads: [X]
- Team: [Scale to X people if revenue supports]

## Resource Constraints & Trade-offs

Identify constraints and trade-offs:

**Example:**

```
Constraint: Only 10 hours/week available
Trade-off: Focus on Ecosystem 3 (Paid Ads) for immediate results
         vs Ecosystem 1 (Content) for long-term compounding
Decision: 60% paid, 40% content (balance short and long-term)
```

## Update Output File

Add resource allocation section:

```markdown
## Resource Allocation

### Budget Allocation (Monthly: ${total_budget})

- Ecosystem 1 (Free Content): ${budget} ({percentage}%)
- Ecosystem 2 (Monetize): ${budget} ({percentage}%)
- Ecosystem 3 (Paid Ads): ${budget} ({percentage}%)
- Ecosystem 4 (Scale Ads): ${budget} ({percentage}%)
- Buffer/Tools: ${budget} ({percentage}%)

### Time Allocation (Weekly: {total_hours} hours)

- Strategy: {hours} hours ({percentage}%)
- Creation: {hours} hours ({percentage}%)
- Execution: {hours} hours ({percentage}%)
- Analysis: {hours} hours ({percentage}%)

### Team & Skills

[Resource Matrix Table]

### Tools & Infrastructure

[List of tools with monthly costs]
Total tool cost: ${monthly_cost}

### Scaling Timeline

- Month 1-3: [Foundation goals]
- Month 4-6: [Validation goals]
- Month 7-12: [Scaling goals]

### Key Constraints

1. [Constraint 1] - [Mitigation]
2. [Constraint 2] - [Mitigation]
```

Update frontmatter:

```yaml
stepsCompleted:
  [
    'step-01-init',
    'step-02-business-model-validation',
    'step-03-strategic-direction',
    'step-04-risk-assessment',
    'step-05-resource-allocation',
  ]
monthlyBudget: { amount }
weeklyTimeAvailable: { hours }
teamSize: { count }
```

## Menu

- **[n]** Next step (Finalize Strategic Plan)
- **[b]** Back to risk assessment
- **[r]** Revise resource allocation
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-06-finalize.md`
