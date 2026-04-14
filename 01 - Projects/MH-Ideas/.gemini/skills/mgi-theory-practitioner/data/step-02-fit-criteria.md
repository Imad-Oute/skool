# Model Fit Assessment Criteria

Use this framework to validate whether the selected model is the right one before proceeding to application.

---

## Fit Levels

**Strong fit** — Proceed without caveats

- The model's core mechanism directly addresses the challenge's root cause
- The applicability conditions described in the model file are met
- No known failure modes from the model file apply to this situation
- A different person using this model would arrive at the same structural insights

**Moderate fit** — Proceed with explicit caveats

- The model partially addresses the challenge (covers 1-2 dimensions, not all)
- Some applicability conditions are met, others are unclear
- Document which parts of the model apply and which do not before proceeding
- Flag the gap to the user

**Weak fit / Mismatch** — Stop. Do not proceed.

- The model's mechanism does not match the challenge's structure
- The applicability conditions are not met
- A known failure mode from the model file applies directly to this situation
- Recommend a better-fitting model or state that no strong-fit model exists for this challenge

---

## Force-Fit Warning

A force-fitted model produces outputs that feel structured but are wrong.
Signs of force-fitting:

- You had to stretch the model's definition to make it apply
- The challenge required ignoring one of the model's core components
- The model's failure modes match the challenge more than its applicability conditions do

When in doubt: weak fit = no model. A clear problem statement with no model is more valuable than a wrong model confidently applied.
