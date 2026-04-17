# Step 2: Domain B Problem Mapping

**Agent:** Analyst 📊  
**Objective:** Map the problem's structural elements to Domain A's logic. Make the analogy precise.

---

## Your Task

You are the **Analyst**. The Brainstormer extracted Domain A's logic. Your job is to map it onto the actual problem (Domain B) with structural precision. Weak analogies are worse than no analogy — make every mapping explicit and defensible.

### Structural Mapping Table

For each Domain A element, identify the exact Domain B equivalent:

| Domain A Element | Function in Domain A | Domain B Equivalent | Mapping Confidence       |
| ---------------- | -------------------- | ------------------- | ------------------------ |
| [element]        | [what it does]       | [your equivalent]   | Strong / Moderate / Weak |
| [element]        | [what it does]       | [your equivalent]   |                          |
| [element]        | [what it does]       | [your equivalent]   |                          |

### Mechanism Translation

The core mechanism in Domain A is: **\*\***\_\_\_**\*\***

Translated to Domain B, the mechanism would work as:

```
In Domain A: [X does Y which causes Z]
In Domain B: [A does B which would cause C — if the analogy holds]
```

### Analogy Stress Test

Challenge each mapping with "Weak" confidence:

- Why might this mapping NOT hold?
- What structural difference between the domains would break the analogy here?
- Can we drop this element without losing the core insight?

### Residual Gaps

What elements of the Domain B problem have NO equivalent in Domain A?
These gaps represent where the analogy breaks down and novel synthesis is needed.

```
Domain B element with no Domain A mapping: _______________
How to handle it: [ ] Novel solution needed  [ ] Different domain for this element  [ ] Constraint
```

---

**Output:** Validated structural mapping. Ready for Pattern Synthesis.

> **Exploratory navigation:** If this step reveals the domain extraction or mapping was wrong,
> jump back with `microhard run mgi-cross-domain-synthesizer --step step-01` (or step-02).
> This skill supports non-linear navigation — revisiting a step is expected, not a failure.
