# 03-AUTOMATION
## The Deployment Interface — Google Ads API

---

## PURPOSE

The automation system is the layer between the SLM machine and the live Google Ads account. It does not define strategy — the SLM machine does that. It executes strategy at speed, removes manual UI work, and eventually closes the feedback loop automatically.

Think of it as the CLI for the acquisition machine. `02-slm-machine/` is where you design the engine. `03-automation/` is where you turn the ignition.

**Position in the ecosystem:** A tool inside Layer 2A (Traffic System). It accelerates deployment and reporting. It does not replace strategic thinking — it executes strategic decisions that have already been made.

---

## THE 3-VERSION ROADMAP

The automation system evolves in three stages, each unlocked when the previous is stable:

```
v1 — DEPLOYMENT (Now)
     Create campaigns, ad groups, keywords, and ads in one command.
     Status: Script built. Waiting on Zone A gate A11 (phone number).

v2 — REPORTING (Month 1)
     Pull performance data back from the account automatically.
     Generate weekly reports. Fire alarms when KPIs cross thresholds.
     Status: Not started.

v3 — OPTIMIZATION (Month 3+)
     Auto-adjust bids. Auto-add negative keywords. Manage A/B rotations.
     Unlocked only after Gate 4 (LTGP:CAC > 3x) is confirmed.
     Status: Planned.
```

---

## FOLDER STRUCTURE

```
03-automation/
│
├── v1-deployment/          Campaign creation — deploys the full account structure
├── v2-reporting/           Performance data pull — weekly reports + alarm detection
└── v3-advanced/            Auto-optimization rules — bid adjustment, negatives, A/B (future)
```

---

## SUBFOLDERS IN DETAIL

### `v1-deployment/`
**Status: Ready — blocked only on Gate A11 (real phone number)**

Contains `create_rolland_campaigns.py` — the script that creates the complete Rolland Assurances campaign structure in Google Ads via the API in a single command:
- 2 campaigns (Senior + Décennale)
- 7 ad groups (S1, S2, S3, D1, D2, D3, D4)
- All keywords with match types
- All call-only ads with headlines and descriptions
- Campaign settings (schedule, device bids, bid strategy, budget)

Also contains:
- `campaign-config.yaml` — all campaign parameters (phone number, budgets, bids, ad schedule)
- `deployment-log.md` — record of every deployment: date, what changed, result
- `README.md` — how to run, prerequisites, troubleshooting

**To deploy:** All Zone A gates must be ✅ (see `00-foundation/README.md`). Then:
```bash
python 03-automation/v1-deployment/create_rolland_campaigns.py
```

### `v2-reporting/`
**Status: Planned — Month 1 priority**

Will contain the performance reporting module:
- `performance-report.py` — pulls CPL, CTR, call volume, CPC from Google Ads API weekly
- `alarm-detection.py` — automatically flags when KPIs cross alarm thresholds:
  - CTR < 3% → Hook failure signal → notify Trace
  - CPL > target × 1.5 → Systemic problem signal → notify Felix + CEO
  - Zero impressions → Config error → immediate alert
  - Calls < 60s > 60% → Wrong audience or wrong number → notify Trace
- `report-config.yaml` — configurable thresholds, alert targets, report schedule

Output from this module feeds directly into `01-intelligence/SS2-performance/kpi/` and `directives/`.

### `v3-advanced/`
**Status: Future — Month 3+ — requires Gate 4 (LTGP:CAC > 3x)**

Will contain auto-optimization logic:
- `auto-bid-rules.py` — adjusts bids based on performance rules defined by Felix
- `negative-keyword-expander.py` — reads search term reports and adds negatives automatically, feeding `01-intelligence/SS1-market/keywords/negative-keywords-master.md`
- `ab-test-manager.py` — manages ad rotation and surfaces winning variants

**Felix and CEO define the rules. Dev implements them. Nothing in v3 runs without explicit gate approval.**

---

## GATE DEPENDENCIES

This folder's activation is sequenced:

| Version | Activation Gate | Condition |
|---------|----------------|-----------|
| v1 | Zone A complete | All 9 foundation gates ✅ |
| v2 | Campaigns live for 2+ weeks | Enough data to report on |
| v3 | LTGP:CAC > 3x confirmed | Felix's Gate 4 cleared |

---

## RELATIONSHIP TO OTHER FOLDERS

- Receives strategy from: `02-slm-machine/traffic/` (campaign structure decisions)
- Deploys to: Live Google Ads account
- Sends data back to: `01-intelligence/SS2-performance/` (performance reports, alarm triggers)
- Reference library: `google-ads-api-developer-assistant/` (API documentation, examples, client libs — do not modify)
