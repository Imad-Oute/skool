# Step 6: Final Output Assembly

**Agent:** Architect 🏛️  
**Objective:** Assemble and save the complete hardened plan artifact.

---

## Your Task

You are the **Architect** producing the final deliverable. The hardened plan from step-05 is complete. Now assemble it into the canonical output format and save it.

### Final Artifact

Assemble the complete hardened plan document:

```markdown
# Hardened Plan: {plan-slug}

**Date:** {YYYY-MM-DD}  
**Adversarial iterations:** {loop count}  
**Attacks analyzed:** {total} **Critical:** {n} **Accepted risk:** {n}

---

## Original Plan (Summary)

{1-2 sentence description of what was stress-tested}

## What Changed

| Element     | Original   | Hardened Version | Why                   |
| ----------- | ---------- | ---------------- | --------------------- |
| [component] | [original] | [hardened]       | [attack it addresses] |

## Hardened Structure

{The rebuilt plan with all structural fixes applied}

## Monitoring & Circuit Breakers

{What to watch. At what threshold to stop or pivot.}

## Pre-Execution Validation Checklist

- [ ] {Critical assumption validated by: \_\_\_}
- [ ] {Single point of failure addressed: \_\_\_}
- [ ] {External dependency confirmed: \_\_\_}

## Residual Risks (Accepted)

| Risk   | Likelihood | Mitigation   | Why Accepted    |
| ------ | ---------- | ------------ | --------------- |
| [risk] | H/M/L      | [mitigation] | [justification] |

## Attack Log

| #   | Attack   | Source              | Severity | Resolution              |
| --- | -------- | ------------------- | -------- | ----------------------- |
| 1   | [attack] | Inversionist/Critic | H/M/L    | Fixed/Accepted/Deferred |
```

### Save and Log

1. Save to `output/knowledge/stress-tests/{plan-slug}-hardened.md`
2. Append to `logs/mgi-adversarial-designer.log`:

```
[{timestamp}] HARDENED  plan={plan-slug}  iterations={n}  attacks={total}  critical_fixed={n}  risks_accepted={n}
```

---

**Skill complete.** The plan has been stress-tested and hardened.
