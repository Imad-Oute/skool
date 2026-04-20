# Step 2: Topic Selection - 5-Category Matrix

**Objective:** Select or categorize the topic using the systematic 5-Category Topic Matrix.

## Instructions

Execute the following in sequence:

### 1. Explain the Matrix

Present to the user:

> **The 5-Category Topic Matrix**
>
> Topics fall into five temporal categories, each with different attention dynamics:
>
> 1. **Far Past** - Historical lessons, origin stories, foundational principles
> 2. **Recent Past** - Last 6-24 months, recent shifts, emerging patterns
> 3. **Present** - Current events, active trends, today's problems
> 4. **Trending** - Hot topics, viral moments, zeitgeist capture
> 5. **Manufactured** - Original frameworks, unique angles, proprietary systems
>
> The best content often combines multiple categories (e.g., Trending + Manufactured).

### 2. Topic Selection

**If user provided a topic in Step 1:**

- Categorize it using the matrix above
- Show: "Your topic '{topic}' falls into: [{category}]"
- Ask: "Does this categorization make sense, or should we adjust?"

**If user needs topic suggestions:**

- Based on `{target_industry}` from config, suggest 3 topics (one from each: Recent Past, Present, Manufactured)
- Format:

  ```
  A. [Recent Past] - {topic title} - {one-line value prop}
  B. [Present] - {topic title} - {one-line value prop}
  C. [Manufactured] - {topic title} - {one-line value prop}
  ```

- Ask: "Which topic resonates, or would you like different suggestions?"

### 3. Record Decision

Append to output file:

```markdown
## Topic Selection

**Chosen Topic:** {final topic}
**Category:** {matrix category}
**Why This Works:** {2-3 sentences on why this topic has attention potential}
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2]
topic: { chosen topic }
topicCategory: { matrix category }
```

### 4. Present Menu

```
✓ Step 2 Complete: Topic selected and categorized

Next Steps:
[C] Continue to Structural Assembly (Retention Mechanics)
[R] Revise topic selection
[X] Exit workflow
```

Wait for user selection.

### 5. Handle Selection

- **If [C]**: Update `stepsCompleted: [1, 2]`, load `./step-03-retention-mechanics.md`
- **If [R]**: Return to section 2 (Topic Selection)
- **If [X]**: Exit gracefully

---

**END OF STEP 2**
