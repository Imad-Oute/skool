# Step 4: Value Validation - Reward Check

**Objective:** Verify that the "Reward" (the takeaway) is clearly articulated and valuable.

## Instructions

Execute the following in sequence:

### 1. Explain Value-Per-Second Principle

Present to the user:

> **Value-Per-Second: The Content Architect's Standard**
>
> Content isn't too long; it's too boring. Every second must deliver:
>
> - **Insight** - New knowledge or perspective
> - **Action** - Tactical step they can take
> - **Validation** - Confirmation of their experience
>
> If a section doesn't serve one of these, cut it.

### 2. Review Current Structure

Display the structure from Step 3 and ask:

```
Let's validate each component:

For each item in your structure:
1. What specific insight/action/validation does it deliver?
2. Can the audience apply this immediately?
3. Would you personally find this valuable?
```

### 3. Reward Articulation

Ask the user:

> "In one sentence: What should the audience be able to DO or KNOW after consuming this content?"

Record their answer as the **Core Reward Statement**.

### 4. Value Density Audit

Run through this checklist with the user:

```
Value Density Checklist:

[ ] The opening clearly states the problem or promise
[ ] Each section delivers on that promise incrementally
[ ] No fluff, filler, or "setup" that doesn't serve the reward
[ ] The closing reinforces the takeaway/action
[ ] The audience can implement something in <24 hours
```

For any unchecked items, ask: "How should we adjust the structure to fix this?"

### 5. Record Validation

Append to output file:

```markdown
## Value Validation

**Core Reward Statement:** {one-sentence reward}

**Value Density Audit:**

- Opening: {status}
- Sections: {status}
- No fluff: {status}
- Closing: {status}
- Immediate action: {status}

**Validated:** {Yes/No - with explanation if No}
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3, 4]
coreReward: { reward statement }
valueValidated: { true/false }
```

### 6. Present Menu

```
✓ Step 4 Complete: Value validated

Next Steps:
[C] Continue to Platform Optimization
[R] Revise structure to improve value density
[X] Exit workflow
```

Wait for user selection.

### 7. Handle Selection

- **If [C]**: Update `stepsCompleted: [1, 2, 3, 4]`, load `./step-05-platform-format.md`
- **If [R]**: Return to Step 3 for structure revision
- **If [X]**: Exit gracefully

---

**END OF STEP 4**
