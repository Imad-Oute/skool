# Step 4: Quality Gates & Red Flags

## Previous Step Check

Verify `stepsCompleted` includes 'step-03-give-ask-audit'. If not, redirect to step-03.

## Quality Gate Framework

CAI maintains quality through systematic checks across 5 gate categories:

### Gate 1: Content Quality

**For content assets, check:**

- [ ] Headline uses 7-Component News Matrix (if applicable)
- [ ] Retention mechanism present (Lists/Steps/Stories)
- [ ] Hook delivers on promise (no clickbait)
- [ ] Value is clear and actionable
- [ ] Length appropriate for category (Education 800-2000 words, etc.)
- [ ] Grammar and spelling checked

**Scoring:** Pass if ≥4/6 checks pass

### Gate 2: Ad Quality

**For ad assets, check:**

- [ ] 3-Chunk System used (Callout + Value + CTA)
- [ ] Targeting defined (Needle vs Haystack)
- [ ] Landing page continuity (message match)
- [ ] Compliant with platform policies
- [ ] Call-to-action is clear
- [ ] Visual quality acceptable

**Scoring:** Pass if ≥5/6 checks pass

### Gate 3: Asset Organization

**For all assets, check:**

- [ ] Filed in correct directory (content/, ads/, etc.)
- [ ] Naming convention followed (from step-02)
- [ ] Version control maintained
- [ ] Associated files linked (creative + copy + landing page)
- [ ] Metadata complete (category, framework, etc.)

**Scoring:** Pass if ≥4/5 checks pass

### Gate 4: Performance Standards

**For published assets, check:**

- [ ] Tracking codes present (UTM parameters)
- [ ] Metrics being collected
- [ ] Performance within expected range
- [ ] No critical issues reported (broken links, 404s)

**Scoring:** Pass if ≥3/4 checks pass

### Gate 5: Blueprint Adherence

**Strategic alignment check:**

- [ ] Aligns with CAI 4 Ecosystems strategy
- [ ] Supports current strategic priorities
- [ ] Target audience match
- [ ] Consistent with brand voice
- [ ] No strategic drift

**Scoring:** Pass if ≥4/5 checks pass

## Red Flag Detection

Critical issues that require immediate attention:

### Critical Red Flags (Must Fix)

- ❌ Violates platform advertising policies
- ❌ Broken links or 404 errors
- ❌ Misleading claims or clickbait
- ❌ No tracking/attribution
- ❌ Give:Ask ratio < 2.5:1 (critical violation)
- ❌ LTGP:CAC ratio < 2:1 (unprofitable)

### Warning Red Flags (Monitor)

- ⚠️ Performance below 50% of benchmark
- ⚠️ Naming violations (HIGH severity)
- ⚠️ Missing version control
- ⚠️ Incomplete asset metadata
- ⚠️ Give:Ask ratio 2.5-3.4:1 (approaching violation)

### Info Red Flags (Improvement Opportunities)

- ℹ️ Could improve headline clarity
- ℹ️ Could strengthen CTA
- ℹ️ Could optimize for SEO
- ℹ️ Could add visual elements

## Quality Audit Execution

For each asset in scope:

1. Run through relevant quality gates
2. Score each gate (pass/fail)
3. Detect any red flags
4. Document findings

**Example Asset Audit:**

```
Asset: CLIENT01_CONTENT_20240406_EDUCATION_v1.md

Gate 1 (Content): ✅ PASS (5/6)
  ✅ Headline clear
  ✅ Retention mechanism (List)
  ✅ Hook delivers
  ✅ Actionable value
  ✅ Appropriate length
  ❌ Minor grammar issues

Gate 3 (Organization): ✅ PASS (5/5)
  ✅ Correct directory
  ✅ Naming compliant
  ✅ Versioned
  ✅ Associated files linked
  ✅ Metadata complete

Gate 5 (Blueprint): ✅ PASS (4/5)
  ✅ Aligns with Ecosystem 1
  ✅ Supports priorities
  ✅ Target audience match
  ❌ Brand voice inconsistency
  ✅ No strategic drift

Red Flags: None

Overall: ✅ COMPLIANT
```

## Quality Scoring

Calculate overall quality score:

```
Quality Score = (Passed Gates / Total Gates) × 100%

Gates Applied: [Gate numbers based on asset type]
Gates Passed: {count}
Quality Score: {percentage}%

90-100%: Excellent
70-89%: Good
50-69%: Needs Improvement
<50%: Critical Issues
```

## Update Output File

Add quality gates section:

```markdown
## Quality Gates & Red Flags

### Summary

- Assets audited: {count}
- Quality score: {percentage}%
- Red flags (Critical): {count}
- Red flags (Warning): {count}
- Red flags (Info): {count}

### Quality Gate Results

| Gate                  | Pass Rate     | Status   |
| --------------------- | ------------- | -------- |
| Content Quality       | {percentage}% | {status} |
| Ad Quality            | {percentage}% | {status} |
| Asset Organization    | {percentage}% | {status} |
| Performance Standards | {percentage}% | {status} |
| Blueprint Adherence   | {percentage}% | {status} |

### Critical Red Flags

{list or "None detected"}

### Warning Red Flags

{list or "None detected"}

### Failed Quality Checks

| Asset | Gate | Issue | Priority |
| ----- | ---- | ----- | -------- |

[Table of failures]

### Recommendations

1. {recommendation_1}
2. {recommendation_2}
3. {recommendation_3}
```

Update frontmatter:

```yaml
stepsCompleted:
  ['step-01-init', 'step-02-naming-validation', 'step-03-give-ask-audit', 'step-04-quality-gates']
qualityScore: { percentage }
criticalRedFlags: { count }
warningRedFlags: { count }
```

## Menu

- **[n]** Next step (Finalize Report)
- **[b]** Back to Give:Ask audit
- **[d]** View detailed red flags
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-05-finalize.md`
