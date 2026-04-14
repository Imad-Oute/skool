# Step 3: Audit Checkpoint

**Agent:** Architect 🏛️  
**Objective:** Apply the next lens and assess whether the audit coverage is complete enough to produce the directive.

---

## Your Task

You are the **Architect** working through the lens set iteratively. Each pass through this checkpoint applies one lens, documents findings, and decides whether more lenses remain.

### Apply the Next Lens

Which lens are you applying in this pass?

```
Current lens:    _______________  (from step-02 selection)
Pass number:     ___  (of ___ total lenses selected)
```

**Audit questions for this lens** (refer to step-02 for lens-specific questions):

```
Key finding 1:   _______________  Severity: H/M/L
Key finding 2:   _______________  Severity: H/M/L
Key finding 3:   _______________  Severity: H/M/L

Root cause:      _______________
Evidence:        _______________
```

### Running Findings Log

Add this lens's findings to the cumulative log:

| Lens        | Finding   | Severity | Root Cause |
| ----------- | --------- | -------- | ---------- |
| [previous]  | [finding] | H/M/L    | [cause]    |
| [this lens] | [finding] | H/M/L    | [cause]    |

### Loop or Proceed?

**Loop back (run `microhard run mgi-system-auditor --loop`):**

- There are more lenses in the step-02 selection that haven't been applied yet
- A finding from this lens revealed a new area that warrants an additional lens
- The findings so far point to a root cause that a specific lens would confirm or refute

**Proceed (run `microhard run mgi-system-auditor --next`):**

- All selected lenses have been applied
- The cumulative findings are sufficient to produce a ranked optimization directive
- No major gaps in the audit coverage remain

---

**Decision:** Loop to apply the next lens, or advance to step-04 to produce the optimization directive.
