# OUTPUT
## Agent Output Dump — Where Work Is Born Before It's Approved

---

## PURPOSE

This folder is where CAI agents produce their first-draft outputs. It is intentionally less structured than `02-slm-machine/` because creative and analytical work is non-linear — drafts are messy, iterations happen, ideas get discarded. That is correct behavior here.

**Nothing in this folder is live. Nothing here is final.**

`output/` is the workshop floor. `02-slm-machine/` is the shelf where finished products go.

---

## THE WORKFLOW

```
Agent produces draft → lands in output/ → reviewed by human or lead agent
        ↓
Approved → copied/moved to 02-slm-machine/ → deployed to campaigns or pages
Rejected → stays in output/ with a note, or discarded
```

This separation is deliberate. It means:
- `02-slm-machine/` is always clean and deployment-ready
- `output/` can contain 10 versions of the same headline — that's fine
- No draft ever accidentally goes live

---

## FOLDER STRUCTURE

```
output/
│
├── plans/          Strategic documents, ecosystem maps, blueprints, architecture docs
├── ads/            First-draft ad copy — headlines, descriptions, CTAs (pre-approval)
├── content/        First-draft organic content — posts, articles, scripts (pre-approval)
├── reports/        Performance reports, audits, financial analyses (raw from Trace + Felix)
└── knowledge/      Agent knowledge outputs — audits, syntheses, stress-tests, blueprints
    ├── audits/
    ├── cross-domain-syntheses/
    ├── first-principles-blueprints/
    └── stress-tests/
```

---

## SUBFOLDERS IN DETAIL

### `plans/`
Strategic and planning documents produced at the project level:
- Ecosystem maps (`RA-LeadGen-Ecosystem-Map-v2.md`)
- Architecture blueprints (`RA-Workspace-Architecture-Blueprint.md`)
- Strategic plans and initiative outlines
- This is where CEO, Analyst, and Thinker output their structural work

### `ads/`
First-draft ad copy from Aura (cai-hook-engineer) and Coda (cai-content-architect):
- Headline variants before selection
- Description copy drafts
- CTA iterations
- Hook brainstorm lists

After review and selection, approved ads move to `02-slm-machine/content/ads/`.

### `content/`
First-draft organic content (activates Month 2+):
- 5-Category Matrix content drafts
- LinkedIn post drafts
- YouTube script drafts
- Any content produced before it is approved for publication

After review, approved content moves to `02-slm-machine/content/organic/`.

### `reports/`
Raw performance reports and audits from agents:
- Weekly performance summaries from Trace before they become official directives
- Monthly financial analyses from Felix
- Three Tens audit drafts from CEO and Coda
- Competitor analysis reports from Analyst
- Any data-driven output that requires review before becoming an official record

After review, finalized reports move to `01-intelligence/SS2-performance/` (for directives and KPIs) or `02-slm-machine/` (for landing page audits).

### `knowledge/`
Specialized knowledge outputs from MGI agents — structural intelligence, not operational files:
- **`audits/`** — system audits from Architect (mgi-system-auditor) and Vera (cai-compliance-auditor)
- **`cross-domain-syntheses/`** — cross-domain insights from Brainstormer (mgi-cross-domain-synthesizer)
- **`first-principles-blueprints/`** — first-principles deconstructions from Thinker (mgi-first-principles-deconstructor)
- **`stress-tests/`** — adversarial stress-test results from Inversionist (mgi-adversarial-designer)

These outputs inform strategy but don't deploy directly. They feed into the persuasion core, avatar profiles, and strategic decisions.

---

## WHAT DOES NOT BELONG HERE

- Final approved ad copy (→ `02-slm-machine/content/ads/`)
- Final approved landing page copy (→ `02-slm-machine/funnels/`)
- Official weekly optimization directives (→ `01-intelligence/SS2-performance/directives/`)
- Official KPI logs (→ `01-intelligence/SS2-performance/kpi/`)
- Campaign structure documents (→ `02-slm-machine/traffic/`)
