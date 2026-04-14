# 03-AUTOMATION — v1 Campaign Deployment

## Status: READY — Waiting on Zone A gates (A11: phone number)

## Files
- `create_rolland_campaigns.py` — creates all campaigns, ad groups, keywords, and ads via Google Ads API CLI

## Prerequisites before running
1. All Zone A gates complete (see `00-foundation/README.md`)
2. `google-ads.yaml` credentials file configured
3. Real phone number added to script (Gate A11)
4. Customer ID confirmed

## How to run
```bash
cd 03-automation/v1-deployment
python create_rolland_campaigns.py
```

## Deployment log
| Date | Run by | Changes | Result |
|------|--------|---------|--------|
| — | — | Initial deployment | — |
