# Step 1: Strategic Planning Initialization

## Context Loading

Load configuration from `{project-root}/.agents/microhard/config.yaml`:

- Target industry: `{target_industry}`
- Acquisition strategy: `{acquisition_strategy}`
- Client ID: `{client_id}`

## Initialize Output File

Create strategic plan document at: `{project-root}/output/plans/ceo-strategic-plan.md`

**Frontmatter:**

```yaml
---
stepsCompleted: []
clientId: { client_id }
targetIndustry: { target_industry }
acquisitionStrategy: { acquisition_strategy }
createdDate: { current_date }
lastUpdated: { current_date }
---
```

## Strategic Context Gathering

Ask the user to provide strategic context:

### 1. Business Model Basics

- What is the core offering (product/service)?
- What is the current revenue model?
- What is the target customer profile (ICP)?
- What is the average deal size/LTV?

### 2. Current State

- What is the current monthly recurring revenue (MRR) or revenue?
- What is the current customer acquisition cost (CAC)?
- How many leads/month are needed to hit growth targets?
- What acquisition channels are currently in use?

### 3. Strategic Goals

- What is the revenue goal for next 6-12 months?
- What is the target market position?
- What are the key competitive advantages?
- What are the primary constraints (budget, time, resources)?

## Update Output File

After gathering context, update the output file:

```markdown
# Strategic Plan: {client_id}

## Business Context

[Document responses above]

## Strategic Overview

[Brief synthesis of the situation]
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init']
```

## Menu

Once context is gathered, present options:

- **[n]** Next step (Business Model Validation)
- **[r]** Restart initialization
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-02-business-model-validation.md`
