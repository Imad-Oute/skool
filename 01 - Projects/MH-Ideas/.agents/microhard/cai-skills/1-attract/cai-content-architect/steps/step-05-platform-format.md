# Step 5: Platform Optimization - Format for Native Expectations

**Objective:** Format the content to match the native expectations and constraints of the target platform.

## Instructions

Execute the following in sequence:

### 1. Platform-Specific Rules

Display the formatting rules based on the platform from Step 1:

**LinkedIn (Text Post):**

- Max 3,000 characters (aim for 1,500-2,000 for full visibility)
- Use line breaks every 2-3 lines for readability
- Emojis: Strategic (1-3 max), not decorative
- Hook: First 2 lines must stop the scroll
- Call-to-action: Explicit at the end

**X/Twitter (Thread):**

- Max 280 characters per tweet
- Thread length: 5-10 tweets ideal
- Tweet 1: Hook (question or bold claim)
- Middle tweets: Value delivery
- Final tweet: CTA + thread summary
- Use numbers (1/, 2/, 3/) for navigation

**YouTube (Video Script):**

- Hook: First 8 seconds critical (state problem/promise)
- Pattern breaks every 20-30 seconds (visual, tonal, or informational)
- Retention mechanic visible in thumbnails/title
- CTA: Mid-video and end-video

**Blog/Article:**

- Headline: Clear value promise (8-12 words)
- Subheadings every 200-300 words
- Short paragraphs (3-4 lines max)
- Use bold for scannable key points
- Images/visual breaks every 400-500 words

### 2. Generate Formatted Content

Based on the validated structure from Steps 3-4 and the platform rules above:

Ask the user: "Should I generate the full formatted content now, or would you prefer to write it yourself using this structure as a guide?"

**If they want you to generate:**

- Write the complete content following platform rules
- Apply the retention mechanic from Step 3
- Ensure the core reward from Step 4 is clear

**If they prefer to write themselves:**

- Provide the structure + platform formatting checklist
- Skip to finalization

### 3. Record Formatted Content

Append to output file:

```markdown
## Platform-Optimized Content

**Platform:** {platform from Step 1}
**Format:** {format from Step 1}

### Final Content

{formatted content OR "User will self-author using provided structure"}

---

**Platform Compliance Checklist:**

- [ ] Hook/opening follows platform best practices
- [ ] Length within platform constraints
- [ ] Formatting optimized for readability
- [ ] CTA is clear and platform-appropriate
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3, 4, 5]
contentGenerated: { true/false }
```

### 4. Present Menu

```
✓ Step 5 Complete: Content formatted for platform

Next Steps:
[C] Continue to Finalization & Audit Tracking
[R] Revise formatting
[X] Exit workflow
```

Wait for user selection.

### 5. Handle Selection

- **If [C]**: Update `stepsCompleted: [1, 2, 3, 4, 5]`, load `./step-06-finalize.md`
- **If [R]**: Return to section 2 (Generate Formatted Content)
- **If [X]**: Exit gracefully

---

**END OF STEP 5**
