# Complete Setup Guide — ERPNext + Metabase
**Date:** 2026-04-18  
**OS:** Arch Linux | Docker 29.4.0 | Docker Compose 5.1.2  
**Goal:** Full local agency operating system — business data, KPIs, dashboards

---

## PORT ALLOCATION

| Tool | External Port | Internal Port | URL |
|---|---|---|---|
| ERPNext | **18080** | 80 | http://localhost:18080 |
| Metabase | **19000** | 3000 | http://localhost:19000 |
| Plane | 33000 | — | http://localhost:33000 ✅ |
| n8n | 5678 | — | http://localhost:5678 ✅ |
| Invoice Ninja | 38080 | — | (to be decommissioned) |

---

## FOLDER STRUCTURE

```
/home/sog/
  ├── microhard-agency/    ← existing (Plane, n8n, PostgreSQL)
  ├── erpnext/             ← NEW (frappe_docker)
  └── metabase/            ← NEW (single container)
```

---
---

# PART 1 — ERPNEXT

---

## 1.1 INSTALLATION

### Clone frappe_docker

```bash
cd /home/sog
git clone https://github.com/frappe/frappe_docker erpnext
cd erpnext
```

### Copy and configure environment

```bash
cp example.env .env
```

Edit `/home/sog/erpnext/.env` — set these values:

```env
ERPNEXT_VERSION=version-15
DB_PASSWORD=YourStrongDBPassword123
ADMIN_PASSWORD=YourAdminPassword123
SITE_NAME=myagency.localhost
```

### Configure custom port (18080)

Copy `pwd.yml` to a custom file so you don't modify the original:

```bash
cp pwd.yml custom.yml
```

Edit `/home/sog/erpnext/custom.yml` — find the `traefik` service and change the ports section:

```yaml
# Find this section in traefik service:
ports:
  - "18080:80"       # ← change from "80:80" to "18080:80"
```

Keep `--entrypoints.web.address=:80` unchanged (internal port stays 80).

### Start ERPNext

```bash
cd /home/sog/erpnext
docker compose -f custom.yml up -d
```

Wait 2–3 minutes. All containers initialize.

Check status:
```bash
docker compose -f custom.yml ps
```

All services should show `Up` or `healthy`.

### Create your site

```bash
docker compose -f custom.yml exec backend bench new-site myagency.localhost \
  --db-root-password YourStrongDBPassword123 \
  --admin-password YourAdminPassword123 \
  --install-app erpnext
```

Takes 3–5 minutes. Wait for the prompt to return.

### Access ERPNext

```
http://localhost:18080
Username: Administrator
Password: YourAdminPassword123
```

---

## 1.2 INITIAL WIZARD — COMPANY SETUP

When you first log in, the Setup Wizard runs. Fill in exactly:

| Field | Value |
|---|---|
| Language | English |
| Country | France |
| Time Zone | Europe/Paris |
| Currency | EUR — Euro |
| Company Name | Your agency name (e.g. Imad Agency) |
| Company Abbreviation | 3 letters (e.g. IMA) |
| What does your company do? | Services |
| Chart of Accounts | Standard — France |

Click **Complete Setup**. ERPNext configures your accounting foundation automatically.

---

## 1.3 ERPNEXT FULL ECOSYSTEM CONFIGURATION

### STEP A — System Settings

Go to: **Settings → System Settings**

| Setting | Value |
|---|---|
| Default Currency | EUR |
| Country | France |
| Time Zone | Europe/Paris |
| Date Format | DD-MM-YYYY |
| Language | English (or French) |

Save.

---

### STEP B — Company Profile

Go to: **Settings → Company → [Your Company Name]**

Fill in:
- **Company Name:** Your agency name
- **Default Currency:** EUR
- **Country:** France
- **Tax ID:** Your SIRET number (when available)
- **Default Receivable Account:** Debtors (auto-created)
- **Default Payable Account:** Creditors (auto-created)

Save.

---

### STEP C — Create Service Items (what you sell)

Go to: **Stock → Items → New Item** for each service:

