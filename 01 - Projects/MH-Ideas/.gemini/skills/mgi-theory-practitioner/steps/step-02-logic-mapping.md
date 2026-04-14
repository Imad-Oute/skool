# Step 2: Fit Validation + Logic Mapping

**Agent:** Analyst 📊  
**Objective:** Validate the selected model is the right fit, then map its causal logic onto the user's context.

---

## Your Task

You are the **Analyst**. The fit criteria have been injected above. Use them before proceeding to mapping.

### Fit Validation

Apply the fit criteria (see injected reference above):

```
Model selected:         _______________
Fit level:              [ ] Strong  [ ] Moderate  [ ] Weak / Mismatch
Applicability check:    [ ] Conditions met  [ ] Partial  [ ] Not met
Known failure modes:    [ ] None apply  [ ] One applies: _______________
```

**If Weak or Mismatch:** Stop. Return to step-01 and select a better-fitting model. Do not proceed to mapping with a weak fit.

**If Strong or Moderate:** Proceed.

---

## Logic Mapping

Translate the model's abstract principles into the concrete reality of this specific challenge.

### Mapping Protocol

**1. Restate the Core Principle in Context**

Take the model's core principle:

> "When [CONDITION X], apply [ACTION Y] → [OUTCOME Z] because [MECHANISM]"

Now rewrite it with the user's specifics substituted in:

> "When [USER'S SPECIFIC CONDITION], apply [SPECIFIC ACTION IN THEIR CONTEXT] → [EXPECTED OUTCOME IN THEIR CONTEXT] because [MECHANISM AS IT OPERATES HERE]"

**2. Identify the Leverage Points**

Where in the user's situation does this model's mechanism have the highest leverage?

- What is the single highest-impact action the model prescribes for this context?
- What would change first if the model's logic were applied?
- What would change second (downstream)?

**3. Map the Variables**

| Model Variable | User's Context Equivalent             |
| -------------- | ------------------------------------- |
| [model term 1] | [how it manifests in their situation] |
| [model term 2] | [how it manifests in their situation] |
| [model term 3] | [how it manifests in their situation] |

**4. Identify Contextual Failure Risks**

Does anything in the user's context trigger the model's known failure modes?

- If yes: flag it explicitly and note how to mitigate
- If no: confirm and proceed

---

**Output:** A completed logic map showing exactly how the model's causal structure maps to the user's challenge. Hand to Engineer for protocol generation.
