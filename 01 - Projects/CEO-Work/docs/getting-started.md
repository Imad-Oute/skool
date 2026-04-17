# Getting Started with MicroHard

## What Is MicroHard?

MicroHard is a modular meta-framework operated by AI agents inside your IDE. Each module
owns a specific domain of intelligence and is invoked by name in Claude Code, Gemini CLI,
or Copilot. Your installed modules are listed in `.agents/microhard/config.yaml`.

---

## How to Invoke Any Skill

In your AI IDE, say:

```
use cai-help
```

The help agent reads your installed module catalog and recommends the right skill for
where you currently are. Always start here when you're unsure.

Or invoke a skill directly by name:

```
use cai-hook-engineer
use mgi-knowledge-curator
```

---

## Module: CAI — Client Acquisition Intelligence

CAI runs a systematic lead generation machine across 4 phases. 6 AI agents each own one
part of the acquisition pipeline.

### Your CAI Team

| Agent        | Skill                       | Phase      | Role                          |
| ------------ | --------------------------- | ---------- | ----------------------------- |
| **Aura** ⚡  | `cai-hook-engineer`         | 1-Attract  | Engineers high-CTR hooks      |
| **Coda** 🏗️  | `cai-content-architect`     | 1-Attract  | Builds full content units     |
| **Felix** 📈 | `cai-growth-controller`     | 3-Scale    | LTGP:CAC scaling decisions    |
| **Vera** 🔍  | `cai-compliance-auditor`    | 4-Optimize | Blueprint compliance audits   |
| **Trace** 🔄 | `cai-feedback-loop-tracker` | 4-Optimize | 3-layer performance diagnosis |
| **CEO** 🎯   | `cai-ceo-architect`         | 4-Optimize | Ecosystem-level strategy      |

### CAI Phase Sequence

```
1-ATTRACT → 3-SCALE → 4-OPTIMIZE → (repeat)
```

**Phase 1 — Attract:** Build content that stops the scroll.

1. Run **Aura** — engineer hooks for every content piece
2. Run **Coda** — build the full content unit around the hook

**Phase 3 — Scale:** Put money behind what's mathematically justified. 3. Run **Felix** — analyze LTGP:CAC, approve scaling budget

**Phase 4 — Optimize:** Diagnose, enforce, set direction. 4. Run **Trace** — weekly performance review 5. Run **Vera** — monthly blueprint audit 6. Run **CEO** — quarterly strategic review

### CAI Output Directories

| Directory                     | What Goes Here             | Agent       |
| ----------------------------- | -------------------------- | ----------- |
| `output/content/hooks/`       | Hook variants + CTR scores | Aura        |
| `output/content/assets/`      | Completed content units    | Coda        |
| `output/ads/campaigns/`       | Ad creative and copy       | Aura + Coda |
| `output/reports/performance/` | Channel metrics            | Felix       |
| `output/reports/compliance/`  | Vera audit reports         | Vera        |
| `output/reports/feedback/`    | Trace diagnosis reports    | Trace       |
| `output/reports/growth/`      | Felix scaling decisions    | Felix       |

### CAI First 7 Days

| Day | Action                                     | Agent |
| --- | ------------------------------------------ | ----- |
| 1   | Define target audience and content pillars | CEO   |
| 2–3 | Engineer 10 hooks for first content batch  | Aura  |
| 4–5 | Build 5 content units from best hooks      | Coda  |
| 6   | Validate naming + structure compliance     | Vera  |
| 7   | Publish, log performance baseline          | Trace |

---

## Module: MGI — Meta-General Intelligence

MGI is a cognitive lab. It gives you structured protocols for hard thinking — distilling
knowledge into reusable mental models, stress-testing plans before you commit, and solving
problems that domain-local thinking can't crack.

### Your MGI Team

