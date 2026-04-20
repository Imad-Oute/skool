# Workflow: mgi-cross-domain-synthesis

**Skill:** mgi-cross-domain-synthesizer  
**Agents:** Brainstormer 💡, Analyst 📊, Engineer ⚙️  
**Objective:** Solve a problem using logic from an entirely different domain.

---

## State Machine

```
DOMAIN_A_EXTRACTION → DOMAIN_B_MAPPING → PATTERN_SYNTHESIS → BLUEPRINTING → COMPLETE
```

## Steps

| Step | ID                           | Agent                  | Action                                                 |
| ---- | ---------------------------- | ---------------------- | ------------------------------------------------------ |
| 1    | step-01-domain-a-extraction  | Brainstormer           | Select and extract structural logic from source domain |
| 2    | step-02-domain-b-mapping     | Analyst                | Map problem structure to Domain A's logic              |
| 3    | step-03-pattern-synthesis    | Brainstormer + Analyst | Extract transferable pattern; generate novel insight   |
| 4    | step-04-structural-blueprint | Engineer               | Translate pattern into implementation blueprint        |

## Output Artifact

`output/knowledge/synthesis/{problem-slug}-synthesis.md` — cross-domain synthesis report with:

- Domain A structural logic
- Domain B mapping
- Transferable pattern (the novel insight)
- Implementation blueprint

## Audit Trail

Each run logs to `logs/mgi-cross-domain-synthesizer.log`.