**Item 1 — Monthly Retainer**
```
Item Name:     Monthly Agency Retainer
Item Code:     SRV-RETAINER
Item Group:    Services
UOM:           Month
Is Sales Item: Yes
```

**Item 2 — Google Ads Management**
```
Item Name:     Google Ads Campaign Management
Item Code:     SRV-GADS
Item Group:    Services
UOM:           Month
Is Sales Item: Yes
```

**Item 3 — SEO Services**
```
Item Name:     SEO & Content Services
Item Code:     SRV-SEO
Item Group:    Services
UOM:           Month
Is Sales Item: Yes
```

**Item 4 — Lead Generation System**
```
Item Name:     Automated Lead Generation
Item Code:     SRV-LEADGEN
Item Group:    Services
UOM:           Month
Is Sales Item: Yes
```

---

### STEP D — CRM Pipeline Configuration

Go to: **CRM → CRM Settings**

Set your **Lead Stages** (pipeline stages):

```
1. New Lead
2. Contacted
3. Qualified
4. Proposal Sent
5. Negotiation
6. Closed Won
7. Closed Lost
```

Set your **Lead Sources:**
```
- Cold Outreach (n8n)
- Referral
- LinkedIn
- Website
- Google Ads
- Word of Mouth
```

---

### STEP E — Create Customers (your clients)

Go to: **CRM → Customer → New** for each client:

**Client 1 — Roland Assurances**
```
Customer Name:    Roland Assurances
Customer Type:    Company
Customer Group:   Commercial
Territory:        France
Currency:         EUR
```

After saving, go to **Contacts** tab → Add Primary Contact:
- Contact name, email, phone of your main contact at Roland

Repeat for every client you have.

---

### STEP F — Create Projects (one per client)

Go to: **Projects → Project → New** for each client:

**Project: Roland Assurances — Lead Gen + Ads**
```
Project Name:       Roland Assurances — Lead Gen & Google Ads
Customer:           Roland Assurances
Status:             Open
Expected Start:     2026-04-18
Project Type:       External
Billing Method:     Monthly Rate
```

Go to **Tasks** tab → add recurring tasks:
```
- Weekly Google Ads optimization
- Monthly performance report
- Lead generation pipeline maintenance
- SEO content review
```

Repeat for every client.

---

### STEP G — Set Yourself as Employee (for timesheets)

Go to: **HR → Employee → New**

```
Employee Name:    Imad [Last Name]
Company:          Your Agency
Department:       Management
Designation:      CEO / Lead Consultant
Date of Joining:  [your start date]
```

Set your **Cost Per Hour** (what your time costs the business):
Go to: **HR → Employee → [Your Name] → Salary Details**
- Or define it in: **Projects → Project Settings → Billing Rate**

---

### STEP H — Timesheet Setup

Go to: **Projects → Timesheet → New**

Every day you work on a client, log:
```
Employee:       Imad [your name]
Company:        Your Agency
Timesheet Detail → Add Row:
  - Activity Type: Consulting / Development / Strategy
  - Project:       Roland Assurances — Lead Gen & Google Ads
  - Task:          Weekly Google Ads optimization
  - From Time:     09:00
  - To Time:       11:00
  - Hours:         2
  - Billing Rate:  [your hourly rate]
```

This auto-feeds the profitability calculation per client.

---

### STEP I — Recurring Sales Invoices

Go to: **Accounts → Sales Invoice → New**

**Invoice: Roland Assurances Monthly Retainer**
```
Customer:           Roland Assurances
Posting Date:       1st of each month
Due Date:           15th of each month

Items → Add Row:
  Item:             Monthly Agency Retainer (SRV-RETAINER)
  Qty:              1
  Rate:             [your monthly retainer amount]

Recurring:          ✅ Enable
Repeat On:          Monthly
Repeat Until:       [end of contract or leave blank]
```

Save and Submit. ERPNext auto-generates this invoice every month.

---

### STEP J — Expense Tracking Per Client

Go to: **Accounts → Expense → New Expense Claim**

Track every tool cost assigned to a client:

```
Employee:       Imad
Expenses Table → Add Row:
  Expense Date:   2026-04-18
  Expense Type:   Software Subscription
  Description:    Google Ads Tools - Roland Assurances
  Amount:         [cost]
  Project:        Roland Assurances — Lead Gen & Google Ads
```

