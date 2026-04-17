# Workflow: mgi-system-entropy-audit

**Skill:** mgi-system-auditor  
**Agents:** Architect 🏛️, Problem Solver 🔧, Engineer ⚙️  
**Objective:** Audit a system for entropy and produce an executable optimization directive.

---

## State Machine

```
ABSTRACTION_AUDIT → COMPLEXITY_ASSESSMENT → OPTIMIZATION_DIRECTIVE → COMPLETE
```

## Steps

| Step | ID                             | Agent          | Action                                               |
| ---- | ------------------------------ | -------------- | ---------------------------------------------------- |
| 1    | step-01-abstraction-audit      | Architect      | Catalog abstraction layers; identify value vs. bloat |
| 2    | step-02-complexity-assessment  | Problem Solver | Score complexity, coupling, redundancy per component |
| 3    | step-03-optimization-directive | Engineer       | Rank targets; produce execution plan                 |

## Output Artifact

`output/knowledge/audits/{system-slug}-optimization.md` — optimization directive with:

- Abstraction audit results
- Complexity scores
- Ranked simplification targets
- Executable optimization plan

## Audit Trail

Each run logs to `logs/mgi-system-auditor.log`.
