# RollandAssurance — n8n Full Building Blueprint
## System-by-System, Step-by-Step

**Stack:** n8n self-hosted · Google Sheets · INSEE SIRENE API · Pappers · Dropcontact · Lusha
**Date:** 2026-04-15
**Status:** Build-Ready

---

## PHASE 0: INFRASTRUCTURE SETUP

### Step 0.1 — Provision VPS

**Provider:** Hetzner Cloud (cheapest reliable option)
**Server:** CX21 — 2 vCPU, 4GB RAM, 40GB SSD — €5.77/month
**OS:** Ubuntu 22.04 LTS

```bash
# After SSH into the server:
apt update && apt upgrade -y
apt install -y docker.io docker-compose nginx certbot python3-certbot-nginx ufw
systemctl enable docker
```

**Firewall setup:**
```bash
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw enable
```

---

### Step 0.2 — Install n8n via Docker Compose

Create the project folder and config:

```bash
mkdir -p /opt/n8n && cd /opt/n8n
```

Create `/opt/n8n/docker-compose.yml`:

```yaml
version: "3.8"

services:
  postgres:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: n8n
      POSTGRES_PASSWORD: CHANGE_THIS_PASSWORD
      POSTGRES_DB: n8n
    volumes:
      - postgres_data:/var/lib/postgresql/data

  n8n:
    image: n8nio/n8n:latest
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_HOST=n8n.yourdomain.com
      - N8N_PORT=5678
      - N8N_PROTOCOL=https
      - NODE_ENV=production
      - WEBHOOK_URL=https://n8n.yourdomain.com/
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_PORT=5432
      - DB_POSTGRESDB_DATABASE=n8n
      - DB_POSTGRESDB_USER=n8n
      - DB_POSTGRESDB_PASSWORD=CHANGE_THIS_PASSWORD
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=CHANGE_THIS_PASSWORD
      - EXECUTIONS_PROCESS=main
      - N8N_LOG_LEVEL=info
    volumes:
      - n8n_data:/home/node/.n8n
    depends_on:
      - postgres

volumes:
  postgres_data:
  n8n_data:
```

```bash
cd /opt/n8n && docker-compose up -d
```

---

### Step 0.3 — Configure Nginx + SSL

Create `/etc/nginx/sites-available/n8n`:

```nginx
server {
    listen 80;
    server_name n8n.yourdomain.com;

    location / {
        proxy_pass http://localhost:5678;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        chunked_transfer_encoding off;
        proxy_buffering off;
        proxy_read_timeout 3600s;
    }
}
```

```bash
ln -s /etc/nginx/sites-available/n8n /etc/nginx/sites-enabled/
nginx -t && systemctl reload nginx
certbot --nginx -d n8n.yourdomain.com
```

**n8n is now live at:** `https://n8n.yourdomain.com`

---

### Step 0.4 — Register All API Accounts

Before building workflows, create accounts and get API keys:

| Service | URL | What you get | Cost |
|---------|-----|-------------|------|
| INSEE SIRENE | api.insee.fr | Consumer Key + Secret | Free |
| Pappers | pappers.fr/api | API Token | Free (1k calls/mo) |
| Dropcontact | dropcontact.com | API Key | €0.10/contact |
| Lusha | lusha.com | API Key | Credit-based |
| Google Cloud | console.cloud.google.com | Service Account JSON | Free |

---

### Step 0.5 — Google Sheets Setup

**Create the Google Sheet with these tabs:**

1. `Leads` — main database
2. `Stats` — dashboard formulas
3. `NAF_Reference` — lookup table
4. `Log` — ingestion run log

**Leads tab — Column headers (Row 1):**

```
A: SIRET | B: SIREN | C: Company Name | D: NAF Code | E: Trade Name
F: Trade Group | G: Décennale Required | H: Creation Date | I: Urgency Tier
J: Days Since Registration | K: Legal Form | L: Address | M: City
N: Postal Code | O: Region | P: Gérant Name | Q: Phone | R: Email
S: Website | T: Quality Score | U: Grade | V: Status | W: Notes
X: Ingested At | Y: Enriched At | Z: Delivered At
```

**Enable Google Sheets API:**
1. Go to console.cloud.google.com
2. Create project → Enable Google Sheets API + Google Drive API
3. Create Service Account → Download JSON key
4. Share the Google Sheet with the service account email

**In n8n:** Add credential → Google Sheets OAuth2 → paste Service Account JSON

---

## PHASE 1: WORKFLOW 1 — SIRENE DATA INGESTION