This feeds into profitability per client automatically.

---

### STEP K — Custom Fields for Campaign Data

ERPNext allows custom fields on any DocType. Add campaign fields to the Customer record.

Go to: **Settings → Customize Form → Select: Customer**

Click **Add Field** and add these custom fields:

| Field Label | Field Type | Description |
|---|---|---|
| Monthly Ad Budget (EUR) | Currency | Client's Google Ads budget |
| Current CPL (EUR) | Currency | Current cost per lead |
| Current CPA (EUR) | Currency | Current cost per acquisition |
| Leads This Month | Int | Total leads generated |
| Contract Start Date | Date | When the contract started |
| Contract Renewal Date | Date | When it renews |
| Client Dashboard URL | Data | Metabase shareable link |
| Campaign Status | Select | Active / Paused / Testing |

Save. These fields now appear on every Customer record and feed into Metabase dashboards.

---

### STEP L — ERPNext Built-in Reports to Use

Go to: **Reports** — these are your weekly reads:

| Report | Where to Find | What It Tells You |
|---|---|---|
| Profit and Loss Statement | Accounts → Reports | Are you profitable? |
| Customer Ledger Summary | Accounts → Reports | What each client owes |
| Accounts Receivable Aging | Accounts → Reports | Who is late paying |
| Cash Flow Statement | Accounts → Reports | Cash in/out projection |
| Project Billing Summary | Projects → Reports | Revenue per project |
| Employee Billing Summary | Projects → Reports | Hours billed per client |
| Sales Invoice Trends | Accounts → Reports | MRR over time |
| Item-wise Sales Register | Accounts → Reports | Revenue by service type |

Bookmark these. Check every Monday.

---

### STEP M — ERPNext Workspace Setup (your home dashboard)

Go to: **Settings → Workspace**

Create a custom workspace called **"Agency Command"** with shortcuts to:
- Customer list
- Active Projects
- Outstanding Invoices
- Today's Timesheets
- Profit & Loss Report
- New Expense

This becomes your daily landing page in ERPNext.

---

## 1.4 DAILY ERPNEXT COMMANDS

```bash
# Start
cd /home/sog/erpnext && docker compose -f custom.yml up -d

# Stop
cd /home/sog/erpnext && docker compose -f custom.yml down

# View logs
docker compose -f custom.yml logs -f backend

# Restart one service
docker compose -f custom.yml restart backend

# Reset admin password
docker compose -f custom.yml exec backend \
  bench --site myagency.localhost set-admin-password NewPassword

# Backup site
docker compose -f custom.yml exec backend \
  bench --site myagency.localhost backup
```

---
---

# PART 2 — METABASE

---

## 2.1 INSTALLATION

### Create folder

```bash
mkdir /home/sog/metabase && cd /home/sog/metabase
```

### Create docker-compose.yml

Create file `/home/sog/metabase/docker-compose.yml`:

```yaml
services:
  metabase:
    image: metabase/metabase:latest
    container_name: metabase
    ports:
      - "19000:3000"
    volumes:
      - ./metabase-data:/metabase-data
    environment:
      MB_DB_TYPE: h2
      MB_DB_FILE: /metabase-data/metabase.db
      MB_SITE_NAME: "Agency Intelligence"
      MB_SITE_LOCALE: en
    restart: unless-stopped

volumes:
  metabase-data:
    driver: local
```

### Start Metabase

```bash
cd /home/sog/metabase
docker compose up -d
```

Wait 60–90 seconds.

### Access Metabase

```
http://localhost:19000
```

---

## 2.2 METABASE SETUP WIZARD

### Account creation

| Field | Value |
|---|---|
| First Name | Imad |
| Last Name | [your last name] |
| Email | your email |
| Company | Your Agency |
| Password | strong password |

### Usage question

Select: **Business Intelligence / Analytics**

---

## 2.3 DATABASE CONNECTIONS

### Connection 1 — ERPNext (MariaDB)

First find your ERPNext database name:

