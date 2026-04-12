# Step 3: Generate Hook Variants

**Objective:** Engineer 5-10 hook variants using the selected news components.

## Instructions

### 1. Hook Engineering Principles

Present to user:

> **Hook Engineering Rules:**
>
> 1. **<15 words** - Clarity beats cleverness
> 2. **Lead with power** - Strongest component first
> 3. **Create curiosity gap** - Promise without revealing
> 4. **Use power words** - Revealed, Exposed, Why, How, Never, Always
> 5. **Test conflict** - "X vs Y", "Why X is wrong about Y"

### 2. Generate Variants

Based on the news components from Step 2, generate 5-10 hook variants.

**Example Format:**

```
Hook Variant 1: [Conflict + Unusual]
"Why the best content marketers never use hooks"

Hook Variant 2: [Recency + Relevancy]
"LinkedIn just changed the algorithm - here's what matters now"

Hook Variant 3: [Celebrity + Conflict]
"Gary Vee was wrong about X. Here's why."

... (continue for 5-10 variants)
```

### 3. Present Variants

Show all variants to the user and ask:

```
Generated {N} hook variants based on your news components.

Which hook variants feel most compelling? (Select 2-3 finalists)

[Numbers corresponding to variants]
```

### 4. Record Hooks

Append to output file:

```markdown
## Hook Variants Generated

### All Variants:

{List all generated hooks}

### Finalists Selected by User:

1. {Hook X}
2. {Hook Y}
3. {Hook Z}
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3]
totalVariants: { number }
finalists: [{ list of finalist hooks }]
```

### 5. Present Menu

```
✓ Step 3 Complete: Hook variants generated and finalists selected

[C] Continue to 3-Second Validation
[R] Generate different variants
[X] Exit
```

### 6. Handle Selection

- **[C]**: Load `./step-04-validate.md`
- **[R]**: Return to section 2
- **[X]**: Exit

---

**END OF STEP 3**
