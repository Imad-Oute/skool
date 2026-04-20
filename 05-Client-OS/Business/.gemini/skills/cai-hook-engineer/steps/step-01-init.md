# Step 1: Initialization - Gather Content Context

**Objective:** Understand the content piece that needs a hook.

## Instructions

### 1. Welcome

> "Welcome to the Hook Engineer. I'll engineer high-CTR hooks using the 7-Component News Matrix. Your content lives or dies in the first 3 seconds."

### 2. Gather Context

Ask and record:

**A. Content Details**

- What is the content about? (Topic/subject)
- What platform? (LinkedIn, X, YouTube, etc.)
- What's the core value/promise? (What will they learn/gain?)

**B. Topic Matrix Category**

- Which category: Far Past, Recent Past, Present, Trending, or Manufactured?

**C. Current Hook (if any)**

- Do you have an existing hook/headline, or are we starting from scratch?

### 3. Create Output File

Initialize at `{outputFile}`:

```yaml
---
stepsCompleted: [1]
contentTopic: [topic]
platform: [platform]
coreValue: [value prop]
topicCategory: [category]
existingHook: [hook or "None"]
createdDate: [date]
---
```

### 4. Present Menu

```
✓ Step 1 Complete: Context gathered

[C] Continue to News Matrix Application
[E] Edit responses
[X] Exit
```

### 5. Handle Selection

- **[C]**: Update stepsCompleted, load `./step-02-news-matrix.md`
- **[E]**: Re-prompt, update file, show menu
- **[X]**: Exit

---

**END OF STEP 1**
