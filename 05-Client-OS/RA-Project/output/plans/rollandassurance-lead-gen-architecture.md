# RollandAssurance — Garantie Décennale Lead Generation Automation
## Full Ecosystem Architecture

**Client:** RollandAssurance
**Project:** Automated Lead Generation — Garantie Décennale
**Date:** 2026-04-15
**Status:** Architecture Locked (MVP)

---

## 0. Decisions Log

| #   | Decision              | Choice                                                | Rationale                                                                |
| --- | --------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------ |
| 1   | Geography             | All of France                                         | Maximum lead volume                                                      |
| 2   | Priority strategy     | New-first (0–14d hottest), backfill last 90 days only | Urgency window closes after 90 days — older leads likely already insured |
| 3   | Enrichment API budget | ~€0.50–1.00/Grade A lead                              | Acceptable                                                               |
| 4   | Orchestration         | TBD — benchmark n8n vs Make.com                       | Deferred                                                                 |
| 5   | Database (MVP)        | Google Sheets                                         | Minimal, shareable, zero setup cost                                      |
| 6   | Delivery (MVP)        | Google Sheets shared view                             | Simple, immediate, no CRM needed                                         |

### Why 90-Day Backfill Limit

The value of this system is speed-to-contact. A company registered yesterday is in active setup mode — garantie décennale is literally on their checklist. After 90 days that urgency window closes: they've either bought insurance elsewhere or gone dormant. Backfilling beyond 90 days generates dead leads that waste cold call time.

**Lead urgency tiers:**
- 🔴 **0–14 days** → Call immediately (highest conversion probability)
- 🟠 **15–45 days** → Still hot
- 🟡 **46–90 days** → Lukewarm, backfill batch
- ⛔ **90+ days** → Skip entirely

---

## 1. Strategic Overview

### Core Concept
Tap the French company registry (SIRENE/INSEE) daily to capture every newly registered company with a BTP-related NAF code. Enrich each record with contact information (gérant name, phone, email, company details). Deliver a categorized, filterable lead database to RollandAssurance — segmented by NAF code so they can target specific trades at will.

### Why NAF-First Architecture
Rather than filtering leads upfront (which loses opportunities), we capture ALL BTP-adjacent NAF codes and label each lead accordingly. RollandAssurance can then:
- Target all codes simultaneously (volume play)
- Focus on specific trades (precision play)
- Build niche campaigns per trade category

### Lead Definition
A qualified lead = a company that:
1. Registered within the last N days (configurable)
2. Has a BTP-related NAF/APE code
3. Has at minimum: company name + SIRET + NAF code + region
4. Ideally enriched with: gérant name + phone + email

---