```bash
docker exec -it erpnext-db-1 mysql \
  -uroot -pYourStrongDBPassword123 \
  -e "SHOW DATABASES;" 2>/dev/null | grep -v "information_schema\|performance_schema\|mysql\|sys"
```

The result will show a database name like `_abc123def456` — that is your ERPNext site database.

In Metabase: **Admin → Databases → Add Database**

```
Database Type:    MySQL
Display Name:     ERPNext
Host:             host.docker.internal
Port:             3306
Database Name:    [the _abc123 name from above]
Username:         root
Password:         YourStrongDBPassword123
```

Click **Save** → Metabase scans all tables. You now have access to every ERPNext table.

---

### Connection 2 — Agency PostgreSQL (existing)

In Metabase: **Admin → Databases → Add Database**

```
Database Type:    PostgreSQL
Display Name:     Agency Data (n8n / Campaign)
Host:             host.docker.internal
Port:             5432
Database Name:    [check microhard-agency .env for DB name]
Username:         [check microhard-agency .env]
Password:         [check microhard-agency .env]
```

This gives Metabase access to data n8n writes into PostgreSQL (Google Ads metrics, leads, etc.)

---

## 2.4 BUILD THE 3 DASHBOARDS

---

### DASHBOARD 1 — Agency Command Center
*Your view. Private. Check every Monday.*

Go to: **New → Dashboard → Name: "Agency Command Center"**

#### Question 1 — MRR by Client (Bar Chart)

New Question → ERPNext database:
```sql
SELECT
  customer AS Client,
  SUM(grand_total) AS Monthly_Revenue
FROM `tabSales Invoice`
WHERE
  status IN ('Paid', 'Submitted')
  AND MONTH(posting_date) = MONTH(CURDATE())
  AND YEAR(posting_date) = YEAR(CURDATE())
GROUP BY customer
ORDER BY Monthly_Revenue DESC
```
Visualize as: **Bar Chart**
Title: "MRR by Client — This Month"

#### Question 2 — Total MRR (Number)

```sql
SELECT SUM(grand_total) AS Total_MRR
FROM `tabSales Invoice`
WHERE
  status IN ('Paid', 'Submitted')
  AND MONTH(posting_date) = MONTH(CURDATE())
  AND YEAR(posting_date) = YEAR(CURDATE())
```
Visualize as: **Number**
Title: "Total MRR"

#### Question 3 — Outstanding Invoices (Table)

```sql
SELECT
  customer AS Client,
  name AS Invoice_ID,
  grand_total AS Amount_EUR,
  due_date AS Due_Date,
  DATEDIFF(CURDATE(), due_date) AS Days_Overdue
FROM `tabSales Invoice`
WHERE status = 'Unpaid'
ORDER BY due_date ASC
```
Visualize as: **Table**
Title: "Outstanding Invoices"

#### Question 4 — Hours Billed This Month (Bar Chart)

```sql
SELECT
  project AS Client_Project,
  SUM(total_hours) AS Hours_Billed
FROM `tabTimesheet`
WHERE
  MONTH(start_date) = MONTH(CURDATE())
  AND YEAR(start_date) = YEAR(CURDATE())
GROUP BY project
ORDER BY Hours_Billed DESC
```
Visualize as: **Bar Chart**
Title: "Hours Billed per Client — This Month"

#### Question 5 — Revenue Trend (Line Chart)

```sql
SELECT
  DATE_FORMAT(posting_date, '%Y-%m') AS Month,
  SUM(grand_total) AS Revenue
FROM `tabSales Invoice`
WHERE
  status IN ('Paid', 'Submitted')
  AND posting_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY DATE_FORMAT(posting_date, '%Y-%m')
ORDER BY Month ASC
```
Visualize as: **Line Chart**
Title: "Revenue Trend — Last 6 Months"

#### Question 6 — Contract Renewal Alerts (Table)

