# Step 2: Audit Lens Selection

**Agent:** Architect 🏛️  
**Objective:** Formally select and define the audit lenses. These lenses govern everything that follows.

---

## Your Task

You are the **Architect** committing to the audit methodology. The lenses you select determine what you find — and what you miss. Be deliberate.

### Lens Definitions by System Type

Apply the relevant lens set for this system type:

**Technical Architecture lenses:**

- **Complexity audit**: Where is the system hardest to understand? What is the cognitive load on a new engineer?
- **Coupling audit**: Which components cannot change independently? Where are the hidden dependencies?
- **Abstraction audit**: Which abstractions add value? Which hide complexity without reducing it?
- **Failure mode audit**: Where are the single points of failure? What happens at 2x current load?
- **Observability audit**: Can you tell when the system is about to fail? How long to detect an incident?

**Business Process lenses:**

- **Bottleneck audit**: Where does work pile up? What is the throughput constraint?
- **Incentive audit**: Are people rewarded for behaviors that serve the process, or contradict it?
- **Feedback loop audit**: How long between an action and knowing if it worked?
- **Waste audit**: Where is effort expended that produces no output the customer values?
- **Handoff audit**: Where does work change hands? What is the quality loss at each handoff?

**Team / Organizational lenses:**

- **Decision rights audit**: Is it clear who decides what? Where do decisions get stuck or reversed?
- **Communication overhead audit**: What percentage of time is coordination vs. execution?
- **Incentive alignment audit**: Does the incentive structure reward team outcomes or individual credit?
- **Ownership audit**: Does every critical function have a single owner? Where is ownership shared (and therefore nobody's)?
- **Trust audit**: Where does distrust create redundant approval steps or duplicated work?

**Marketing / Acquisition lenses:**

- **Funnel audit**: Where is the highest drop-off? Is it pre-click, post-click, or post-trial?
- **Feedback loop audit**: How long from publishing content to knowing if it worked?
- **Unit economics audit**: Is LTGP:CAC above 3x? Which channels are profitable vs. burning cash?
- **Signal quality audit**: Are you optimizing for real outcomes or proxy metrics?
- **Channel health audit**: Which channels are saturated? Where is the next unit of spend still efficient?

**Knowledge / Cognitive lenses:**

- **Mental model currency audit**: Which models/beliefs are outdated given recent evidence?
- **Blind spot audit**: What categories of information are systematically absent from decisions?
- **Update mechanism audit**: When new information arrives, how does the decision framework update?
- **Decision quality audit**: How often are decisions revisited? What is the cost of late corrections?

---

### Formal Lens Selection

Commit to 3-5 lenses for this audit:

```
Lens 1: _______________
  Why selected: _______________
  What evidence it will surface: _______________

Lens 2: _______________
  Why selected: _______________
  What evidence it will surface: _______________

Lens 3: _______________
  Why selected: _______________
  What evidence it will surface: _______________

Lens 4 (optional): _______________
Lens 5 (optional): _______________

Lenses deliberately excluded:
  _______________  → reason: _______________
```

---

**Output:** Committed lens set. Advance to step-03 checkpoint, then apply each lens systematically.
