# RESSOURCES
## Raw Source Material — The Library, Not the Workshop

---

## PURPOSE

This folder is the project's reference library. It contains raw source material — frameworks, PDFs, guides, and documentation — that agents and team members consult to inform their work. Nothing in this folder is produced by the project. Everything in it was brought in from the outside.

**This folder is read-only by convention.** Files here are not modified, not updated with project progress, and not moved to other folders. They are referenced as-is.

---

## WHAT BELONGS HERE

- Source frameworks and methodology documents (SLM, Hormozi, etc.)
- Client-provided PDFs and strategy reports
- External guides and platform documentation
- Any reference material that informs the work but is not produced by the work

## WHAT DOES NOT BELONG HERE

- Agent outputs (→ `output/`)
- Approved production assets (→ `02-slm-machine/`)
- Automation scripts (→ `03-automation/`) — `create_rolland_campaigns.py` has been moved
- Performance data (→ `01-intelligence/SS2-performance/`)

---

## FOLDER STRUCTURE

```
Ressources/
│
├── Straight-Line-Marketing/
│   └── SLM-Ecosystem-Map.md            The SLM framework map — governs all persuasion logic
│
├── CLICK-TO-CALL-GoogleAds-RollandAssurances.md
│                                        Google Ads click-to-call setup reference for RA
│
└── Rolland_Assurances_Strategy_Report.pdf
                                         Original strategy report — foundational context
```

---

## KEY FILES

### `Straight-Line-Marketing/SLM-Ecosystem-Map.md`
The Straight-Line Marketing framework that governs all persuasion logic in the acquisition machine. This is the operating system. The Three Tens, the Threshold System, the Straight-Line Structure — all come from here. Agents reference this when designing copy, auditing landing pages, or writing call scripts.

### `CLICK-TO-CALL-GoogleAds-RollandAssurances.md`
Reference guide for the Google Ads click-to-call setup specific to Rolland Assurances. Covers call extensions, call-only ads, forwarding numbers, and conversion tracking configuration.

### `Rolland_Assurances_Strategy_Report.pdf`
The original strategy document that defined the project scope, offer structure, and initial market analysis. The starting point from which the ecosystem map was built.

---

## ADDING NEW RESOURCES

When adding a new resource:
1. Place it directly in `Ressources/` or in a relevant subfolder if the volume warrants it
2. Add it to the file list above with a one-line description
3. Do not rename or modify the original file