**Workflow name:** `01 - SIRENE Daily Ingestion`
**Trigger:** Cron — every day at 06:00 Paris time
**Purpose:** Pull all new BTP companies registered in France, filtered by NAF codes

---

### Node 1.1 — Cron Trigger

```
Node type: Schedule Trigger
Settings:
  - Mode: Cron Expression
  - Expression: 0 6 * * *   (every day at 06:00)
  - Timezone: Europe/Paris
```

---

### Node 1.2 — Set Run Variables

```
Node type: Set
Purpose: Define the date range and NAF code list for this run

Variables to set:
  date_today:     {{ $now.toFormat('yyyy-MM-dd') }}
  date_yesterday: {{ $now.minus({days: 1}).toFormat('yyyy-MM-dd') }}
  date_90days:    {{ $now.minus({days: 90}).toFormat('yyyy-MM-dd') }}
  is_first_run:   false   (set to true manually for the initial backfill run)

  naf_codes_list: "4110Z,4120A,4120B,4211Z,4212Z,4213A,4213B,4221Z,4222Z,4291Z,4299Z,4311Z,4312A,4312B,4313Z,4321A,4321B,4322A,4322B,4329A,4329B,4331Z,4332A,4332B,4332C,4333Z,4334Z,4339Z,4391A,4391B,4399A,4399B,4399C,4399D,4399E,7111Z,7112B"
```

**Note on NAF format:** INSEE API uses codes without dots (4120A not 41.20A)

---

### Node 1.3 — Get INSEE Bearer Token

INSEE uses OAuth2 client credentials flow. Token expires every hour.

```
Node type: HTTP Request
Method: POST
URL: https://api.insee.fr/token

Authentication: None (we send credentials in body)

Body (Form-URL-Encoded):
  grant_type: client_credentials

Headers:
  Authorization: Basic {{ Buffer.from('YOUR_CONSUMER_KEY:YOUR_CONSUMER_SECRET').toString('base64') }}
  Content-Type: application/x-www-form-urlencoded

Output: Save {{ $json.access_token }} for next nodes
```

---

### Node 1.4 — Set Bearer Token

```
Node type: Set
  insee_token: {{ $json.access_token }}
```

---

### Node 1.5 — Build NAF Query String

```
Node type: Function
Purpose: Build the Lucene query for SIRENE API

Code:
const nafCodes = items[0].json.naf_codes_list.split(',');
const nafQuery = nafCodes.map(c => `"${c}"`).join(' OR ');

const dateFrom = items[0].json.is_first_run === 'true'
  ? items[0].json.date_90days
  : items[0].json.date_yesterday;

const query = `activitePrincipaleEtablissement:(${nafQuery}) AND dateCreationEtablissement:[${dateFrom} TO ${items[0].json.date_today}] AND etatAdministratifEtablissement:A`;

return [{ json: {
  ...items[0].json,
  sirene_query: query,
  date_from: dateFrom,
  page: 0,
  all_results: []
}}];
```

---

### Node 1.6 — SIRENE API First Call

```
Node type: HTTP Request
Method: GET
URL: https://api.insee.fr/entreprises/sirene/V3.11/siret

Headers:
  Authorization: Bearer {{ $('Set Bearer Token').item.json.insee_token }}
  Accept: application/json

Query Parameters:
  q:      {{ $json.sirene_query }}
  nombre: 1000
  debut:  0
  champs: siret,siren,denominationUniteLegale,nomUniteLegale,prenomUsuelUniteLegale,activitePrincipaleEtablissement,dateCreationEtablissement,categorieJuridiqueUniteLegale,codePostalEtablissement,libelleCommuneEtablissement,codeCommuneEtablissement,adresseEtablissement,trancheEffectifsUniteLegale

Output: raw SIRENE response with etablissements array + header.total
```

---

### Node 1.7 — Check Total Count & Plan Pagination

```
Node type: Function
Code:
const total = items[0].json.header.total;
const perPage = 1000;
const pages = Math.ceil(total / perPage);
const pageNumbers = [];

for (let i = 0; i < pages; i++) {
  pageNumbers.push({ json: { page: i, debut: i * perPage, total } });
}

// Store first page results
const firstPageResults = items[0].json.etablissements || [];

// If only 1 page, pass results directly
if (pages <= 1) {
  return [{ json: { etablissements: firstPageResults, total, pages: 1 } }];
}

return pageNumbers.map(p => ({ json: { ...p.json, firstPageResults } }));
```

---

### Node 1.8 — Fetch Remaining Pages (if total > 1000)

