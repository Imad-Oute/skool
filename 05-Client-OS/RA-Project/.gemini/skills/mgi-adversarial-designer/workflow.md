# Workflow: mgi-adversarial-design

**Skill:** mgi-adversarial-designer  
**Agents:** Inversionist 🔄, Critic 🎯, Architect 🏛️  
**Objective:** Bulletproof a high-stakes plan before execution.

---

## State Machine

```
PLAN_PROPOSAL → INVERSIONIST_ATTACK → CRITIC_AUDIT → ARCHITECT_HARDENING → COMPLETE
```

## Steps

| Step | ID                          | Agent        | Action                                               |
| ---- | --------------------------- | ------------ | ---------------------------------------------------- |
| 1    | step-01-plan-proposal       | All          | Define plan, scope stakes, set hardening constraints |
| 2    | step-02-inversionist-attack | Inversionist | Force plan to fail — pre-mortem failure map          |
| 3    | step-03-critic-audit        | Critic       | Cognitive bias scan, logical fallacy detection       |
| 4    | step-04-architect-hardening | Architect    | Rebuild surviving elements into reinforced structure |

## Output Artifact

`output/knowledge/stress-tests/{plan-slug}-hardened.md` — hardened plan with:

- Original plan summary
- Failure map (top risks, single points of failure, optimistic assumptions)
- Bias audit results
- Hardened version with structural fixes applied

## Audit Trail

Each run logs to `logs/mgi-adversarial-designer.log`.
