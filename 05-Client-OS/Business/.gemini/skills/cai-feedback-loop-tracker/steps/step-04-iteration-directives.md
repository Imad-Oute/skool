# Step 4: Iteration Directives

**Objective:** Convert the diagnosis into specific, actionable instructions for the next production cycle.

## Instructions

### 1. Previous Step Check

Verify `stepsCompleted` includes `3`. If not, redirect to step-03.

### 2. Load Diagnosis Context

Review from step-03:

- Primary failure layer: {layer}
- Top performer patterns: {patterns}
- Specific failure root causes per asset

### 3. Generate Layer-Specific Directives

Based on the primary failure layer, generate targeted directives:

---

**IF PRIMARY FAILURE LAYER = HOOK:**

```
DIRECTIVE TYPE: Hook Overhaul

Problem: Content/ads are not stopping the scroll or getting the click.
Root Cause(s): {from diagnosis}

Directives for Next Cycle:

1. HEADLINE TESTING
   - Write 5 alternative headlines for each underperforming piece
   - Test using the 7-Component News Matrix (Invoke cai-hook-engineer)
   - Required components: [Callout] + [Big Claim] + [Time Frame or Number]
   - A/B test: Run original vs. new hook for 7 days

2. PATTERN INTERRUPT
   - Current hooks look like: {describe the pattern}
   - New hook style to test: [Question / Bold Claim / Controversy / Story Open]
   - Visual change required: [Yes/No] — {reason}

3. TIMING & DISTRIBUTION
   - Current posting time: {time}
   - Recommended test window: {new time} (when audience is most active)
   - Distribution boost: Try paid amplification of best organic hooks

4. KILL LIST (Retire these hook styles)
   - {hook style 1} — because {reason from data}
   - {hook style 2} — because {reason from data}

5. REPLICATE (Double down on these hook styles)
   - {hook style from top performer} — because {data-backed reason}
```

---

**IF PRIMARY FAILURE LAYER = RETENTION:**

```
DIRECTIVE TYPE: Retention Architecture Rebuild

Problem: People are clicking/starting but not finishing or engaging deeply.
Root Cause(s): {from diagnosis}

Directives for Next Cycle:

1. STRUCTURE OVERHAUL
   - Current structure failing because: {reason}
   - New structure to test: [List / Story Arc / Revelation Sequence / How-To Steps]
   - Rule: Every paragraph must earn the next paragraph.
   - Value-per-second audit: Remove any section that doesn't add density.

2. RETENTION MECHANICS
   - Add open loops: End each section with a question or partial answer
   - Use pattern breaks: Bold statements, short paragraphs, white space
   - Add specificity: Replace vague claims with precise numbers and examples

3. PROMISE ALIGNMENT
   - Hook promise: {what the hook promised}
   - Content delivery: {what was actually delivered}
   - Gap: {where the promise broke down}
   - Fix: Rewrite to ensure delivery matches the hook's implied contract

4. LENGTH CALIBRATION
   - Current avg. length: {words/minutes}
   - Audience consumption pattern suggests: {shorter/longer}
   - Target length for next cycle: {length}

5. REPLICATE (From top performer)
   - Retention mechanic used: {mechanic}
   - Replicate this structure in next {count} pieces
```

---

**IF PRIMARY FAILURE LAYER = REWARD:**

```
DIRECTIVE TYPE: Conversion & Offer Optimization

Problem: Content is being consumed but not converting to action.
Root Cause(s): {from diagnosis}

Directives for Next Cycle:

1. CTA OVERHAUL
   - Current CTA: "{current CTA text}"
   - Why it's underperforming: {reason}
   - New CTA variants to test:
     a. "{variant 1}" — [Softer ask]
     b. "{variant 2}" — [Higher value offer]
     c. "{variant 3}" — [Social proof-based]

2. GIVE:ASK RATIO AUDIT
   - Current ratio: {ratio}:1
   - If below 3.5:1: PAUSE all asks until ratio restored
   - Immediate action: Publish {count} pure Give pieces before next Ask

3. OFFER REFINEMENT
   - Current offer: {offer}
   - Why audience isn't converting: {reason from data}
   - Offer adjustment: [Lower friction / Higher value / Better timing / Different format]

4. LANDING PAGE / FOLLOW-UP FIX (if applicable)
   - Current landing page conversion rate: {%}
   - Issue identified: {issue}
   - Fix: {specific change to make}

5. AUDIENCE TEMPERATURE CHECK
   - Traffic is: [Too cold / Right temperature / Too warm for the ask]
   - If too cold: Add {count} awareness/education pieces before conversion content
```

