# Step 1: Financial Review Initialization

## Context Loading

Load configuration from `{project-root}/.agents/microhard/config.yaml`:

- Client ID: `{client_id}`
- Target industry: `{target_industry}`
- Current monthly budget: (to be collected)

## Initialize Output File

Create growth scaling plan at: `{project-root}/output/plans/growth-scaling-plan.md`

**Frontmatter:**

```yaml
---
stepsCompleted: []
clientId: { client_id }
reviewDate: { current_date }
currentPhase: [track/invest/print]
ltgpCacRatio: null
scalingRecommendation: null
---
```

## Review Context

Ask the user about the current state:

### 1. Current Scaling Phase

Where are you in the scaling journey?

- **[t]** Track Phase (Testing, collecting data)
- **[i]** Invest Phase (Proven profitable, starting to scale)
- **[p]** Print Phase (Scaling aggressively)
- **[u]** Unsure / First time review

### 2. Time Period for Review

What time period should we analyze?

- Last 30 days (standard)
- Last 90 days (longer trend)
- All time (complete history)
- Custom date range

### 3. Review Purpose

Why are you running this review?

- Monthly financial check-in
- Deciding whether to scale up
- Performance is struggling, need diagnosis
- Preparing for major budget increase

## Update Output File

```markdown
# Growth Scaling Plan: {client_id}

**Review Date:** {current_date}
**Current Phase:** {phase}
**Review Period:** {period}
**Review Purpose:** {purpose}

## Context

{summary of current state}
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init']
reviewPeriod: { period }
reviewPurpose: { purpose }
```

## Menu

- **[n]** Next step (Metrics Collection)
- **[r]** Restart with different context
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-02-metrics-collection.md`