## 2. Full System Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                         TRIGGER LAYER                               │
│              Daily Cron Job (every morning at 6h00)                 │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYSTEM 1: DATA INGESTION                                           │
│  Source: API SIRENE (INSEE) + BODACC                                │
│  → Pull new registrations with BTP NAF codes                       │
│  → Raw output: SIRET, company name, NAF code, address,             │
│    creation date, gérant name (if available), legal form           │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYSTEM 2: NAF CLASSIFICATION ENGINE                                │
│  → Assign NAF label + trade category to each lead                  │
│  → Tag: trade_name, trade_group, decennale_required (bool)         │
│  → Output: enriched record with full NAF taxonomy                  │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYSTEM 3: DEDUPLICATION & LEAD DATABASE                           │
│  → Check if SIRET already exists in database                       │
│  → If new: insert record with status = "raw"                       │
│  → If exists: update if data changed, skip if identical            │
│  Storage: Airtable / Supabase / Google Sheets                      │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYSTEM 4: CONTACT ENRICHMENT PIPELINE                             │
│  → For each new "raw" lead, attempt contact enrichment             │
│                                                                     │
│  Layer 1 — Structural Data (free/cheap):                           │
│    • Pappers.fr API → gérant name, capital, effectifs              │
│    • Infogreffe → dirigeants, actes                                │
│                                                                     │
│  Layer 2 — Contact Data (paid APIs):                               │
│    • Dropcontact → professional email from name + company          │
│    • Kaspr / Lusha → phone number lookup                           │
│    • Societe.ninja → aggregated contact data                       │
│                                                                     │
│  Layer 3 — Web Footprint (scraping):                               │
│    • Google search: "[company name] contact téléphone"             │
│    • Scrape their first website if found (contact page)            │
│    • Check Pages Jaunes / Kompass                                   │
│                                                                     │
│  Output: lead status updated to "enriched" or "partial"            │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYSTEM 5: QUALITY SCORING                                         │
│  → Score each lead based on enrichment completeness                │
│    • 5 pts: has gérant name                                        │
│    • 5 pts: has phone number                                       │
│    • 5 pts: has email                                              │
│    • 3 pts: has website                                            │
│    • 2 pts: has full address                                       │
│  → Tag: quality_score (0–20), quality_tier (A/B/C)                │
│  → A = 15-20pts, B = 8-14pts, C = <8pts                           │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYSTEM 6: DELIVERY & EXPORT                                       │
│  → Daily digest email to RollandAssurance:                         │
│    "X new leads today — Y are Grade A"                             │
│  → Shared Airtable/Sheet view (live, filterable by NAF)            │
│  → Weekly CSV export of all new Grade A leads                      │
│  → Optional: webhook to their CRM (Hubspot / Pipedrive)            │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYSTEM 7: MONITORING & ALERTS                                     │
│  → Track: daily ingestion count, enrichment rate, error rate       │
│  → Alert if: API fails, enrichment rate drops below threshold      │
│  → Weekly report: leads generated, quality distribution            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. System-by-System Specification

---

### SYSTEM 1: Data Ingestion

**Purpose:** Pull every new BTP company registered in France daily.

**Primary Source: API SIRENE (INSEE)**
- Endpoint: `https://api.insee.fr/entreprises/sirene/V3/`
- Auth: Bearer token (free registration at api.insee.fr)
- Key query: filter by `dateCreationEtablissement` (yesterday) + NAF code list
- Returns: SIRET, siren, denominationUniteLegale, activitePrincipaleUniteLegale (NAF), codePostalEtablissement, gérant name (if individual company)

**Secondary Source: BODACC**
- URL: bodacc.fr (public data, also available via data.gouv.fr)
- Cross-reference for announcement of new company creation
- Useful for: gérant name confirmation, capital social

**Trigger:** Daily cron at 06:00 France time

**Output Schema (raw lead):**
```json
{
  "siret": "12345678901234",
  "siren": "123456789",
  "company_name": "DUPONT MAÇONNERIE",
  "naf_code": "43.99C",
  "creation_date": "2026-04-14",
  "legal_form": "EI",
  "address": "12 rue des Bâtisseurs",
  "city": "Lyon",
  "postal_code": "69001",
  "region": "Auvergne-Rhône-Alpes",
  "gerant_name": "Jean Dupont",
  "status": "raw",
  "ingested_at": "2026-04-15T06:12:00Z"
}
```

---

### SYSTEM 2: NAF Classification Engine

**Purpose:** Label every lead with a human-readable trade name and group, so RollandAssurance can instantly understand who they're calling.

**Full BTP NAF Code Reference Table:**