| Agent(s)                                               | Skill                                | Phase          | When to Use                                                    |
| ------------------------------------------------------ | ------------------------------------ | -------------- | -------------------------------------------------------------- |
| **Curator** 📚                                         | `mgi-knowledge-curator`              | 1-Distillation | You have raw material to internalize                           |
| **Analyst** 📊                                         | `mgi-theory-practitioner`            | 1-Distillation | Apply a known model to a real challenge                        |
| **Inversionist** 🔄 + **Critic** 🎯 + **Architect** 🏛️ | `mgi-adversarial-designer`           | 2-Stress-Test  | Before committing to a high-stakes plan                        |
| **Thinker** 🧠 + **Engineer** ⚙️                       | `mgi-first-principles-deconstructor` | 2-Stress-Test  | When every solution is a variation of the same broken approach |
| **Brainstormer** 💡 + **Analyst** 📊                   | `mgi-cross-domain-synthesizer`       | 3-Synthesis    | Domain-local thinking is exhausted                             |
| **Architect** 🏛️ + **Problem Solver** 🔧               | `mgi-system-auditor`                 | 3-Synthesis    | A working system is slowing down or no one understands it      |

### MGI Phase Sequence

```
1-DISTILLATION → 2-STRESS-TEST → 3-SYNTHESIS
(phases are independent — use what the problem requires)
```

**Phase 1 — Distillation:** Build your cognitive library.

- Run **Curator** (`mgi-knowledge-curator`) — ingest any framework, book, or article into a structured mental model
- Run **Analyst** (`mgi-theory-practitioner`) — apply a library model to a real challenge

**Phase 2 — Stress-Test:** Pressure-test before you commit.

- Run **Inversionist + Critic + Architect** (`mgi-adversarial-designer`) — bulletproof any plan
- Run **Thinker + Engineer** (`mgi-first-principles-deconstructor`) — strip a stuck problem to axioms and rebuild

**Phase 3 — Synthesis:** Generate non-obvious solutions.

- Run **Brainstormer + Analyst** (`mgi-cross-domain-synthesizer`) — import logic from a different domain
- Run **Architect + Problem Solver** (`mgi-system-auditor`) — audit any system for entropy

### MGI Knowledge Library

Your mental model library lives at:

```
.agents/microhard/mgi-skills/_library/
  mental-models/    ← 99 pre-loaded models + anything you add
  distillates/      ← curated artifacts from mgi-knowledge-curator
```

### MGI Output Directories

| Directory                         | What Goes Here                  | Skill                              |
| --------------------------------- | ------------------------------- | ---------------------------------- |
| `output/knowledge/mental-models/` | Curated mental model artifacts  | mgi-knowledge-curator              |
| `output/knowledge/protocols/`     | Applied theory reports          | mgi-theory-practitioner            |
| `output/knowledge/stress-tests/`  | Adversarial design outputs      | mgi-adversarial-designer           |
| `output/knowledge/blueprints/`    | First-principles blueprints     | mgi-first-principles-deconstructor |
| `output/knowledge/synthesis/`     | Cross-domain synthesis reports  | mgi-cross-domain-synthesizer       |
| `output/knowledge/audits/`        | System audit directives         | mgi-system-auditor                 |
| `logs/`                           | Audit trails for all MGI skills | All MGI agents                     |

---

## Naming Schema (Non-Negotiable for CAI)

All CAI output files must follow:

```
[CLIENT_ID]_[DEPT]_[YYYYMMDD]_[CATEGORY]_[VERSION]
```

Examples:

- `ABC_CONTENT_20260407_HOOK_v01.md`
- `ABC_ADS_20260407_CAMPAIGN_v01.md`
- `ABC_AUDIT_20260407_COMPLIANCE_v01.md`

Vera (`cai-compliance-auditor`) enforces this on every audit.

---

## Tracking Your Progress

```bash
microhard status                    # see all skill states at a glance
microhard run <skill>               # show current step
microhard run <skill> --next        # mark step done, advance
microhard run <skill> --skip        # skip current step
microhard reset <skill>             # restart from step 1
```

State persists across sessions — close your IDE, come back tomorrow, and
`microhard run <skill>` picks up exactly where you left off.
