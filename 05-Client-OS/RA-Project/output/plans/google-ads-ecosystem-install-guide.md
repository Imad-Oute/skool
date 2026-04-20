## GOOGLE ADS LEAD GENERATION ECOSYSTEM — FULL INSTALLATION & CONFIGURATION GUIDE
**Project:** RA-Project | **Date:** April 20, 2026
**Stack:** Custom-coded website | Oggo Data CRM (configured separately) | No CallRail

---

## BEFORE YOU START — MASTER CHECKLIST

Before touching any tool, gather everything in this list. You will need these credentials and access points repeatedly throughout setup.

```
ACCOUNTS TO CREATE/HAVE READY:
□ Google Account (used for everything Google)
□ Google Ads account (ads.google.com)
□ Google Analytics 4 property
□ Google Tag Manager account
□ Google Search Console property
□ Google Looker Studio account
□ Make.com account
□ GitHub account (for MCP server)

CREDENTIALS TO PREPARE:
□ Google Ads Developer Token (apply at: developers.google.com/google-ads/api/docs/get-started/dev-token)
□ Google Ads Customer ID (10-digit number in your Ads account, top right)
□ OAuth 2.0 Client ID + Client Secret (from Google Cloud Console)
□ Google Ads Manager Account (MCC) if managing multiple accounts

YOUR WEBSITE:
□ Access to your website codebase (HTML/JS files)
□ Ability to deploy/push changes to production
□ A thank-you or confirmation page URL (post-form submission)
□ Your lead form's HTML structure (form ID or submit button selector)

SYSTEM REQUIREMENTS:
□ Python 3.10 or newer installed
□ Node.js 18+ installed
□ Git installed
□ pip installed
□ A code editor (VS Code recommended)
```

---

## TOOL INSTALLATION ORDER (CRITICAL — DO NOT SKIP STEPS)

```
PHASE 1 — Foundation (complete before anything else)
  Step 01 → Google Ads Account Setup
  Step 02 → Google Analytics 4
  Step 03 → Google Tag Manager
  Step 04 → GTM on Your Custom Website
  Step 05 → Google Ads Conversion Tracking
  Step 06 → GA4 Events Configuration
  Step 07 → Link GA4 ↔ Google Ads

PHASE 2 — Intelligence Tools
  Step 08 → Google Search Console
  Step 09 → Google Looker Studio
  Step 10 → Google Ads API Developer Assistant (credentials setup)

PHASE 3 — Automation
  Step 11 → Make.com Setup + Core Flows
  Step 12 → Google Ads Scripts

PHASE 4 — AI Orchestration Layer
  Step 13 → Google Ads MCP Server
  Step 14 → Connect MCP to Claude Code
  Step 15 → Gemini CLI Full Configuration
  Step 16 → End-to-End Verification
```

---

## PHASE 1 — FOUNDATION

---

### STEP 01 — Google Ads Account Setup {{Done}}

**Time required:** 20-30 minutes
**URL:** https://ads.google.com

#### 1.1 Create Your Account

```
1. Go to ads.google.com
2. Click "Start now"
3. Sign in with your Google account
4. When asked "What's your main advertising goal?" → click
   "Switch to Expert Mode" (bottom of page) — CRITICAL
   (Guided mode will force you into Smart campaigns — avoid)
5. Select "Create a campaign without a goal's guidance"
6. You'll land in the full Google Ads interface
```

#### 1.2 Account Settings Configuration

```
Google Ads → Settings → Account Settings

FILL IN:
□ Time zone: Set to YOUR timezone (cannot be changed later)
□ Currency: Set to your billing currency (cannot be changed later)
□ Auto-tagging: ENABLED (required for GA4 and conversion tracking)
   Settings → Account Settings → Auto-tagging → ON

BILLING:
□ Tools → Billing → Payment methods → Add card
□ Set billing threshold (recommended: start at $500)
□ Enable email notifications for billing alerts
```

#### 1.3 Note Your Customer ID

```
Top right of Google Ads interface → shows XXX-XXX-XXXX format
Write this down — you will need it for every API configuration.

Example: 123-456-7890 (store as: 1234567890 without dashes for API use)
```

#### 1.4 Create Your First Campaign Structure (Do Not Launch Yet)

```
Campaigns → + New Campaign → Lead generation
→ Search
→ Don't add campaign goals (skip)
→ Campaign name: [Client/Project]-Search-01

SETTINGS:
□ Networks: Uncheck "Display Network" and "Search Network partners"
   (Search only — cleaner data for new accounts)
□ Locations: Your target geography
□ Languages: Your target language(s)
□ Budget: Start conservative (e.g., $30-50/day)
□ Bidding: "Maximize conversions" (switch to Target CPA after 30+ conversions)
□ Ad schedule: Leave default for now (optimize after data)

DO NOT PUBLISH YET — complete conversion tracking first (Step 05)
```

---

### STEP 02 — Google Analytics 4 {{Done}}

**Time required:** 15-20 minutes
**URL:** https://analytics.google.com

#### 2.1 Create GA4 Property

```
1. analytics.google.com → Admin (gear icon, bottom left)
2. In "Account" column → Create Account (if new) OR select existing
3. In "Property" column → Create Property
4. Property name: [Project Name] - Production
5. Reporting time zone: Match your Google Ads timezone EXACTLY
6. Currency: Match your Google Ads currency EXACTLY
7. Click Next → Industry: choose closest match
8. Business size: choose yours
9. Click Create → Accept terms
```

#### 2.2 Create Web Data Stream

```
Property → Data Streams → Add Stream → Web

FILL IN:
□ Website URL: https://yourdomain.com (exact, no trailing slash)
□ Stream name: [Domain] - Web
□ Enhanced measurement: LEAVE ALL TOGGLES ON
   (Page views, Scrolls, Outbound clicks, Site search, Video, File downloads)

After creation, you'll see:
□ Measurement ID: G-XXXXXXXXXX  ← COPY AND SAVE THIS
□ Stream ID: (a number)
```

#### 2.3 Get Your GA4 Tracking Snippet

```
Data Stream → View tag instructions → Install manually

You'll see two options:
□ Option A: Global site tag (gtag.js) — if adding directly to HTML
□ Option B: Use Google Tag Manager — RECOMMENDED (we'll use this in Step 03)

COPY THE MEASUREMENT ID: G-XXXXXXXXXX
(You will configure the actual tracking via GTM in Step 04)
```

---

### STEP 03 — Google Tag Manager Account Setup {{Done}}

**Time required:** 10 minutes
**URL:** https://tagmanager.google.com

#### 3.1 Create GTM Account and Container

```
1. tagmanager.google.com → Create Account
2. Account name: [Your Company/Project Name]
3. Country: Your country
4. Container name: yourdomain.com (exact domain)
5. Target platform: Web
6. Click Create → Accept terms
```

