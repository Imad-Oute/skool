---
config: '{project-root}/.agents/microhard/config.yaml'
outputFile: '{project-root}/output/reports/compliance-audit-report.md'
---

# Compliance Auditor Workflow

## Purpose

Quality assurance for Client Acquisition Intelligence campaigns. This workflow validates blueprint adherence, checks operational compliance, and ensures quality standards across all CAI assets.

## Role Definition

**The Compliance Auditor** is the quality gatekeeper. While other agents create and execute, the Compliance Auditor validates:

- Are assets following naming conventions?
- Is the Give:Ask ratio maintained at 3.5:1?
- Are quality standards met?
- Is the blueprint being followed?
- Are there any red flags or violations?

## Step Sequence

This workflow executes in 5 sequential steps:

1. **step-01-init.md** - Initialize compliance audit session
2. **step-02-naming-validation.md** - Validate asset naming conventions
3. **step-03-give-ask-audit.md** - Audit Give:Ask ratio compliance
4. **step-04-quality-gates.md** - Check quality standards and red flags
5. **step-05-finalize.md** - Generate compliance report and recommendations

## Output Structure

The workflow produces a compliance audit report containing:

- Naming convention violations
- Give:Ask ratio analysis
- Quality gate results
- Red flags and warnings
- Compliance score and recommendations

## Integration with Other CAI Skills

- **After Content Creation:** Audit content assets
- **After Ad Creation:** Audit ad assets
- **Weekly/Monthly:** Run full compliance audit
- **Before Scaling:** Validate everything is compliant

## Compliance Standards

- Asset naming: `[ID]_[DEPT]_[DATE]_[CATEGORY]_[VERSION]`
- Give:Ask ratio: Minimum 3.5:1 (3.5 free for every 1 ask)
- Quality gates: Pass all critical checks

## Menu Navigation

Each step provides menu options to navigate forward, backward, or jump to specific steps as needed.
