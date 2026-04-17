# Step 3: Axiom Checkpoint

**Agent:** Thinker 🧠  
**Objective:** Verify the axiom set is genuinely axiomatic before rebuilding from it.

---

## Your Task

You are the **Thinker** at the loop decision point. You have a candidate axiom set from step-02. Before handing it to the Engineer for re-synthesis, verify these are _actual axioms_ — not inherited assumptions wearing axiom clothing.

### Axiom Quality Test

For each axiom in your set, run this test:

```
Axiom: _______________

1. Constraint type:     [ ] Physical  [ ] Logical  [ ] Legal  [ ] Economic
                        [ ] Cultural  [ ] Organizational  [ ] Technological

2. Has anyone solved a similar problem by violating this?
   [ ] Yes → this is NOT an axiom. Remove it or reclassify.
   [ ] No  → continue

3. Can you state WHY this is true at a fundamental level (not "because it's the rule")?
   [ ] Yes: _______________
   [ ] No  → this is an assumption. Remove it.

4. Would this still be true if the industry, company, or team changed completely?
   [ ] Yes → genuine axiom
   [ ] No  → convention or organizational assumption
```

### Axiom Set Verdict

```
Axioms that passed all 4 tests:  ___  → these are your real axioms
Axioms removed or reclassified:  ___  → log what they were

Final axiom count: ___
```

### Loop or Proceed?

**Loop back (run `microhard run mgi-first-principles-deconstructor --loop`):**

- More than half the "axioms" from step-02 failed the test
- One or more axioms are actually organizational conventions that could be questioned
- The axiom set feels too large (more than 5-6 axioms usually means assumptions slipped through)
- A new, genuinely foundational truth emerged during the test that wasn't in the original set

**Proceed (run `microhard run mgi-first-principles-deconstructor --next`):**

- All remaining axioms pass the 4-part test
- The set is minimal (only what is absolutely true)
- You can defend each axiom to a skeptic who knows nothing about the industry

---

**Decision:** Loop to step-02 for a cleaner deconstruction, or advance to step-04 for re-synthesis.
