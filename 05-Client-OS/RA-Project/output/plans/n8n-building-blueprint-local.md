# RollandAssurance — n8n Local Building Blueprint
## Localhost + ngrok + Docker — Validation Stack

**Stack:** n8n local · Docker Desktop · ngrok · Google Sheets · INSEE SIRENE · Pappers · Dropcontact · Lusha
**Date:** 2026-04-15
**Status:** Build-Ready (Local Validation Phase)

---

## WHY THIS ORDER

```
Localhost + ngrok + Docker
        ↓ (once validated end-to-end)
Hetzner VPS + Docker + Nginx + SSL
```

Local first = zero cost, fast iteration, safe to break things.
ngrok = gives n8n a public HTTPS URL so webhooks (Dropcontact async callback) work correctly.
Once the full pipeline runs clean locally, migrating to VPS is a 1-hour lift.

---

## PHASE 0: LOCAL INFRASTRUCTURE SETUP

### Step 0.1 — Install Prerequisites

**Docker Desktop:**
- Download from docker.com/products/docker-desktop
- Install for your OS (Mac/Windows/Linux)
- Verify: `docker --version` and `docker-compose --version`

**ngrok:**
- Download from ngrok.com/download
- Create free account at ngrok.com
- Get your authtoken from ngrok.com/dashboard → Auth
- Install authtoken:
```bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

---

### Step 0.2 — Create Local n8n Project Folder Structure

```bash
mkdir -p ~/n8n-rolland
cd ~/n8n-rolland
mkdir -p postgres_data
mkdir -p n8n_data
```

Your folder structure on disk:
```
~/n8n-rolland/
├── docker-compose.yml      ← config file
├── postgres_data/          ← all PostgreSQL data lives here (workflows, credentials, history)
└── n8n_data/               ← n8n encryption key + config lives here
```

**This is the key principle:** data lives in these two folders on YOUR machine.
Containers are disposable. Folders are permanent.
Delete a container → create a new one → point to same folders → everything is back instantly.

---

Create `docker-compose.yml` inside `~/n8n-rolland/`:

```yaml
version: "3.8"

services:

  postgres:
    image: postgres:15
    restart: unless-stopped
    environment:
      POSTGRES_USER: n8n
      POSTGRES_PASSWORD: n8n_local_password
      POSTGRES_DB: n8n
    volumes:
      - ./postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U n8n"]
      interval: 10s
      timeout: 5s
      retries: 5

  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      # Server
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - N8N_EDITOR_BASE_URL=http://localhost:5678
      - WEBHOOK_URL=https://YOUR_NGROK_URL   # update after ngrok starts
      # Database — PostgreSQL
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_PORT=5432
      - DB_POSTGRESDB_DATABASE=n8n
      - DB_POSTGRESDB_USER=n8n
      - DB_POSTGRESDB_PASSWORD=n8n_local_password
      # Timezone
      - GENERIC_TIMEZONE=Europe/Paris
      - TZ=Europe/Paris
      # Execution logs
      - EXECUTIONS_DATA_SAVE_ON_ERROR=all
      - EXECUTIONS_DATA_SAVE_ON_SUCCESS=last
      - EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=true
      - N8N_LOG_LEVEL=info
    volumes:
      - ./n8n_data:/home/node/.n8n
    depends_on:
      postgres:
        condition: service_healthy
```

**No `volumes:` block at the bottom — bind mounts only. Data is in your folders, not in Docker.**

---

**What each folder stores:**

| Local Folder | Mounted to container | Stores | If folder deleted |
|---|---|---|---|
| `./postgres_data/` | `/var/lib/postgresql/data` | All workflows, credentials, execution history, settings | Everything lost |
| `./n8n_data/` | `/home/node/.n8n` | n8n encryption key — required to decrypt stored credentials | Credentials unreadable even if DB intact |

**Both folders must exist before starting. If they don't exist, PostgreSQL will fail to start.**

---

**Daily commands:**

```bash
# Start everything
cd ~/n8n-rolland && docker-compose up -d

# Stop everything (data stays in folders — safe)
docker-compose down

# View logs
docker-compose logs -f n8n
docker-compose logs -f postgres

# Restart n8n only (e.g. after updating WEBHOOK_URL)
docker-compose restart n8n

# Nuclear reset — delete containers, keep your data folders intact
docker-compose down
docker-compose up -d
```

**If a container dies or gets corrupted:**
```bash
# Remove all containers
docker-compose down

# (Optional) Pull latest images
docker-compose pull

# Start fresh — points to same local folders, all data is back
docker-compose up -d
```

**Backup (run weekly — takes 10 seconds):**
```bash
cd ~/n8n-rolland

# Backup PostgreSQL — dump to a SQL file
docker-compose exec postgres pg_dump -U n8n n8n > backup-postgres-$(date +%Y%m%d).sql

# Backup n8n encryption key
cp -r ./n8n_data ./n8n_data_backup_$(date +%Y%m%d)

echo "Backup done ✅"
```

**Restore from backup:**
```bash
# Restore PostgreSQL
docker-compose exec -T postgres psql -U n8n n8n < backup-postgres-20260415.sql
```

---

### Step 0.3 — Start n8n

```bash
cd ~/n8n-rolland
docker-compose up -d

# Verify it's running:
docker-compose logs -f n8n
```

**n8n is now running at:** `http://localhost:5678`

Open browser → `http://localhost:5678` → create your admin account on first visit.

---

### Step 0.4 — Start ngrok Tunnel

Open a **new terminal** (keep Docker running):

```bash
ngrok http 5678
```

ngrok output will show something like:
```
Forwarding  https://abc123def456.ngrok-free.app -> http://localhost:5678
```

**Copy the HTTPS URL** — this is your public n8n address.

---

### Step 0.5 — Update WEBHOOK_URL in Docker Compose

Edit `docker-compose.yml` — replace `YOUR_NGROK_URL` with your actual ngrok URL:

```yaml
- WEBHOOK_URL=https://abc123def456.ngrok-free.app
```

Restart n8n to apply:
```bash
docker-compose down && docker-compose up -d
```

