# Credentials & Accounts Preparation Guide
## RollandAssurance Lead Generation System

**Date:** 2026-04-15
**Complete this before building any workflow.**
**Estimated total setup time: 2–3 hours**

---

## CHECKLIST OVERVIEW

```
[ ] 1. Docker Desktop installed
[ ] 2. ngrok installed + authtoken configured
[ ] 3. INSEE SIRENE API — Consumer Key + Secret
[ ] 4. Pappers API — API Token
[ ] 5. Dropcontact — API Key
[ ] 6. Lusha — API Key
[ ] 7. Google Cloud — Service Account JSON
[ ] 8. Google Sheet created + shared with service account
[ ] 9. Gmail configured in n8n (for digest email)
[optional] 10. Telegram Bot + Chat ID (for error alerts)
```

---

## 1. DOCKER DESKTOP

**What it is:** Runs n8n and PostgreSQL as containers on your local machine.

**Steps:**
1. Go to docker.com/products/docker-desktop
2. Download for your OS (Mac/Windows/Linux)
3. Install and launch Docker Desktop
4. Wait for the whale icon in your taskbar to turn green (engine running)

**Verify installation:**
```bash
docker --version
# Expected: Docker version 25.x.x or higher

docker compose version
# Expected: Docker Compose version v2.x.x
```

**Create your project folder structure immediately after installing:**
```bash
mkdir -p ~/n8n-rolland/postgres_data
mkdir -p ~/n8n-rolland/n8n_data
```

These two folders are your permanent data store.
Containers are disposable — these folders are not.

**Save here:**
```
Docker Desktop: installed ✅ / not installed ❌
Project folder: ~/n8n-rolland/
postgres_data:  ~/n8n-rolland/postgres_data/   (PostgreSQL data)
n8n_data:       ~/n8n-rolland/n8n_data/         (n8n encryption key)
```

---

## 2. NGROK

**What it is:** Creates a public HTTPS tunnel to your localhost:5678.
Required so Dropcontact's async callback (and any future webhooks) can reach your local n8n.

**Steps:**
1. Go to ngrok.com → Sign up (free account)
2. After login → go to ngrok.com/dashboard/get-started/your-authtoken
3. Copy your authtoken (looks like: `2abc123...xyz_AbC...`)
4. Open terminal and run:
```bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

**How to start the tunnel (each session):**
```bash
ngrok http 5678
```

Output looks like:
```
Forwarding  https://abc123def456.ngrok-free.app -> http://localhost:5678
```

**Important:** Free ngrok gives a NEW URL every time you restart it.
After each restart → copy the new URL → update `WEBHOOK_URL` in docker-compose.yml → restart n8n.

**Save here:**
```
ngrok authtoken: _________________________________
ngrok dashboard: ngrok.com/dashboard
Note: URL changes on each restart — update docker-compose.yml each time
```

---

## 3. INSEE SIRENE API

**What it is:** Official French government API for the SIRENE company registry.
Free, unlimited (well, 500k calls/month). This is the core data source.

**Steps:**

1. Go to: **portail-api.insee.fr**
2. Click "S'inscrire" (Register)
3. Fill in registration form:
   - Email, password, name
   - Organization: your company name or personal
   - Use case: describe as "Research and lead generation for BTP sector"
4. Confirm email → log in
5. Go to "Mes applications" → "Créer une application"
6. Application name: `rolland-lead-gen`
7. Select API: **"Sirene V3"** (and also **"Sirene V3.11"** if available)
8. Submit → application is created
9. Go to your application → you will see:
   - **Consumer Key** (also called Client ID)
   - **Consumer Secret** (also called Client Secret)

**Build your Base64 auth string:**
You need this for the token request. Run in your browser console (F12 → Console):
```javascript
btoa("YOUR_CONSUMER_KEY:YOUR_CONSUMER_SECRET")
```
Copy the result — this is your Base64 string.

**Test the token endpoint:**
```bash
curl -X POST "https://api.insee.fr/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic YOUR_BASE64_STRING" \
  -d "grant_type=client_credentials"