#### 3.2 Save Your GTM Container Code

```
After creation, a popup shows two code snippets:

SNIPPET 1 (for <head>):
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->

SNIPPET 2 (for <body>):
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

SAVE YOUR CONTAINER ID: GTM-XXXXXXX
```

---

### STEP 04 — Install GTM on Your Custom Website

**Time required:** 10-15 minutes
**Requirement:** Access to your website HTML source code

#### 4.1 Add GTM Snippets to Every Page

Open your main HTML template file (the one that wraps all pages — typically `index.html`, `_layout.html`, `base.html`, `app.html`, or equivalent):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Page Title</title>
  
  <!-- =============================================
       GOOGLE TAG MANAGER — paste as HIGH as possible in <head>
       ============================================= -->
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
  <!-- End Google Tag Manager -->
  
  <!-- rest of your <head> content -->
</head>

<body>
  <!-- =============================================
       GTM NOSCRIPT — paste IMMEDIATELY after opening <body> tag
       ============================================= -->
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

  <!-- rest of your page content -->
</body>
</html>
```

**Replace `GTM-XXXXXXX` with your actual Container ID from Step 03.**

#### 4.2 Add dataLayer Push for Lead Form Submission

On your **thank-you page** (or in your form's success handler JavaScript), add:

```html
<!-- Option A: If you have a dedicated thank-you page -->
<!-- Add this in <head> of thank-you page, BEFORE GTM snippet -->
<script>
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    'event': 'lead_form_submit',
    'form_name': 'main_contact_form',
    'page_type': 'thank_you'
  });
</script>
```

```javascript
// Option B: If form submits via JavaScript (AJAX / fetch)
// Add inside your form submission success handler:

document.getElementById('your-form-id').addEventListener('submit', function(e) {
  // ... your existing form submission logic ...
  
  // After successful submission:
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    'event': 'lead_form_submit',
    'form_name': 'contact_form',
    'lead_email': document.getElementById('email').value  // for Enhanced Conversions
  });
});
```

#### 4.3 Deploy and Verify GTM Is Loading

```bash
# After deploying your site changes:
1. Open your website in Chrome
2. Install Chrome extension: "Tag Assistant Legacy" by Google
   OR use: tagassistant.google.com
3. Navigate to your site
4. Tag Assistant should show GTM-XXXXXXX as "firing"

# Alternative verification via browser console:
# Open DevTools (F12) → Console → type:
window.dataLayer
# Should return an array with gtm.js event
```

---

### STEP 05 — Google Ads Conversion Tracking

**Time required:** 20-30 minutes

#### 5.1 Create Conversion Action in Google Ads

```
Google Ads → Tools & Settings → Measurement → Conversions → + New conversion action

SELECT: Website
```

#### 5.2 Configure Lead Form Conversion

```
CATEGORY: Submit lead form
CONVERSION NAME: Lead - Form Submission
VALUE: 
  □ Use the same value for each conversion: $50 
    (use your estimated value per lead — adjust later)
COUNT: One (count only 1 conversion per click, standard for lead gen)
CLICK-THROUGH CONVERSION WINDOW: 30 days
ENGAGED-VIEW CONVERSION WINDOW: 3 days
VIEW-THROUGH CONVERSION WINDOW: 1 day
INCLUDE IN "CONVERSIONS": Yes (used for Smart Bidding)
ATTRIBUTION MODEL: Data-driven (if eligible) OR Last click

Click: Save and continue
```

#### 5.3 Get Your Conversion Tag Details

```
After creating, Google shows you:
□ Conversion ID: AW-XXXXXXXXX
□ Conversion Label: XXXXXXXXXXXX

SAVE BOTH — you'll configure these in GTM next.
```

#### 5.4 Configure Google Ads Conversion Tag in GTM

```
GTM → Tags → New → Tag Configuration → Google Ads Conversion Tracking

FIELDS:
□ Conversion ID: AW-XXXXXXXXX  (from 5.3)
□ Conversion Label: XXXXXXXXXXXX  (from 5.3)
□ Conversion Value: (leave blank — use dynamic value or hardcode 50)
□ Currency Code: USD (or your currency)
□ Order ID: (optional, leave blank for lead gen)

TRIGGERING:
→ New Trigger → Trigger Type: Page View
→ "Some Page Views" 
→ Condition: Page URL → contains → /thank-you
  (use your actual thank-you page URL path)

Tag Name: "Google Ads - Lead Form Conversion"
→ Save
```

#### 5.5 Configure Enhanced Conversions (Critical for accuracy)

```
Google Ads → Tools → Conversions → Settings → Enhanced conversions for web
→ Turn ON

In GTM:
Tags → New → Tag Configuration → Google Ads Enhanced Conversions

FIELDS:
□ Conversion Linker: Make sure Conversion Linker tag exists (GTM creates it auto)
□ Enhanced conversions:
  - Email: {{DLV - lead_email}}  (Data Layer Variable — see below)
  - Phone: {{DLV - lead_phone}}  (optional)

CREATE DATA LAYER VARIABLES IN GTM:
Variables → New → Variable Type: Data Layer Variable
  Name: DLV - lead_email
  Data Layer Variable Name: lead_email
  (matches what you pushed in Step 4.2)
```

#### 5.6 Publish GTM Container

```
GTM → Top right → SUBMIT button
Version name: "v1.0 - Initial Tracking Setup"
Version description: "GA4, Google Ads conversion, Enhanced Conversions"
→ Publish
```

#### 5.7 Verify Conversion Tag Is Firing

```
1. Install Chrome extension: "Google Tag Assistant" 
   OR use Google Ads Tag Assistant at tagassistant.google.com
2. Navigate to your thank-you page
3. Confirm: AW-XXXXXXXXX fires on that page
4. In Google Ads → Conversions → your conversion should show "Recording"
   (can take 24 hours to confirm first recording)
```

---

### STEP 06 — GA4 Events Configuration via GTM

**Time required:** 20-30 minutes

#### 6.1 Add GA4 Configuration Tag

```
GTM → Tags → New → Tag Configuration → Google Analytics: GA4 Configuration

FIELDS:
□ Measurement ID: G-XXXXXXXXXX  (from Step 2.3)
□ Send a page view event when this tag fires: YES

TRIGGERING: All Pages (Initialization - All Pages)

Tag Name: "GA4 - Configuration"
→ Save
```

#### 6.2 Add GA4 Lead Form Event Tag

```
GTM → Tags → New → Tag Configuration → Google Analytics: GA4 Event