**Important:** ngrok free tier gives a new URL every time you restart it.
When ngrok restarts → update `WEBHOOK_URL` → restart n8n.
For validation this is fine. On VPS you get a fixed domain.

---

### Step 0.6 — Register All API Accounts

Get these before building workflows:

| Service | Registration URL | What you get | Cost |
|---------|-----------------|-------------|------|
| INSEE SIRENE | portail-api.insee.fr | Consumer Key + Consumer Secret | Free |
| Pappers | pappers.fr/api | API Token | Free (1k/month) |
| Dropcontact | dropcontact.com | API Key | Pay-as-you-go ~€0.10/contact |
| Lusha | lusha.com | API Key + credits | Credit-based |
| Google Cloud | console.cloud.google.com | Service Account JSON | Free |

**Do all registrations first. You will need the keys during workflow build.**

---

### Step 0.7 — Google Sheets Setup

**1. Create the Google Sheet**

Create a new Google Sheet named: `RollandAssurance — Leads BTP`

Add these 4 tabs:
- `Leads` — main database
- `Log` — ingestion run log
- `NAF_Reference` — code lookup
- `Stats` — dashboard

**2. Set up Leads tab headers (Row 1):**

```
A: SIRET
B: SIREN
C: Company Name
D: NAF Code
E: Trade Name
F: Trade Group
G: Décennale Required
H: Creation Date
I: Urgency Tier
J: Days Since Registration
K: Legal Form
L: Address
M: City
N: Postal Code
O: Region
P: Gérant Name
Q: Phone
R: Email
S: Website
T: Quality Score
U: Grade
V: Status
W: Notes
X: Ingested At
Y: Enriched At
Z: Delivered At
```

**3. Set up Log tab headers (Row 1):**
```
A: Run Date | B: SIRET | C: Company Name | D: Grade | E: NAF Code | F: Status | G: Notes
```

**4. Enable Google Sheets API:**
1. Go to console.cloud.google.com
2. New project → name it `n8n-rolland`
3. Enable APIs: search and enable both:
   - `Google Sheets API`
   - `Google Drive API`
4. Go to IAM & Admin → Service Accounts → Create Service Account
   - Name: `n8n-sheets`
   - Role: Editor
5. Click the service account → Keys tab → Add Key → JSON → Download
6. **Copy the service account email** (looks like `n8n-sheets@n8n-rolland.iam.gserviceaccount.com`)
7. Open your Google Sheet → Share → paste service account email → Editor access

**5. Add credential in n8n:**
- n8n → Settings → Credentials → Add Credential
- Type: Google Sheets API
- Authentication: Service Account
- Paste the full JSON content of the downloaded key file
- Test → Save

---

### Step 0.8 — Add All Credentials in n8n

Go to `http://localhost:5678` → Settings → Credentials → New

| Credential Name | Type | Fields |
|----------------|------|--------|
| `INSEE API` | HTTP Header Auth | Header: Authorization, Value: Basic [base64(key:secret)] — explained in Workflow 1 |
| `Pappers API` | HTTP Query Auth | Name: api_token, Value: your token |
| `Dropcontact API` | HTTP Header Auth | Header: X-Access-Token, Value: your key |
| `Lusha API` | HTTP Header Auth | Header: api_key, Value: your key |
| `Google Sheets` | Google Sheets API | Service Account JSON |
| `Gmail` (optional) | Gmail OAuth2 | For digest email |

---

## PHASE 1: WORKFLOW 1 — SIRENE DAILY INGESTION

**Workflow name:** `01 - SIRENE Daily Ingestion`
**Trigger:** Schedule (Cron) — 06:00 every day, Europe/Paris
**Purpose:** Pull all new BTP companies registered in France

**How to create in n8n:**
- Click `+ New Workflow`
- Name it `01 - SIRENE Daily Ingestion`
- Add nodes one by one as described below

---

### Node 1.1 — Schedule Trigger

```
Node type: Schedule Trigger
Settings:
  Trigger Interval: Custom (Cron)
  Cron Expression: 0 6 * * *
  Timezone: Europe/Paris

For local testing: change to "Every Minute" or "Every 5 Minutes"
to trigger immediately without waiting until 06:00
```

---

### Node 1.2 — Set Run Variables

```
Node type: Edit Fields (Set)
Mode: Manual Mapping

Add these fields:

Name: date_today
Type: String
Value: {{ $now.setZone('Europe/Paris').toFormat('yyyy-MM-dd') }}

Name: date_yesterday
Type: String
Value: {{ $now.setZone('Europe/Paris').minus({days: 1}).toFormat('yyyy-MM-dd') }}

Name: date_90days_ago
Type: String
Value: {{ $now.setZone('Europe/Paris').minus({days: 90}).toFormat('yyyy-MM-dd') }}

Name: is_backfill_run
Type: Boolean
Value: false
(Set to true ONLY when running the initial 90-day backfill)

Name: naf_codes_solr
Type: String
Value: (4110Z OR 4120A OR 4120B OR 4211Z OR 4212Z OR 4213A OR 4213B OR 4221Z OR 4222Z OR 4291Z OR 4299Z OR 4311Z OR 4312A OR 4312B OR 4313Z OR 4321A OR 4321B OR 4322A OR 4322B OR 4329A OR 4329B OR 4331Z OR 4332A OR 4332B OR 4332C OR 4333Z OR 4334Z OR 4339Z OR 4391A OR 4391B OR 4399A OR 4399B OR 4399C OR 4399D OR 4399E OR 7111Z OR 7112B)
```

---

### Node 1.3 — Get INSEE Bearer Token

INSEE uses OAuth2 client credentials. The token expires every 60 minutes.

**Preparation — Build your Base64 auth string:**
```
base64("YOUR_CONSUMER_KEY:YOUR_CONSUMER_SECRET")
```
Do this in browser console:
```javascript
btoa("your_consumer_key:your_consumer_secret")
```
Copy the result.

```
Node type: HTTP Request
Method: POST
URL: https://api.insee.fr/token

Authentication: None

Headers:
  Content-Type: application/x-www-form-urlencoded
  Authorization: Basic YOUR_BASE64_STRING_HERE

Body:
  Content Type: Form-URL-Encoded (x-www-form-urlencoded)
  Parameters:
    grant_type = client_credentials
```