```
Expected response:
```json
{ "access_token": "eyJ...", "token_type": "Bearer", "expires_in": 3600 }
```

**Rate limits:**
- 30 requests/minute
- 500,000 requests/month
- Free — no credit card needed

**Save here:**
```
Consumer Key:    _________________________________
Consumer Secret: _________________________________
Base64 string:   _________________________________
(base64 of "ConsumerKey:ConsumerSecret")

Registration URL: portail-api.insee.fr
Token URL: https://api.insee.fr/token
API base URL: https://api.insee.fr/entreprises/sirene/V3.11/
```

---

## 4. PAPPERS API

**What it is:** French company data API. Returns dirigeants (gérant name), capital,
effectif, website. Covers all French companies from official registry.
Free tier = 1,000 calls/month (enough for early validation).

**Steps:**

1. Go to: **pappers.fr/api**
2. Click "Obtenir une clé API" or go directly to pappers.fr/api/documentation
3. Create account: email + password
4. After login → go to your profile → API section
5. Your API token is displayed there (looks like: `abc123def456...`)

**Test the API:**
```bash
curl "https://api.pappers.fr/v2/entreprise?api_token=YOUR_TOKEN&siren=889297453&_fields=dirigeants,site_internet,effectif"
```
Expected: JSON with company details and dirigeants array.

**Free tier limits:**
- 1,000 API calls/month
- Resets on the 1st of each month
- Paid plans start at €49/month for 10,000 calls

**When you'll hit the limit:**
- If you process 33+ new companies per day → upgrade to paid
- During the 90-day backfill run → temporarily upgrade, then downgrade

**Save here:**
```
API Token:  _________________________________

Registration URL: pappers.fr/api
API base URL: https://api.pappers.fr/v2/
Free tier: 1,000 calls/month
```

---

## 5. DROPCONTACT

**What it is:** GDPR-compliant French email enrichment tool.
You give it a name + company → it returns a verified professional email.
French company = built for French market = high accuracy for BTP contacts.

**Steps:**

1. Go to: **dropcontact.com**
2. Click "Essai gratuit" (Free trial) or "S'inscrire"
3. Create account with your email
4. Free trial gives ~25 free enrichments to test with
5. After login → go to Settings → API
6. Your API Key is displayed (looks like: `DTCA...`)

**Add credits:**
- Go to Billing → Add credits
- No subscription needed — pay-as-you-go
- Recommended to start: €10 (≈100 contacts)
- Each enrichment costs ~€0.10

**How it works (async):**
1. POST your request → get a `request_id`
2. Wait 10–15 seconds
3. GET with the `request_id` → get the email result

**Test:**
```bash
# Step 1: Submit
curl -X POST "https://api.dropcontact.com/batch" \
  -H "X-Access-Token: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data":[{"first_name":"Jean","last_name":"Dupont","company":"Dupont Maçonnerie"}],"language":"fr"}'

# Returns: {"request_id": "abc123", "credits_used": 1, ...}

# Step 2: Retrieve (after 15 seconds)
curl "https://api.dropcontact.com/batch/abc123" \
  -H "X-Access-Token: YOUR_API_KEY"
```

**Save here:**
```
API Key:  _________________________________
Credits balance: _________________________
Pay-as-you-go: ~€0.10/contact

Registration URL: dropcontact.com
API base URL: https://api.dropcontact.com/
```

---

## 6. LUSHA (Phone Numbers)

**What it is:** B2B contact data platform with phone number lookup.
You give it a name + company → it returns a direct/mobile phone number.

**Option A — Lusha (recommended):**
1. Go to: **lusha.com**
2. Click "Get Started Free"
3. Create account (work email preferred)
4. Free plan gives 5 credits/month (for testing)
5. After login → go to Settings → API → Get API Key
6. Paid plan needed for volume: starts at ~$36/month for 480 credits/year

**Option B — Apollo.io (larger database, cheaper):**
1. Go to: **apollo.io**
2. Create free account
3. Free plan: 50 mobile credits/month
4. Paid: $49/month for 24,000 credits/year
5. Settings → Integrations → API Keys → Create API Key
6. API endpoint: `https://api.apollo.io/api/v1/people/match`

**Recommendation for validation phase:**
Start with **Apollo.io free plan** (50 credits/month, no credit card) to validate the pipeline works, then switch to Lusha or Apollo paid when you confirm enrichment rate is acceptable.

