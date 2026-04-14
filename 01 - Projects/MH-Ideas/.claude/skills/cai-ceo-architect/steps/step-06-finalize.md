# Step 6: Finalize Strategic Plan

## Previous Step Check

Verify `stepsCompleted` includes 'step-05-resource-allocation'. If not, redirect to step-05.

## Review Complete Strategic Plan

Load the strategic plan output file and review all sections:

1. ✅ Business Context (step-01)
2. ✅ Business Model Validation (step-02)
3. ✅ Strategic Direction (step-03)
4. ✅ Risk Assessment (step-04)
5. ✅ Resource Allocation (step-05)

## Strategic Plan Summary

Generate an executive summary at the top of the strategic plan document:

```markdown
# Strategic Plan: {client_id}

**Created:** {date}
**Target Industry:** {target_industry}
**Acquisition Strategy:** {acquisition_strategy}

## Executive Summary

### Business Model Status

- **LTGP:CAC Ratio:** {ratio}:1
- **Status:** {Green Light/Proceed with Caution/Strategic Risk}
- **Payback Period:** {months} months
- **Verdict:** {one-sentence verdict}

### Strategic Direction

**Primary Focus:** {ecosystem_priority_1}
**Secondary Focus:** {ecosystem_priority_2}

**Top 3 Objectives (Next Quarter):**

1. {objective_1}
2. {objective_2}
3. {objective_3}

### Resource Commitment

- **Monthly Budget:** ${budget}
- **Weekly Time:** {hours} hours
- **Team Size:** {count} people

### Key Risks

**High Priority:**

1. {risk_1}
2. {risk_2}

### Success Metrics

- {metric_1}: {target}
- {metric_2}: {target}
- {metric_3}: {target}

---
```

## Success Metrics & KPIs

Define 5-7 key metrics to track:

### Acquisition Metrics

- **Leads per month:** {target}
- **CAC:** ${target} (maintain or decrease)
- **LTGP:CAC ratio:** {target}:1 (maintain > 3:1)

### Content Metrics (if Ecosystem 1 prioritized)

- **Content pieces published:** {count}/month
- **Organic reach:** {target} impressions/month
- **Engagement rate:** {target}%

### Ad Metrics (if Ecosystem 3 prioritized)

- **Ad spend:** ${budget}/month
- **Cost per lead (CPL):** ${target}
- **Click-through rate (CTR):** {target}%
- **Conversion rate:** {target}%

### Financial Metrics

- **Revenue from acquisition:** ${target}/month
- **Payback period:** {target} months
- **ROI:** {target}x

## Review Cadence

Set up regular strategic review schedule:

**Weekly:**

- Review key metrics (CAC, leads, spend)
- Flag any high-priority risks materializing
- Quick wins and blockers review

**Monthly:**

- Full metrics dashboard review
- Risk register update
- Resource allocation adjustment if needed

**Quarterly:**

- Full strategic plan review
- Re-run CEO Architect workflow
- Adjust strategy based on results

## Next Steps & Action Items

Create concrete action items for the next 30 days:

**Immediate Actions (This Week):**

1. [ ] Set up tracking infrastructure (analytics, UTM codes, dashboards)
2. [ ] Finalize content calendar for Month 1
3. [ ] Set up ad accounts and payment methods (if Ecosystem 3)
4. [ ] Brief team on strategic priorities

**Month 1 Actions:**

1. [ ] Launch first {X} content pieces
2. [ ] Launch first {X} ad campaigns (if applicable)
3. [ ] Set up weekly metrics review meeting
4. [ ] Establish feedback loop process

**Month 2-3 Actions:**

1. [ ] Optimize based on Month 1 data
2. [ ] Scale what's working
3. [ ] Pause/pivot what's not
4. [ ] Prepare for quarterly strategic review

## Integration with Other CAI Skills

Recommend which CAI skills to invoke next:

**Based on Strategic Direction:**

**If Ecosystem 1 (Content) is priority:**
→ Next: Invoke `cai-content-architect` to build content strategy

**If Ecosystem 3 (Ads) is priority:**
→ Next: Invoke `cai-hook-engineer` to develop ad creative

**Always recommended:**
→ Invoke `cai-compliance-auditor` to validate plan adherence
→ Invoke `cai-feedback-loop-tracker` to set up tracking

## Final Update to Output File

Update frontmatter to mark completion:

```yaml
stepsCompleted:
  [
    'step-01-init',
    'step-02-business-model-validation',
    'step-03-strategic-direction',
    'step-04-risk-assessment',
    'step-05-resource-allocation',
    'step-06-finalize',
  ]
workflowStatus: 'complete'
completedDate: { current_date }
nextReviewDate: { date + 90 days }
```

Add final sections:

```markdown
## Success Metrics & KPIs

[Metrics defined above]

## Review Cadence

- Weekly: [Schedule]
- Monthly: [Schedule]
- Quarterly: [Schedule]

## Action Items (Next 30 Days)

[Checklist above]

## Next Steps

Recommended CAI skills to invoke:

1. [Skill name] - [Purpose]
2. [Skill name] - [Purpose]
```

## Completion Message

Present completion message to user:

```
✅ CEO Strategic Plan Complete!

Your strategic plan has been saved to:
{project-root}/output/plans/ceo-strategic-plan.md

Key Takeaways:
- Business Model Status: {status}
- Primary Focus: {ecosystem}
- Monthly Budget: ${budget}
- Next Review: {date}

Recommended Next Steps:
1. Invoke {next_skill_1} to {purpose}
2. Set up weekly metrics review
3. Brief team on strategic priorities

Would you like to:
[a] View complete plan
[b] Export plan summary
[c] Invoke next recommended skill
[q] Quit
```

## Menu

- **[a]** View complete strategic plan
- **[b]** Export executive summary
- **[c]** Invoke next recommended CAI skill
- **[r]** Restart CEO Architect workflow
- **[q]** Quit

**Workflow Complete!** 🎉