Expected response:
```json
{
  "access_token": "eyJ...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

---

### Node 1.4 — Set Bearer Token Variable

```
Node type: Edit Fields (Set)
Mode: Manual Mapping

Name: insee_token
Type: String
Value: {{ $json.access_token }}
```

---

### Node 1.5 — Build SIRENE Query

```
Node type: Code (JavaScript)

const runVars = $('Set Run Variables').item.json;

const dateFrom = runVars.is_backfill_run
  ? runVars.date_90days_ago
  : runVars.date_yesterday;

const dateTo = runVars.date_today;

// Build Lucene query for SIRENE API
const query = [
  `activitePrincipaleEtablissement:${runVars.naf_codes_solr}`,
  `dateCreationEtablissement:[${dateFrom} TO ${dateTo}]`,
  `etatAdministratifEtablissement:A`
].join(' AND ');

return [{
  json: {
    ...runVars,
    insee_token: $('Set Bearer Token').item.json.insee_token,
    sirene_query: query,
    date_from: dateFrom,
    date_to: dateTo,
    current_page: 0,
    per_page: 1000
  }
}];
```

---

### Node 1.6 — SIRENE API First Call (Page 0)

```
Node type: HTTP Request
Method: GET
URL: https://api.insee.fr/entreprises/sirene/V3.11/siret

Authentication: None (we set header manually)

Headers:
  Authorization: Bearer {{ $('Set Bearer Token').item.json.insee_token }}
  Accept: application/json

Query Parameters (add each as separate param):
  q       = {{ $json.sirene_query }}
  nombre  = 1000
  debut   = 0
  champs  = siret,siren,denominationUniteLegale,nomUniteLegale,prenomUsuelUniteLegale,activitePrincipaleEtablissement,dateCreationEtablissement,categorieJuridiqueUniteLegale,codePostalEtablissement,libelleCommuneEtablissement,adresseEtablissement,trancheEffectifsUniteLegale

Options:
  Continue On Fail: true
  Response Format: JSON
```

Expected response structure:
```json
{
  "header": { "total": 847, "debut": 0, "nombre": 1000 },
  "etablissements": [ {...}, {...}, ... ]
}
```

---

### Node 1.7 — Check Total & Handle Pagination

```
Node type: Code (JavaScript)

const response = items[0].json;
const total = response.header?.total || 0;
const perPage = 1000;
const pages = Math.ceil(total / perPage);

// Store first page results
const firstPageResults = response.etablissements || [];

console.log(`SIRENE total results: ${total}, pages needed: ${pages}`);

if (pages <= 1) {
  // Single page — pass results directly
  return [{ json: {
    etablissements: firstPageResults,
    total,
    pages: 1,
    current_page: 0
  }}];
}

// Multiple pages — create one item per additional page
const pageItems = [];

// Page 0 already fetched, start from page 1
for (let i = 1; i < pages; i++) {
  pageItems.push({ json: {
    debut: i * perPage,
    page_number: i,
    total,
    pages,
    first_page_results: firstPageResults
  }});
}

return pageItems;
```

---

### Node 1.8 — Fetch Additional Pages (if total > 1000)

*Connect this only from the multi-page branch of Node 1.7*

```
Node type: HTTP Request
(Same configuration as Node 1.6)

Query Parameters:
  debut = {{ $json.debut }}
  (all others identical to Node 1.6)
```

---

### Node 1.9 — Merge All Pages

```
Node type: Code (JavaScript)

// Collect all etablissements from all responses
const allEtablissements = [];

for (const item of items) {
  const etabs = item.json.etablissements || item.json.first_page_results || [];
  allEtablissements.push(...etabs);
}

console.log(`Total companies to process: ${allEtablissements.length}`);

// Return one item per company for Split processing
return allEtablissements.map(e => ({ json: e }));
```

---

### Node 1.10 — Parse Raw SIRENE Record

```
Node type: Code (JavaScript)

const e = items[0].json;
const ul = e.uniteLegale || {};
const adresse = e.adresseEtablissement || {};

// Gérant name: available for individual companies (EI, EIRL)
const gerantFirst = ul.prenomUsuelUniteLegale || '';
const gerantLast = ul.nomUniteLegale || '';
const gerantName = [gerantFirst, gerantLast].filter(Boolean).join(' ') || null;

// Company name: société name OR individual name
const companyName = ul.denominationUniteLegale
  || `${gerantFirst} ${gerantLast}`.trim()
  || 'Nom inconnu';

// Full address
const addressParts = [
  adresse.numeroVoieEtablissement,
  adresse.indiceRepetitionEtablissement,
  adresse.typeVoieEtablissement,
  adresse.libelleVoieEtablissement
].filter(Boolean).join(' ');