| NAF Code | Trade Name | Group | Décennale Required |
|----------|-----------|-------|-------------------|
| 41.10Z | Promotion immobilière | Promotion | Yes |
| 41.20A | Construction maisons individuelles | Gros Œuvre | Yes |
| 41.20B | Construction autres bâtiments | Gros Œuvre | Yes |
| 42.11Z | Construction routes et autoroutes | Génie Civil | Yes |
| 42.12Z | Construction voies ferrées | Génie Civil | Yes |
| 42.13A | Construction ouvrages d'art béton | Génie Civil | Yes |
| 42.13B | Construction et entretien tunnels | Génie Civil | Yes |
| 42.21Z | Construction réseaux fluides | Réseaux | Yes |
| 42.22Z | Construction réseaux électriques/télécoms | Réseaux | Yes |
| 42.91Z | Construction ouvrages maritimes/fluviaux | Génie Civil | Yes |
| 42.99Z | Construction autres ouvrages génie civil | Génie Civil | Yes |
| 43.11Z | Travaux de démolition | Démolition | Yes |
| 43.12A | Terrassement courant | Terrassement | Yes |
| 43.12B | Terrassement spécialisé | Terrassement | Yes |
| 43.13Z | Forages et sondages | Spécialisé | Yes |
| 43.21A | Installation électrique tous locaux | Électricité | Yes |
| 43.21B | Installation électrique voie publique | Électricité | Yes |
| 43.22A | Installation eau et gaz | Plomberie | Yes |
| 43.22B | Installation thermique et climatisation | CVC | Yes |
| 43.29A | Travaux d'isolation | Isolation | Yes |
| 43.29B | Autres travaux d'installation | Spécialisé | Yes |
| 43.31Z | Travaux de plâtrerie | Second Œuvre | Yes |
| 43.32A | Menuiserie bois et PVC | Menuiserie | Yes |
| 43.32B | Menuiserie métallique et serrurerie | Menuiserie | Yes |
| 43.32C | Agencement lieux de vente | Agencement | Yes |
| 43.33Z | Revêtement sols et murs | Second Œuvre | Yes |
| 43.34Z | Peinture et vitrerie | Second Œuvre | Yes |
| 43.39Z | Autres travaux de finition | Second Œuvre | Yes |
| 43.91A | Travaux de charpente | Charpente | Yes |
| 43.91B | Travaux de couverture | Couverture | Yes |
| 43.99A | Travaux d'étanchéité | Étanchéité | Yes |
| 43.99B | Montage structures métalliques | Métal | Yes |
| 43.99C | Maçonnerie générale et gros œuvre | Gros Œuvre | Yes |
| 43.99D | Autres travaux spécialisés | Spécialisé | Yes |
| 43.99E | Location avec opérateur engins BTP | Location | Partial |
| 71.11Z | Activités d'architecture | Bureau d'études | Partial |
| 71.12B | Ingénierie et études techniques | Bureau d'études | Partial |
| 81.10Z | Soutien lié aux bâtiments | Services BTP | No |

**Output:** Each lead gets `trade_name`, `trade_group`, `decennale_required` fields appended.

---

### SYSTEM 3: Deduplication & Lead Database

**Purpose:** Single source of truth. No company appears twice.

**Dedup Key:** SIRET (unique per établissement)

**Lead Lifecycle States:**
```
raw → enriching → enriched → delivered → contacted → converted/lost
```

**Recommended Storage Options (choose one):**

| Option | Pros | Cons | Best for |
|--------|------|------|----------|
| Airtable | Visual, easy to share with RollandAssurance, filterable | Cost at scale, API limits | MVP / small volume |
| Google Sheets + Apps Script | Free, familiar | Limited scalability, no proper API | Very early MVP |
| Supabase (PostgreSQL) | Scalable, free tier, REST API | Requires more setup | Production system |
| Notion Database | Easy sharing | Poor for automation | Not recommended |

**Recommended: Airtable for MVP → Supabase for scale**

**Database Schema:**
```
leads table:
- id (auto)
- siret (unique, indexed)
- siren
- company_name
- naf_code
- trade_name
- trade_group
- decennale_required
- creation_date
- legal_form
- address, city, postal_code, region
- gerant_name
- phone
- email
- website
- quality_score (0-20)
- quality_tier (A/B/C)
- status (raw/enriching/enriched/delivered/contacted)
- ingested_at
- enriched_at
- delivered_at
- notes
```

---

### SYSTEM 4: Contact Enrichment Pipeline

**Purpose:** Turn a SIRET into a callable, emailable person.

**Enrichment Waterfall (try in order, stop when sufficient data found):**

