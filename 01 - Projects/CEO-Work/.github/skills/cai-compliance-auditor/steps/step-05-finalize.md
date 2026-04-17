# Step 5: Finalize Compliance Report

## Previous Step Check

Verify `stepsCompleted` includes 'step-04-quality-gates'. If not, redirect to step-04.

## Compliance Report Summary

Generate executive summary at top of report:

```markdown
# Compliance Audit Report

**Client ID:** {client_id}
**Audit Date:** {current_date}
**Auditor:** CAI Compliance Auditor
**Report Status:** FINAL

---

## Executive Summary

### Overall Compliance Score: {score}/100

**Status:** [COMPLIANT/NEEDS IMPROVEMENT/CRITICAL]

### Key Findings

- **Naming Compliance:** {score}% ({violations} violations)
- **Give:Ask Ratio:** {ratio}:1 ({status})
- **Quality Score:** {percentage}% ({failed} failed gates)
- **Red Flags:** {critical} critical, {warning} warnings

### Verdict

{one_sentence_verdict}

### Priority Actions Required

1. {action_1}
2. {action_2}
3. {action_3}

---
```

## Overall Compliance Score Calculation

Calculate weighted compliance score:

```
Overall Compliance Score =
  (Naming Compliance × 25%) +
  (Give:Ask Compliance × 35%) +
  (Quality Gates × 30%) +
  (Red Flag Penalty × 10%)

Naming: {score}% × 0.25 = {points}
Give:Ask: {score}% × 0.35 = {points}
Quality: {score}% × 0.30 = {points}
Red Flags: (100 - penalty) × 0.10 = {points}

Total: {overall_score}/100
```

**Give:Ask Score Conversion:**

- Ratio ≥ 3.5:1 = 100%
- Ratio 3.0-3.4:1 = 70%
- Ratio 2.5-2.9:1 = 40%
- Ratio < 2.5:1 = 0%

**Red Flag Penalty:**

- Each critical red flag: -10 points
- Each warning red flag: -3 points
- Max penalty: -30 points

**Compliance Levels:**

- 90-100: ✅ COMPLIANT (Excellent operational hygiene)
- 70-89: ⚠️ NEEDS IMPROVEMENT (Address warnings)
- 50-69: ⚠️ CRITICAL (Immediate action required)
- <50: 🚨 SEVERE (Operations compromised)

## Compliance Trend Analysis

If previous audit reports exist, show trend:

```
Compliance History:
- Current: {score} ({date})
- Previous: {score} ({date})
- Change: {+/-} points ({trend})

Trend: [IMPROVING/STABLE/DECLINING]
```

## Action Plan

Based on findings, create prioritized action plan:

### Immediate Actions (This Week)

Critical issues requiring immediate attention:

1. [ ] Fix {count} critical red flags
2. [ ] Rename {count} HIGH severity naming violations
3. [ ] Create {count} Give assets to restore 3.5:1 ratio (if needed)

### Short-Term Actions (Next 30 Days)

Important improvements:

1. [ ] Fix {count} MEDIUM severity naming violations
2. [ ] Address {count} warning red flags
3. [ ] Improve quality gates pass rate to >80%
4. [ ] Update {count} assets missing metadata

### Long-Term Actions (Next Quarter)

Continuous improvement:

1. [ ] Implement automated naming validation
2. [ ] Set up Give:Ask monitoring dashboard
3. [ ] Establish weekly compliance checks
4. [ ] Train team on quality standards

## Next Audit Schedule

Set reminder for next compliance audit:

**Recommended Frequency:**

- If Overall Score ≥90%: Monthly audits
- If Overall Score 70-89%: Bi-weekly audits
- If Overall Score <70%: Weekly audits until improved

**Next Audit Due:** {date}

## Integration with Other CAI Skills

Recommend which CAI skills to invoke based on findings:

**If Give:Ask ratio is low:**
→ Invoke `cai-content-architect` to create more Give assets

**If quality scores are low:**
→ Invoke `cai-hook-engineer` to improve content quality
→ Invoke `cai-editorial-review-prose` for quality review

**If naming violations exist:**
→ Use naming fix commands generated in step-02

**For ongoing monitoring:**
→ Invoke `cai-feedback-loop-tracker` to track metrics

## Final Update to Output File

Update frontmatter to mark completion:

```yaml
stepsCompleted:
  [
    'step-01-init',
    'step-02-naming-validation',
    'step-03-give-ask-audit',
    'step-04-quality-gates',
    'step-05-finalize',
  ]
workflowStatus: 'complete'
overallComplianceScore: { score }
complianceLevel: [compliant/needs-improvement/critical/severe]
completedDate: { current_date }
nextAuditDate: { date }
```

Add final sections:

```markdown
## Overall Compliance Score: {score}/100

### Score Breakdown

- Naming Compliance: {score}% (weight: 25%) = {points}
- Give:Ask Ratio: {score}% (weight: 35%) = {points}
- Quality Gates: {score}% (weight: 30%) = {points}
- Red Flag Penalty: {penalty} points (weight: 10%) = {points}

**Total Score:** {overall_score}/100
**Status:** {compliance_level}

## Compliance Trend

{trend_analysis}

## Action Plan

[Immediate/Short-term/Long-term actions]

## Next Steps

Recommended CAI skills to invoke:

1. [Skill name] - [Purpose]
2. [Skill name] - [Purpose]

## Next Audit

**Scheduled:** {date}
**Frequency:** {frequency}
```

## Completion Message

```
✅ Compliance Audit Complete!

Your compliance report has been saved to:
{project-root}/output/reports/compliance-audit-report.md

Overall Compliance Score: {score}/100
Status: {level}

Key Findings:
- Naming: {score}% ({violations} violations)
- Give:Ask: {ratio}:1 ({status})
- Quality: {score}%
- Red Flags: {critical} critical, {warning} warnings

{priority_message}

Would you like to:
[a] View complete report
[b] Export action plan
[c] Invoke recommended CAI skill
[f] Generate fix commands for violations
[q] Quit
```

## Menu

- **[a]** View complete compliance report
- **[b]** Export action plan as checklist
- **[c]** Invoke recommended CAI skill
- **[f]** Generate fix commands (renaming, etc.)
- **[r]** Restart compliance audit
- **[q]** Quit

**Workflow Complete!** 🎉