// Postal code → region mapping (simplified)
const postalCode = adresse.codePostalEtablissement || '';
const deptCode = postalCode.substring(0, 2);
const DEPT_REGION = {
  '75': 'Île-de-France', '77': 'Île-de-France', '78': 'Île-de-France',
  '91': 'Île-de-France', '92': 'Île-de-France', '93': 'Île-de-France',
  '94': 'Île-de-France', '95': 'Île-de-France',
  '13': 'PACA', '83': 'PACA', '84': 'PACA', '04': 'PACA', '05': 'PACA', '06': 'PACA',
  '69': 'Auvergne-Rhône-Alpes', '01': 'Auvergne-Rhône-Alpes', '03': 'Auvergne-Rhône-Alpes',
  '63': 'Auvergne-Rhône-Alpes', '38': 'Auvergne-Rhône-Alpes', '73': 'Auvergne-Rhône-Alpes',
  '74': 'Auvergne-Rhône-Alpes', '07': 'Auvergne-Rhône-Alpes', '26': 'Auvergne-Rhône-Alpes',
  '42': 'Auvergne-Rhône-Alpes', '43': 'Auvergne-Rhône-Alpes', '15': 'Auvergne-Rhône-Alpes',
  '31': 'Occitanie', '34': 'Occitanie', '11': 'Occitanie', '66': 'Occitanie',
  '09': 'Occitanie', '12': 'Occitanie', '30': 'Occitanie', '32': 'Occitanie',
  '46': 'Occitanie', '48': 'Occitanie', '65': 'Occitanie', '81': 'Occitanie', '82': 'Occitanie',
  '33': 'Nouvelle-Aquitaine', '64': 'Nouvelle-Aquitaine', '40': 'Nouvelle-Aquitaine',
  '47': 'Nouvelle-Aquitaine', '24': 'Nouvelle-Aquitaine', '19': 'Nouvelle-Aquitaine',
  '87': 'Nouvelle-Aquitaine', '23': 'Nouvelle-Aquitaine', '79': 'Nouvelle-Aquitaine',
  '17': 'Nouvelle-Aquitaine', '16': 'Nouvelle-Aquitaine', '86': 'Nouvelle-Aquitaine',
  '44': 'Pays de la Loire', '85': 'Pays de la Loire', '49': 'Pays de la Loire',
  '72': 'Pays de la Loire', '53': 'Pays de la Loire',
  '35': 'Bretagne', '56': 'Bretagne', '22': 'Bretagne', '29': 'Bretagne',
  '14': 'Normandie', '76': 'Normandie', '27': 'Normandie', '61': 'Normandie', '50': 'Normandie',
  '59': 'Hauts-de-France', '62': 'Hauts-de-France', '02': 'Hauts-de-France',
  '60': 'Hauts-de-France', '80': 'Hauts-de-France',
  '67': 'Grand Est', '68': 'Grand Est', '57': 'Grand Est', '54': 'Grand Est',
  '88': 'Grand Est', '55': 'Grand Est', '52': 'Grand Est', '51': 'Grand Est', '08': 'Grand Est',
  '10': 'Grand Est', '89': 'Bourgogne-Franche-Comté', '21': 'Bourgogne-Franche-Comté',
  '71': 'Bourgogne-Franche-Comté', '58': 'Bourgogne-Franche-Comté',
  '39': 'Bourgogne-Franche-Comté', '25': 'Bourgogne-Franche-Comté',
  '70': 'Bourgogne-Franche-Comté', '90': 'Bourgogne-Franche-Comté',
  '45': 'Centre-Val de Loire', '28': 'Centre-Val de Loire', '37': 'Centre-Val de Loire',
  '41': 'Centre-Val de Loire', '36': 'Centre-Val de Loire', '18': 'Centre-Val de Loire',
};

const region = DEPT_REGION[deptCode] || `Dept. ${deptCode}`;

return [{
  json: {
    siret: e.siret,
    siren: e.siren,
    company_name: companyName,
    naf_code_raw: (e.activitePrincipaleEtablissement || '').replace('.', ''),
    creation_date: e.dateCreationEtablissement || '',
    legal_form_code: ul.categorieJuridiqueUniteLegale || '',
    address: addressParts,
    city: adresse.libelleCommuneEtablissement || '',
    postal_code: postalCode,
    region: region,
    gerant_name: gerantName,
    company_size_code: ul.trancheEffectifsUniteLegale || '',
    status: 'raw',
    ingested_at: new Date().toISOString()
  }
}];
```

---

### Node 1.11 — Loop: Split Into Batches of 1

```
Node type: Split In Batches
Batch Size: 1

This sends one company at a time into the next workflow.
```

---

## PHASE 2: WORKFLOW 2 — NAF CLASSIFICATION ENGINE

**Workflow name:** `02 - NAF Classification`
**Trigger:** Called inline by Workflow 1 (connect node output directly)
**In n8n local:** Keep it as one continuous workflow — don't split into separate workflows until you move to VPS. Connect nodes directly.

---

### Node 2.1 — NAF Lookup + Urgency Scoring

```
Node type: Code (JavaScript)

const NAF_TABLE = {
  '4110Z': { trade_name: 'Promotion immobilière',               trade_group: 'Promotion',       decennale: 'Yes' },
  '4120A': { trade_name: 'Construction maisons individuelles',  trade_group: 'Gros Œuvre',      decennale: 'Yes' },
  '4120B': { trade_name: 'Construction autres bâtiments',       trade_group: 'Gros Œuvre',      decennale: 'Yes' },
  '4211Z': { trade_name: 'Construction routes et autoroutes',   trade_group: 'Génie Civil',     decennale: 'Yes' },
  '4212Z': { trade_name: 'Construction voies ferrées',          trade_group: 'Génie Civil',     decennale: 'Yes' },
  '4213A': { trade_name: "Ouvrages d'art béton",               trade_group: 'Génie Civil',     decennale: 'Yes' },
  '4213B': { trade_name: 'Construction tunnels',                trade_group: 'Génie Civil',     decennale: 'Yes' },
  '4221Z': { trade_name: 'Réseaux fluides',                    trade_group: 'Réseaux',         decennale: 'Yes' },
  '4222Z': { trade_name: 'Réseaux électriques/télécoms',       trade_group: 'Réseaux',         decennale: 'Yes' },
  '4291Z': { trade_name: 'Ouvrages maritimes/fluviaux',         trade_group: 'Génie Civil',     decennale: 'Yes' },
  '4299Z': { trade_name: 'Autres ouvrages génie civil',         trade_group: 'Génie Civil',     decennale: 'Yes' },
  '4311Z': { trade_name: 'Travaux de démolition',              trade_group: 'Démolition',      decennale: 'Yes' },
  '4312A': { trade_name: 'Terrassement courant',               trade_group: 'Terrassement',    decennale: 'Yes' },
  '4312B': { trade_name: 'Terrassement spécialisé',            trade_group: 'Terrassement',    decennale: 'Yes' },
  '4313Z': { trade_name: 'Forages et sondages',                trade_group: 'Spécialisé',      decennale: 'Yes' },
  '4321A': { trade_name: 'Électricité tous locaux',            trade_group: 'Électricité',     decennale: 'Yes' },
  '4321B': { trade_name: 'Électricité voie publique',          trade_group: 'Électricité',     decennale: 'Yes' },
  '4322A': { trade_name: 'Plomberie eau et gaz',               trade_group: 'Plomberie',       decennale: 'Yes' },
  '4322B': { trade_name: 'Thermique et climatisation',         trade_group: 'CVC',             decennale: 'Yes' },
  '4329A': { trade_name: "Travaux d'isolation",                trade_group: 'Isolation',       decennale: 'Yes' },
  '4329B': { trade_name: "Autres installations",               trade_group: 'Spécialisé',      decennale: 'Yes' },
  '4331Z': { trade_name: 'Plâtrerie',                          trade_group: 'Second Œuvre',    decennale: 'Yes' },
  '4332A': { trade_name: 'Menuiserie bois et PVC',             trade_group: 'Menuiserie',      decennale: 'Yes' },
  '4332B': { trade_name: 'Menuiserie métallique / serrurerie', trade_group: 'Menuiserie',      decennale: 'Yes' },
  '4332C': { trade_name: 'Agencement lieux de vente',          trade_group: 'Agencement',      decennale: 'Yes' },
  '4333Z': { trade_name: 'Revêtement sols et murs',            trade_group: 'Second Œuvre',    decennale: 'Yes' },
  '4334Z': { trade_name: 'Peinture et vitrerie',               trade_group: 'Second Œuvre',    decennale: 'Yes' },
  '4339Z': { trade_name: 'Autres finitions',                   trade_group: 'Second Œuvre',    decennale: 'Yes' },
  '4391A': { trade_name: 'Charpente',                          trade_group: 'Charpente',       decennale: 'Yes' },
  '4391B': { trade_name: 'Couverture',                         trade_group: 'Couverture',      decennale: 'Yes' },
  '4399A': { trade_name: 'Étanchéité',                         trade_group: 'Étanchéité',      decennale: 'Yes' },
  '4399B': { trade_name: 'Structures métalliques',             trade_group: 'Métal',           decennale: 'Yes' },
  '4399C': { trade_name: 'Maçonnerie générale / gros œuvre',   trade_group: 'Gros Œuvre',      decennale: 'Yes' },
  '4399D': { trade_name: 'Autres travaux spécialisés',         trade_group: 'Spécialisé',      decennale: 'Yes' },
  '4399E': { trade_name: 'Location engins BTP avec opérateur', trade_group: 'Location',        decennale: 'Partial' },
  '7111Z': { trade_name: "Architecture",                       trade_group: "Bureau d'études", decennale: 'Partial' },
  '7112B': { trade_name: 'Ingénierie / études techniques',     trade_group: "Bureau d'études", decennale: 'Partial' },
};