```
Node type: HTTP Request (same config as Node 1.6)
Query Parameters:
  debut: {{ $json.debut }}
  (others same as Node 1.6)

Note: This node runs once per page. Connect after Node 1.7
with a Split In Batches node if needed for large datasets.
```

---

### Node 1.9 — Merge All Pages + Flatten Results

```
Node type: Function
Code:
// Collect all etablissements from all pages
const allEtablissements = [];

for (const item of items) {
  const etabs = item.json.etablissements || [];
  allEtablissements.push(...etabs);
}

// Flatten each établissement into our standard raw lead format
const rawLeads = allEtablissements.map(e => {
  const ul = e.uniteLegale || {};
  const adresse = e.adresseEtablissement || {};

  // Build gérant name for individual companies (EI, EIRL, etc.)
  const gerantName = [ul.prenomUsuelUniteLegale, ul.nomUniteLegale]
    .filter(Boolean).join(' ') || null;

  // Build full address
  const addressParts = [
    adresse.numeroVoieEtablissement,
    adresse.typeVoieEtablissement,
    adresse.libelleVoieEtablissement
  ].filter(Boolean).join(' ');

  return {
    siret: e.siret,
    siren: e.siren,
    company_name: ul.denominationUniteLegale || `${ul.prenomUsuelUniteLegale || ''} ${ul.nomUniteLegale || ''}`.trim(),
    naf_code_raw: e.activitePrincipaleEtablissement || '',
    creation_date: e.dateCreationEtablissement,
    legal_form_code: ul.categorieJuridiqueUniteLegale,
    address: addressParts,
    city: adresse.libelleCommuneEtablissement,
    postal_code: adresse.codePostalEtablissement,
    gerant_name: gerantName,
    status: 'raw',
    ingested_at: new Date().toISOString()
  };
});

return rawLeads.map(lead => ({ json: lead }));
```

---

### Node 1.10 — Split Into Individual Items

```
Node type: Split In Batches
Batch Size: 1
(Processes each lead one at a time through the rest of the workflow)
```

**→ Output feeds into Workflow 2 (NAF Classification)**

---

## PHASE 2: WORKFLOW 2 — NAF CLASSIFICATION ENGINE

**Workflow name:** `02 - NAF Classification`
**Trigger:** Called by Workflow 1 for each raw lead
**Purpose:** Enrich each lead with trade name, group, urgency tier

---

### Node 2.1 — NAF Lookup Function

