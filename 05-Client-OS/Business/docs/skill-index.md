# CAI Skill Index

A human-readable catalog of all installed skills. For the machine-readable version, see `.agents/microhard/_config/microhard-help.csv`.

---

## Domain Skills (cai-skills)

### Phase 1 — Attract

---

#### cai-hook-engineer · Aura ⚡

**Menu Code:** HE  
**Role:** Noise-Piercing Hook Specialist  
**When to use:** Before creating any content asset. Always run first.

Engineers high-CTR headlines and hooks using the 7-Component News Matrix. Aura combines psychological triggers with news-cycle relevance to produce hooks that stop the scroll. She generates 5-10 variants per session, scored by emotional intensity and timeliness.

**Inputs:** Content topic, target audience, current news angle  
**Outputs:** Ranked hook variants with CTR rationale → `output/content/hooks/`  
**Validation metric:** CTR vs. benchmark

---

#### cai-content-architect · Coda 🏗️

**Menu Code:** CA  
**Role:** Value Assembly-Line Manager  
**When to use:** After Aura delivers hooks. Use to build the full content unit.

Architects high-value content units using the 5-Category Topic Matrix (Educate, Inspire, Relate, Entertain, Convert) and Retention Mechanics. Every content piece is engineered for a specific funnel stage and measured against AVD and completion rate.

**Inputs:** Selected hook, target funnel stage, content category  
**Outputs:** Complete content unit with retention structure → `output/content/assets/`  
**Validation metric:** AVD (Average View Duration), completion rate

---

### Phase 3 — Scale

---

#### cai-growth-controller · Felix 📈

**Menu Code:** GC  
**Role:** Financial Growth Specialist  
**When to use:** When CAC data is 30+ days old, or before any budget decision.

Analyzes LTGP:CAC ratios and produces a 90-day scaling roadmap using the Track → Invest → Print framework. Felix will not approve scaling below a 3x LTGP:CAC ratio. He models three budget tiers and sets hard stop guardrails before any spend increase.

**Inputs:** Channel spend, conversion data, deal value, LTV  
**Outputs:** Unit economics report, scaling verdict, 90-day plan → `output/reports/growth/`  
**Validation metric:** LTGP:CAC ratio (must exceed 3x to scale)

---

### Phase 4 — Optimize

---

#### cai-feedback-loop-tracker · Trace 🔄

**Menu Code:** FT  
**Role:** Diagnostic Engine  
**When to use:** Weekly review cycle, or when any asset underperforms its benchmark.

Runs 3-layer performance diagnosis (Hook, Body, CTA) across content and ad assets. Produces a Kill/Keep/Scale matrix with specific iteration directives. Trace's key metric is MTTI (Mean Time To Insight) — she compresses the feedback loop relentlessly.

**Inputs:** Performance data for review period (CTR, AVD, CVR, CPL)  
**Outputs:** Asset diagnosis, Kill/Keep/Scale matrix → `output/reports/feedback/`  
**Validation metric:** MTTI, iteration velocity, recovery rate

---

#### cai-compliance-auditor · Vera 🔍

**Menu Code:** AU  
**Role:** Blueprint Gatekeeper  
**When to use:** Before any scaling decision, or monthly ecosystem health check.

Audits naming schema adherence, Give:Ask ratio balance, and structural compliance across all output directories. Issues structured findings (ID, severity, finding, required action). Zero tolerance for blueprint drift.

**Inputs:** Output directory contents  
**Outputs:** Compliance audit report → `output/reports/compliance/`  
**Validation metric:** Audit pass rate, non-compliant asset count

---

#### cai-ceo-architect · CEO 🎯

**Menu Code:** CEO  
**Role:** Visionary Ecosystem Orchestrator  
**When to use:** Quarterly, or when pivoting acquisition strategy.

Strategic oversight of the entire acquisition machine. Validates business model assumptions, sets cross-agent priorities, and coordinates direction across all five agents. CEO operates above the skills — he ensures the system compounds rather than optimizes in isolation.

**Inputs:** Ecosystem health snapshot (outputs from Felix, Vera, Trace)  
**Outputs:** Strategic directive, agent coordination plan  
**Validation metric:** Pipeline contribution, ecosystem compounding rate

---

## Core Skills (core-skills)

These skills support all domain skills and are available at any time.

| Skill                            | When to use                                                 |
| -------------------------------- | ----------------------------------------------------------- |
| `cai-help`                       | "What should I do next?" — navigates you to the right skill |
| `cai-init`                       | First-time project setup or loading config variables        |
| `cai-brainstorming`              | Structured ideation sessions before content production      |
| `cai-distillator`                | Compress large documents into LLM-optimized distillates     |
| `cai-advanced-elicitation`       | Push outputs deeper — Socratic, pre-mortem, red team        |
| `cai-editorial-review-prose`     | Copy-editing for communication quality                      |
| `cai-editorial-review-structure` | Structural editing — cuts, reorganization, simplification   |
| `cai-review-adversarial-general` | Cynical/critical review of any output                       |
| `cai-review-edge-case-hunter`    | Exhaustive edge-case analysis                               |
| `cai-party-mode`                 | Multi-agent group discussion between all CAI agents         |
| `cai-shard-doc`                  | Split large markdown documents into organized files         |
| `cai-index-docs`                 | Generate or update an index of all files in a folder        |