```
Step 1: Pappers.fr API
  → Input: SIREN
  → Output: dirigeants (name, role), capital, effectifs, site web
  → Cost: Free tier available, paid for volume
  → API: pappers.fr/api

Step 2: Infogreffe API
  → Input: SIREN
  → Output: dirigeants officiels, actes déposés
  → Cost: Paid (€0.05-0.20/query)

Step 3: Societe.com / Societe.ninja scraping
  → Input: SIREN or company name
  → Output: phone number, email if public
  → Cost: Free (scraping) or API

Step 4: Dropcontact API
  → Input: first name + last name + company name/domain
  → Output: professional email (GDPR-compliant, verified)
  → Cost: ~€0.10/contact
  → API: dropcontact.com

Step 5: Kaspr or Lusha API
  → Input: name + company
  → Output: direct phone number (mobile preferred)
  → Cost: credit-based (~€0.20-0.50/phone)

Step 6: Web Scraping Fallback
  → Google: "[company_name] [city] téléphone contact"
  → Pages Jaunes lookup by SIRET
  → Scrape their website contact page if found

Step 7: Mark as partial if only name found, raw if nothing found
```

**Enrichment Priority:**
1. Phone number (highest value for cold calling)
2. Gérant full name
3. Email
4. Website

---

### SYSTEM 5: Quality Scoring

**Purpose:** Let RollandAssurance prioritize Grade A leads first.

**Scoring Matrix:**
```
Gérant name found:    +5 pts
Phone number found:   +5 pts
Email found:          +5 pts
Website found:        +3 pts
Full address:         +2 pts
─────────────────────────────
Max:                  20 pts

Grade A: 15–20 pts  (ready to call)
Grade B: 8–14 pts   (usable, missing one key field)
Grade C: 0–7 pts    (SIRET only, needs manual work)
```

---

### SYSTEM 6: Delivery & Export

**Purpose:** Get leads in front of RollandAssurance in a usable format.

**Delivery Channels:**

**Channel 1 — Daily Email Digest**
```
Subject: [RollandAssurance] X nouveaux leads BTP — 15 avril 2026

Bonjour,

Voici le résumé de la veille automatisée garantie décennale :

📊 Nouveaux leads aujourd'hui : 47
✅ Grade A (appelables) : 18
⚠️ Grade B (partiels) : 21
❌ Grade C (incomplets) : 8

Top NAF codes d'aujourd'hui :
• 43.99C — Maçonnerie (12 leads)
• 43.22A — Plomberie (8 leads)
• 43.34Z — Peinture (7 leads)

→ [Voir tous les leads dans Airtable]
→ [Télécharger CSV Grade A uniquement]
```

**Channel 2 — Shared Airtable Base (live)**
- RollandAssurance gets a read/write view
- Filterable by: NAF code, region, quality grade, status
- They update "contacted" / "not interested" / "signed" status
- This creates a feedback loop for system improvement

**Channel 3 — Weekly CSV Export**
- Every Monday: all new Grade A leads from the past 7 days
- Columns: Company, Gérant, Phone, Email, NAF Code, Trade, Region, Creation Date

---

### SYSTEM 7: Monitoring & Alerts

**Purpose:** Ensure the pipeline never silently breaks.

**Metrics to Track:**
| Metric | Target | Alert if |
|--------|--------|----------|
| Daily leads ingested | 20–100 | < 5 |
| Enrichment rate (phone found) | > 40% | < 20% |
| Enrichment rate (email found) | > 60% | < 30% |
| Grade A rate | > 30% | < 15% |
| API error rate | < 5% | > 15% |
| Duplicate rate | < 2% | > 10% |

**Alert Channels:** Email to system admin + Slack/Telegram notification

---

## 4. Technology Stack

| Layer            | Recommended Tool                 | Alternative        |
| ---------------- | -------------------------------- | ------------------ |
| Orchestration    | n8n (self-hosted)                | Make.com           |
| SIRENE data      | API INSEE (official)             | data.gouv.fr dumps |
| Gérant data      | Pappers.fr API                   | Infogreffe API     |
| Email enrichment | Dropcontact                      | Hunter.io          |
| Phone enrichment | Kaspr                            | Lusha              |
| Web scraping     | Playwright + Python              | Scrapy             |
| Database         | Airtable (MVP) / Supabase (prod) | Google Sheets      |
| Delivery         | SMTP email + Airtable            | Notion / Hubspot   |
| Monitoring       | n8n built-in + email alerts      | Datadog            |
| Hosting          | VPS (Hetzner/OVH) or serverless  | Vercel / Railway   |