```
Node type: Function
Code:

const NAF_TABLE = {
  '4110Z': { trade_name: 'Promotion immobilière', trade_group: 'Promotion', decennale: 'Yes' },
  '4120A': { trade_name: 'Construction maisons individuelles', trade_group: 'Gros Œuvre', decennale: 'Yes' },
  '4120B': { trade_name: 'Construction autres bâtiments', trade_group: 'Gros Œuvre', decennale: 'Yes' },
  '4211Z': { trade_name: 'Construction routes et autoroutes', trade_group: 'Génie Civil', decennale: 'Yes' },
  '4212Z': { trade_name: 'Construction voies ferrées', trade_group: 'Génie Civil', decennale: 'Yes' },
  '4213A': { trade_name: "Construction ouvrages d'art béton", trade_group: 'Génie Civil', decennale: 'Yes' },
  '4213B': { trade_name: 'Construction et entretien tunnels', trade_group: 'Génie Civil', decennale: 'Yes' },
  '4221Z': { trade_name: 'Construction réseaux fluides', trade_group: 'Réseaux', decennale: 'Yes' },
  '4222Z': { trade_name: 'Construction réseaux électriques/télécoms', trade_group: 'Réseaux', decennale: 'Yes' },
  '4291Z': { trade_name: 'Construction ouvrages maritimes/fluviaux', trade_group: 'Génie Civil', decennale: 'Yes' },
  '4299Z': { trade_name: 'Construction autres ouvrages génie civil', trade_group: 'Génie Civil', decennale: 'Yes' },
  '4311Z': { trade_name: 'Travaux de démolition', trade_group: 'Démolition', decennale: 'Yes' },
  '4312A': { trade_name: 'Terrassement courant', trade_group: 'Terrassement', decennale: 'Yes' },
  '4312B': { trade_name: 'Terrassement spécialisé', trade_group: 'Terrassement', decennale: 'Yes' },
  '4313Z': { trade_name: 'Forages et sondages', trade_group: 'Spécialisé', decennale: 'Yes' },
  '4321A': { trade_name: 'Installation électrique tous locaux', trade_group: 'Électricité', decennale: 'Yes' },
  '4321B': { trade_name: 'Installation électrique voie publique', trade_group: 'Électricité', decennale: 'Yes' },
  '4322A': { trade_name: 'Installation eau et gaz', trade_group: 'Plomberie', decennale: 'Yes' },
  '4322B': { trade_name: 'Installation thermique et climatisation', trade_group: 'CVC', decennale: 'Yes' },
  '4329A': { trade_name: "Travaux d'isolation", trade_group: 'Isolation', decennale: 'Yes' },
  '4329B': { trade_name: "Autres travaux d'installation", trade_group: 'Spécialisé', decennale: 'Yes' },
  '4331Z': { trade_name: 'Travaux de plâtrerie', trade_group: 'Second Œuvre', decennale: 'Yes' },
  '4332A': { trade_name: 'Menuiserie bois et PVC', trade_group: 'Menuiserie', decennale: 'Yes' },
  '4332B': { trade_name: 'Menuiserie métallique et serrurerie', trade_group: 'Menuiserie', decennale: 'Yes' },
  '4332C': { trade_name: 'Agencement lieux de vente', trade_group: 'Agencement', decennale: 'Yes' },
  '4333Z': { trade_name: 'Revêtement sols et murs', trade_group: 'Second Œuvre', decennale: 'Yes' },
  '4334Z': { trade_name: 'Peinture et vitrerie', trade_group: 'Second Œuvre', decennale: 'Yes' },
  '4339Z': { trade_name: 'Autres travaux de finition', trade_group: 'Second Œuvre', decennale: 'Yes' },
  '4391A': { trade_name: 'Travaux de charpente', trade_group: 'Charpente', decennale: 'Yes' },
  '4391B': { trade_name: 'Travaux de couverture', trade_group: 'Couverture', decennale: 'Yes' },
  '4399A': { trade_name: "Travaux d'étanchéité", trade_group: 'Étanchéité', decennale: 'Yes' },
  '4399B': { trade_name: 'Montage structures métalliques', trade_group: 'Métal', decennale: 'Yes' },
  '4399C': { trade_name: 'Maçonnerie générale et gros œuvre', trade_group: 'Gros Œuvre', decennale: 'Yes' },
  '4399D': { trade_name: 'Autres travaux spécialisés', trade_group: 'Spécialisé', decennale: 'Yes' },
  '4399E': { trade_name: 'Location avec opérateur engins BTP', trade_group: 'Location', decennale: 'Partial' },
  '7111Z': { trade_name: "Activités d'architecture", trade_group: "Bureau d'études", decennale: 'Partial' },
  '7112B': { trade_name: 'Ingénierie et études techniques', trade_group: "Bureau d'études", decennale: 'Partial' },
};

const LEGAL_FORM_MAP = {
  '1000': 'Entrepreneur individuel (EI)',
  '5410': 'SARL',
  '5499': 'SARL',
  '5720': 'SA',
  '5210': 'SNC',
  '5215': 'EURL',
  '1100': 'Artisan',
  '6540': 'SAS',
  '6541': 'SASU',
};

const lead = items[0].json;
const nafRaw = (lead.naf_code_raw || '').replace('.', '');
const nafInfo = NAF_TABLE[nafRaw] || {
  trade_name: 'Non classifié',
  trade_group: 'Autre',
  decennale: 'Unknown'
};

// Calculate urgency tier
const creationDate = new Date(lead.creation_date);
const today = new Date();
const daysSince = Math.floor((today - creationDate) / (1000 * 60 * 60 * 24));

let urgencyTier, urgencyEmoji;
if (daysSince <= 14) { urgencyTier = 'HOT'; urgencyEmoji = '🔴'; }
else if (daysSince <= 45) { urgencyTier = 'WARM'; urgencyEmoji = '🟠'; }
else if (daysSince <= 90) { urgencyTier = 'LUKEWARM'; urgencyEmoji = '🟡'; }
else { urgencyTier = 'COLD'; urgencyEmoji = '⛔'; }

// Format NAF code with dot for display
const nafDisplay = nafRaw.length >= 5
  ? nafRaw.slice(0, 4) + '.' + nafRaw.slice(4)
  : nafRaw;

return [{
  json: {
    ...lead,
    naf_code: nafDisplay,
    trade_name: nafInfo.trade_name,
    trade_group: nafInfo.trade_group,
    decennale_required: nafInfo.decennale,
    legal_form: LEGAL_FORM_MAP[lead.legal_form_code] || lead.legal_form_code,
    days_since_registration: daysSince,
    urgency_tier: `${urgencyEmoji} ${urgencyTier}`,
  }
}];
```

