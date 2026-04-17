# Workflow: mgi-ingest-mental-model

**Skill:** mgi-knowledge-curator  
**Agents:** Curator 📚, Analyst 📊  
**Objective:** Transform raw source material into an executable mental model artifact.

---

## State Machine

```
RAW_CAPTURE → DISTILLATION → TAGGING → REGISTRY_UPDATE → COMPLETE
```

## Steps

| Step | ID                      | Agent   | Action                                     |
| ---- | ----------------------- | ------- | ------------------------------------------ |
| 1    | step-01-raw-capture     | Analyst | Define source, extract raw content         |
| 2    | step-02-distillation    | Curator | Strip noise, extract core principles       |
| 3    | step-03-tagging         | Curator | Apply domain tags, index keys, cross-links |
| 4    | step-04-registry-update | Curator | Write artifact to mental-models/ library   |

## Output Artifact

`output/knowledge/mental-models/{domain}/{model-name}.md` — structured mental model with:

- `## Core Principle` — the axiomatic truth
- `## When To Apply` — conditions for use
- `## Failure Modes` — when the model breaks down
- `## Cross-Links` — related models in the library
- `## Distillation Source` — provenance

## Audit Trail

Each run logs to `logs/mgi-knowledge-curator.log`.