const LEGAL_FORM_MAP = {
  '1000': 'EI — Entrepreneur individuel',
  '1100': 'EI — Artisan',
  '1200': 'EI — Commerçant',
  '5215': 'EURL',
  '5410': 'SARL',
  '5499': 'SARL',
  '5499': 'SARL unipersonnelle',
  '6541': 'SASU',
  '6540': 'SAS',
  '5720': 'SA',
  '5210': 'SNC',
  '5310': 'SC',
};

const lead = items[0].json;
const nafRaw = (lead.naf_code_raw || '').replace('.', '').toUpperCase();
const nafInfo = NAF_TABLE[nafRaw] || {
  trade_name: 'Non classifié',
  trade_group: 'Autre',
  decennale: 'Unknown'
};

// Urgency calculation
const creationDate = new Date(lead.creation_date);
const today = new Date();
const daysSince = isNaN(creationDate)
  ? 999
  : Math.floor((today - creationDate) / (1000 * 60 * 60 * 24));

let urgencyTier;
if (daysSince <= 14)      urgencyTier = '🔴 HOT (0-14j)';
else if (daysSince <= 45) urgencyTier = '🟠 WARM (15-45j)';
else if (daysSince <= 90) urgencyTier = '🟡 LUKEWARM (46-90j)';
else                       urgencyTier = '⛔ COLD (90j+)';

// Format NAF with dot for display: 4120A → 41.20A
const nafDisplay = nafRaw.length >= 5
  ? nafRaw.slice(0, 2) + '.' + nafRaw.slice(2)
  : nafRaw;

return [{
  json: {
    ...lead,
    naf_code: nafDisplay,
    trade_name: nafInfo.trade_name,
    trade_group: nafInfo.trade_group,
    decennale_required: nafInfo.decennale,
    legal_form: LEGAL_FORM_MAP[lead.legal_form_code] || `Code ${lead.legal_form_code}`,
    days_since_registration: daysSince,
    urgency_tier: urgencyTier,
  }
}];
```

---

## PHASE 3: DEDUPLICATION CHECK

### Node 3.1 — Read SIRET Column from Google Sheets

```
Node type: Google Sheets
Operation: Read Rows
Document: RollandAssurance — Leads BTP
Sheet: Leads
Range: A2:A
(Only read column A — SIRET — fast and efficient)

Options:
  First Row Is Header: false
  Return All Rows: true
```

---

### Node 3.2 — Check for Duplicate SIRET

```
Node type: Code (JavaScript)

const incomingLead = $('NAF Classification').item.json;
const sheetRows = items;

// Extract all existing SIRETs from column A
const existingSirets = new Set(
  sheetRows
    .map(i => String(i.json.col_A || i.json.A || Object.values(i.json)[0] || '').trim())
    .filter(s => s.length > 0)
);

const isDuplicate = existingSirets.has(String(incomingLead.siret).trim());

if (isDuplicate) {
  console.log(`SKIP duplicate SIRET: ${incomingLead.siret} — ${incomingLead.company_name}`);
}

return [{
  json: {
    ...incomingLead,
    is_duplicate: isDuplicate
  }
}];
```

---

### Node 3.3 — IF: Route New vs Duplicate

```
Node type: IF
Condition:
  Value 1: {{ $json.is_duplicate }}
  Operation: is equal to
  Value 2: true (Boolean)

TRUE branch  → NoOp (end, skip this lead)
FALSE branch → Continue to enrichment
```

---

## PHASE 4: CONTACT ENRICHMENT PIPELINE

---

### Node 4.1 — Pappers API Call

```
Node type: HTTP Request
Method: GET
URL: https://api.pappers.fr/v2/entreprise

Query Parameters:
  api_token = {{ $credentials.PappersAPI.value }}
  siren      = {{ $json.siren }}
  _fields    = dirigeants,effectif,site_internet,capital

Options:
  Continue On Fail: true
  Timeout: 10000 (10 seconds)