**Apollo test:**
```bash
curl -X POST "https://api.apollo.io/api/v1/people/match" \
  -H "Content-Type: application/json" \
  -H "Cache-Control: no-cache" \
  -d '{
    "api_key": "YOUR_API_KEY",
    "first_name": "Jean",
    "last_name": "Dupont",
    "organization_name": "Dupont Maçonnerie",
    "reveal_personal_emails": false,
    "reveal_phone_number": true
  }'
```

**Save here:**
```
Choice: [ ] Lusha  [ ] Apollo.io

Lusha API Key:  _________________________________
Lusha credits:  _________________________________

-- OR --

Apollo API Key: _________________________________
Apollo credits: _________________________________

API base URL (Apollo): https://api.apollo.io/api/v1/
```

---

## 7. GOOGLE CLOUD — SERVICE ACCOUNT

**What it is:** Allows n8n to read and write your Google Sheet automatically,
without needing your personal Google login. The service account is a "robot user"
that has access to the sheet.

**Steps:**

### 7a. Create Google Cloud Project

1. Go to: **console.cloud.google.com**
2. Top bar → click the project dropdown → "New Project"
3. Project name: `n8n-rolland-leadgen`
4. Click Create → wait ~30 seconds

### 7b. Enable Required APIs

5. In your new project → top search bar → search "Google Sheets API"
6. Click it → click "Enable"
7. Go back → search "Google Drive API"
8. Click it → click "Enable"

### 7c. Create Service Account

9. Left menu → IAM & Admin → Service Accounts
10. Click "+ Create Service Account"
11. Name: `n8n-sheets-writer`
12. Description: "n8n automation — reads and writes leads sheet"
13. Click "Create and Continue"
14. Role: Select "Editor" → click Continue → Done

### 7d. Download JSON Key

15. Click on the service account you just created
16. Go to "Keys" tab
17. "Add Key" → "Create New Key" → JSON → Create
18. A JSON file downloads automatically — **keep this file safe**
19. Open it — it looks like:
```json
{
  "type": "service_account",
  "project_id": "n8n-rolland-leadgen",
  "private_key_id": "abc123...",
  "private_key": "-----BEGIN RSA PRIVATE KEY-----\n...",
  "client_email": "n8n-sheets-writer@n8n-rolland-leadgen.iam.gserviceaccount.com",
  "client_id": "...",
  ...
}
```

20. **Copy the `client_email` value** — you will need it to share your Sheet

**Save here:**
```
Project ID:      _________________________________
Service Account Email: _________________________________
                 (looks like: n8n-xxx@project.iam.gserviceaccount.com)
JSON Key file path: _________________________________
                 (keep this file — do not lose it)
```

---

## 8. GOOGLE SHEET — CREATE & CONFIGURE

### 8a. Create the Sheet

1. Go to: **sheets.google.com**
2. Click "+" to create a new spreadsheet
3. Name it: `RollandAssurance — Leads BTP`
4. Add these 4 tabs (click "+" at the bottom for each):
   - `Leads`
   - `Log`
   - `NAF_Reference`
   - `Stats`

### 8b. Set Up Leads Tab Headers

Click on the `Leads` tab → Row 1 → type each header in order:

```
A1: SIRET
B1: SIREN
C1: Company Name
D1: NAF Code
E1: Trade Name
F1: Trade Group
G1: Décennale Required
H1: Creation Date
I1: Urgency Tier
J1: Days Since Registration
K1: Legal Form
L1: Address
M1: City
N1: Postal Code
O1: Region
P1: Gérant Name
Q1: Phone
R1: Email
S1: Website
T1: Quality Score
U1: Grade
V1: Status
W1: Notes
X1: Ingested At
Y1: Enriched At
Z1: Delivered At
```

### 8c. Set Up Log Tab Headers

Click `Log` tab → Row 1:
```
A1: Run Date
B1: SIRET
C1: Company Name
D1: Grade
E1: NAF Code
F1: Status
G1: Notes
```

### 8d. Share Sheet with Service Account

