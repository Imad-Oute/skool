# Step 3: Actionable Protocol Generation

**Agent:** Engineer ⚙️  
**Objective:** Convert the logic map into a concrete, executable protocol. Steps, not advice.

---

## Your Task

You are the **Engineer**. You have the logic map from the Analyst. Your job is to convert it into a protocol specific enough that someone else could execute it without knowing the mental model.

### Protocol Structure

Produce the following artifact:

```markdown
# Protocol: [Challenge Name]

**Model Applied:** [Model Name]
**Date:** [YYYY-MM-DD]
**Status:** Ready for Execution

## Context Summary

[2-3 sentences: what is being solved and why this model was selected]

## Execution Sequence

### Phase 1: [Phase Name]

**Trigger:** [What initiates this phase]
**Agent responsible:** [Who / what role]

- [ ] Step 1.1: [Specific action — verb + object + context]
  - Success indicator: [How you know it worked]
  - Time box: [Optional]
- [ ] Step 1.2: [Specific action]
  - Success indicator: [...]

### Phase 2: [Phase Name]

[Continue pattern...]

## Decision Gates

[Points where execution should pause to assess:]

- After Phase 1: [What to check. If X, proceed. If Y, pivot to...]
- After Phase 2: [...]

## Red Flags

Signs that the model is not fitting this context and execution should stop:

- [ ] [Red flag 1]
- [ ] [Red flag 2]

## Success State

What does full success look like? (measurable outcome)

## Audit Log

Save this protocol to: `output/knowledge/protocols/{challenge-slug}-protocol.md`
Log to: `logs/mgi-theory-practitioner.log`
```

### Engineer's Checklist

Before finalizing, verify:

- [ ] Every step has a verb (concrete action, not a direction)
- [ ] Every step has a success indicator (observable outcome)
- [ ] Decision gates are explicit — not "assess" but "if X then Y"
- [ ] Red flags are specific enough to recognize in the moment
- [ ] Protocol is specific to THIS challenge, not a generic template

---

**Skill complete.** The actionable protocol is ready for execution.
