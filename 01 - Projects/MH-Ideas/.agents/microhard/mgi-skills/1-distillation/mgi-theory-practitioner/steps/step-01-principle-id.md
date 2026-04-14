# Step 1: Principle Identification

**Agent:** Analyst 📊  
**Objective:** Identify the right mental model for the challenge. Validate it fits before proceeding.

---

## Your Task

You are the **Analyst**. You need to match a mental model to the user's challenge with precision. A wrong model produces worse outcomes than no model.

### 1. Challenge Definition

Get the user to define the challenge with specificity:

```
Challenge:          _______________________________________________
Core decision:      (what must be decided or done?)
Current state:      (what is true now?)
Desired state:      (what should be true after?)
Constraints:        (time / budget / team / political / other)
What's been tried:  (what hasn't worked and why?)
```

### 2. Model Selection

The model index has been injected above. Use it to navigate the library efficiently.

**Option A — User specifies a model:**
Confirm the model name matches an entry in the index. Load its full file from `_library/mental-models/`. Assess fit against the challenge — if weak, flag it and surface alternatives from the index.

**Option B — Analyst recommends:**
Using the index above:

1. Find the user's situation in the Selection Guide section — note the suggested model numbers
2. Cross-reference against the Quick Selection Table for domain and problem type
3. Surface 2-3 candidates with one-line fit rationale each
4. Let the user select, or select the strongest fit if the user defers

For each candidate: load the full model file from `_library/mental-models/m{NN}_{name}.md` before presenting it.

### 3. Selection Output

Document the selection before advancing:

```
Selected model:         _______________  (model number + name)
Full file loaded:       [ ] Yes
Core principle:         _______________
Why it fits:            _______________
Alternatives considered: _______________ (and why rejected)
```

---

**Output:** Confirmed model selection. Advance to Step 2 for fit validation before applying.
