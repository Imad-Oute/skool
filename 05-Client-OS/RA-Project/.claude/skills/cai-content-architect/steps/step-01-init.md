# Step 1: Initialization

**Objective:** Gather context and objectives for the content unit to be created.

## Instructions

Execute the following in sequence:

### 1. Welcome & Context

Greet the user and explain:

> "Welcome to the Content Architect. I'll help you build a high-value content unit using systematic topic selection and retention mechanics."

### 2. Gather Context

Ask the following questions and record responses:

**A. Platform & Format**

- What platform is this content for? (LinkedIn, X/Twitter, YouTube, Blog, etc.)
- What format? (Video, Text Post, Thread, Article, etc.)

**B. Audience & Goal**

- Who is the target audience?
- What action should they take after consuming this content?

**C. Topic Input (Optional)**

- Do you have a topic in mind, or should I suggest one based on your industry/niche?

### 3. Load Config

Read the configuration from `{config}`:

- `target_industry` - Use for topic suggestions
- `output_content` - Output location
- `acquisition_strategy` - Influences content approach

### 4. Create Output File

Create the output file at: `{outputFile}`

Initialize with this frontmatter:

```yaml
---
stepsCompleted: [1]
platform: [user's answer]
format: [user's answer]
targetAudience: [user's answer]
goal: [user's answer]
topicInput: [user's answer or "TBD"]
createdDate: [current date]
---
```

### 5. Present Menu

Show the user:

```
✓ Step 1 Complete: Context gathered

Next Steps:
[C] Continue to Topic Selection (5-Category Matrix)
[E] Edit responses before continuing
[X] Exit workflow
```

Wait for user selection.

### 6. Handle Selection

- **If [C]**: Update `stepsCompleted: [1]` in frontmatter, then load `./step-02-topic-matrix.md`
- **If [E]**: Re-prompt for any field they want to change, update output file, show menu again
- **If [X]**: Exit gracefully with "Workflow paused. Run this skill again to resume."

---

**END OF STEP 1**
