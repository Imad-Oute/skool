# Step 1: Compliance Audit Initialization

## Context Loading

Load configuration from `{project-root}/.agents/microhard/config.yaml`:

- Client ID: `{client_id}`
- Target industry: `{target_industry}`
- Acquisition strategy: `{acquisition_strategy}`

## Initialize Output File

Create compliance audit report at: `{project-root}/output/reports/compliance-audit-report.md`

**Frontmatter:**

```yaml
---
stepsCompleted: []
clientId: { client_id }
auditDate: { current_date }
auditType: [full/content/ads/weekly]
complianceScore: null
---
```

## Audit Scope Definition

Ask the user to define the audit scope:

### 1. Audit Type

What are you auditing?

- **[f]** Full audit (all assets, all standards)
- **[c]** Content audit (content assets only)
- **[a]** Ad audit (ad assets only)
- **[w]** Weekly compliance check (quick scan)

### 2. Asset Scope

Which assets should be audited?

- All assets in project
- Assets created since [date]
- Specific asset category
- Assets in specific folder

### 3. Compliance Standards to Check

Which standards to validate? (can select multiple)

- [x] Naming conventions
- [x] Give:Ask ratio
- [x] Quality gates
- [ ] Performance thresholds (optional)
- [ ] Budget compliance (optional)

## Asset Discovery

Scan the project directories for assets to audit:

**Content Assets Location:** `{project-root}/output/content/`
**Ad Assets Location:** `{project-root}/ads/`
**Credentials Location:** `{project-root}/credentials/`

List all discovered assets:

```
Discovered Assets:
- Content: {count} files
- Ads: {count} files
- Credentials: {count} files
Total: {count} assets to audit
```

## Update Output File

```markdown
# Compliance Audit Report

**Client ID:** {client_id}
**Audit Date:** {current_date}
**Audit Type:** {type}
**Assets Audited:** {count}

## Audit Scope

- Content assets: {count}
- Ad assets: {count}
- Standards checked: [list]
```

Update frontmatter:

```yaml
stepsCompleted: ['step-01-init']
auditType: { type }
assetsToAudit: { count }
```

## Menu

- **[n]** Next step (Naming Validation)
- **[r]** Restart with different scope
- **[q]** Quit and save progress

**If user selects 'n':** Proceed to `step-02-naming-validation.md`
