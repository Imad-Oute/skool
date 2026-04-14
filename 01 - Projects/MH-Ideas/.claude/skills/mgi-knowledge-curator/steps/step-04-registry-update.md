# Step 4: Registry Update

**Agent:** Curator 📚  
**Objective:** Assemble the final artifact and write it to the mental-models/ library.

---

## Your Task

You are the **Curator** finalizing the knowledge artifact. Assemble all outputs from the previous steps into the canonical library format, then write it to `output/knowledge/mental-models/{domain}/{model-name}.md`.

### Final Artifact Template

```markdown
---
name: { model-name-kebab-case }
displayName: '{Human Readable Model Name}'
domain: { primary-domain }
subDomain: { sub-domain }
problemTypes: [{ type1 }, { type2 }]
tags: [{ keyword1 }, { keyword2 }, { keyword3 }]
source: '{Author/Origin}'
version: 1.0
created: { YYYY-MM-DD }
crossLinks:
  reinforces: []
  contradicts: []
  dependsOn: []
  enables: []
---

# {Human Readable Model Name}

## Core Principle

{One sentence causal law: When X, apply Y → Z because MECHANISM}

## Mechanism

{2-3 sentences on HOW it works}

## When To Apply

- {Condition 1}
- {Condition 2}
- {Condition 3}

## Failure Modes

- **Fails when:** {condition}
- **Systematically ignores:** {blind spot}
- **Second-order risk:** {downstream effect}

## Leverage Points

{Where this model produces highest ROI}

## Cross-Links

- **Reinforces:** {model} — {why}
- **Contradicts:** {model} — {tension}
- **Depends On:** {model} — {prerequisite}
- **Enables:** {model} — {what it unlocks}

## Distillation Source

- **Origin:** {author/title}
- **Distilled by:** MGI Knowledge Curator
- **Date:** {YYYY-MM-DD}
```

### Checklist Before Saving

- [ ] Core Principle is one sentence in causal law format
- [ ] Failure modes are specific, not vague
- [ ] Cross-links point to real models in the library (or flag as "pending")
- [ ] YAML frontmatter is valid
- [ ] File saved to correct domain subfolder: `output/knowledge/mental-models/{domain}/{model-name}.md`

### Audit Log Entry

After saving, append to `logs/mgi-knowledge-curator.log`:

```
[{timestamp}] INGESTED  model={model-name}  domain={domain}  source={source}
```

---

**Skill complete.** The mental model is now part of the MGI cognitive library.
