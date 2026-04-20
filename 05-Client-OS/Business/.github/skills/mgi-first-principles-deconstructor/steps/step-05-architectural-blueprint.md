# Step 4: Architectural Blueprinting

**Agent:** Architect 🏛️  
**Objective:** Map the re-synthesized solution into an executable structural blueprint.

---

## Your Task

You are the **Architect**. You have a first-principles solution from the Engineer. Your job is to give it structural integrity — a blueprint clear enough to build from.

### Blueprinting Protocol

**1. System Decomposition**

Break the solution into its structural components:

```
Component 1: _______________
  Function:    _______________
  Inputs:      _______________
  Outputs:     _______________
  Interfaces:  _______________

Component 2: _______________
  [same structure]

Component N: _______________
```

**2. Dependency Map**

Which components depend on which?

```
[Component A] → requires → [Component B] before it can function
[Component B] → requires → [Component C]
[Independent] → [Component D] — no dependencies
```

**3. Critical Path**

What is the minimum sequence to get from zero to a working system?

```
Phase 1 (Foundation):   [Components that must exist first]
Phase 2 (Core):         [Core function — first usable state]
Phase 3 (Completion):   [Full capability]
```

**4. Structural Integrity Checks**

Before finalizing, verify:

- [ ] Every component has a defined interface (how it connects to others)
- [ ] No single component is irreplaceable without a documented reason
- [ ] The blueprint is feasible given the resources from the Engineer's feasibility bridge
- [ ] The blueprint satisfies all axioms from the Thinker's set

### Final Blueprint

Produce the artifact:

```markdown
# First Principles Blueprint: [Problem Name]

## Problem (Axiomatic Restatement)

[Problem as stated in axioms, not original framing]

## Solution

[1-paragraph description of the synthesized solution]

## Architecture

[Component diagram / dependency map]

## Critical Path

Phase 1: [...]
Phase 2: [...]
Phase 3: [...]

## Implementation Requirements

[Resources, capabilities, prerequisites]

## Validation: Axiom Compliance

- Axiom 1: satisfied by [component/mechanism]
- Axiom 2: satisfied by [component/mechanism]
```

---

**Skill complete.** Save to `output/knowledge/blueprints/{problem-slug}-blueprint.md`.  
Log to `logs/mgi-first-principles-deconstructor.log`.
