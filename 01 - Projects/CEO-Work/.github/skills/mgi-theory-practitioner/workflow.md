# Workflow: mgi-theory-to-practice

**Skill:** mgi-theory-practitioner  
**Agents:** Analyst 📊, Engineer ⚙️  
**Objective:** Apply a mental model to a real challenge and generate an actionable protocol.

---

## State Machine

```
PRINCIPLE_ID → LOGIC_MAPPING → PROTOCOL_GENERATION → COMPLETE
```

## Steps

| Step | ID                          | Agent    | Action                                          |
| ---- | --------------------------- | -------- | ----------------------------------------------- |
| 1    | step-01-principle-id        | Analyst  | Load mental model, validate fit to challenge    |
| 2    | step-02-logic-mapping       | Analyst  | Map model's causal logic onto challenge context |
| 3    | step-03-protocol-generation | Engineer | Produce executable step-by-step protocol        |

## Output Artifact

`output/knowledge/protocols/{challenge-slug}-protocol.md` — actionable protocol with:

- Model selected and fit assessment
- Context-mapped principle
- Execution steps with success indicators
- Red flags / misfit conditions

## Audit Trail

Each run logs to `logs/mgi-theory-practitioner.log`.