---

**IF NO PRIMARY FAILURE LAYER (All Green):**

```
DIRECTIVE TYPE: Scale & Systematize

Situation: Performance is strong across all three layers.

Directives for Next Cycle:

1. SCALE VOLUME
   - Current output: {count} pieces/period
   - Recommended output: {count × 1.5}/period
   - Maintain same quality standards — do not dilute for volume

2. DOCUMENT THE PLAYBOOK
   - Extract the winning hook format as a template
   - Extract the winning retention structure as a template
   - Extract the winning CTA as a template
   - File templates at: {project-root}/output/content/templates/

3. CHANNEL EXPANSION
   - Current channels: {list}
   - Recommended next channel to test: {channel}
   - Repurpose top-performing content to new format

4. RAISE THE BAR
   - New benchmark targets for next cycle:
     - Engagement rate: {current + 20%}%
     - CPL: ${current × 0.8}
     - LTGP:CAC: {current + 0.5}:1
```

### 4. Prioritized Action Plan

Synthesize all directives into a prioritized list:

```
ITERATION DIRECTIVES: Priority Order

🔴 IMMEDIATE (This Week):
1. {action} — because {data-backed reason}
2. {action} — because {data-backed reason}

🟡 SHORT-TERM (Next 30 Days):
1. {action} — {expected impact}
2. {action} — {expected impact}
3. {action} — {expected impact}

🟢 OPTIMIZE (Ongoing):
1. {system or habit to establish}
2. {metric to monitor weekly}
```

### 5. Kill / Keep / Scale Matrix

For each asset reviewed, assign a verdict:

| Asset  | Status | Verdict | Reason                      | Action                        |
| ------ | ------ | ------- | --------------------------- | ----------------------------- |
| {name} | {tier} | KILL    | Below avg across all layers | Archive, do not repeat format |
| {name} | {tier} | KEEP    | Average performance         | Optimize hook, retest         |
| {name} | {tier} | SCALE   | Top performer               | Repurpose to 3+ formats       |

### 6. Update Output File

Add iteration directives section:

```markdown
## Iteration Directives

### Primary Directive: {Layer} Overhaul / Scale

**Diagnosis:** {summary}

### Immediate Actions (This Week)

1. {action_1}
2. {action_2}

### 30-Day Actions

1. {action_1}
2. {action_2}
3. {action_3}

### Kill / Keep / Scale Matrix

| Asset  | Verdict | Action   |
| ------ | ------- | -------- |
| {name} | KILL    | {action} |
| {name} | KEEP    | {action} |
| {name} | SCALE   | {action} |

### Metrics to Track in Next Cycle

| Metric   | Current | Target   | Improvement |
| -------- | ------- | -------- | ----------- |
| {metric} | {value} | {target} | {%}         |
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3, 4]
primaryDirective: { directive_type }
immediateActions: { count }
killCount: { count }
keepCount: { count }
scaleCount: { count }
```

### 7. Present Menu

```
✓ Step 4 Complete: Iteration directives generated
  Immediate actions: {count}
  Kill: {count} assets
  Keep: {count} assets
  Scale: {count} assets

[C] Continue to Finalize Report
[A] Add/edit any directive
[X] Exit workflow
```

Wait for user selection.

### 8. Handle Selection

- **If [C]**: Update frontmatter, load `./step-05-finalize.md`
- **If [A]**: Allow additions/edits to directives, update report, show menu again
- **If [X]**: Exit with "Workflow paused. Run this skill again to resume."

---

**END OF STEP 4**