---

## 5. Data Flow Summary

```
INSEE SIRENE API
      ↓ (pull daily new BTP registrations)
Raw Lead Record (SIRET + NAF + basic info)
      ↓
NAF Classification → trade_name + trade_group + decennale_required
      ↓
Dedup Check → insert if new SIRET
      ↓
Enrichment Waterfall:
  Pappers → gérant name + effectifs
  Dropcontact → professional email
  Kaspr → phone number
  Web scraping → fallback contact info
      ↓
Quality Scoring → Grade A / B / C
      ↓
Delivery:
  Daily email digest → RollandAssurance
  Live Airtable view → RollandAssurance filters by NAF
  Weekly CSV → cold calling list
      ↓
Feedback Loop:
  RollandAssurance marks "contacted / signed / lost"
  System learns which NAF codes convert best
```

---

## 6. Build Order (System-by-System)

| Priority | System | Complexity | Dependencies |
|----------|--------|------------|--------------|
| 1 | Data Ingestion (SIRENE API) | Low | INSEE API key |
| 2 | NAF Classification Engine | Low | NAF code table |
| 3 | Lead Database (Airtable) | Low | Airtable account |
| 4 | Deduplication Logic | Low | Database setup |
| 5 | Pappers Enrichment | Medium | Pappers API key |
| 6 | Email Enrichment (Dropcontact) | Medium | Dropcontact account |
| 7 | Phone Enrichment (Kaspr) | Medium | Kaspr account |
| 8 | Quality Scoring | Low | Enrichment complete |
| 9 | Delivery (Email digest) | Medium | SMTP config |
| 10 | Airtable shared view | Low | Database setup |
| 11 | Web scraping fallback | High | Python/Playwright |
| 12 | Monitoring & alerts | Medium | All systems live |

---

## 7. MVP Architecture — Google Sheets Stack

For the MVP, the entire system collapses into a lean, zero-infrastructure setup:

```
INSEE SIRENE API
      ↓ (daily pull via script/automation)
Python script or n8n/Make workflow
      ↓
Dedup check against Google Sheet (SIRET column)
      ↓
Pappers API → gérant name, effectifs
      ↓
Dropcontact → email
Kaspr → phone
      ↓
Quality score calculated
      ↓
New rows appended to Google Sheet
      ↓
RollandAssurance opens Sheet, filters by NAF code, grade, region
      ↓
They mark "contacted / signed / lost" in status column
```

**Google Sheet Structure (MVP):**

| Column | Field | Notes |
|--------|-------|-------|
| A | SIRET | Unique key, dedup on this |
| B | Company Name | |
| C | NAF Code | |
| D | Trade Name | From classification table |
| E | Trade Group | Gros Œuvre / Plomberie / etc. |
| F | Décennale Required | Yes/Partial/No |
| G | Creation Date | |
| H | Urgency Tier | 🔴/🟠/🟡 |
| I | Region | |
| J | City | |
| K | Postal Code | |
| L | Gérant Name | From Pappers |
| M | Phone | From Kaspr |
| N | Email | From Dropcontact |
| O | Website | |
| P | Quality Score | 0–20 |
| Q | Grade | A / B / C |
| R | Status | New / Contacted / Signed / Lost |
| S | Notes | RollandAssurance fills this |
| T | Ingested At | Auto timestamp |
| U | Enriched At | Auto timestamp |

**Sheet tabs:**
- `All Leads` — full database
- `Grade A — This Week` — auto-filtered view, ready to call
- `NAF Reference` — code table for lookup
- `Stats Dashboard` — simple formulas tracking counts/rates

## 8. Open Questions (Remaining)

1. **Orchestration platform:** Benchmark n8n (self-hosted VPS) vs Make.com — key factors: budget, technical comfort, volume of operations/month
2. **Pappers API tier:** Free tier = 1,000 calls/month. If daily ingestion exceeds ~33 companies/day, need paid plan
