# 00-FOUNDATION
## Prerequisites — The Hard Gates Before Any Work Begins

---

## PURPOSE

This folder contains everything that must exist and be verified **before a single euro is spent or a single campaign is deployed**. The Foundation is not a formality — it is the precondition for the entire acquisition machine to function correctly.

Without the Foundation complete:
- Campaigns run blind (no conversion tracking)
- Optimization is impossible (no data)
- Legal exposure exists (no ORIAS on landing pages)
- The Google Ads API script cannot deploy (no credentials, no phone number)

No agent, no developer, and no operator should touch `02-slm-machine/` or `03-automation/` until every gate in this folder is ✅.

---

## FOLDER STRUCTURE

```
00-foundation/
├── credentials/        API keys, account IDs, OAuth tokens
├── tracking/           Conversion tracking setup and verification
└── legal/              ORIAS compliance, advertiser verification
```

---

## SUBFOLDERS

### `credentials/`
Stores all authentication and access documentation for the project's external services:
- Google Ads account ID and MCC link
- Google Ads API developer token and OAuth credentials
- GA4 property ID and measurement ID
- Customer ID used by `create_rolland_campaigns.py`

**Do not store raw secret files here in plaintext.** Document where credentials live and how to access them. Actual `.yaml` credential files belong in the system-level config referenced by the Google Ads API client library.

### `tracking/`
Step-by-step setup documentation for every tracking layer in the stack:
- **Call conversion tracking** — calls ≥60 seconds = 1 conversion (the only metric that matters)
- **Google Number Transfer** — Google forwarding number setup so calls are attributed to clicks
- **GA4 ↔ Google Ads link** — audience sharing and conversion import
- **Google Tag Manager** — site-level installation, container ID, trigger verification
- **Conversion testing** — how to verify that tracking fires correctly before going live

None of this is optional. If call tracking is broken, every optimization decision will be wrong.

### `legal/`
Documentation for legal and platform compliance requirements:
- **ORIAS number** — must appear visibly on both landing pages (`/landing/sante-senior` and `/landing/garantie-decennale`) — this is a French insurance brokerage legal requirement
- **Google financial services advertiser verification** — Google requires verification for insurance advertisers. Process takes 2–7 days. Apply immediately.
- **Google Business Profile** — not blocking, but strongly recommended for trust signals and local search presence

---

## ZONE A GATE CHECKLIST

| Gate | Item | Owner | Status |
|------|------|-------|--------|
| A3 | Google Ads account created | Rolland | ❌ |
| A4 | Financial services advertiser verification approved | Rolland | ❌ |
| A5 | Call conversion tracking (≥60s) activated | Technical | ❌ |
| A6 | Google Number Transfer enabled | Technical | ❌ |
| A7 | GA4 ↔ Google Ads linked | Technical | ❌ |
| A8 | Google Tag Manager installed on site | Technical | ❌ |
| A9 | Google Business Profile created + verified | Rolland | ❌ |
| A10 | ORIAS number on both landing pages | Rolland | ❌ |
| A11 | Real phone number in create_rolland_campaigns.py | Dev | ❌ |

Update statuses here as each gate clears. When all 9 are ✅, the machine is cleared for deployment.

**Last updated:** 2026-04-13