```sql
SELECT
  customer_name AS Client,
  custom_contract_renewal_date AS Renewal_Date,
  DATEDIFF(custom_contract_renewal_date, CURDATE()) AS Days_Until_Renewal
FROM `tabCustomer`
WHERE
  custom_contract_renewal_date IS NOT NULL
  AND custom_contract_renewal_date >= CURDATE()
  AND DATEDIFF(custom_contract_renewal_date, CURDATE()) <= 60
ORDER BY Days_Until_Renewal ASC
```
Visualize as: **Table**
Title: "Contract Renewals — Next 60 Days"

**Arrange the dashboard:**
```
[ Total MRR ]  [ MRR by Client Bar Chart        ]
[ Outstanding Invoices Table                     ]
[ Hours Billed Bar Chart ] [ Revenue Trend Line  ]
[ Contract Renewals Table                        ]
```

---

### DASHBOARD 2 — Client Performance Dashboard
*One per client. Shareable public URL. Client bookmarks this.*

Go to: **New → Dashboard → Name: "Roland Assurances — Performance"**

> Note: Once n8n is configured to push Google Ads data into PostgreSQL,
> these questions pull live campaign data. Build the structure now,
> data flows in when n8n is connected.

#### Question 1 — Leads This Month (Number)

```sql
-- Once n8n writes leads to PostgreSQL table: campaign_leads
SELECT COUNT(*) AS Leads_This_Month
FROM campaign_leads
WHERE
  client = 'roland_assurances'
  AND MONTH(created_at) = MONTH(CURDATE())
  AND YEAR(created_at) = YEAR(CURDATE())
```
Visualize as: **Number**
Title: "Leads Generated — This Month"

#### Question 2 — Ad Spend vs. Budget (Progress Bar)

```sql
-- Once n8n writes Google Ads data to PostgreSQL table: campaign_metrics
SELECT
  SUM(cost_eur) AS Spend_To_Date,
  MAX(monthly_budget) AS Monthly_Budget,
  ROUND((SUM(cost_eur) / MAX(monthly_budget)) * 100, 1) AS Burn_Rate_Pct
FROM campaign_metrics
WHERE
  client = 'roland_assurances'
  AND MONTH(date) = MONTH(CURDATE())
```
Visualize as: **Progress Bar**
Title: "Ad Budget Utilization"

#### Question 3 — CPL Trend (Line Chart)

```sql
SELECT
  DATE(date) AS Day,
  ROUND(SUM(cost_eur) / NULLIF(SUM(conversions), 0), 2) AS CPL_EUR
FROM campaign_metrics
WHERE
  client = 'roland_assurances'
  AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
GROUP BY DATE(date)
ORDER BY Day ASC
```
Visualize as: **Line Chart**
Title: "Cost Per Lead — Daily Trend"

#### Question 4 — Campaign Funnel (Funnel Chart)

```sql
SELECT 'Impressions' AS Stage, SUM(impressions) AS Volume FROM campaign_metrics WHERE client='roland_assurances' AND MONTH(date)=MONTH(CURDATE())
UNION ALL
SELECT 'Clicks', SUM(clicks) FROM campaign_metrics WHERE client='roland_assurances' AND MONTH(date)=MONTH(CURDATE())
UNION ALL
SELECT 'Leads', SUM(conversions) FROM campaign_metrics WHERE client='roland_assurances' AND MONTH(date)=MONTH(CURDATE())
```
Visualize as: **Funnel**
Title: "Campaign Funnel — This Month"

#### Question 5 — Performance Summary (Table)

```sql
SELECT
  ROUND(SUM(cost_eur), 2) AS Total_Spend,
  SUM(clicks) AS Total_Clicks,
  SUM(conversions) AS Total_Leads,
  ROUND(AVG(cpc_eur), 2) AS Avg_CPC,
  ROUND(SUM(cost_eur) / NULLIF(SUM(conversions), 0), 2) AS CPL,
  ROUND((SUM(conversions) / NULLIF(SUM(clicks), 0)) * 100, 2) AS Conv_Rate_Pct
FROM campaign_metrics
WHERE
  client = 'roland_assurances'
  AND MONTH(date) = MONTH(CURDATE())
```
Visualize as: **Table**
Title: "Monthly Summary"

**Share with client:**
Dashboard → (3 dots) → **Sharing** → Enable public link → Copy URL → Send to Roland

---