FIELDS:
□ Configuration tag: GA4 - Configuration
□ Event name: generate_lead
  (this is GA4's recommended event name for lead gen)

EVENT PARAMETERS:
  form_name → contact_form
  page_location → {{Page URL}}

TRIGGERING:
→ New Trigger → Custom Event
→ Event name: lead_form_submit
  (matches what you pushed in dataLayer in Step 4.2)

Tag Name: "GA4 - Event - Lead Form Submit"
→ Save
```

#### 6.3 Mark generate_lead as GA4 Conversion

```
GA4 Admin → Property → Events
→ Find "generate_lead" event
→ Toggle "Mark as conversion" → ON

(Note: event must fire at least once before it appears here)
```

#### 6.4 Add GA4 Scroll Depth Tracking (Already automatic via Enhanced Measurement)

```
Verify in GA4:
Admin → Data Streams → your stream → Enhanced Measurement
→ Scrolls: ON
→ Outbound clicks: ON
→ Site search: ON (if you have search)
→ File downloads: ON
```

#### 6.5 Publish Updated GTM

```
GTM → Submit
Version name: "v1.1 - GA4 Events Added"
→ Publish
```

---

### STEP 07 — Link GA4 ↔ Google Ads

**Time required:** 5 minutes

#### 7.1 Link from Google Ads Side

```
Google Ads → Tools & Settings → Measurement → Linked accounts
→ Google Analytics (GA4) → Details → Link

SELECT your GA4 property → check "Enable Google Analytics 4 property"
→ Save

This enables:
□ Import GA4 audiences into Google Ads
□ See Google Ads data inside GA4
□ Import GA4 conversions into Google Ads (optional)
```

#### 7.2 Import GA4 Audiences into Google Ads

```
Google Ads → Tools → Audience Manager → + New audience
→ Use a Google Analytics segment

AUDIENCES TO CREATE IN GA4 FIRST (GA4 → Admin → Audiences):

1. "All Website Visitors - 30 days"
   Condition: Session count > 0
   Duration: 30 days

2. "Visited but No Conversion - 14 days"
   Condition: Session count > 0 AND (NOT) generate_lead = 0
   Duration: 14 days

3. "High Intent - Pricing Page Visitors"
   Condition: page_location contains /pricing (or your equivalent)
   Duration: 7 days

Then import these into Google Ads for remarketing campaigns.
```

---

## PHASE 2 — INTELLIGENCE TOOLS

---

### STEP 08 — Google Search Console

**Time required:** 15-20 minutes
**URL:** https://search.google.com/search-console

#### 8.1 Add Your Property

```
search.google.com/search-console → Add Property

CHOOSE: URL prefix
→ Enter: https://yourdomain.com (exact URL with https)

VERIFICATION METHOD (choose easiest for your setup):
```

**Option A — HTML Tag (recommended for custom-coded sites):**
```html
<!-- Add to <head> of your homepage ONLY: -->
<meta name="google-site-verification" content="XXXXXXXXXXXXXX" />
```

**Option B — HTML File:**
```
Download verification file → upload to root of your website
(e.g., https://yourdomain.com/google1234abcd.html)
```

**Option C — Google Analytics (fastest if GA4 already installed):**
```
Select "Google Analytics" verification method
→ Automatically verified if GA4 tag is on site
→ Click Verify
```

#### 8.2 Submit Your Sitemap

```
Search Console → Sitemaps → Enter sitemap URL
Common sitemap locations:
  yourdomain.com/sitemap.xml
  yourdomain.com/sitemap_index.xml

→ Submit

If you don't have a sitemap, generate one:
  For static sites: use xml-sitemaps.com
  For dynamic sites: add sitemap generation to your build
```

#### 8.3 Connect Search Console to GA4

```
GA4 → Admin → Property Settings → Search Console Links
→ Link → Select your Search Console property
→ Select web stream → Save

This gives you:
□ Organic search queries inside GA4
□ Landing page performance data
□ Click and impression data per query
```

#### 8.4 Key Reports to Monitor (Weekly)

```
Search Console Reports:
□ Performance → Queries: What people search to find you
   → Filter: Position > 10 (page 2+ keywords to target with ads)
□ Coverage: Any indexing errors
□ Core Web Vitals: Page speed/UX scores (affects Quality Score)
□ Mobile Usability: Critical for Google Ads landing page experience
```

---

### STEP 09 — Google Looker Studio

**Time required:** 30-45 minutes
**URL:** https://lookerstudio.google.com

#### 9.1 Access Looker Studio

```
lookerstudio.google.com → Sign in with Google account
→ No installation required — entirely browser-based
```

#### 9.2 Create Campaign Performance Dashboard

```
Looker Studio → + Blank Report

ADD DATA SOURCE 1: Google Ads
→ Click "Add data" → Select Google Ads connector
→ Authorize → Select your Google Ads account
→ Select table: Campaign

ADD DATA SOURCE 2: Google Analytics 4
→ Add data → Select GA4 connector
→ Authorize → Select your GA4 property
→ Select table: Events
```

#### 9.3 Build Dashboard 1 — Daily Campaign Performance

```
CREATE THESE CHARTS:

CHART 1: Scorecard row (top of page)
→ Add chart → Scorecard
Create 6 scorecards:
  - Metric: Cost (label: Total Spend)
  - Metric: Impressions
  - Metric: Clicks
  - Metric: CTR (Click-through rate)
  - Metric: Conversions
  - Metric: Cost/Conversion (label: CPA)

CHART 2: Time series — spend + conversions over 30 days
→ Add chart → Time series
  Dimension: Date
  Metrics: Cost, Conversions
  Date range: Last 30 days

CHART 3: Campaign breakdown table
→ Add chart → Table
  Dimension: Campaign Name
  Metrics: Cost, Clicks, CTR, Conversions, CPA, Conv. Rate
  Sort: Cost (descending)

CHART 4: Date range control
→ Add control → Date range control
→ Default: Last 30 days
```

#### 9.4 Build Dashboard 2 — Lead Quality (Add new page)

```
Page → Add page → "Lead Quality"

CHART 1: Funnel visualization
Steps:
  1. Clicks (from Google Ads)
  2. Sessions (from GA4)
  3. Lead Form Views (GA4 event: page_view on /contact)
  4. Lead Submissions (GA4 event: generate_lead)

CHART 2: Geographic performance
→ Add chart → Google Maps
  Dimension: City/Region
  Metric: Conversions

CHART 3: Device breakdown
→ Add chart → Pie chart
  Dimension: Device
  Metric: Conversions
```

#### 9.5 Build Dashboard 3 — Account Health (Add new page)

```
Page → Add page → "Account Health"

CHART 1: Quality Score distribution
→ Table with Keyword, Quality Score, Impressions, Conversions

CHART 2: Budget utilization
→ Bar chart: Campaign vs. Budget vs. Spend

CHART 3: Search Impression Share
→ Scorecard: Search Impr. share, Lost IS (budget), Lost IS (rank)
```

#### 9.6 Share Dashboard

```
Top right → Share → Manage access
→ Add email addresses of team/clients
→ Set permission: Viewer
→ Enable: "Link sharing" → Anyone with link can view
   (safe — they can only view, not edit)
```

---

### STEP 10 — Google Ads API Developer Assistant (Credentials Setup)

**Time required:** 45-60 minutes
**Already cloned at:** `RA-Project/google-ads-api-developer-assistant/`

#### 10.1 Verify Python Version

```bash
python3 --version
# Must show 3.10 or higher
# If not: install from python.org or via your package manager

# macOS:
brew install python@3.12

# Ubuntu/Debian:
sudo apt update && sudo apt install python3.12

# Verify pip:
pip3 --version
```

#### 10.2 Install Gemini CLI

```bash
# Install via npm (requires Node.js 18+)
npm install -g @google/gemini-cli

# Verify installation:
gemini --version

# If Node.js not installed:
# macOS: brew install node
# Ubuntu: sudo apt install nodejs npm
# Or download from: nodejs.org
```

#### 10.3 Authenticate Gemini CLI

```bash
gemini auth login
# Opens browser → sign in with your Google account
# Grant requested permissions
# Returns to terminal when complete
```

#### 10.4 Create Google Cloud Project for OAuth

```
1. Go to: console.cloud.google.com
2. Top bar → Select project → New Project
3. Project name: google-ads-api-dev
4. Click Create → wait for creation

5. Enable Google Ads API:
   APIs & Services → Enable APIs and Services
   → Search "Google Ads API" → Enable

6. Create OAuth Credentials:
   APIs & Services → Credentials → Create Credentials → OAuth client ID
   
   If prompted to configure consent screen:
   → OAuth consent screen → External → Create
   → App name: Google Ads Dev Assistant
   → User support email: your email
   → Developer contact: your email
   → Save and Continue (skip scopes for now)
   → Add yourself as test user
   → Save and Continue → Back to Dashboard

7. Create OAuth Client ID:
   Credentials → Create Credentials → OAuth client ID
   Application type: Desktop app
   Name: google-ads-dev-assistant
   → Create
   
   DOWNLOAD the JSON file → rename to client_secret.json
   SAVE THESE VALUES:
   □ Client ID: XXXXXXXX.apps.googleusercontent.com
   □ Client Secret: XXXXXXXXXXXX
```

#### 10.5 Apply for Google Ads API Developer Token

```
This is REQUIRED and takes 1-5 business days for approval.

1. Sign in to your Google Ads account
2. Tools & Settings → Setup → API Center
3. Fill in:
   □ Company name: Your company
   □ Company website: yourdomain.com
   □ Email: your email
   □ Reason for access: "Building internal tools for campaign management 
     and performance analysis using the Google Ads API Developer Assistant"
   □ Are you building for clients?: Yes/No (based on your use)
4. Agree to terms → Submit

WHILE WAITING (you'll get basic/test access immediately):
→ You can use TEST ACCOUNTS immediately with test developer token
→ Production token required for live accounts
→ Token looks like: XXXXXXXX-XXXXXXXX (22 chars)
```

#### 10.6 Configure Developer Assistant Credentials

```bash
# Navigate to the developer assistant directory:
cd /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant

# Run the install script:
./install.sh

# If permission denied:
chmod +x install.sh && ./install.sh
```

Now create the credentials file:

```bash
# Create google-ads.yaml in your HOME directory:
nano ~/.google-ads.yaml
```

```yaml
# ~/.google-ads.yaml
developer_token: YOUR_DEVELOPER_TOKEN_HERE
client_id: YOUR_CLIENT_ID.apps.googleusercontent.com
client_secret: YOUR_CLIENT_SECRET
refresh_token: (leave blank for now — generated in next step)
login_customer_id: YOUR_MANAGER_ACCOUNT_ID  # if using MCC, else omit
use_proto_plus: True
```

#### 10.7 Generate OAuth Refresh Token

```bash
# From the developer assistant directory, run:
python3 client_libs/google-ads-python/examples/authentication/authenticate_in_standalone_application.py \
  --client_id YOUR_CLIENT_ID \
  --client_secret YOUR_CLIENT_SECRET

# Browser will open → sign in with Google Ads account owner
# Grant permissions → copy the authorization code back to terminal
# Script outputs your REFRESH TOKEN

# Copy the refresh token into ~/.google-ads.yaml:
# refresh_token: 1//XXXXXXXXXXXXXXXXX
```

Updated `~/.google-ads.yaml`:

```yaml
developer_token: YOUR_DEVELOPER_TOKEN_HERE
client_id: YOUR_CLIENT_ID.apps.googleusercontent.com
client_secret: YOUR_CLIENT_SECRET
refresh_token: 1//XXXXXXXXXXXXXXXXX
login_customer_id: YOUR_CUSTOMER_ID  # 10 digits, no dashes
use_proto_plus: True
```

#### 10.8 Create customer_id.txt (Optional but Convenient)

```bash
# In the developer assistant directory:
echo "1234567890" > customer_id.txt
# Replace with your actual Customer ID (no dashes)
```

#### 10.9 Test the Installation

```bash
cd /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant
gemini

# Inside Gemini CLI, test with:
> Show me all active campaigns in my account

# Expected output:
# The assistant queries your Google Ads account and returns campaign list
# If successful: you see campaigns with status, budget, impressions
# If error: check ~/.google-ads.yaml credentials
```

---

## PHASE 3 — AUTOMATION

---

### STEP 11 — Make.com Setup + Core Flows

**Time required:** 45-60 minutes
**URL:** https://make.com

#### 11.1 Create Account and Workspace

```
1. make.com → Sign up (free plan: 1,000 operations/month)
   Recommended: Start with Core plan ($9/mo, 10,000 ops) for production use
2. Create organization: [Your Company Name]
3. Create workspace: RA-Project
```

#### 11.2 Connect Google Ads Integration

```
Make → Connections → Add connection → Google Ads

1. Click Connect
2. Sign in with Google account that has Google Ads access
3. Grant permissions
4. Name connection: "Google Ads - [Account Name]"
5. Save

Verify: Connection shows green "Connected" status
```

#### 11.3 Connect Google Sheets (for reporting logs)

```
Make → Connections → Add connection → Google Sheets

1. Sign in with Google account
2. Grant permissions
3. Name: "Google Sheets - Main"

CREATE A LOGGING SPREADSHEET IN GOOGLE SHEETS:
sheets.google.com → New spreadsheet
Name: "RA-Project - Automation Logs"

Create sheets (tabs):
□ "Lead Log" - columns: Date, Source, Campaign, Ad Group, Keyword, Name, Email, Phone
□ "Conversion Log" - columns: Date, Lead ID, Status, Revenue, Sent to Ads
□ "Alert Log" - columns: Date, Alert Type, Campaign, Detail, Action Taken

COPY THE SPREADSHEET ID from the URL:
docs.google.com/spreadsheets/d/SPREADSHEET_ID_IS_HERE/edit
```

#### 11.4 Build FLOW 1 — Budget Alert Automation

```
Make → Create new scenario

TRIGGER: Google Ads → Watch Campaigns
  Connection: your Google Ads connection
  Customer ID: your customer ID
  Schedule: Every 1 hour

FILTER (add after trigger):
  Condition: Daily Budget Spent Percentage > 80
  (calculate: Cost / Campaign Budget * 100 > 80)

ACTION 1: Email (Gmail) or Slack → Send Message
  Content:
  Subject: ⚠️ Budget Alert: {{Campaign Name}} at {{percentage}}%
  Body: 
  Campaign: {{Campaign Name}}
  Spent today: ${{Cost}}
  Daily budget: ${{Daily Budget}}
  Remaining: ${{remaining}}
  Time: {{current time}}

ACTION 2: Google Sheets → Add Row to "Alert Log"
  Spreadsheet: RA-Project - Automation Logs
  Sheet: Alert Log
  Values: {{Date}}, "Budget Alert", {{Campaign Name}}, {{Cost}}, "Notified"

→ Save scenario
→ Name: "FLOW 1 - Budget Alerts"
→ Enable scenario (toggle ON)
```

#### 11.5 Build FLOW 2 — Weekly Performance Report

```
Make → Create new scenario

TRIGGER: Schedule → Every week on Monday at 8:00 AM (your timezone)

ACTION 1: Google Ads → Search Campaigns
  Date range: Last 7 days
  Fields: Campaign name, Cost, Clicks, Impressions, Conversions, CPA

ACTION 2: Google Ads → Search Keywords  
  Date range: Last 7 days
  Filter: Conversions > 0
  Sort: Conversions DESC
  Limit: 10

ACTION 3: Google Sheets → Add Row(s)
  Log performance data for historical tracking

ACTION 4: Gmail → Send Email
  To: your email (+ client email if applicable)
  Subject: 📊 Weekly Google Ads Report - {{Date Range}}
  Body: (HTML email with performance summary table)

→ Save
→ Name: "FLOW 2 - Weekly Performance Report"
→ Enable
```

#### 11.6 Build FLOW 3 — Lead Capture Logging

```
This flow receives webhook from your website when a lead submits.

Make → Create new scenario

TRIGGER: Webhooks → Custom Webhook
  → Create webhook
  → Copy webhook URL: https://hook.make.com/XXXXXXXXXXXXXXXX
  SAVE THIS URL — you'll add it to your website form handler

ACTION 1: Google Sheets → Add Row to "Lead Log"
  Spreadsheet: RA-Project
  Sheet: Lead Log
  Values: 
    Date: {{timestamp}}
    Source: {{utm_source}}
    Campaign: {{utm_campaign}}
    Ad Group: {{utm_content}}
    Keyword: {{utm_term}}
    Name: {{name}}
    Email: {{email}}
    Phone: {{phone}}

ACTION 2: Gmail → Send notification email
  To: your email
  Subject: 🎯 New Lead: {{name}}
  Body: Contact details + UTM parameters

→ Save
→ Name: "FLOW 3 - Lead Capture Logging"
→ Enable
```

#### 11.7 Add Webhook URL to Your Website Form

In your custom website form handler, add this after successful form submission:

```javascript
// In your form submission handler (JavaScript):
async function handleFormSubmit(formData) {
  // ... your existing form logic ...
  
  // Send lead data to Make.com webhook:
  const urlParams = new URLSearchParams(window.location.search);
  
  await fetch('https://hook.make.com/YOUR_WEBHOOK_ID_HERE', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      timestamp: new Date().toISOString(),
      name: formData.name,
      email: formData.email,
      phone: formData.phone,
      utm_source: urlParams.get('utm_source') || 'direct',
      utm_campaign: urlParams.get('utm_campaign') || '',
      utm_content: urlParams.get('utm_content') || '',
      utm_term: urlParams.get('utm_term') || '',
      page_url: window.location.href
    })
  });
}
```

#### 11.8 Build FLOW 4 — Offline Conversion Import (For Future CRM Connection)

```
NOTE: This flow will be completed when Oggo Data CRM is configured.
For now, create the scenario structure and leave the trigger blank.

