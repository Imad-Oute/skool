# Step 4: 3-Second Validation

**Objective:** Test finalist hooks against the 3-Second Rule and CTR criteria.

## Instructions

### 1. Explain 3-Second Rule

> **The 3-Second Rule:**
>
> On any platform, you have 3 seconds to:
>
> 1. **Stop** the scroll/browse behavior
> 2. **Create** a need-to-know loop
> 3. **Compel** the click/read action
>
> If your hook fails any of these, it's dead content.

### 2. Validation Checklist

For each finalist hook from Step 3, run through:

```
Hook Validation Checklist:

Hook: "{finalist hook}"

[ ] <15 words - Meets length requirement
[ ] Contains 2+ news components - Matrix compliance
[ ] Creates immediate curiosity gap - "I need to know this"
[ ] Uses power words or conflict - Emotional trigger present
[ ] Passes "scroll test" - Would I stop for this?
[ ] Platform-appropriate - Fits native expectations
[ ] Clear value promise - I know what I'll get

Score: {X}/7
```

Do this for each finalist.

### 3. Identify Winner

Ask user:

```
Based on validation scores:

Hook A: {score}/7
Hook B: {score}/7
Hook C: {score}/7

Which hook do you want to deploy?
Or should we iterate on the highest-scoring variant?

[A/B/C] Deploy selected hook
[I] Iterate on best-scoring hook
```

### 4. Record Validation

Append to output file:

```markdown
## 3-Second Validation Results

### Finalist A: "{hook}"

- Length: {word count} words
- Components: {list}
- Curiosity gap: {Yes/No}
- Power words: {list found}
- Scroll test: {Pass/Fail}
- Platform fit: {Yes/No}
- Value promise: {Clear/Unclear}
  **Score: {X}/7**

[Repeat for each finalist]

### Selected Winner:

**Hook:** "{winning hook}"
**Score:** {X}/7
**Rationale:** {why this hook won}
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3, 4]
winningHook: '{selected hook}'
validationScore: { score }
```

### 5. Present Menu

```
✓ Step 4 Complete: Hook validated and winner selected

[C] Continue to Finalization & Tracking
[R] Revise/iterate on hook
[X] Exit
```

### 6. Handle Selection

- **[C]**: Load `./step-05-finalize.md`
- **[R]**: Return to Step 3 for iteration
- **[X]**: Exit

---

**END OF STEP 4**