### DASHBOARD 3 — Campaign Operations
*Your internal view. All clients. Daily check.*

Go to: **New → Dashboard → Name: "Campaign Operations — All Clients"**

#### Question 1 — All Clients Budget Status (Table)

```sql
SELECT
  client AS Client,
  SUM(cost_eur) AS Spend_To_Date,
  MAX(monthly_budget) AS Budget,
  ROUND((SUM(cost_eur) / NULLIF(MAX(monthly_budget), 0)) * 100, 1) AS Burn_Pct,
  ROUND(SUM(cost_eur) / NULLIF(SUM(conversions), 0), 2) AS CPL
FROM campaign_metrics
WHERE MONTH(date) = MONTH(CURDATE())
GROUP BY client
ORDER BY Burn_Pct DESC
```
Visualize as: **Table**
Title: "Budget Pacing — All Clients"

#### Question 2 — CPL Comparison (Bar Chart)

```sql
SELECT
  client AS Client,
  ROUND(SUM(cost_eur) / NULLIF(SUM(conversions), 0), 2) AS CPL_EUR
FROM campaign_metrics
WHERE MONTH(date) = MONTH(CURDATE())
GROUP BY client
ORDER BY CPL_EUR ASC
```
Visualize as: **Bar Chart**
Title: "CPL by Client — Best to Worst"

#### Question 3 — Total Leads All Clients (Number)

```sql
SELECT COUNT(*) AS Total_Leads
FROM campaign_leads
WHERE
  MONTH(created_at) = MONTH(CURDATE())
  AND YEAR(created_at) = YEAR(CURDATE())
```
Visualize as: **Number**
Title: "Total Leads — All Clients This Month"

---

## 2.5 METABASE ALERTS

Set up automatic alerts so you never miss a KPI breach.

Go to: **Any Question → Bell icon → Create Alert**

| Alert | Condition | Notify |
|---|---|---|
| CPL too high | CPL > €50 | Email immediately |
| Budget overspend | Burn Rate > 95% | Email immediately |
| No leads today | Leads today = 0 | Email at 5pm |
| Invoice overdue | Days_Overdue > 7 | Email every Monday |

---

## 2.6 SCHEDULED REPORTS (auto-email to clients)

Go to: **Dashboard → Subscriptions → New Subscription**

For each client dashboard:
```
Send to:    client@email.com
Schedule:   Weekly — Every Monday at 8:00am
Format:     PDF attachment
Message:    "Your weekly performance report from [Agency Name]"
```

This replaces manual reporting. Client receives their dashboard every Monday automatically.

---

## 2.7 DAILY METABASE COMMANDS

```bash
# Start
cd /home/sog/metabase && docker compose up -d

# Stop
cd /home/sog/metabase && docker compose down

# View logs
docker logs metabase -f

# Restart
docker compose restart metabase
```

---
---

# PART 3 — ECOSYSTEM CONNECTION MAP

---

## How ERPNext and Metabase connect

```
ERPNext MariaDB ──────────────────────► Metabase
  (business data)    direct DB read    (dashboards)
  Invoices, timesheets,
  customers, projects

Agency PostgreSQL ────────────────────► Metabase
  (campaign data)    direct DB read    (dashboards)
  Google Ads metrics,
  leads, SEO data

n8n ─────────────────────────────────► Agency PostgreSQL
  (automation)       writes nightly    (data layer)
  Pulls Google Ads API,
  GSC API, stores structured data
```

---

## n8n Pipelines to Build (after both tools are running)

### Pipeline 1 — Google Ads → PostgreSQL (nightly)

In n8n: **New Workflow → "Google Ads Nightly Sync"**

```
Schedule Trigger (11pm daily)
  → Google Ads Node (fetch campaign metrics)
  → Transform Node (map fields to table schema)
  → PostgreSQL Node (insert into campaign_metrics table)
```

