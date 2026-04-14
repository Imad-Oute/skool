# Step 3: Give:Ask Ratio Audit

## Previous Step Check

Verify `stepsCompleted` includes 'step-02-naming-validation'. If not, redirect to step-02.

## The 3.5:1 Give:Ask Law

**CAI Compliance Standard:**
For every 1 "Ask" (commercial, ad, direct CTA), you must have 3.5 "Give" (free value content).

**Rationale:**

- Builds trust and authority
- Prevents audience fatigue
- Maintains goodwill balance
- Enables sustainable monetization

**Violation Warning:**
If ratio drops below 3.5:1, growth slows and audience trust erodes.

## Asset Classification

Classify all assets as either "Give" or "Ask":

### "Give" Assets (Free Value)

Content that delivers value without asking for anything:

- Educational content (how-to, tutorials, insights)
- Entertainment (stories, case studies, behind-scenes)
- Tools/resources (templates, checklists, calculators)
- Social proof (testimonials, results, wins)

**Ask:** "Does this ask for money or lead information?"

- If NO → It's a "Give"

### "Ask" Assets (Commercial)

Content that requests action/money:

- Direct sales content (product pitches, offers)
- Lead magnets (gated content requiring email)
- Ads (all paid ads are "Asks")
- Webinar registrations (require signup)
- Promotional emails

**Ask:** "Does this ask for money or lead information?"

- If YES → It's an "Ask"

## Give:Ask Ratio Calculation

Count assets in each category:

**Example Count:**

- Give assets: 28 pieces
- Ask assets: 8 pieces

**Calculate Ratio:**

```
Give:Ask Ratio = Give Assets / Ask Assets
                = 28 / 8
                = 3.5:1

Status: ✅ COMPLIANT (exactly at minimum)
```

**Compliance Thresholds:**

- ≥ 3.5:1 → ✅ COMPLIANT
- 3.0-3.4:1 → ⚠️ WARNING (approaching violation)
- < 3.0:1 → ❌ VIOLATION (must fix)

## Time-Based Analysis

Calculate ratio over different time periods:

**Last 30 Days:**

- Give: 12 pieces
- Ask: 4 pieces
- Ratio: 3.0:1 ⚠️ WARNING

**Last 90 Days:**

- Give: 28 pieces
- Ask: 8 pieces
- Ratio: 3.5:1 ✅ COMPLIANT

**This identifies if recent activity is drifting from compliance.**

## Violation Remediation

If ratio is below 3.5:1:

**Immediate Actions:**

1. PAUSE all new "Ask" content until ratio improves
2. Create {count} more "Give" assets to reach 3.5:1
3. Review upcoming content calendar
4. Shift scheduled "Asks" to "Gives"

**Example:**

```
Current: 20 Give, 8 Ask = 2.5:1 ❌ VIOLATION
Need: 28 Give to reach 3.5:1
Action: Create 8 more free value pieces before next Ask
```

## Content Calendar Projection

Project future ratio based on content calendar:

**Scheduled Next 30 Days:**

- Give planned: 10 pieces
- Ask planned: 5 pieces
- Projected ratio: 2.0:1 ❌ PROJECTED VIOLATION

**Recommendation:** Reduce Ask to 2 pieces OR increase Give to 18 pieces

## Update Output File

Add Give:Ask audit section:

```markdown
## Give:Ask Ratio Audit

### Current Ratio: {ratio}:1

**Status:** [COMPLIANT/WARNING/VIOLATION]

### Asset Breakdown

- Give assets: {count}
- Ask assets: {count}
- Ratio: {ratio}:1

### Time-Based Analysis

- Last 30 days: {ratio}:1 ({status})
- Last 90 days: {ratio}:1 ({status})
- All time: {ratio}:1 ({status})

### Compliance Assessment

{compliance_message}

### Remediation Plan (if needed)

1. {action_1}
2. {action_2}
3. {action_3}

### Content Calendar Projection

- Planned Give: {count}
- Planned Ask: {count}
- Projected ratio: {ratio}:1 ({status})
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02-naming-validation', 'step-03-give-ask-audit']
giveAskRatio: { ratio }
giveAskStatus: [compliant/warning/violation]
```

## Menu

- **[n]** Next step (Quality Gates)
- **[b]** Back to naming validation
- **[c]** Adjust asset classification
- **[p]** View remediation plan
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-04-quality-gates.md`