```

---

### Node 4.2 — Extract Pappers Data

```
Node type: Code (JavaScript)

const lead = $('IF Dedup').item.json;  // adjust node name as needed
const pappers = items[0].json;

let gerantName = lead.gerant_name;
let website = lead.website || null;
let effectif = null;

// Extract primary dirigeant
if (pappers.dirigeants && pappers.dirigeants.length > 0) {
  const d = pappers.dirigeants.find(d => d.qualite && d.qualite.toLowerCase().includes('gérant'))
    || pappers.dirigeants[0];
  const fname = (d.prenom || '').trim();
  const lname = (d.nom || '').trim();
  if (fname || lname) {
    gerantName = `${fname} ${lname}`.trim();
  }
}

if (pappers.site_internet && pappers.site_internet.length > 3) {
  website = pappers.site_internet.startsWith('http')
    ? pappers.site_internet
    : `https://${pappers.site_internet}`;
}

if (pappers.effectif) effectif = pappers.effectif;

return [{
  json: {
    ...lead,
    gerant_name: gerantName,
    website: website,
    company_size: effectif,
    pappers_ok: true
  }
}];
```

---

### Node 4.3 — IF: Has Name for Email Search?

```
Node type: IF
Condition:
  {{ $json.gerant_name }} is not empty

TRUE  → Dropcontact call
FALSE → Skip to quality scoring (no name = no email possible)
```

---

### Node 4.4 — Parse Gérant First/Last Name

```
Node type: Code (JavaScript)

const lead = items[0].json;
const fullName = (lead.gerant_name || '').trim();
const parts = fullName.split(' ');
const firstName = parts[0] || '';
const lastName = parts.slice(1).join(' ') || '';

return [{
  json: {
    ...lead,
    gerant_first_name: firstName,
    gerant_last_name: lastName
  }
}];
```

---

### Node 4.5 — Dropcontact API Call

```
Node type: HTTP Request
Method: POST
URL: https://api.dropcontact.com/batch

Headers:
  X-Access-Token: {{ $credentials.DropcontactAPI.value }}
  Content-Type: application/json

Body (JSON — Raw):
{
  "data": [
    {
      "first_name": "{{ $json.gerant_first_name }}",
      "last_name": "{{ $json.gerant_last_name }}",
      "company": "{{ $json.company_name }}",
      "website": "{{ $json.website || '' }}"
    }
  ],
  "siren": true,
  "language": "fr"
}

Options:
  Continue On Fail: true
```

Response contains `request_id` — Dropcontact is async.

---

### Node 4.6 — Wait 15 Seconds

```
Node type: Wait
Resume: After Time Interval
Amount: 15
Unit: Seconds
```

---

### Node 4.7 — Poll Dropcontact Result

```
Node type: HTTP Request
Method: GET
URL: https://api.dropcontact.com/batch/{{ $('Dropcontact Call').item.json.request_id }}

Headers:
  X-Access-Token: {{ $credentials.DropcontactAPI.value }}

Options:
  Continue On Fail: true
```

---

### Node 4.8 — Extract Email

```
Node type: Code (JavaScript)

const lead = $('Parse Gérant Name').item.json;
const dc = items[0].json;

let email = null;
let emailConfidence = null;

try {
  if (dc.data && dc.data[0] && dc.data[0].email && dc.data[0].email.length > 0) {
    const emails = dc.data[0].email;
    // Sort by qualification score descending
    const best = emails.sort((a, b) => (b.qualification || 0) - (a.qualification || 0))[0];
    email = best.email || null;
    emailConfidence = best.qualification || null;
  }
} catch(e) {
  console.log('Dropcontact parse error:', e.message);
}

return [{
  json: {
    ...lead,
    email: email,
    email_confidence: emailConfidence,
    dropcontact_ok: !!email
  }
}];
```

---

### Node 4.9 — Lusha API Call (Phone Number)

```
Node type: HTTP Request
Method: GET
URL: https://api.lusha.com/person

Headers:
  api_key: {{ $credentials.LushaAPI.value }}

Query Parameters:
  firstName = {{ $json.gerant_first_name }}
  lastName  = {{ $json.gerant_last_name }}
  company   = {{ $json.company_name }}

Options:
  Continue On Fail: true
  Timeout: 8000
```

---

### Node 4.10 — Extract Phone

```
Node type: Code (JavaScript)

const lead = $('Extract Email').item.json;
const lusha = items[0].json;

let phone = null;

try {
  if (lusha.data && lusha.data.phoneNumbers && lusha.data.phoneNumbers.length > 0) {
    const phones = lusha.data.phoneNumbers;
    const mobile = phones.find(p => p.type === 'mobile' || p.type === 'direct');
    phone = mobile
      ? (mobile.localizedNumber || mobile.internationalNumber)
      : (phones[0].localizedNumber || phones[0].internationalNumber);
  }
} catch(e) {
  console.log('Lusha parse error:', e.message);
}

return [{
  json: {
    ...lead,
    phone: phone,
    lusha_ok: !!phone,
    enriched_at: new Date().toISOString()
  }
}];
```

---

## PHASE 5: QUALITY SCORING

### Node 5.1 — Calculate Score & Grade

```
Node type: Code (JavaScript)

const lead = items[0].json;
let score = 0;

if (lead.gerant_name && lead.gerant_name.trim().length > 2)      score += 5; // name
if (lead.phone && lead.phone.toString().trim().length > 6)        score += 5; // phone
if (lead.email && lead.email.includes('@'))                       score += 5; // email
if (lead.website && lead.website.includes('.'))                   score += 3; // website
if (lead.address && lead.city && lead.postal_code)               score += 2; // full address

const grade = score >= 15 ? 'A' : score >= 8 ? 'B' : 'C';

console.log(`${lead.company_name} | Score: ${score} | Grade: ${grade} | NAF: ${lead.naf_code}`);

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

## PHASE 6: WRITE TO GOOGLE SHEETS

### Node 6.1 — Append Row