PostgreSQL table schema:
```sql
CREATE TABLE campaign_metrics (
  id SERIAL PRIMARY KEY,
  client VARCHAR(100),
  date DATE,
  campaign_name VARCHAR(255),
  impressions INTEGER,
  clicks INTEGER,
  cost_eur DECIMAL(10,2),
  conversions INTEGER,
  cpc_eur DECIMAL(10,2),
  monthly_budget DECIMAL(10,2),
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Pipeline 2 — New Lead → ERPNext CRM (real-time)

```
Webhook Trigger (when new lead comes in)
  → ERPNext API Node (create Lead record)
  → PostgreSQL Node (insert into campaign_leads)
  → Telegram/Email Node (alert you instantly)
```

PostgreSQL table schema:
```sql
CREATE TABLE campaign_leads (
  id SERIAL PRIMARY KEY,
  client VARCHAR(100),
  lead_name VARCHAR(255),
  phone VARCHAR(50),
  email VARCHAR(255),
  source VARCHAR(100),
  campaign VARCHAR(255),
  status VARCHAR(50) DEFAULT 'new',
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Pipeline 3 — Weekly Client Report Email (Monday 8am)

```
Schedule Trigger (Every Monday 8am)
  → Metabase API (generate dashboard snapshot)
  → Email Node (send to client with PDF)
```

Note: Metabase Subscriptions (Step 2.6) handles this natively.
Use n8n only for custom logic or multiple recipients.

### Pipeline 4 — KPI Breach Alert (real-time)

```
Schedule Trigger (Every hour)
  → PostgreSQL Query (check CPL, burn rate)
  → IF Node: CPL > €50 OR burn > 95%
    → Telegram Node (alert your phone)
```

---

## Full Local Port Map

| Tool | URL | Purpose |
|---|---|---|
| **ERPNext** | http://localhost:18080 | Business OS — CRM, Finance, Projects |
| **Metabase** | http://localhost:19000 | Intelligence — All dashboards |
| Plane | http://localhost:33000 | Task management |
| n8n | http://localhost:5678 | Automation pipelines |
| Invoice Ninja | http://localhost:38080 | ⚠️ Decommission after ERPNext stable |

---

## Start Everything (morning routine)

```bash
# ERPNext
cd /home/sog/erpnext && docker compose -f custom.yml up -d

# Metabase
cd /home/sog/metabase && docker compose up -d

# Check all containers
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

---

## Decommission Invoice Ninja (when ERPNext is stable)

Once you have ERPNext handling invoicing and have migrated all client data:

```bash
# Stop Invoice Ninja containers
docker stop invoice-ninja invoice-ninja-nginx invoice-ninja-db
docker rm invoice-ninja invoice-ninja-nginx invoice-ninja-db

# Remove from microhard-agency compose (edit the docker-compose.yml)
# Delete the invoice-ninja service blocks
```

Free up port 38080 and the MariaDB container.

---

## VPS Migration (when ready)

The exact same files deploy on any VPS:

```bash
# On VPS:
git clone your-private-repo /srv/agency
cd /srv/agency/erpnext && docker compose -f custom.yml up -d
cd /srv/agency/metabase && docker compose up -d
```

Change ports back to standard (80/443) with SSL via Traefik on VPS.
All data migrates via ERPNext bench backup + restore.

---

## Quick Checklist — Setup Complete When:

```
ERPNext
  ☐ All containers running (docker compose -f custom.yml ps)
  ☐ Site created (bench new-site completed)
  ☐ Login works at localhost:18080
  ☐ Company configured (France, EUR)
  ☐ Service items created (retainer, gads, seo, leadgen)
  ☐ All clients entered as Customers
  ☐ One Project per client created
  ☐ Recurring invoices set up
  ☐ Yourself added as Employee
  ☐ Custom campaign fields added to Customer

Metabase
  ☐ Container running
  ☐ Login works at localhost:19000
  ☐ ERPNext database connected
  ☐ Agency PostgreSQL connected
  ☐ Dashboard 1 (Agency Command Center) built
  ☐ Dashboard 2 (Roland Assurances) built + shared
  ☐ Dashboard 3 (Campaign Operations) built
  ☐ Alerts configured
  ☐ Scheduled reports set up

n8n
  ☐ Google Ads pipeline built
  ☐ campaign_metrics table created in PostgreSQL
  ☐ campaign_leads table created in PostgreSQL
  ☐ KPI breach alert configured
```
