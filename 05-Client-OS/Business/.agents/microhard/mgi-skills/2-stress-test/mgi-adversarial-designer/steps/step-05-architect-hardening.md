# Step 4: Architect Hardening

**Agent:** Architect 🏛️  
**Objective:** Rebuild the plan's surviving elements into a structurally reinforced version.

---

## Your Task

You are the **Architect**. You have the Inversionist's failure map and the Critic's bias audit. Your job is not to patch the plan — it is to redesign the elements that failed, while preserving the intent.

### Hardening Protocol

**1. Triage the Findings**

Categorize everything from the failure map + bias audit:

| Finding        | Source              | Fix Required   | Priority             |
| -------------- | ------------------- | -------------- | -------------------- |
| [failure/bias] | Inversionist/Critic | [specific fix] | Critical/High/Medium |

**2. Address Each Critical Finding**

For every **Critical** finding, produce a structural fix:

```
Finding:          _______________
Root cause:       _______________
Structural fix:   _______________  (not a mitigation — a redesign)
Why this works:   _______________
Tradeoff:         _______________  (what does this fix cost?)
```

**3. Redundancy Design**

For every **Single Point of Failure** identified:

- What is the backup mechanism if SPOF fails?
- At what threshold should the backup activate?
- Who is responsible for monitoring the SPOF?

**4. Assumption Validation Protocol**

For every critical assumption:

- How can this assumption be validated before full commitment?
- What is the cheapest/fastest test to validate it?
- At what point in execution is the assumption no longer reversible?

### Hardened Plan Output

Produce the final hardened version:

```markdown
## Hardened Plan: [Plan Name]

### What Changed (vs. Original Plan)

- [Change 1]: [Why it changed]
- [Change 2]: [Why it changed]

### Core Structure (Unchanged)

[What survived stress-testing intact]

### Hardened Elements

[Redesigned components with their fixes]

### Monitoring & Circuit Breakers

[What to watch. At what trigger to stop or pivot]

### Pre-Execution Validation Steps

[Tests to run before full commitment]

### Residual Risks (Accepted)

[Risks that remain after hardening — acknowledged, not ignored]
```

---

**Skill complete.** Save hardened plan to `output/knowledge/stress-tests/{plan-slug}-hardened.md`.  
Log to `logs/mgi-adversarial-designer.log`.
