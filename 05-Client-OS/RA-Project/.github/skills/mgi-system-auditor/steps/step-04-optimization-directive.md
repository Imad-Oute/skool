# Step 4: Optimization Directive

**Agent:** Architect 🏛️  
**Objective:** Synthesize all lens findings into a ranked, executable optimization directive.

---

## Your Task

You are the **Architect**. You have applied all selected lenses through the step-03 checkpoint loop. The cumulative findings log from those passes is your raw material. Convert it into a ranked, executable directive — specific enough to act on, sequenced to minimize disruption.

### 1. Prioritization Matrix

Rank each optimization target by: **Impact / Effort** ratio:

| Target                  | Type                          | Impact | Effort | Priority | Sequence         |
| ----------------------- | ----------------------------- | ------ | ------ | -------- | ---------------- |
| [component/abstraction] | Remove/Merge/Clarify/Refactor | H/M/L  | H/M/L  | 1/2/3... | Before/After [X] |

**Prioritization rules:**

- High Impact + Low Effort → do first (quick wins that create momentum)
- High Impact + High Effort → schedule with dedicated resources
- Low Impact + Low Effort → batch together as maintenance
- Low Impact + High Effort → defer or drop

### 2. Optimization Directive

For each Priority 1-3 target, produce a specific directive:

```
TARGET: _______________
Action: [ ] Remove  [ ] Merge with: ___  [ ] Clarify interface  [ ] Refactor
Specific steps:
  1. _______________
  2. _______________
  3. _______________
Success criteria: (how do you know it's done?)
_______________________________________________
Risks: (what could go wrong during this optimization?)
_______________________________________________
Dependencies: (must be done before/after which other changes?)
_______________________________________________
```

### 3. Execution Sequence

The full optimization plan in execution order:

```
Phase 1 — Quick Wins (do immediately, low risk):
  □ [Action 1]
  □ [Action 2]

Phase 2 — Core Simplifications (planned, medium effort):
  □ [Action 3]
  □ [Action 4]

Phase 3 — Structural Refactors (scheduled, high effort):
  □ [Action 5]

Deferred / Dropped:
  - [Target] — reason: _______________
```

### Final Optimization Directive Artifact

```markdown
# Optimization Directive: [System Name]

**Date:** [YYYY-MM-DD]
**Audit Team:** Architect, Problem Solver, Engineer

## System Health Assessment

[Healthy / Degraded / Critical / Requires Rebuild]
[1-2 sentence summary of primary entropy source]

## Top Entropy Sources

1. [Component/Layer] — [primary issue] — [impact]
2. [Component/Layer] — [primary issue] — [impact]
3. [Component/Layer] — [primary issue] — [impact]

## Execution Plan

[Phase 1, 2, 3 as above]

## Expected Outcomes

After executing this directive:

- Cognitive load reduction: \_\_\_\_%
- Coupling reduction: \_\_\_\_%
- Redundancy eliminated: \_\_\_\_%
- Velocity improvement: [qualitative]
```

---

**Skill complete.** Save to `output/knowledge/audits/{system-slug}-optimization.md`.  
Log to `logs/mgi-system-auditor.log`.
