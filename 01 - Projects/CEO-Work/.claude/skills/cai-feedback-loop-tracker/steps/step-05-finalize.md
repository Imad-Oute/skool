# Step 5: Finalization

**Objective:** Save the completed report, log metrics to the audit trail, and schedule the next feedback cycle.

## Instructions

### 1. Previous Step Check

Verify `stepsCompleted` includes `4`. If not, redirect to step-04.

### 2. Generate Executive Summary

Prepend a concise executive summary to the top of the report:

```markdown
# Feedback Loop Report: {client_id}

**Period:** {review_period}
**Date:** {current_date}
**Assets Reviewed:** {count} content + {count} campaigns

---

## Executive Summary

### Performance Snapshot

- **Average Engagement Rate:** {%} ({vs benchmark})
- **Average CPL (Ads):** ${amount} ({vs benchmark})
- **Average LTGP:CAC:** {ratio}:1 ({status})
- **Top Performer:** {asset name}

### Diagnosis

**Primary Failure Layer:** {Hook / Retention / Reward / None — All Green}
**System Pattern:** {one-sentence diagnosis}

### Priority Actions

1. {immediate_action_1}
2. {immediate_action_2}
3. {immediate_action_3}

### Assets Verdict

- KILL: {count} assets
- KEEP: {count} assets (with optimizations)
- SCALE: {count} assets

---
```

### 3. Log to Audit Trail

Append a row to the performance log at `{project-root}/logs/feedback-loop-log.csv`.

**CSV format:**

```
Date,Period,ContentAssets,AdCampaigns,AvgEngagementRate,AvgCPL,AvgLTGPCAC,PrimaryFailureLayer,KillCount,KeepCount,ScaleCount,TopPerformer,Notes
```

**Add this row:**

```
{current_date},{review_period},{content_count},{campaign_count},{engagement_rate},{cpl},{ltgp_cac},{failure_layer},{kill},{keep},{scale},{top_performer},{notes}
```

### 4. Schedule Next Feedback Cycle

Based on current performance status, recommend review cadence:

**If All Green (no failures):**

```
Next Review: In 30 days
Reason: Strong performance — monthly cadence is sufficient
Trigger for Earlier Review: LTGP:CAC drops below {threshold}:1
```

**If Conditional (1 failure layer, minor):**

```
Next Review: In 14 days
Reason: Monitoring optimization efforts
Trigger for Earlier Review: {specific metric} drops below {threshold}
```

**If Critical (multiple failures or declining):**

```
Next Review: In 7 days
Reason: Active issues require fast feedback loops
Weekly rhythm until primary failure layer is resolved
```

Add to output file:

```markdown
## Next Feedback Cycle

**Recommended Cadence:** {daily/weekly/bi-weekly/monthly}
**Next Review Date:** {date}
**What to Measure at Next Review:**

1. Did immediate action #1 improve {metric}?
2. Did immediate action #2 improve {metric}?
3. Has primary failure layer ({layer}) improved?

**Trigger for Unscheduled Review:**

- {specific metric} drops below {threshold}
```

### 5. Recommended Next CAI Skills

Based on findings, recommend which CAI skills to invoke next:

**If Hook failures detected:**
→ Invoke `cai-hook-engineer` — build better headlines and opening lines

**If content volume needs to increase:**
→ Invoke `cai-content-architect` — architect more content units

**If Give:Ask ratio is low:**
→ Invoke `cai-compliance-auditor` — full compliance audit

**If scaling decisions needed:**
→ Invoke `cai-growth-controller` — financial validation before increasing spend

**If strategic direction unclear:**
→ Invoke `cai-ceo-architect` — re-assess ecosystem priorities

### 6. Final Update to Output File

Update frontmatter to mark completion:

```yaml
stepsCompleted: [1, 2, 3, 4, 5]
workflowStatus: 'complete'
completedDate: { current_date }
nextReviewDate: { date }
reviewCadence: { cadence }
```

Add final sections:

```markdown
## Audit Log Entry

- Logged to: {project-root}/logs/feedback-loop-log.csv
- Date: {current_date}

## Recommended Next Steps

1. {skill_name} — {reason}
2. {skill_name} — {reason}

---

## Workflow Complete

The feedback loop is closed. Use the iteration directives to guide the next production cycle. The system improves only through consistent measurement and honest diagnosis.

**Key Reminder:** Kill what doesn't work fast. Scale what does work aggressively. Measure everything.
```

### 7. Completion Message

```
=====================================
FEEDBACK LOOP TRACKER: CYCLE COMPLETE
=====================================

Report saved to:
{project-root}/output/plans/feedback-loop-report.md

Summary:
- Primary Failure Layer: {layer}
- Immediate Actions: {count}
- Kill: {count} | Keep: {count} | Scale: {count}
- Next Review: {date}

The loop is closed. Time to iterate.

Would you like to:
[A] View the full report
[B] View the prioritized action list only
[C] Invoke recommended CAI skill
[Q] Quit
```

### 8. Handle Selection

- **If [A]**: Display the full output report
- **If [B]**: Display only the Iteration Directives section
- **If [C]**: Recommend which skill to invoke next based on findings, then exit
- **If [Q]**: Exit

---

**END OF STEP 5**
**END OF WORKFLOW**
