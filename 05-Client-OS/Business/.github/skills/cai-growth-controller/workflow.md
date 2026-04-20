---
config: '{project-root}/.agents/microhard/config.yaml'
outputFile: '{project-root}/output/plans/growth-scaling-plan.md'
---

# Growth Controller Workflow

## Purpose

Financial oversight and scaling strategy for Client Acquisition Intelligence campaigns. This workflow monitors unit economics, validates scaling readiness, and manages the transition from testing to scaling.

## Role Definition

**The Growth Controller** is the financial strategist. While other agents create and execute, the Growth Controller ensures:

- Are the unit economics profitable (LTGP:CAC > 3:1)?
- Is it safe to scale (payback period < 12 months)?
- What is the optimal scaling budget?
- When do we pause, pivot, or print money?

## Step Sequence

This workflow executes in 6 sequential steps:

1. **step-01-init.md** - Initialize financial review
2. **step-02-metrics-collection.md** - Collect current performance metrics
3. **step-03-unit-economics.md** - Calculate LTGP:CAC and profitability
4. **step-04-scaling-readiness.md** - Assess readiness to scale
5. **step-05-scaling-plan.md** - Define scaling budget and phases
6. **step-06-finalize.md** - Finalize growth plan and controls

## Output Structure

The workflow produces a growth scaling plan containing:

- Current performance metrics
- Unit economics analysis (LTGP:CAC ratio)
- Scaling readiness assessment
- Scaling budget and phases (Track → Invest → Print)
- Financial controls and guardrails

## Integration with Other CAI Skills

- **After Initial Campaigns:** Review metrics, decide to scale or pivot
- **Monthly:** Run financial review
- **Before Scaling:** Validate economics justify investment
- **When Struggling:** Diagnose financial issues

## The Scaling Logic: Track → Invest → Print

1. **Track:** Test at small scale ($500-2k), collect data
2. **Invest:** If profitable, increase budget 2-3x
3. **Print:** If still profitable, scale aggressively

## Menu Navigation

Each step provides menu options to navigate forward, backward, or jump to specific steps as needed.