```
Node type: Google Sheets
Operation: Append or Update Row
Document: RollandAssurance — Leads BTP
Sheet: Leads

Column Mappings (map each field):
  SIRET                   → {{ $json.siret }}
  SIREN                   → {{ $json.siren }}
  Company Name            → {{ $json.company_name }}
  NAF Code                → {{ $json.naf_code }}
  Trade Name              → {{ $json.trade_name }}
  Trade Group             → {{ $json.trade_group }}
  Décennale Required      → {{ $json.decennale_required }}
  Creation Date           → {{ $json.creation_date }}
  Urgency Tier            → {{ $json.urgency_tier }}
  Days Since Registration → {{ $json.days_since_registration }}
  Legal Form              → {{ $json.legal_form }}
  Address                 → {{ $json.address }}
  City                    → {{ $json.city }}
  Postal Code             → {{ $json.postal_code }}
  Region                  → {{ $json.region }}
  Gérant Name             → {{ $json.gerant_name }}
  Phone                   → {{ $json.phone }}
  Email                   → {{ $json.email }}
  Website                 → {{ $json.website }}
  Quality Score           → {{ $json.quality_score }}
  Grade                   → {{ $json.grade }}
  Status                  → Nouveau
  Notes                   → (leave empty)
  Ingested At             → {{ $json.ingested_at }}
  Enriched At             → {{ $json.enriched_at }}
  Delivered At            → (leave empty)

Options:
  Value Input Option: USER_ENTERED
```

---

### Node 6.2 — Append to Log Tab

```
Node type: Google Sheets
Operation: Append
Sheet: Log

Columns:
  Run Date     → {{ $now.toISO() }}
  SIRET        → {{ $json.siret }}
  Company Name → {{ $json.company_name }}
  Grade        → {{ $json.grade }}
  NAF Code     → {{ $json.naf_code }}
  Status       → OK — Written to Leads
  Notes        → Score: {{ $json.quality_score }}
```

---

## PHASE 7: DAILY DIGEST EMAIL

**Workflow name:** `07 - Daily Digest Email`
**Separate workflow with its own cron trigger**
**Trigger:** 08:30 every day (after ingestion finishes at ~07:30)

---

### Node 7.1 — Schedule Trigger

```
Cron: 30 8 * * *
Timezone: Europe/Paris
```

---

### Node 7.2 — Read Today's Leads

```
Node type: Google Sheets
Operation: Read Rows
Sheet: Leads

Get all rows — we filter by date in the next node.
```

---

### Node 7.3 — Build Digest Stats

```
Node type: Code (JavaScript)

const today = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
const allRows = items;

// Filter rows ingested today
const todayLeads = allRows.filter(i => {
  const ingestedAt = i.json['Ingested At'] || i.json.ingested_at || '';
  return ingestedAt.startsWith(today);
});

const gradeA = todayLeads.filter(i => (i.json.Grade || i.json.grade) === 'A').length;
const gradeB = todayLeads.filter(i => (i.json.Grade || i.json.grade) === 'B').length;
const gradeC = todayLeads.filter(i => (i.json.Grade || i.json.grade) === 'C').length;
const hot = todayLeads.filter(i => (i.json['Urgency Tier'] || '').includes('HOT')).length;
const total = todayLeads.length;

// Top trade groups
const groups = {};
todayLeads.forEach(i => {
  const g = i.json['Trade Group'] || i.json.trade_group || 'Autre';
  groups[g] = (groups[g] || 0) + 1;
});
const topGroups = Object.entries(groups)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 5)
  .map(([g, c]) => `• ${g}: ${c}`)
  .join('\n');

return [{
  json: { today, total, gradeA, gradeB, gradeC, hot, topGroups }
}];
```

---

### Node 7.4 — Send Email

```
Node type: Gmail
Operation: Send
To: contact@rollandassurance.fr
Subject: [Leads BTP] {{ $json.total }} nouveaux leads — {{ $json.today }}

Message Type: HTML
Message:
<h2 style="color:#1a1a2e">Rapport quotidien — Leads Garantie Décennale</h2>
<p><b>Date:</b> {{ $json.today }}</p>

<h3>Résumé du jour</h3>
<table style="border-collapse:collapse;width:300px">
  <tr><td>🔥 Leads chauds (0–14j)</td><td><b>{{ $json.hot }}</b></td></tr>
  <tr><td>✅ Grade A — appelables</td><td><b>{{ $json.gradeA }}</b></td></tr>
  <tr><td>⚠️ Grade B — partiels</td><td><b>{{ $json.gradeB }}</b></td></tr>
  <tr><td>❌ Grade C — incomplets</td><td><b>{{ $json.gradeC }}</b></td></tr>
  <tr style="border-top:2px solid #ccc"><td><b>Total</b></td><td><b>{{ $json.total }}</b></td></tr>
</table>

<h3>Top corps de métier aujourd'hui</h3>
<pre>{{ $json.topGroups }}</pre>

<p>
  <a href="YOUR_GOOGLE_SHEET_URL" style="background:#1a73e8;color:white;padding:10px 20px;text-decoration:none;border-radius:4px">
    Voir tous les leads →
  </a>
</p>

<p style="color:#888;font-size:12px">
  Filtrez la colonne "Grade" = A pour voir les leads prioritaires.<br>
  Marquez chaque lead "Contacté" dans la colonne Statut après appel.
</p>
```

---

## PHASE 8: ERROR HANDLING

### Setup Global Error Workflow

1. Create new workflow: `08 - Error Monitor`
2. In n8n Settings → Workflows → Error Workflow → select `08 - Error Monitor`
3. This workflow fires automatically when any other workflow fails

---

### Node 8.1 — Error Trigger

```
Node type: Error Trigger
(No configuration needed — receives error data automatically)
```

---

### Node 8.2 — Send Telegram Alert

```
Node type: Telegram
(Set up Bot via @BotFather on Telegram, get bot token + your chat ID)

Chat ID: {{ $credentials.TelegramAPI.chatId }}
Text:
🚨 *n8n Error*

*Workflow:* {{ $json.workflow.name }}
*Node:* {{ $json.execution.lastNodeExecuted }}
*Error:* {{ $json.execution.error.message }}
*Time:* {{ $now.toISO() }}

→ Check: http://localhost:5678
```

---

### Node 8.3 — Log Error to Google Sheets

