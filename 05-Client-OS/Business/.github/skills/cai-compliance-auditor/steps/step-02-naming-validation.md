# Step 2: Naming Convention Validation

## Previous Step Check

Verify `stepsCompleted` includes 'step-01-init'. If not, redirect to step-01.

## Load Asset List

Load the list of assets to audit from step-01.

## Naming Convention Standard

**CAI Naming Schema:**

```
Content Assets: [CLIENT_ID]_[DEPT]_[DATE]_[CATEGORY]_[VERSION].ext
Ad Assets:      [CLIENT_ID]_ADS_[DATE]_[FRAMEWORK]_[VERSION].ext
Credentials:    [CLIENT_ID]_CREDS_[PLATFORM]_[DATE].ext
```

**Component Rules:**

- **CLIENT_ID:** All caps, alphanumeric, no spaces
- **DEPT:** CONTENT, ADS, CREDS, AUDIT
- **DATE:** YYYYMMDD format
- **CATEGORY:** Content categories (EDUCATION, ENTERTAINMENT, etc.)
- **FRAMEWORK:** Ad framework (CALLOUT, VALUE, CTA)
- **VERSION:** v1, v2, v3, etc.
- **Extension:** .md, .mp4, .jpg, .pdf, etc.

## Validation Process

For each asset, validate naming compliance:

### Pattern Matching

Check if filename matches the expected pattern using regex:

```
^[A-Z0-9]+_(CONTENT|ADS|CREDS|AUDIT)_\d{8}_[A-Z]+_v\d+\.[a-z0-9]+$
```

### Component Validation

For each asset, validate individual components:

**Example Asset:** `CLIENT01_CONTENT_20240406_EDUCATION_v1.md`

- ✅ CLIENT_ID: CLIENT01 (valid)
- ✅ DEPT: CONTENT (valid)
- ✅ DATE: 20240406 (valid format)
- ✅ CATEGORY: EDUCATION (valid category)
- ✅ VERSION: v1 (valid format)
- ✅ **Result: COMPLIANT**

### Violation Detection

Common violations:

- ❌ Lowercase letters: `client01_content_...`
- ❌ Spaces in name: `CLIENT 01_CONTENT_...`
- ❌ Wrong date format: `CLIENT01_CONTENT_04-06-2024_...`
- ❌ Missing version: `CLIENT01_CONTENT_20240406_EDUCATION.md`
- ❌ Invalid category: `CLIENT01_CONTENT_20240406_RANDOM_v1.md`

## Naming Violations Report

Create a violations table:

| Asset                         | Issue           | Severity | Fix                              |
| ----------------------------- | --------------- | -------- | -------------------------------- |
| client01*content_20240406*... | Lowercase ID    | HIGH     | Rename: CLIENT01\_...            |
| CLIENT01_CONTENT_20240406.md  | Missing version | MEDIUM   | Add \_v1 before .md              |
| CLIENT01*RANDOM*...           | Invalid dept    | HIGH     | Should be CONTENT, ADS, or CREDS |

**Severity Levels:**

- **HIGH:** Breaks naming schema, must fix
- **MEDIUM:** Non-compliant but understandable
- **LOW:** Minor inconsistency

## Compliance Scoring

Calculate naming compliance score:

```
Naming Compliance Score = (Compliant Assets / Total Assets) × 100%

100%: Perfect compliance
90-99%: Good (minor issues)
70-89%: Needs improvement
<70%: Critical (major violations)
```

## Update Output File

Add naming validation section:

```markdown
## Naming Convention Validation

### Summary

- Total assets: {count}
- Compliant: {count} ({percentage}%)
- Violations: {count}

### Naming Compliance Score: {score}%

**Status:** [Perfect/Good/Needs Improvement/Critical]

### Violations

| Asset | Issue | Severity | Recommended Fix |
| ----- | ----- | -------- | --------------- |

[Table rows]

### Recommendations

1. Rename {count} assets with HIGH severity violations
2. Fix {count} assets with MEDIUM severity violations
3. Monitor LOW severity issues
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02-naming-validation']
namingComplianceScore: { score }
namingViolations: { count }
```

## Menu

- **[n]** Next step (Give:Ask Audit)
- **[b]** Back to initialization
- **[f]** Generate fix commands for violations
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-03-give-ask-audit.md`
