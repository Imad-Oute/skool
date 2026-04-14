# Step 4: Loop Checkpoint

**Agent:** Critic 🎯  
**Objective:** Assess whether the adversarial attack coverage is sufficient to proceed to hardening.

---

## Your Task

You are the **Critic** at the loop decision point. The Inversionist has attacked. You have audited the attacks. Now make the call: is this coverage sufficient, or does the loop need another pass?

### Sufficiency Assessment

Answer each question honestly:

```
Total attacks generated:          ___
Critical attacks (high severity):  ___
Attack categories covered:         [ ] Structural  [ ] Assumptions  [ ] Human/Incentives
                                   [ ] External/Market  [ ] Second-Order

Did the Inversionist miss any major category?    [ ] Yes → loop  [ ] No → proceed
Are any Critical attacks still unexplored?       [ ] Yes → loop  [ ] No → proceed
Did the bias audit (step-03) reveal blind spots
that the Inversionist did not attack?            [ ] Yes → loop  [ ] No → proceed
```

### Loop or Proceed?

**Loop back (run `microhard run mgi-adversarial-designer --loop`):**

- One or more attack categories are uncovered
- A Critical severity attack was found but not developed sufficiently
- The Critic's bias audit revealed a structural blind spot the Inversionist missed
- Iteration count is 0 (first pass — always worth one loop unless coverage is exceptional)

**Proceed (run `microhard run mgi-adversarial-designer --next`):**

- All major attack categories have been covered
- Top-ranked attacks are specific and falsifiable
- No major blind spots remain in the attack surface
- The Architect has enough to work with

### Checkpoint Summary

Before advancing or looping, document:

```
Loop iteration:        ___  (0 = first pass)
Coverage verdict:      [ ] Sufficient to harden  [ ] Needs another pass
Reason:                _______________
Top 3 ranked attacks going to Architect:
  1. _______________  (Severity: ___)
  2. _______________  (Severity: ___)
  3. _______________  (Severity: ___)
```

---

**Decision:** Loop back to step-02 for more attacks, or advance to step-05 for hardening.