1. In your Google Sheet → click "Share" (top right)
2. In the "Add people" field → paste your service account email:
   `n8n-sheets-writer@n8n-rolland-leadgen.iam.gserviceaccount.com`
3. Set permission to "Editor"
4. Uncheck "Notify people"
5. Click "Share"

### 8e. Get the Sheet ID

From your browser URL when the sheet is open:
```
https://docs.google.com/spreadsheets/d/  THIS_PART_IS_THE_ID  /edit
```

**Save here:**
```
Spreadsheet name: RollandAssurance — Leads BTP
Spreadsheet ID:   _________________________________
                  (from the URL)
Sheet URL:        _________________________________
Tabs created:     [ ] Leads  [ ] Log  [ ] NAF_Reference  [ ] Stats
Shared with service account: [ ] Yes
```

---

## 9. GMAIL — DIGEST EMAIL SENDER

**What it is:** n8n will send daily digest emails to RollandAssurance using a Gmail account.
Use a dedicated Gmail account (not your main personal one) for cleanliness.

**Option A — New dedicated Gmail (recommended):**
1. Create new Gmail: `rolland.leadgen.bot@gmail.com` (or similar)
2. In n8n → Credentials → Gmail OAuth2
3. Follow n8n's OAuth2 setup (it will redirect you to Google to authorize)

**Option B — SMTP with any email provider:**
If you prefer not to use Gmail OAuth, use any SMTP provider:
- Gmail SMTP: smtp.gmail.com, port 587
- You'll need to enable "App Passwords" in your Google account
- Settings → Security → 2FA must be ON → then App Passwords → Generate

**For n8n Gmail OAuth2 setup:**
1. Go to console.cloud.google.com → same project
2. Enable "Gmail API"
3. OAuth Consent Screen → External → fill basic info
4. Credentials → Create Credentials → OAuth 2.0 Client ID
5. Application type: Web Application
6. Authorized redirect URIs: add `http://localhost:5678/rest/oauth2-credential/callback`
7. Download Client ID + Client Secret
8. In n8n → New Credential → Gmail OAuth2 → paste Client ID + Secret → Connect

**Save here:**
```
Gmail account used: _________________________________
Setup method: [ ] OAuth2  [ ] SMTP App Password

OAuth2 Client ID:     _________________________________  (if OAuth2)
OAuth2 Client Secret: _________________________________  (if OAuth2)

SMTP Password:        _________________________________  (if SMTP)
SMTP Host: smtp.gmail.com
SMTP Port: 587
```

---

## 10. TELEGRAM BOT (Optional — Highly Recommended)

**What it is:** Instant error alerts sent to your phone when any workflow fails.
Takes 5 minutes to set up and will save you hours of debugging blind.

**Steps:**

### Create the Bot:
1. Open Telegram → search for **@BotFather**
2. Send: `/newbot`
3. Give it a name: `RollandLeadBot`
4. Give it a username: `rolland_lead_bot` (must be unique, end in "bot")
5. BotFather sends you a **token** like: `7123456789:AAFhY...`

### Get your Chat ID:
1. Search for your new bot in Telegram → click it → click "Start"
2. Send any message to your bot (e.g. "hello")
3. Open in browser:
   `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. In the JSON response, find: `"chat":{"id": 123456789}`
5. That number is your Chat ID

**Test the bot:**
```bash
curl -X POST "https://api.telegram.org/botYOUR_TOKEN/sendMessage" \
  -d "chat_id=YOUR_CHAT_ID" \
  -d "text=n8n bot is online ✅"
```
You should receive the message on your phone.

**In n8n:**
- Credentials → New → Telegram API
- Token: paste your bot token

**Save here:**
```
Bot name:    _________________________________
Bot token:   _________________________________
Chat ID:     _________________________________
Test passed: [ ] Yes
```

---

## PUTTING IT ALL IN N8N — CREDENTIALS SETUP

Once n8n is running at localhost:5678, add all credentials:

Go to: `http://localhost:5678` → Settings (left sidebar) → Credentials → + Add Credential