**→ Output feeds into Workflow 3 (Deduplication check)**

---

## PHASE 3: WORKFLOW 3 — DEDUPLICATION & GOOGLE SHEETS CHECK

**Workflow name:** `03 - Dedup Check`
**Purpose:** Check if this SIRET already exists in Google Sheets. Skip if yes, continue if no.

---

### Node 3.1 — Read Google Sheets SIRET Column

```
Node type: Google Sheets
Operation: Read Rows
Spreadsheet: [your spreadsheet ID]
Sheet: Leads
Range: A:A   (SIRET column only — fast, minimal data transfer)
Options:
  - Return All Rows: true
```

---

### Node 3.2 — Check If SIRET Exists

```
Node type: Function
Code:

const incomingLead = $('NAF Classification').item.json;
const existingSirets = items.map(i => String(i.json.SIRET || i.json.A || '').trim());

const exists = existingSirets.includes(String(incomingLead.siret).trim());

return [{
  json: {
    ...incomingLead,
    is_duplicate: exists
  }
}];
```

---

### Node 3.3 — IF: Skip Duplicates

```
Node type: IF
Condition: {{ $json.is_duplicate }} equals true

True branch  → Stop and Error (or just NoOp — skip this lead)
False branch → Continue to Enrichment
```

---

## PHASE 4: WORKFLOW 4 — CONTACT ENRICHMENT PIPELINE

**Workflow name:** `04 - Contact Enrichment`
**Purpose:** Waterfall enrichment — Pappers → Dropcontact → Lusha
**Input:** New, deduplicated, classified lead

---

### Node 4.1 — Pappers API Call (Gérant Name + Company Details)

```
Node type: HTTP Request
Method: GET
URL: https://api.pappers.fr/v2/entreprise

Query Parameters:
  api_token: {{ $credentials.pappersApiKey }}
  siren:     {{ $json.siren }}
  _fields:   dirigeants,effectif,site_internet,capital,date_creation

Error Handling: Continue on Fail = true
```

---

### Node 4.2 — Extract Pappers Data

```
Node type: Function
Code:

const lead = $('Dedup Check').item.json;
const pappers = items[0].json;

// Extract gérant — first dirigeant with quality > 0
let gerantName = lead.gerant_name; // fallback to SIRENE value
let website = null;
let effectif = null;

if (pappers.dirigeants && pappers.dirigeants.length > 0) {
  const dirigeant = pappers.dirigeants[0];
  const firstName = dirigeant.prenom || '';
  const lastName = dirigeant.nom || '';
  if (firstName || lastName) {
    gerantName = `${firstName} ${lastName}`.trim();
  }
}

if (pappers.site_internet) website = pappers.site_internet;
if (pappers.effectif) effectif = pappers.effectif;

return [{
  json: {
    ...lead,
    gerant_name: gerantName,
    website: website,
    company_size: effectif,
    pappers_enriched: true
  }
}];
```

---

### Node 4.3 — IF: Has Gérant Name for Email Enrichment?

```
Node type: IF
Condition: {{ $json.gerant_name }} is not empty AND {{ $json.gerant_name }} is not null

True  → Continue to Dropcontact
False → Skip to quality scoring (no name = can't find email)
```

---

### Node 4.4 — Dropcontact API Call (Professional Email)

```
Node type: HTTP Request
Method: POST
URL: https://api.dropcontact.com/batch

Headers:
  X-Access-Token: {{ $credentials.dropcontactApiKey }}
  Content-Type: application/json

Body (JSON):
{
  "data": [
    {
      "first_name": "{{ $json.gerant_name.split(' ')[0] }}",
      "last_name": "{{ $json.gerant_name.split(' ').slice(1).join(' ') }}",
      "company": "{{ $json.company_name }}",
      "website": "{{ $json.website || '' }}"
    }
  ],
  "siren": true,
  "language": "fr"
}

Note: Dropcontact is async — it returns a request_id.
You then poll GET /batch/{request_id} until status = "done"
```

---

### Node 4.5 — Wait for Dropcontact Result

```
Node type: Wait
Duration: 10 seconds
(Dropcontact typically responds in 5-15 seconds)
```

---

### Node 4.6 — Poll Dropcontact Result

```
Node type: HTTP Request
Method: GET
URL: https://api.dropcontact.com/batch/{{ $('Dropcontact Call').item.json.request_id }}

Headers:
  X-Access-Token: {{ $credentials.dropcontactApiKey }}
```

---

### Node 4.7 — Extract Email from Dropcontact

