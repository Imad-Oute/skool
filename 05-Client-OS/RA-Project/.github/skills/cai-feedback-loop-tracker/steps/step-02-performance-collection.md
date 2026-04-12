# Step 2: Performance Collection

**Objective:** Gather raw performance metrics for all assets in scope.

## Instructions

### 1. Previous Step Check

Verify `stepsCompleted` includes `1`. If not, redirect to step-01.

### 2. Load Review Context

Review scope from step-01: asset types, review period, purpose.

### 3. Content Performance Metrics

For each **content asset**, collect the following:

**Reach & Distribution**

- Impressions / Reach
- Follower/non-follower split (if available)
- Shares / Reposts / Amplification

**Engagement (Retention Signal)**

- Engagement rate (%)
- Comments count
- Saves / Bookmarks
- Average view duration (video) or read time (articles)
- Click-through rate (if link included)

**Conversion (Reward Signal)**

- Clicks to landing page or profile
- Lead magnet downloads (if applicable)
- DMs / Inquiries generated
- Sales attributed (if trackable)

**Collect in this format per asset:**

```
Asset: [name/ID]
Platform: [LinkedIn/X/YouTube/etc.]
Published: [date]
Type: [Video/Post/Thread/Article]

Reach Metrics:
- Impressions: {count}
- Reach: {count}
- Shares: {count}

Engagement Metrics:
- Engagement rate: {%}
- Comments: {count}
- Saves: {count}
- Avg. view duration / Read time: {time}

Conversion Metrics:
- Clicks: {count}
- CTR: {%}
- Leads generated: {count}
- Sales attributed: {count}
```

### 4. Ad Campaign Metrics

For each **ad campaign**, collect the following:

**Spend & Reach**

- Total spend: ${amount}
- Impressions: {count}
- CPM (cost per 1000 impressions): ${amount}

**Click Performance (Hook Signal)**

- Clicks: {count}
- CTR (click-through rate): {%}
- CPC (cost per click): ${amount}

**Lead Performance (Retention Signal)**

- Leads generated: {count}
- CPL (cost per lead): ${amount}
- Lead quality score (1-10, based on fit): {score}

**Revenue Performance (Reward Signal)**

- Customers acquired: {count}
- CAC (customer acquisition cost): ${amount}
- Revenue attributed: ${amount}
- LTGP:CAC ratio (if calculable): {ratio}:1

**Collect in this format per campaign:**

```
Campaign: [name/ID]
Platform: [Facebook/LinkedIn/Google/etc.]
Period: [date range]
Objective: [Lead Gen/Awareness/Conversion]

Spend & Reach:
- Total spend: ${amount}
- Impressions: {count}
- CPM: ${amount}

Click Performance:
- CTR: {%}
- CPC: ${amount}
- Clicks: {count}

Lead Performance:
- Leads: {count}
- CPL: ${amount}
- Lead quality: {score}/10

Revenue Performance:
- Customers: {count}
- CAC: ${amount}
- Revenue: ${amount}
- LTGP:CAC: {ratio}:1
```

### 5. Benchmark Comparison

After collecting raw data, compare against benchmarks:

**Content Benchmarks (General B2B)**

| Metric                   | Below Avg | Average | Above Avg | Excellent |
| ------------------------ | --------- | ------- | --------- | --------- |
| Engagement rate          | < 1%      | 1-3%    | 3-6%      | > 6%      |
| CTR (if link)            | < 0.5%    | 0.5-2%  | 2-4%      | > 4%      |
| Comments (LinkedIn post) | 0-2       | 3-10    | 11-30     | > 30      |

**Ad Benchmarks (B2B Lead Gen)**

| Metric         | Below Avg | Average  | Above Avg | Excellent |
| -------------- | --------- | -------- | --------- | --------- |
| CTR (LinkedIn) | < 0.3%    | 0.3-0.7% | 0.7-1.5%  | > 1.5%    |
| CTR (Facebook) | < 0.5%    | 0.5-1.5% | 1.5-3%    | > 3%      |
| CPL (B2B)      | > $200    | $100-200 | $50-100   | < $50     |
| LTGP:CAC       | < 3:1     | 3:1-5:1  | 5:1-7:1   | > 7:1     |

For each asset, flag performance tier: **Below Avg / Average / Above Avg / Excellent**

### 6. Update Output File

Add performance data section:

```markdown
## Performance Data: {review_period}

### Content Assets

#### [Asset 1 Name]

| Metric          | Value   | Benchmark | Status |
| --------------- | ------- | --------- | ------ |
| Impressions     | {count} | —         | —      |
| Engagement Rate | {%}     | 1-3%      | {tier} |
| Comments        | {count} | 3-10      | {tier} |
| Saves           | {count} | —         | —      |
| CTR             | {%}     | 0.5-2%    | {tier} |
| Leads           | {count} | —         | —      |

[Repeat for each content asset]

### Ad Campaigns

#### [Campaign 1 Name]

| Metric   | Value     | Benchmark | Status |
| -------- | --------- | --------- | ------ |
| Ad Spend | ${amount} | —         | —      |
| CTR      | {%}       | 0.3-0.7%  | {tier} |
| CPL      | ${amount} | $100-200  | {tier} |
| CAC      | ${amount} | —         | —      |
| LTGP:CAC | {ratio}:1 | > 3:1     | {tier} |

[Repeat for each campaign]

### Performance Snapshot

**Top Performer:** {asset/campaign name} — {why it stood out}
**Lowest Performer:** {asset/campaign name} — {what underperformed}
**Average LTGP:CAC (ads):** {ratio}:1
**Average Engagement Rate (content):** {%}
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2]
contentAssetsReviewed: { count }
adCampaignsReviewed: { count }
avgLtgpCac: { ratio }
avgEngagementRate: { % }
```

### 7. Present Menu

```
✓ Step 2 Complete: Performance data collected
  Content assets: {count}
  Ad campaigns: {count}

[C] Continue to 3-Layer Diagnosis
[E] Edit/correct any metrics
[X] Exit workflow
```

Wait for user selection.

### 8. Handle Selection

- **If [C]**: Update `stepsCompleted: [1, 2]` in frontmatter, load `./step-03-diagnosis.md`
- **If [E]**: Allow corrections to any metrics, update report, show menu again
- **If [X]**: Exit with "Workflow paused. Run this skill again to resume."

---

**END OF STEP 2**