Make → Create new scenario → Save as DRAFT

FUTURE TRIGGER: Oggo Data CRM Webhook (when deal = Closed Won)

FUTURE ACTIONS:
1. Format conversion data for Google Ads API
2. Google Ads → Upload Click Conversion
   - GCLID: {{gclid from CRM}}
   - Conversion Name: "Closed Won - Revenue"
   - Conversion Time: {{close date}}
   - Conversion Value: {{deal value}}
3. Log to Sheets

→ Name: "FLOW 4 - Offline Conversions [PENDING CRM]"
→ Save as DRAFT (do not enable yet)
```

---

### STEP 12 — Google Ads Scripts

**Time required:** 20-30 minutes
**Location:** Google Ads → Tools → Bulk Actions → Scripts

#### 12.1 Access Google Ads Scripts

```
Google Ads → Tools & Settings → Bulk Actions → Scripts
→ + button to create new script
```

#### 12.2 Script 1 — Budget Overspend Alert

```javascript
/**
 * SCRIPT 1: Budget Overspend Alert
 * Runs: Hourly
 * Action: Emails if any campaign exceeds 90% of daily budget
 */
function main() {
  var ALERT_THRESHOLD = 0.90; // 90% of budget
  var EMAIL = 'your@email.com';
  
  var campaignIterator = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();
  
  var alerts = [];
  
  while (campaignIterator.hasNext()) {
    var campaign = campaignIterator.next();
    var budget = campaign.getBudget().getAmount();
    var spent = campaign.getStats().getCost();
    var ratio = spent / budget;
    
    if (ratio >= ALERT_THRESHOLD) {
      alerts.push({
        name: campaign.getName(),
        budget: budget.toFixed(2),
        spent: spent.toFixed(2),
        percent: (ratio * 100).toFixed(1)
      });
    }
  }
  
  if (alerts.length > 0) {
    var body = 'Budget Alert - ' + new Date().toLocaleString() + '\n\n';
    alerts.forEach(function(a) {
      body += 'Campaign: ' + a.name + '\n';
      body += 'Budget: $' + a.budget + ' | Spent: $' + a.spent;
      body += ' (' + a.percent + '%)\n\n';
    });
    MailApp.sendEmail(EMAIL, '⚠️ Google Ads Budget Alert', body);
  }
}
```

**Schedule:** Hourly

#### 12.3 Script 2 — Zero Conversion Keyword Pauser

```javascript
/**
 * SCRIPT 2: Pause Wasted Spend Keywords
 * Runs: Weekly (Sunday night)
 * Action: Pauses keywords with 150+ clicks and 0 conversions over 30 days
 */