```
Node type: Function
Code:

const lead = $('Pappers Extract').item.json;
const dc = items[0].json;

let email = null;
if (dc.data && dc.data[0] && dc.data[0].email && dc.data[0].email.length > 0) {
  // Take highest confidence email
  const sorted = dc.data[0].email.sort((a, b) => b.qualification - a.qualification);
  email = sorted[0].email;
}

return [{
  json: {
    ...lead,
    email: email,
    dropcontact_enriched: !!email
  }
}];
```

---

### Node 4.8 — Lusha API Call (Phone Number)

```
Node type: HTTP Request
Method: GET
URL: https://api.lusha.com/person

Headers:
  api_key: {{ $credentials.lushaApiKey }}

Query Parameters:
  firstName: {{ $json.gerant_name.split(' ')[0] }}
  lastName:  {{ $json.gerant_name.split(' ').slice(1).join(' ') }}
  company:   {{ $json.company_name }}

Error Handling: Continue on Fail = true
```

---

### Node 4.9 — Extract Phone from Lusha

```
Node type: Function
Code:

const lead = $('Dropcontact Extract').item.json;
const lusha = items[0].json;

let phone = null;
if (lusha.data && lusha.data.phoneNumbers && lusha.data.phoneNumbers.length > 0) {
  // Prefer mobile over direct
  const mobile = lusha.data.phoneNumbers.find(p => p.type === 'mobile');
  phone = mobile ? mobile.localizedNumber : lusha.data.phoneNumbers[0].localizedNumber;
}

return [{
  json: {
    ...lead,
    phone: phone,
    lusha_enriched: !!phone,
    enriched_at: new Date().toISOString()
  }
}];
```

---

## PHASE 5: WORKFLOW 5 — QUALITY SCORING

**Workflow name:** `05 - Quality Scoring`
**Purpose:** Score each enriched lead and assign Grade A/B/C

---

### Node 5.1 — Calculate Quality Score

```
Node type: Function
Code:

const lead = items[0].json;
let score = 0;

if (lead.gerant_name && lead.gerant_name.trim().length > 2) score += 5;
if (lead.phone && lead.phone.trim().length > 6)             score += 5;
if (lead.email && lead.email.includes('@'))                 score += 5;
if (lead.website && lead.website.includes('.'))             score += 3;
if (lead.address && lead.city && lead.postal_code)         score += 2;

let grade;
if (score >= 15)      grade = 'A';
else if (score >= 8)  grade = 'B';
else                  grade = 'C';

return [{
  json: {
    ...lead,
    quality_score: score,
    grade: grade,
    status: 'enriched'
  }
}];
```

---

## PHASE 6: WORKFLOW 6 — GOOGLE SHEETS WRITE

**Workflow name:** `06 - Write to Google Sheets`
**Purpose:** Append enriched, scored lead as a new row

---

### Node 6.1 — Format Row for Google Sheets

```
Node type: Set
Purpose: Map lead fields to exact column order

Values:
  col_A:  {{ $json.siret }}
  col_B:  {{ $json.siren }}
  col_C:  {{ $json.company_name }}
  col_D:  {{ $json.naf_code }}
  col_E:  {{ $json.trade_name }}
  col_F:  {{ $json.trade_group }}
  col_G:  {{ $json.decennale_required }}
  col_H:  {{ $json.creation_date }}
  col_I:  {{ $json.urgency_tier }}
  col_J:  {{ $json.days_since_registration }}
  col_K:  {{ $json.legal_form }}
  col_L:  {{ $json.address }}
  col_M:  {{ $json.city }}
  col_N:  {{ $json.postal_code }}
  col_O:  {{ $json.region || '' }}
  col_P:  {{ $json.gerant_name || '' }}
  col_Q:  {{ $json.phone || '' }}
  col_R:  {{ $json.email || '' }}
  col_S:  {{ $json.website || '' }}
  col_T:  {{ $json.quality_score }}
  col_U:  {{ $json.grade }}
  col_V:  Nouveau
  col_W:  (empty — RollandAssurance fills this)
  col_X:  {{ $json.ingested_at }}
  col_Y:  {{ $json.enriched_at }}
  col_Z:  (empty)
```

---

### Node 6.2 — Append Row to Google Sheets