| # | Credential Name in n8n | Type to select | Fields to fill |
|---|----------------------|----------------|----------------|
| 1 | `INSEE API Auth` | HTTP Header Auth | Header Name: `Authorization` / Header Value: `Basic YOUR_BASE64_STRING` |
| 2 | `Pappers API` | HTTP Query Auth | Name: `api_token` / Value: `your_pappers_token` |
| 3 | `Dropcontact API` | HTTP Header Auth | Header Name: `X-Access-Token` / Header Value: `your_dropcontact_key` |
| 4 | `Lusha API` or `Apollo API` | HTTP Header Auth | Header Name: `api_key` / Value: `your_key` |
| 5 | `Google Sheets` | Google Sheets API | Paste full JSON content of service account key file |
| 6 | `Gmail` | Gmail OAuth2 (or SMTP) | Follow OAuth2 flow or paste SMTP password |
| 7 | `Telegram Bot` | Telegram API | Token: your bot token |

**After adding each credential:** click "Test" to verify it works before saving.

---

## MASTER CREDENTIALS RECORD

Fill this in as you complete each section. Store this file securely (not in git).

```
=== INFRASTRUCTURE ===
Docker Desktop version:   _________________________________
ngrok authtoken:          _________________________________
ngrok current URL:        _________________________________  (changes each restart)

=== APIS ===
INSEE Consumer Key:       _________________________________
INSEE Consumer Secret:    _________________________________
INSEE Base64 Auth:        _________________________________

Pappers API Token:        _________________________________
Pappers calls used/month: _________________________________

Dropcontact API Key:      _________________________________
Dropcontact credits €:    _________________________________

Lusha/Apollo API Key:     _________________________________
Lusha/Apollo credits:     _________________________________

=== GOOGLE ===
GCP Project ID:           _________________________________
Service Account Email:    _________________________________
JSON Key file location:   _________________________________
Spreadsheet ID:           _________________________________
Spreadsheet URL:          _________________________________

=== NOTIFICATIONS ===
Gmail address:            _________________________________
Gmail OAuth Client ID:    _________________________________
Gmail OAuth Secret:       _________________________________
Telegram Bot Token:       _________________________________
Telegram Chat ID:         _________________________________

=== N8N ===
Local URL:                http://localhost:5678
ngrok URL:                _________________________________  (update each session)
Admin username:           _________________________________
Admin password:           _________________________________
```

---

## ESTIMATED COSTS DURING VALIDATION

| Item | Cost | Notes |
|------|------|-------|
| Docker Desktop | Free | |
| ngrok | Free | New URL each restart — fine for validation |
| INSEE SIRENE | Free | 500k calls/month |
| Pappers | Free | 1,000 calls/month (covers ~33 companies/day) |
| Dropcontact | ~€5–10 | Buy €10 credits for testing (~100 contacts) |
| Lusha / Apollo | Free trial | Apollo free = 50 phone credits/month |
| Google Cloud | Free | Service account + Sheets API = free |
| Gmail | Free | |
| Telegram | Free | |
| **TOTAL** | **~€10–15** | One-time for validation phase |

---

## COMPLETION CHECKLIST

Work through these in order — don't skip ahead:

```
[ ] Step 1:  Docker Desktop installed and running (green icon)
[ ] Step 2:  ngrok installed + authtoken added
[ ] Step 3:  INSEE account created + Consumer Key/Secret saved
[ ] Step 4:  Pappers account created + API Token saved
[ ] Step 5:  Dropcontact account created + API Key saved + €10 credits added
[ ] Step 6:  Lusha or Apollo account created + API Key saved
[ ] Step 7:  Google Cloud project created
[ ] Step 8:  Sheets API + Drive API enabled
[ ] Step 9:  Service Account created + JSON key downloaded
[ ] Step 10: Google Sheet created with all 4 tabs and headers in Leads + Log tabs
[ ] Step 11: Sheet shared with service account email
[ ] Step 12: Spreadsheet ID copied from URL
[ ] Step 13: Gmail account ready (new or existing)
[ ] Step 14: Telegram bot created + Chat ID found + test message received
[ ] Step 15: n8n running at localhost:5678 (via docker-compose up -d)
[ ] Step 16: All 7 credentials added in n8n and tested green
[ ] Step 17: Ready to build Workflow 1
```

**When all 17 boxes are checked → open the building blueprint and start M5.**
```
