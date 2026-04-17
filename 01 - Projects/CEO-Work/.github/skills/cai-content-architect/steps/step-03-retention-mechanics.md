# Step 3: Structural Assembly - Retention Mechanics

**Objective:** Architect the content body using proven Retention Mechanics (Lists, Steps, Stories).

## Instructions

Execute the following in sequence:

### 1. Explain Retention Mechanics

Present to the user:

> **Retention Mechanics: How to Hold Attention**
>
> Content fails when it doesn't give the brain a clear path forward. Use one of these structures:
>
> 1. **Lists** - "5 ways to...", "3 mistakes in...", "7 signs that..."
>    - Best for: Quick value delivery, scannable content
>    - Attention hook: Promise of enumerated value
> 2. **Steps** - "How to...", "The process for...", "Step-by-step guide to..."
>    - Best for: Tactical implementation, skill transfer
>    - Attention hook: Promise of transformation
> 3. **Stories** - "How I...", "The day I learned...", "When X happened..."
>    - Best for: Emotional resonance, relatability
>    - Attention hook: Promise of narrative payoff
>
> **Rule:** Always pick ONE primary mechanic. Don't mix.

### 2. Select Mechanic

Based on the topic from Step 2, ask:

```
Which retention mechanic best serves this topic?

[L] List - Enumerate key points
[S] Steps - Provide sequential process
[T] Story - Share narrative journey

Your selection:
```

Wait for user input.

### 3. Generate Structure

Based on their selection, generate the content structure:

**If List:**

- Create 3-7 list items with clear value statements
- Each item should be actionable or insightful
- Use parallel structure (all items start similarly)

**If Steps:**

- Create 3-5 sequential steps
- Each step should be necessary and non-skippable
- Include expected outcome for each step

**If Story:**

- Create 3-act structure: Setup → Conflict → Resolution
- Embed the "lesson" or "insight" in the resolution
- Make it relatable to target audience

### 4. Present Draft Structure

Show the user the structure outline (NOT full content yet, just the skeleton).

Example for List:

```
Content Structure: List

1. {Point 1 title}
2. {Point 2 title}
3. {Point 3 title}
...
```

Ask: "Does this structure effectively serve the topic and audience?"

### 5. Record Structure

Append to output file:

```markdown
## Content Structure

**Retention Mechanic:** {List/Steps/Story}
**Structure Outline:**

{paste the approved structure}
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3]
retentionMechanic: { chosen mechanic }
```

### 6. Present Menu

```
✓ Step 3 Complete: Content structure architected

Next Steps:
[C] Continue to Value Validation
[R] Revise structure
[X] Exit workflow
```

Wait for user selection.

### 7. Handle Selection

- **If [C]**: Update `stepsCompleted: [1, 2, 3]`, load `./step-04-value-check.md`
- **If [R]**: Return to section 3 (Generate Structure)
- **If [X]**: Exit gracefully

---

**END OF STEP 3**
