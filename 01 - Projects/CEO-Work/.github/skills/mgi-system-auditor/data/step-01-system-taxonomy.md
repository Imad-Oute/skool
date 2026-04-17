# System Taxonomy — Audit Lens Selection

Identify the system type first. The audit lenses you apply depend entirely on what kind of system you are auditing.

---

## System Types and Their Primary Failure Modes

### Technical Architecture

A software system, infrastructure, or data pipeline.
**Primary failure modes:** abstraction bloat, coupling failures, scalability cliffs, undocumented dependencies, test coverage gaps
**Relevant audit lenses:** complexity, coupling, abstraction layers, failure modes, observability

### Business Process

A repeatable operational workflow (sales, fulfillment, onboarding, support).
**Primary failure modes:** bottlenecks, incentive misalignment, manual handoffs, invisible feedback loops, process drift
**Relevant audit lenses:** bottlenecks, incentive alignment, feedback loops, waste, handoff quality

### Team / Organizational Structure

A team, department, or organizational unit.
**Primary failure modes:** decision rights confusion, communication overhead, misaligned incentives, trust deficits, unclear ownership
**Relevant audit lenses:** decision rights, communication overhead, incentives, trust, ownership clarity

### Marketing / Acquisition System

A lead generation, content, or paid acquisition pipeline.
**Primary failure modes:** vanity metrics, broken feedback loops, unit economics drift, attribution gaps, channel saturation
**Relevant audit lenses:** funnel, feedback loops, unit economics, signal quality, channel health

### Knowledge / Cognitive System

A decision-making framework, knowledge base, or institutional intelligence structure.
**Primary failure modes:** outdated mental models, blind spots, confirmation bias in data selection, no update mechanism
**Relevant audit lenses:** mental model currency, blind spots, update mechanisms, decision quality

---

## Selecting 3-5 Audit Lenses

After identifying system type:

1. Select the 3-5 most relevant lenses from the list above
2. Prioritize lenses that match the user's reported symptoms
3. Explicitly state which lenses you are NOT applying and why
4. Document your selection — the Architect's findings are only as good as the lens selection
