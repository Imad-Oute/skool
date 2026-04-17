# Step 2: Apply 7-Component News Matrix

**Objective:** Identify which news components apply to this content.

## Instructions

### 1. Explain the Matrix

> **The 7-Component News Matrix**
>
> What makes people click? Journalists have known for decades:
>
> 1. **Recency** - "Just happened", "Breaking", "New"
> 2. **Relevancy** - Directly affects audience's life/business
> 3. **Celebrity** - Known person/brand involved
> 4. **Proximity** - Geographic or community closeness
> 5. **Conflict** - Opposition, controversy, tension
> 6. **Unusual** - Unexpected, counter-intuitive, rare
> 7. **Ongoing** - Part of larger narrative/trend
>
> **Rule:** Use at least 2 components for maximum hook power.

### 2. Analyze Content

Based on the content from Step 1, identify which components apply:

```
Which news components are present in your content?

[R] Recency - Is this new/breaking?
[V] Relevancy - Does this directly impact them?
[C] Celebrity - Does this involve known figures?
[P] Proximity - Is this in their world/industry?
[F] Conflict - Is there tension/opposition?
[U] Unusual - Is this counter-intuitive/rare?
[O] Ongoing - Part of a bigger trend?

Select 2-4 that apply:
```

### 3. Record Matrix

Append to output file:

```markdown
## News Matrix Analysis

**Selected Components:**

- {Component 1}: {why it applies}
- {Component 2}: {why it applies}
- {Component 3}: {why it applies (if applicable)}

**Hook Strategy:** Combine {Component X} + {Component Y} for maximum stopping power.
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2]
newsComponents: [{ list }]
```

### 4. Present Menu

```
✓ Step 2 Complete: News components identified

[C] Continue to Hook Generation
[R] Revise component selection
[X] Exit
```

### 5. Handle Selection

- **[C]**: Load `./step-03-generate-hooks.md`
- **[R]**: Return to section 2
- **[X]**: Exit

---

**END OF STEP 2**