function main() {
  var CLICK_THRESHOLD = 150;
  var LOOKBACK_DAYS = 30;
  var EMAIL = 'your@email.com';
  
  var dateRange = getDateRange(LOOKBACK_DAYS);
  
  var keywordIterator = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .withCondition('Clicks > ' + CLICK_THRESHOLD)
    .withCondition('Conversions = 0')
    .forDateRange(dateRange)
    .get();
  
  var paused = [];
  
  while (keywordIterator.hasNext()) {
    var keyword = keywordIterator.next();
    paused.push({
      keyword: keyword.getText(),
      campaign: keyword.getCampaign().getName(),
      adGroup: keyword.getAdGroup().getName(),
      clicks: keyword.getStats().getClicks(),
      cost: keyword.getStats().getCost().toFixed(2)
    });
    keyword.pause();
  }
  
  if (paused.length > 0) {
    var body = 'Paused ' + paused.length + ' keywords (30-day window):\n\n';
    paused.forEach(function(k) {
      body += '[' + k.campaign + ' > ' + k.adGroup + ']\n';
      body += '"' + k.keyword + '" — ' + k.clicks + ' clicks, $' + k.cost + ' spent\n\n';
    });
    MailApp.sendEmail(EMAIL, '🛑 Keywords Paused - No Conversions', body);
  } else {
    Logger.log('No keywords met pause criteria.');
  }
}

