# Step 6: Finalize Growth Plan & Controls

## Previous Step Check

Verify `stepsCompleted` includes 'step-05-scaling-plan'. If not, redirect to step-05.

## Review Complete Growth Plan

Load the growth scaling plan output file and review all sections:

1. ✅ Financial Review Context (step-01)
2. ✅ Performance Metrics (step-02)
3. ✅ Unit Economics Analysis (step-03)
4. ✅ Scaling Readiness Assessment (step-04)
5. ✅ Scaling Plan (step-05)

## Executive Summary

Generate an executive summary at the top of the growth scaling plan:

```markdown
# Growth Scaling Plan: {client_id}

**Review Date:** {review_date}
**Review Period:** {review_period}
**Current Phase:** {track/invest/print}

---

## Executive Summary

### Financial Health

- **LTGP:CAC Ratio:** {ratio}:1 ({status})
- **Payback Period:** {months} months ({status})
- **CAC:** ${amount}
- **Monthly Leads:** {count}

### Scaling Verdict

**{READY/CONDITIONALLY READY/NOT READY}**
Readiness Score: {percentage}%

### Approved Budget

- **Current Budget:** ${amount}/month
- **Month 1 Target:** ${amount}/month
- **Month 2 Target:** ${amount}/month (conditional on metrics)
- **Month 3 Target:** ${amount}/month (conditional on metrics)

### Top Priority Actions

1. {action_1}
2. {action_2}
3. {action_3}

---
```

## Financial Controls Dashboard

Set up the monitoring system:

### Weekly Metrics to Track

Create or reference the audit log at `{project-root}/logs/growth-metrics.csv`:

**CSV Headers:**

```
Date,Week,AdSpend,Leads,CPL,Customers,CAC,Revenue,LTGP,LTGPCACRatio,PaybackMonths,Status,Notes
```

**Alert Thresholds:**

| Metric       | Target      | Warning        | Critical      |
| ------------ | ----------- | -------------- | ------------- |
| LTGP:CAC     | > 5:1       | 3:1-5:1        | < 3:1         |
| CAC          | < ${target} | ${target}×1.25 | ${target}×1.5 |
| CPL          | < ${target} | ${target}×1.3  | ${target}×1.5 |
| Weekly Leads | > {target}  | {target}×0.7   | {target}×0.5  |

### Monthly Review Protocol

Define the monthly review ritual:

```
1st of every month:
□ Pull all metrics from past 30 days
□ Calculate LTGP:CAC (fresh calculation)
□ Compare to previous month
□ Re-score Scaling Readiness (Step 4 checklist)
□ Adjust budget for next month
□ Re-run Growth Controller if scaling up significantly
```

## Integration with CAI Ecosystem

Connect growth decisions to other CAI skills:

**If Scaling Up (LTGP:CAC > 5:1):**
→ Invoke `cai-content-architect` to increase content volume
→ Invoke `cai-hook-engineer` to develop more ad creative
→ Invoke `cai-compliance-auditor` to validate Give:Ask ratio at scale

**If Optimizing (LTGP:CAC 3:1-5:1):**
→ Invoke `cai-hook-engineer` to test new hooks and improve CTR
→ Invoke `cai-compliance-auditor` to audit current asset quality
→ Invoke `cai-feedback-loop-tracker` to identify what's working

**If Pausing (LTGP:CAC < 3:1):**
→ Invoke `cai-compliance-auditor` to find conversion leaks
→ Invoke `cai-ceo-architect` to reconsider strategic direction
→ Invoke `cai-feedback-loop-tracker` to diagnose performance

## Final Update to Output File

Update frontmatter to mark completion:

```yaml
stepsCompleted:
  [
    'step-01-init',
    'step-02-metrics-collection',
    'step-03-unit-economics',
    'step-04-scaling-readiness',
    'step-05-scaling-plan',
    'step-06-finalize',
  ]
workflowStatus: 'complete'
completedDate: { current_date }
nextReviewDate: { date + 30 days }
```

Add final sections:

```markdown
## Financial Controls

### Weekly Tracking

- File: {project-root}/logs/growth-metrics.csv
- Review: Every Monday
- Alert thresholds: [as defined above]

### Hard Stop Conditions

1. LTGP:CAC < 2:1 for 2 weeks → PAUSE ALL PAID SPEND
2. CPL > 50% above baseline → PAUSE and audit creative
3. Monthly spend exceeds ${cap} → STOP and review

### Monthly Review

- Date: 1st of each month
- Protocol: Full metrics review + readiness re-score
- Decision: Scale up / maintain / optimize / pause

## Next Steps (Recommended CAI Skills)

{skill_recommendations_based_on_verdict}

## Next Review

**Scheduled:** {date}
**Trigger for Earlier Review:** LTGP:CAC drops below {threshold}:1
```

## Completion Message

```
✅ Growth Controller: Workflow Complete!

Your growth scaling plan has been saved to:
{project-root}/output/plans/growth-scaling-plan.md

Summary:
- LTGP:CAC: {ratio}:1 ({status})
- Payback Period: {months} months
- Scaling Verdict: {verdict}
- Month 1 Budget: ${amount}

Guardrails Active:
- Hard Stop: LTGP:CAC < 2:1
- Weekly Review: Scheduled
- Next Full Review: {date}

Would you like to:
[a] View complete growth plan
[b] Set up tracking spreadsheet template
[c] Invoke recommended CAI skill
[q] Quit
```

## Menu

- **[a]** View complete growth scaling plan
- **[b]** Generate tracking spreadsheet headers
- **[c]** Invoke recommended CAI skill based on verdict
- **[r]** Restart Growth Controller
- **[q]** Quit

**Workflow Complete!** 🎉

---

**END OF STEP 6**
**END OF WORKFLOW**
