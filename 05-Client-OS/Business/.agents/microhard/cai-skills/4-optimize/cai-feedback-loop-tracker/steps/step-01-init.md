# Step 1: Initialization

**Objective:** Define the review scope, time period, and assets to analyze.

## Instructions

Execute the following in sequence:

### 1. Welcome & Context

Greet the user and explain:

> "Welcome to the Feedback Loop Tracker. I'll help you systematically review performance, diagnose what worked and what didn't, and generate iteration directives for the next cycle."

### 2. Load Config

Read the configuration from `{config}`:

- `client_id` — For labeling the report
- `output_content` — Where content assets live
- `output_ads` — Where ad assets live
- `logs` — Where to log performance data

### 3. Define Review Scope

Ask the user:

**A. Review Period**

- Last 7 days (weekly review)
- Last 30 days (monthly review)
- Last 90 days (quarterly review)
- Custom date range: [start] to [end]

**B. Asset Types to Review**
Select all that apply:

- [x] Content assets (LinkedIn posts, articles, videos, threads)
- [x] Ad campaigns (paid acquisition)
- [ ] Email sequences
- [ ] Landing pages

**C. Review Purpose**

- Routine weekly/monthly check-in
- Post-campaign analysis
- Diagnosing performance drop
- Pre-scaling validation
- Other: [specify]

### 4. Asset Inventory

Ask the user to list the specific assets to review (or describe where to find them):

```
Assets for Review:
1. [Asset name / ID] — [Type] — [Platform]
2. [Asset name / ID] — [Type] — [Platform]
3. [Asset name / ID] — [Type] — [Platform]
...
```

If the user has many assets, help them prioritize:

- Top 5 by spend (ads)
- Top 5 by impressions (content)
- Any that significantly over- or underperformed

### 5. Create Output File

Create the report at: `{outputFile}`

Initialize with this frontmatter:

```yaml
---
stepsCompleted: [1]
clientId: { client_id }
reviewPeriod: { period }
reviewPurpose: { purpose }
assetTypes: [list]
assetCount: { count }
createdDate: { current date }
---
```

Add initial header:

```markdown
# Feedback Loop Report: {client_id}

**Period:** {review_period}
**Date:** {current_date}
**Purpose:** {review_purpose}
**Assets Reviewed:** {count}

---
```

### 6. Present Menu

```
✓ Step 1 Complete: Review scope defined
  Period: {review_period}
  Assets: {count} to review

[C] Continue to Performance Collection
[E] Edit review scope
[X] Exit workflow
```

Wait for user selection.

### 7. Handle Selection

- **If [C]**: Update `stepsCompleted: [1]` in frontmatter, load `./step-02-performance-collection.md`
- **If [E]**: Re-prompt for scope fields, update frontmatter, show menu again
- **If [X]**: Exit with "Workflow paused. Run this skill again to resume."

---

**END OF STEP 1**