function getDateRange(days) {
  var end = new Date();
  var start = new Date();
  start.setDate(start.getDate() - days);
  
  function formatDate(d) {
    return Utilities.formatDate(d, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
  }
  
  return formatDate(start) + ',' + formatDate(end);
}
```

**Schedule:** Weekly (Sunday 11pm)

#### 12.4 Script 3 — Search Term Mining Report

```javascript
/**
 * SCRIPT 3: Search Term Report - New Keyword Opportunities
 * Runs: Weekly (Monday morning)
 * Action: Emails search terms with conversions that aren't exact keywords
 */
function main() {
  var EMAIL = 'your@email.com';
  var MIN_CONVERSIONS = 1;
  
  var report = AdsApp.report(
    'SELECT SearchTerm, CampaignName, AdGroupName, Clicks, ' +
    'Conversions, ConversionValue, Cost ' +
    'FROM SEARCH_QUERY_PERFORMANCE_REPORT ' +
    'WHERE Conversions > ' + MIN_CONVERSIONS + ' ' +
    'AND QueryMatchTypeWithVariant != EXACT ' +
    'DURING LAST_30_DAYS ' +
    'ORDER BY Conversions DESC'
  );
  
  var rows = report.rows();
  var opportunities = [];
  
  while (rows.hasNext()) {
    var row = rows.next();
    opportunities.push({
      term: row['SearchTerm'],
      campaign: row['CampaignName'],
      conversions: row['Conversions'],
      cost: parseFloat(row['Cost']).toFixed(2)
    });
  }
  
  if (opportunities.length > 0) {
    var body = '🎯 Search Terms Worth Adding as Keywords (Last 30 Days):\n\n';
    opportunities.forEach(function(o) {
      body += '"' + o.term + '"\n';
      body += 'Campaign: ' + o.campaign + '\n';
      body += 'Conversions: ' + o.conversions + ' | Cost: $' + o.cost + '\n\n';
    });
    MailApp.sendEmail(EMAIL, '🔍 Keyword Opportunities - Search Term Report', body);
  }
}
```

**Schedule:** Weekly (Monday 7am)

#### 12.5 Activate All Scripts

```
For each script:
Scripts list → click script name → 
→ Authorize (first time only — sign in to authorize)
→ Set frequency (Hourly / Weekly)
→ Preview run (click Run Preview to test)
→ Save
```

---

## PHASE 4 — AI ORCHESTRATION LAYER

---

### STEP 13 — Google Ads MCP Server Installation

**Time required:** 30-45 minutes
**GitHub:** https://github.com/google-marketing-solutions/google_ads_mcp

#### 13.1 Clone the Repository

```bash
cd /home/sog/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/

git clone https://github.com/google-marketing-solutions/google_ads_mcp
cd google_ads_mcp
```

#### 13.2 Create Python Virtual Environment

```bash
# Create isolated environment:
python3 -m venv venv

# Activate it:
source venv/bin/activate          # Linux/macOS
# OR:
venv\Scripts\activate              # Windows

# Verify activation (you should see (venv) in prompt):
which python  # Should point to venv/bin/python
```

#### 13.3 Install Dependencies

```bash
# With venv activated:
pip install -r requirements.txt

# Verify installation:
pip list | grep google-ads
# Should show google-ads package installed
```

#### 13.4 Configure MCP Server Credentials

```bash
# Copy example env file:
cp .env.example .env

# Edit with your credentials:
nano .env
```

```bash
# .env file contents:
GOOGLE_ADS_DEVELOPER_TOKEN=YOUR_DEVELOPER_TOKEN_HERE
GOOGLE_ADS_CLIENT_ID=YOUR_CLIENT_ID.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=YOUR_CLIENT_SECRET
GOOGLE_ADS_REFRESH_TOKEN=YOUR_REFRESH_TOKEN
GOOGLE_ADS_LOGIN_CUSTOMER_ID=YOUR_CUSTOMER_ID  # 10 digits, no dashes
GOOGLE_ADS_USE_PROTO_PLUS=true

# Same credentials as ~/.google-ads.yaml from Step 10.6
```

#### 13.5 Test MCP Server Standalone

```bash
# With venv activated, from google_ads_mcp directory:
python server.py

# Expected output:
# Server starting on stdio...
# MCP server ready
# (Ctrl+C to stop)

# If you see errors:
# → Check .env file credentials
# → Verify developer token is approved
# → Check refresh token is valid
```

#### 13.6 Determine Server Start Command

```bash
# Get the full path to python in your venv:
which python
# Example output: /home/sog/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/google_ads_mcp/venv/bin/python

# Get full path to server.py:
realpath server.py
# Example: /home/sog/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/google_ads_mcp/server.py

# SAVE BOTH PATHS — needed for Step 14
```

---

### STEP 14 — Connect MCP to Claude Code

**Time required:** 10 minutes

#### 14.1 Locate Claude Code Settings

```bash
# Claude Code settings file location:
~/.claude/settings.json

# Open it:
nano ~/.claude/settings.json
# OR:
code ~/.claude/settings.json  # if using VS Code
```

#### 14.2 Add Google Ads MCP Server

```json
{
  "mcpServers": {
    "google-ads": {
      "command": "/home/sog/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/google_ads_mcp/venv/bin/python",
      "args": [
        "/home/sog/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/google_ads_mcp/server.py"
      ],
      "env": {
        "GOOGLE_ADS_DEVELOPER_TOKEN": "YOUR_DEVELOPER_TOKEN",
        "GOOGLE_ADS_CLIENT_ID": "YOUR_CLIENT_ID.apps.googleusercontent.com",
        "GOOGLE_ADS_CLIENT_SECRET": "YOUR_CLIENT_SECRET",
        "GOOGLE_ADS_REFRESH_TOKEN": "YOUR_REFRESH_TOKEN",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "YOUR_CUSTOMER_ID"
      }
    }
  }
}
```

**Security note:** Alternatively, keep credentials only in the `.env` file and omit the `env` block here — the server reads from `.env` automatically. Do not commit `settings.json` with credentials to git.

#### 14.3 Restart Claude Code and Verify

```bash
# Exit and restart Claude Code (this session)
# Then verify MCP is connected:
# You should see "google-ads" listed in available MCP tools

# Test by asking:
# "Using the Google Ads MCP, list all active campaigns"
```

#### 14.4 Create Project-Level MCP Config (Recommended)

```bash
# Create project-level settings (overrides global for this project):
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/.claude/

# Create/edit settings:
nano /home/sog/skool/05-Client-OS/RA-Project/.claude/settings.json
```

```json
{
  "mcpServers": {
    "google-ads": {
      "command": "/home/sog/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/google_ads_mcp/venv/bin/python",
      "args": [
        "/home/sog/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/google_ads_mcp/server.py"
      ]
    }
  }
}
```

```bash
# Add .env to .gitignore to protect credentials:
echo "*.env" >> /home/sog/skool/05-Client-OS/RA-Project/.gitignore
echo ".env" >> /home/sog/skool/05-Client-OS/RA-Project/.gitignore
echo "credentials/" >> /home/sog/skool/05-Client-OS/RA-Project/.gitignore
echo "~/.google-ads.yaml" >> /home/sog/skool/05-Client-OS/RA-Project/.gitignore
```

---

### STEP 15 — Gemini CLI Full Configuration

**Time required:** 15-20 minutes
**Already installed in Step 10.2**

#### 15.1 Verify Gemini CLI is Authenticated

```bash
gemini auth status
# Should show: Authenticated as your@email.com

# If not authenticated:
gemini auth login
```

#### 15.2 Configure Gemini for Developer Assistant Project

```bash
# The Developer Assistant already has a .gemini/ directory configured
# Verify the settings:
cat /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant/.gemini/settings.json
```

#### 15.3 Add Your Customer ID to Context

```bash
# Ensure customer_id.txt exists:
cat /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant/customer_id.txt
# Should show your 10-digit customer ID

# If empty or missing:
echo "YOUR_CUSTOMER_ID_HERE" > \
  /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant/customer_id.txt
```

#### 15.4 Update Developer Assistant Libraries

```bash
cd /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant

# Always run this before starting a new session to ensure latest API version:
./update.sh

# On Windows:
# ./update.ps1
```

#### 15.5 Test Full Developer Assistant Workflow

```bash
cd /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant
gemini

# Test queries (type these inside Gemini CLI):

# Query 1 — Account overview:
> Show me all active campaigns with their daily budgets and current spend

# Query 2 — Performance analysis:
> What are my top 5 keywords by conversions in the last 30 days?

# Query 3 — Optimization opportunity:
> Show me keywords with more than 50 clicks and 0 conversions in the last 14 days

# Query 4 — Use /step_by_step for debugging:
> /step_by_step
> Show me campaigns with CPA above $100 last 7 days

# Exit Gemini CLI:
> exit
# OR: Ctrl+C
```

#### 15.6 Set Up Gemini CLI Output to Project Folders

```bash
# Verify saved/ directory exists and is writable:
ls -la /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant/saved/

# Should show: code/ csv/ data/ directories
# If missing:
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant/saved/{code,csv,data}
```

---

### STEP 16 — End-to-End Verification

**Time required:** 15-20 minutes

Run through this full verification checklist after completing all steps.

#### 16.1 Tracking Verification

```
□ Visit your website → open Chrome DevTools (F12) → Network tab
  Filter: "google" → should see requests to:
  ✓ www.googletagmanager.com (GTM loading)
  ✓ www.google-analytics.com (GA4 firing)
  ✓ googleads.g.doubleclick.net (if on ad-driven page)

□ Submit your lead form → check:
  ✓ Thank-you page loads correctly
  ✓ GTM fires Google Ads conversion tag (Tag Assistant)
  ✓ GTM fires GA4 generate_lead event
  ✓ Make.com FLOW 3 received webhook (check scenario history)
  ✓ Google Sheets Lead Log has new row

□ Google Ads → Conversions:
  ✓ Status shows "Recording" (may take up to 24 hours)
```

#### 16.2 Intelligence Tools Verification

```
□ Search Console:
  ✓ Property verified (green checkmark)
  ✓ Sitemap submitted and processing

□ Looker Studio:
  ✓ Dashboard loads with Google Ads data
  ✓ GA4 data appears (may take 24 hours for first data)
  ✓ Date range controls work

□ Developer Assistant:
  cd google-ads-api-developer-assistant && gemini
  > Show all campaigns
  ✓ Returns campaign list from your account
  ✓ Code saved to saved/code/
```

#### 16.3 Automation Verification

```
□ Make.com:
  ✓ All enabled scenarios show green status
  ✓ Test FLOW 1 manually: click Run Once → check email
  ✓ FLOW 3 webhook URL returns 200 response

□ Google Ads Scripts:
  ✓ All scripts show "Authorized" status
  ✓ Preview run on Script 1 completes without errors
```

#### 16.4 AI Orchestration Verification

```
□ MCP Server:
  ✓ Server starts without errors: python server.py
  
□ Claude Code + MCP:
  ✓ Ask Claude: "List my Google Ads campaigns using the MCP"
  ✓ Response includes real campaign data from your account

□ Full pipeline test:
  Run test lead through entire system:
  1. Click an ad (or simulate by visiting landing page with UTM params)
  2. Submit lead form
  3. Confirm: GTM fires → GA4 records → Make.com logs → Sheets updated
  4. Query via Developer Assistant: "How many conversions today?"
  5. Check Looker Studio dashboard reflects new data
```

---

## CREDENTIALS REFERENCE SHEET

Store this in `RA-Project/00-foundation/credentials/` (DO NOT commit to git):

```
=== GOOGLE ADS ===
Account email: 
Customer ID (with dashes): 
Customer ID (API format, no dashes): 
Developer Token: 
API Access Level: Basic / Standard

=== GOOGLE CLOUD PROJECT ===
Project ID: 
Project Name: google-ads-api-dev
OAuth Client ID: 
OAuth Client Secret: 
Refresh Token: 

=== TRACKING IDs ===
GTM Container ID: GTM-XXXXXXX
GA4 Measurement ID: G-XXXXXXXXXX
GA4 Stream ID: 
Google Ads Conversion ID: AW-XXXXXXXXX
Google Ads Conversion Label: 

=== AUTOMATION ===
Make.com Organization: 
Make.com Lead Webhook URL: https://hook.make.com/XXXXX
Google Sheets ID (Automation Logs): 

=== FILE LOCATIONS ===
Developer Assistant: ~/skool/05-Client-OS/RA-Project/google-ads-api-developer-assistant/
MCP Server: ~/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/google_ads_mcp/
Credentials file: ~/.google-ads.yaml
MCP env file: ~/skool/05-Client-OS/RA-Project/03-automation/v3-advanced/google_ads_mcp/.env
```

---

## MAINTENANCE SCHEDULE

| Frequency | Task | Tool | Action |
|-----------|------|------|--------|
| Daily | Check budget pacing | Script 1 auto-emails | Review alerts |
| Daily | Check new leads | Make FLOW 3 auto-logs | Review Sheets |
| Weekly | Run performance analysis | Developer Assistant | Query campaigns |
| Weekly | Review keyword waste | Script 3 auto-emails | Add negatives |
| Weekly | Review Looker dashboard | Looker Studio | Strategic decisions |
| Monthly | Update Developer Assistant | `./update.sh` | CLI command |
| Monthly | Review Search Console | Search Console | Keyword opportunities |
| Monthly | Audit conversion tracking | Google Ads UI | Verify recording status |
| Per Google Ads API release | Update client libraries | `./update.sh` | CLI command |

---

## COMMON ERRORS & FIXES

### GTM Not Firing
```
Problem: Tag Assistant shows GTM not detected
Fix 1: Verify snippet is in <head> BEFORE other scripts
Fix 2: Check for ad blockers (disable for testing)
Fix 3: Verify GTM container is Published (not just saved)
Fix 4: Clear browser cache → hard refresh (Ctrl+Shift+R)
```

### Developer Token Error
```
Problem: "Developer token is not approved"
Fix: Check approval status at Google Ads → Tools → API Center
     Test accounts work immediately; production requires approval
     Use test customer ID while waiting: 7474447747
```

### OAuth Token Expired
```
Problem: "Invalid credentials" or "Token has been expired or revoked"
Fix: Re-run authentication script from Step 10.7
     Or run: 
     python3 client_libs/google-ads-python/examples/authentication/authenticate_in_standalone_application.py
     Update refresh_token in ~/.google-ads.yaml and .env
```

### MCP Server Not Starting
```
Problem: "Module not found" or import errors
Fix 1: Verify venv is activated: source venv/bin/activate
Fix 2: Re-install: pip install -r requirements.txt
Fix 3: Check Python version: python --version (must be 3.10+)
Fix 4: Check .env file exists and has all required fields
```

### Make.com Webhook Not Receiving
```
Problem: Form submits but no data in Make.com
Fix 1: Verify webhook URL in website code is correct
Fix 2: Check CORS headers on your website allow fetch to external URLs
Fix 3: Verify scenario is ENABLED (green toggle)
Fix 4: Check Make.com scenario execution history for error logs
Fix 5: Test webhook manually: 
       curl -X POST https://hook.make.com/YOURWEBHOOKID \
         -H "Content-Type: application/json" \
         -d '{"test": "data"}'
```

### GA4 Events Not Showing
```
Problem: generate_lead event not appearing in GA4
Fix 1: Check GTM trigger is correct (event name matches dataLayer push exactly)
Fix 2: Verify GTM container is published
Fix 3: Use GA4 DebugView (Admin → DebugView) with GTM Preview mode
Fix 4: Wait up to 24-48 hours for events to appear in standard reports
       (DebugView shows real-time)
```

### Looker Studio No Data
```
Problem: Charts show "No data available"
Fix 1: Google Ads: verify account has campaign data in selected date range
Fix 2: Re-authorize data source: Edit → Data sources → Reconnect
Fix 3: Check date range control — may be set to future dates
Fix 4: GA4 data has 24-48h delay — use "Today" range for real-time
```

---

## OGGO DATA CRM — INTEGRATION NOTE (Pending)

```
When you are ready to configure Oggo Data CRM, the following 
integrations need to be set up:

1. LEAD CAPTURE INTEGRATION:
   → Configure Make.com FLOW 3 to also create contact in Oggo Data
   → Add Oggo Data as additional action after Google Sheets logging
   → Map fields: name, email, phone, utm_source, utm_campaign, utm_term

2. OFFLINE CONVERSION IMPORT:
   → Activate Make.com FLOW 4 (currently saved as DRAFT)
   → Configure Oggo Data webhook: fires when deal = Closed Won
   → Fields required: gclid (Google Click ID), conversion_time, deal_value
   → This is the highest-impact integration in the entire ecosystem

3. GCLID CAPTURE (do this NOW — even before CRM setup):
   → Add this to your website to capture Google Click ID:
   
   // In your page initialization JavaScript:
   const urlParams = new URLSearchParams(window.location.search);
   const gclid = urlParams.get('gclid');
   if (gclid) {
     // Store in cookie (90-day expiry):
     document.cookie = `gclid=${gclid}; max-age=7776000; path=/`;
     // Also store in localStorage as backup:
     localStorage.setItem('gclid', gclid);
   }
   
   // In your form submit handler, include:
   gclid: getCookie('gclid') || localStorage.getItem('gclid') || ''
   
   // getCookie helper:
   function getCookie(name) {
     const value = `; ${document.cookie}`;
     const parts = value.split(`; ${name}=`);
     if (parts.length === 2) return parts.pop().split(';').shift();
   }
   
   → This GCLID, passed to Oggo Data with each lead, enables
     offline conversion import when the deal closes.
```

---

*Installation guide generated by CAI + MGI Council | RA-Project | April 20, 2026*
*Tools covered: Google Ads, GTM, GA4, Search Console, Looker Studio, Dev Assistant, Make.com, Google Ads Scripts, MCP Server, Claude Code, Gemini CLI*
*Excluded: CallRail | Pending: Oggo Data CRM (FLOW 4 pre-built and awaiting activation)*
