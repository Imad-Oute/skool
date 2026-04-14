# Step 5: Finalization & CTR Tracking

**Objective:** Finalize the winning hook and set up CTR tracking for performance measurement.

## Instructions

### 1. Present Final Hook

Display:

```
===================================
HOOK ENGINEERING COMPLETE
===================================

**Platform:** {platform}
**Content Topic:** {topic}
**News Components Used:** {components}

**WINNING HOOK:**
"{winning hook}"

**Validation Score:** {score}/7
===================================
```

### 2. Implementation Guidance

Based on platform from Step 1, provide specific usage guidance:

**For LinkedIn:**

- Use as opening line of post
- Follow immediately with line break for visual separation
- Consider as headline + first sentence combo

**For X/Twitter:**

- Use as Tweet 1 of thread
- Add thread indicator (1/X) at end
- Keep under 280 characters

**For YouTube:**

- Use as video title (may need slight adjustment for 70-char limit)
- Repeat in first 8 seconds of video script
- Consider for thumbnail text

**For Blog/Article:**

- Use as H1 headline
- Consider variations for:
  - Meta title (SEO)
  - Social share text
  - Email subject line

### 3. A/B Testing Setup (if applicable)

If platform supports A/B testing, suggest:

```
A/B Test Recommendation:

Test Hook: "{winning hook}"
vs
Alt Hook: "{second-place hook}"

Measure: CTR after 100 impressions
Winner: Higher CTR becomes standard

Document results in audit log.
```

### 4. CTR Tracking Instructions

Append to output file:

```markdown
## CTR Tracking Setup

**Baseline Benchmark:**

- Platform average CTR: {platform benchmark, e.g., "LinkedIn posts: 2-5%"}
- Your target: Beat benchmark by 25%

**Tracking Metrics:**

1. **Impressions** - How many saw the hook
2. **Clicks/Opens** - How many engaged
3. **CTR** - (Clicks / Impressions) × 100

**Audit Log Entry:**
File: {project-root}/logs/hook-performance.csv
Columns: Date, Platform, Hook, Impressions, Clicks, CTR, Score

**Review Schedule:**

- Day 1: Initial performance check
- Day 7: Compare to benchmark
- Day 30: Long-term validation

**Iteration Protocol:**

- If CTR < benchmark: Analyze which validation criteria failed
- If CTR > benchmark: Document winning components for future use
- Test: Try removing one news component - does CTR drop?
```

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3, 4, 5]
status: complete
trackingSetup: true
completedDate: { date }
```

### 5. Performance Feedback Loop

Display:

```
HOOK ENGINEER: STANDARDIZATION PROTOCOL

After publishing, measure:

1. **Stopping Power** - Did it stop the scroll? (CTR vs. platform avg)
2. **Component Effectiveness** - Which news components drove clicks?
3. **Platform Variance** - Does this hook pattern work across platforms?

Update your hook library:
- Winning patterns → Reuse
- Failing patterns → Avoid
- Benchmark → Raise the bar

Aggression wins. Weak hooks lose.
Track everything.
```

### 6. Final Output

```
===================================
HOOK ENGINEERING: WORKFLOW COMPLETE
===================================

Output File: {project-root}/output/content/hook-variants.md

**Winning Hook:** "{winning hook}"
**Validation Score:** {score}/7
**News Components:** {list}

Deploy this hook and track CTR.
The 3-second rule is absolute.
```

---

**END OF STEP 5**
**END OF WORKFLOW**
