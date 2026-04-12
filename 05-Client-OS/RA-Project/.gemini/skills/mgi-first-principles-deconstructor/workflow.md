# Workflow: mgi-first-principles-deconstruction

**Skill:** mgi-first-principles-deconstructor  
**Agents:** Thinker 🧠, Engineer ⚙️, Architect 🏛️  
**Objective:** Unblock impossible problems by deconstruction to axioms and re-synthesis.

---

## State Machine

```
PROBLEM_FORMULATION → AXIOM_STRIP_DOWN → RE_SYNTHESIS → BLUEPRINTING → COMPLETE
```

## Steps

| Step | ID                              | Agent     | Action                                      |
| ---- | ------------------------------- | --------- | ------------------------------------------- |
| 1    | step-01-problem-formulation     | Thinker   | Precise problem statement; constraint audit |
| 2    | step-02-axiom-strip-down        | Thinker   | Deconstruct to irreducible truths           |
| 3    | step-03-re-synthesis            | Engineer  | Build solution from axioms only             |
| 4    | step-04-architectural-blueprint | Architect | Map solution into executable structure      |

## Output Artifact

`output/knowledge/blueprints/{problem-slug}-blueprint.md` — first principles blueprint with:

- Problem restated at axiomatic level
- Constraint audit (real vs. inherited)
- Axiom set used for re-synthesis
- Synthesized solution
- Architectural implementation map

## Audit Trail

Each run logs to `logs/mgi-first-principles-deconstructor.log`.
