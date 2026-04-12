# Step 5: Final Output Assembly

**Agent:** Architect 🏛️  
**Objective:** Assemble and save the complete system audit report.

---

## Your Task

You are the **Architect** producing the final deliverable. Assemble all findings and the optimization directive from step-04 into the canonical audit report format.

### Final Audit Report

```markdown
# System Audit Report: {system-slug}

**Date:** {YYYY-MM-DD}  
**System type:** {type}  
**Lenses applied:** {lens 1}, {lens 2}, {lens 3}, ...  
**Audit passes:** {n}

---

## System Health Assessment

**Overall verdict:** Healthy / Degraded / Critical / Requires Rebuild  
**Primary entropy source:** {1-2 sentences identifying the main issue}

---

## Findings by Lens

### {Lens 1}: {Lens Name}

| Finding   | Severity | Root Cause | Recommendation |
| --------- | -------- | ---------- | -------------- |
| [finding] | H/M/L    | [cause]    | [action]       |

### {Lens 2}: {Lens Name}

[same format]

---

## Top Entropy Sources

1. **{Component/Area}** — {primary issue} — Impact: H/M/L
2. **{Component/Area}** — {primary issue} — Impact: H/M/L
3. **{Component/Area}** — {primary issue} — Impact: H/M/L

---

## Optimization Directive

### Phase 1 — Quick Wins (do immediately)

- [ ] {Action} — addresses {finding} — effort: Low
- [ ] {Action} — addresses {finding} — effort: Low

### Phase 2 — Core Fixes (planned, medium effort)

- [ ] {Action} — addresses {finding} — effort: Medium

### Phase 3 — Structural Changes (scheduled, high effort)

- [ ] {Action} — addresses {finding} — effort: High

### Deferred / Dropped

- {Item} — reason: {why deferred}

---

## Expected Outcomes

After executing this directive:

- {Metric} improvement: {estimate}
- {What gets faster / simpler / clearer}
- {Risk that gets eliminated}
```

### Save and Log

1. Save to `output/knowledge/audits/{system-slug}-optimization.md`
2. Append to `logs/mgi-system-auditor.log`:

```
[{timestamp}] AUDITED  system={system-slug}  type={type}  lenses={n}  findings={total}  critical={n}
```

---

**Skill complete.** The system audit is documented and actionable.