```
Node type: Google Sheets
Operation: Append
Sheet: Log

Columns:
  Run Date     → {{ $now.toISO() }}
  SIRET        → ERROR
  Company Name → {{ $json.workflow.name }}
  Grade        → —
  NAF Code     → —
  Status       → FAILED
  Notes        → {{ $json.execution.error.message }}
```

---

## COMPLETE LOCAL WORKFLOW DIAGRAM

```
[Schedule 06:00]
      │
      ▼
[Get INSEE Token]
      │
      ▼
[Set Run Variables]
      │
      ▼
[Build SIRENE Query]
      │
      ▼
[SIRENE API Call (Page 0)]
      │
      ▼
[Handle Pagination] ──→ [Fetch More Pages] ─┐
      │                                      │
      └──────────────────────────────────────┘
      │
      ▼
[Merge & Flatten All Results]
      │
      ▼
[Parse Raw Record]
      │
      ▼
[Split In Batches: 1]  ←──────────────────┐
      │                                    │ (loops)
      ▼                                    │
[NAF Classification + Urgency]             │
      │                                    │
      ▼                                    │
[Read Sheets SIRET Column]                 │
      │                                    │
      ▼                                    │
[Duplicate Check]                          │
      │                                    │
   ┌──┴──┐                                 │
   │     │                                 │
DUPL   NEW                                 │
   │     │                                 │
  END    ▼                                 │
      [Pappers API] → [Extract Gérant]     │
              │                            │
              ▼                            │
      [Has Name?]                          │
      ┌───┴───┐                            │
     NO      YES                           │
      │       │                            │
      │    [Parse Name]                    │
      │       │                            │
      │    [Dropcontact POST]              │
      │       │                            │
      │    [Wait 15s]                      │
      │       │                            │
      │    [Poll Result]                   │
      │       │                            │
      │    [Extract Email]                 │
      │       │                            │
      └───────┤                            │
              │                            │
              ▼                            │
      [Lusha Phone Lookup]                 │
              │                            │
              ▼                            │
      [Extract Phone]                      │
              │                            │
              ▼                            │
      [Quality Score + Grade]              │
              │                            │
              ▼                            │
      [Append to Google Sheets]            │
              │                            │
              ▼                            │
      [Log Entry]                          │
              │                            │
              └────────────────────────────┘
                    (next lead in batch)

[Schedule 08:30] → [Read Leads] → [Build Stats] → [Send Email]
[Error Trigger]  → [Telegram Alert] → [Log Error]
```

---

## BUILD MILESTONES (LOCAL)

| # | Milestone | What to build | How to test |
|---|-----------|--------------|-------------|
| M1 | Docker running | `docker-compose up -d` | Open localhost:5678 |
| M2 | ngrok tunnel | `ngrok http 5678` | Access via ngrok URL |
| M3 | Google Sheet ready | Create all tabs + headers | Manually add 1 test row |
| M4 | Google Sheets credential | Service account JSON in n8n | Test connection succeeds |
| M5 | INSEE token works | Run Node 1.3 manually | See access_token in output |
| M6 | SIRENE query works | Run Nodes 1.4–1.6 | See companies in output |
| M7 | NAF classification | Run Node 2.1 on test record | See trade_name, urgency |
| M8 | Dedup works | Run workflow twice | Second run adds 0 rows |
| M9 | Pappers enrichment | Run Node 4.1 with a test SIREN | See gérant name returned |
| M10 | Dropcontact works | Run Nodes 4.5–4.8 | See email returned |
| M11 | Lusha works | Run Nodes 4.9–4.10 | See phone returned |
| M12 | Quality scoring | Run Node 5.1 | See Grade A/B/C |
| M13 | Full end-to-end | Trigger full workflow | 1 lead appears in Sheet |
| M14 | Digest email | Trigger Workflow 07 | Email arrives in inbox |
| M15 | Error monitor | Deliberately break a node | Telegram alert fires |
| M16 | Backfill run | Set is_backfill_run = true | 90 days of leads imported |
| M17 | 3-day live test | Let it run Mon–Wed | Leads flowing daily |

---

## LOCAL TESTING TIPS

**Test single nodes without running the full workflow:**
- Click any node → Execute Node → inspect output
- This is the fastest way to debug API calls

**Simulate a company record for testing:**
In any Code node, hardcode a test lead:
```javascript
return [{
  json: {
    siret: "89234567800012",
    siren: "892345678",
    company_name: "DUPONT MAÇONNERIE",
    naf_code_raw: "4399C",
    creation_date: "2026-04-10",
    legal_form_code: "1000",
    address: "12 Rue des Bâtisseurs",
    city: "Lyon",
    postal_code: "69001",
    gerant_name: "Jean Dupont"
  }
}];
```

**ngrok free tier limits:**
- 1 tunnel at a time
- New URL every restart
- 40 connections/minute (enough for this)
- Upgrade to ngrok paid ($8/month) if you want a fixed URL during validation

**Data persistence:**
Your n8n workflows are saved in `./n8n_data` — this persists across `docker-compose down/up`.
Don't delete this folder. Back it up before any experiments.

---

## MIGRATION TO VPS (WHEN READY)

When local validation passes M17:

1. Provision Hetzner CX21 (5 min)
2. Copy `docker-compose.yml` to VPS, add Nginx + PostgreSQL (see VPS blueprint)
3. Import all workflows from n8n: Settings → Import (JSON export)
4. Update `WEBHOOK_URL` to your domain
5. Update Google Sheet service account credentials if needed
6. Switch cron triggers back on
7. Done — same logic, same code, just different host

---

## CREDENTIAL CHECKLIST

Before starting M5, have these ready:

- [ ] INSEE Consumer Key + Secret (portail-api.insee.fr)
- [ ] Pappers API Token (pappers.fr/api)
- [ ] Dropcontact API Key (dropcontact.com)
- [ ] Lusha API Key (lusha.com)
- [ ] Google Service Account JSON (console.cloud.google.com)
- [ ] Google Sheet ID (from the URL: docs.google.com/spreadsheets/d/**SHEET_ID**/edit)
- [ ] Gmail account for digest (or SMTP credentials)
- [ ] Telegram Bot Token + Chat ID (optional but recommended for M15)