```
Node type: Google Sheets
Operation: Append
Spreadsheet: [your spreadsheet ID]
Sheet: Leads
Options:
  - Value Input Option: USER_ENTERED (so dates format correctly)
  - Insert Data Option: INSERT_ROWS

Column Mapping:
  SIRET           → col_A
  SIREN           → col_B
  Company Name    → col_C
  NAF Code        → col_D
  Trade Name      → col_E
  Trade Group     → col_F
  Décennale       → col_G
  Creation Date   → col_H
  Urgency Tier    → col_I
  Days Since Reg  → col_J
  Legal Form      → col_K
  Address         → col_L
  City            → col_M
  Postal Code     → col_N
  Region          → col_O
  Gérant Name     → col_P
  Phone           → col_Q
  Email           → col_R
  Website         → col_S
  Quality Score   → col_T
  Grade           → col_U
  Status          → col_V
  Notes           → col_W
  Ingested At     → col_X
  Enriched At     → col_Y
  Delivered At    → col_Z
```

---

### Node 6.3 — Log Run Entry

```
Node type: Google Sheets
Operation: Append
Sheet: Log

Columns:
  Run Date:       {{ $now.toFormat('yyyy-MM-dd HH:mm') }}
  SIRET:          {{ $json.siret }}
  Company:        {{ $json.company_name }}
  Grade:          {{ $json.grade }}
  NAF:            {{ $json.naf_code }}
  Status:         Written
```

---

## PHASE 7: WORKFLOW 7 — DAILY DIGEST EMAIL

**Workflow name:** `07 - Daily Digest Email`
**Trigger:** Cron — every day at 08:30 (after ingestion finishes)
**Purpose:** Send RollandAssurance a summary of new leads

---

### Node 7.1 — Read Today's Leads from Google Sheets

```
Node type: Google Sheets
Operation: Read Rows
Sheet: Leads
Filter: Ingested At contains today's date
```

---

### Node 7.2 — Build Digest Stats

```
Node type: Function
Code:

const today = new Date().toISOString().split('T')[0];
const allLeads = items.filter(i => (i.json['Ingested At'] || '').startsWith(today));

const gradeA = allLeads.filter(i => i.json.Grade === 'A').length;
const gradeB = allLeads.filter(i => i.json.Grade === 'B').length;
const gradeC = allLeads.filter(i => i.json.Grade === 'C').length;
const total = allLeads.length;

// Count by NAF group
const nafCounts = {};
allLeads.forEach(i => {
  const group = i.json['Trade Group'] || 'Autre';
  nafCounts[group] = (nafCounts[group] || 0) + 1;
});

const nafSummary = Object.entries(nafCounts)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 5)
  .map(([group, count]) => `• ${group}: ${count} leads`)
  .join('\n');

const hotLeads = allLeads.filter(i => i.json['Urgency Tier']?.includes('HOT')).length;

return [{
  json: {
    total, gradeA, gradeB, gradeC, hotLeads, nafSummary, date: today
  }
}];
```

---

### Node 7.3 — Send Email via Gmail/SMTP

```
Node type: Gmail (or Send Email)
To: [RollandAssurance email]
Subject: [Leads BTP] {{ $json.total }} nouveaux leads — {{ $json.date }}

Body (HTML):
<h2>Rapport quotidien — Leads Garantie Décennale</h2>
<p><strong>Date:</strong> {{ $json.date }}</p>

<h3>Résumé</h3>
<ul>
  <li>🔥 Leads chauds (0-14j): {{ $json.hotLeads }}</li>
  <li>✅ Grade A (appelables): {{ $json.gradeA }}</li>
  <li>⚠️ Grade B (partiels): {{ $json.gradeB }}</li>
  <li>❌ Grade C (incomplets): {{ $json.gradeC }}</li>
  <li><strong>Total: {{ $json.total }}</strong></li>
</ul>

<h3>Top corps de métier aujourd'hui</h3>
<pre>{{ $json.nafSummary }}</pre>

<p><a href="[GOOGLE_SHEET_LINK]">→ Voir tous les leads dans Google Sheets</a></p>
<p><em>Filtrez par colonne "Grade" = A pour voir les leads prioritaires.</em></p>
```

---

## PHASE 8: WORKFLOW 8 — ERROR HANDLING & MONITORING

**Workflow name:** `08 - Error Monitor`
**Purpose:** Catch failures across all workflows and alert

---

### Node 8.1 — Error Trigger

```
Node type: Error Trigger
(Attach this workflow as Error Workflow in n8n Settings)
```

---

### Node 8.2 — Format Error Alert

```
Node type: Set
Values:
  error_workflow: {{ $json.workflow.name }}
  error_node:     {{ $json.execution.lastNodeExecuted }}
  error_message:  {{ $json.execution.error.message }}
  error_time:     {{ $now.toISO() }}
```

---

### Node 8.3 — Send Telegram Alert (instant)

```
Node type: Telegram
Chat ID: [your telegram chat ID]
Text:
🚨 n8n Error Alert

Workflow: {{ $json.error_workflow }}
Node: {{ $json.error_node }}
Error: {{ $json.error_message }}
Time: {{ $json.error_time }}

→ Check: https://n8n.yourdomain.com
```

---

### Node 8.4 — Log Error to Google Sheets

```
Node type: Google Sheets
Operation: Append
Sheet: Log

Columns:
  Run Date:    {{ $now.toISO() }}
  SIRET:       ERROR
  Company:     {{ $json.error_workflow }}
  Grade:       —
  NAF:         —
  Status:      FAILED — {{ $json.error_message }}
```

---

## PHASE 9: COMPLETE WORKFLOW CONNECTIONS MAP

```
Workflow 01 (Cron 06:00)
  → INSEE Token
  → Build Query
  → SIRENE API (paginated)
  → Flatten Results
  → Split per lead
      ↓ (each lead)
Workflow 02 - NAF Classification
      ↓
Workflow 03 - Dedup Check
      ↓ (new only)
Workflow 04 - Enrichment
  → Pappers (gérant, website)
  → Dropcontact (email)
  → Lusha (phone)
      ↓
Workflow 05 - Quality Scoring
      ↓
Workflow 06 - Write Google Sheets
      ↓
Workflow 07 (Cron 08:30)
  → Read today's leads
  → Build digest
  → Send email to RollandAssurance

Workflow 08 (Error handler — always on)
  → Catches any failure in 01-07
  → Telegram alert + log entry
```

---

## PHASE 10: BUILD ORDER & MILESTONES

| Milestone | What to build | Test criteria |
|-----------|--------------|---------------|
| **M1** | VPS + n8n running | Can access https://n8n.yourdomain.com |
| **M2** | Google Sheet structure | All 26 columns correct, API access works |
| **M3** | INSEE token flow | Can get Bearer token, see it in n8n |
| **M4** | SIRENE single query | Returns raw JSON with companies |
| **M5** | NAF Classification | Input SIRET → output correct trade_name |
| **M6** | Dedup logic | Running twice doesn't create duplicate rows |
| **M7** | Pappers enrichment | Gérant name returned for a test SIREN |
| **M8** | Dropcontact email | Email returned for a test person |
| **M9** | Lusha phone | Phone returned for a test person |
| **M10** | Quality scoring | Grade A/B/C assigned correctly |
| **M11** | Full end-to-end | One lead goes from SIRENE to Google Sheet |
| **M12** | Daily digest email | Email arrives at 08:30 with correct stats |
| **M13** | Error monitoring | Kill a node → Telegram alert fires |
| **M14** | Backfill run | 90-day backfill completes without errors |
| **M15** | Production | Schedule live, running daily |

---

## PHASE 11: API CREDENTIALS REFERENCE

### INSEE SIRENE API
- Register: https://portail-api.insee.fr
- Get: Consumer Key + Consumer Secret
- Token endpoint: POST https://api.insee.fr/token
- Rate limit: 30 calls/minute, 500k calls/month (free)

### Pappers API
- Register: https://www.pappers.fr/api
- Get: API Token (in account settings)
- Free tier: 1,000 calls/month
- Paid: from €49/month for higher volume

### Dropcontact API
- Register: https://www.dropcontact.com
- Get: API Key
- Cost: ~€0.10 per enriched contact
- Note: GDPR compliant — critical for French market

### Lusha API
- Register: https://www.lusha.com/api/
- Get: API Key + credits
- Cost: credit-based, varies by plan
- Alternative: Apollo.io API (larger database, cheaper)

### Google Sheets
- Console: https://console.cloud.google.com
- Create Service Account → download JSON
- Enable: Google Sheets API + Google Drive API
- Share Sheet with service account email address

---

## PHASE 12: ESTIMATED COSTS (MONTHLY, AT SCALE)

| Item | Cost |
|------|------|
| Hetzner CX21 VPS | €5.77 |
| Pappers API (paid) | €49 if >1k companies/month |
| Dropcontact | ~€15 (150 emails/month at 30% hit rate) |
| Lusha | ~€20 (50 phones/month at 20% hit rate) |
| **Total estimate** | **~€90/month** |
| **Cost per Grade A lead** | **~€0.60–1.20** |

---

## NEXT STEP

Start with **Milestone M1** — provision the VPS and get n8n running.
Everything else is blocked on this. Once n8n is live, build M2 (Google Sheet) in parallel.
First working lead in Google Sheets is the M11 target.
