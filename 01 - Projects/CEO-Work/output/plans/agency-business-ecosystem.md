# Agency Business Ecosystem — Full Blueprint
**Date:** 2026-04-18
**Owner:** Imad
**Status:** Architecture Phase — v2.0 (Complete)

---

## THE CORE PROBLEM

Running an agency and serving clients without data is flying blind. Every decision made on gut feel is a decision made wrong. This ecosystem engineers complete visibility and decision-making infrastructure — for the agency itself, and for every client it serves.

The goal: **see the business like a chess grandmaster. Every move based on data. Nothing on guesswork.**

---

## THE TWO MACHINES TO INSTRUMENT

```
MACHINE 1 — THE AGENCY (your business)
  → Are you profitable overall?
  → Which clients make money, which drain you?
  → What is your capacity ceiling?
  → What is your pipeline worth?
  → What is your cash flow in 30/60/90 days?

MACHINE 2 — THE CLIENT (their business)
  → How many leads did we generate?
  → What did each lead cost?
  → What is the ROI on their spend?
  → Are we moving their numbers?
```

---

## THE 7 BUSINESS DOMAINS
*Every area of the agency. All must be instrumented.*

```
1. SALES          How clients find you and become paying clients
2. DELIVERY       How you execute the work you sold
3. FINANCE        How money moves — in, out, and what remains
4. INTELLIGENCE   How you see everything in real time
5. CLIENT         What clients experience and what they see
6. OPERATIONS     How the machine runs without constant attention
7. GROWTH         How the business scales beyond where it is today
```

---

## THE CHOSEN STACK

| Layer | Tool | Purpose |
|---|---|---|
| **Business OS** | ERPNext | CRM + Finance + Projects + Contracts + Reports |
| **Intelligence** | Metabase | All dashboards — agency + client + campaign |
| **Web Analytics** | Matomo | Client website traffic and conversion tracking |
| **Automation** | n8n | All data pipelines + alerts + scheduled reports |
| **Task Management** | Plane | Day-to-day delivery (faster UX than ERPNext projects) |
| **Contract Signing** | DocuSeal | Legal — client contract signing and storage |
| **Data Backbone** | PostgreSQL | ERPNext's native DB — Metabase reads directly |

**GitHub repos:**

| Tool     | GitHub                               |
| -------- | ------------------------------------ |
| ERPNext  | https://github.com/frappe/erpnext    |
| Metabase | https://github.com/metabase/metabase |
| Matomo   | https://github.com/matomo-org/matomo |
| n8n      | https://github.com/n8n-io/n8n        |
| Plane    | https://github.com/makeplane/plane   |
| DocuSeal | https://github.com/docuseal/docuseal |

---

## FULL ECOSYSTEM ARCHITECTURE

```
╔══════════════════════════════════════════════════════════════════════╗
║              AGENCY OPERATING SYSTEM v2.0 — COMPLETE MAP            ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ┌─────────────────────── DATA SOURCES ──────────────────────────┐  ║
║  │                                                               │  ║
║  │  Google Ads API    GSC/SEO API    Matomo    Manual Input      │  ║
║  │  (campaign data)   (rankings)    (traffic)  (finance/ops)     │  ║
║  └───────────────────────────┬───────────────────────────────────┘  ║
║                              │                                       ║
║                    ┌─────────▼──────────┐                           ║
║                    │   n8n AUTOMATION   │                           ║
║                    │  (data pipelines)  │                           ║
║                    └─────────┬──────────┘                           ║
║                              │                                       ║
║  ┌───────────────────────────▼───────────────────────────────────┐  ║
║  │                          ERPNext                              │  ║
║  │                                                               │  ║
║  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │  ║
║  │  │   CRM    │  │ PROJECTS │  │ FINANCE  │  │  SUPPORT    │  │  ║
║  │  │ Pipeline │  │ Tasks    │  │ Invoices │  │  Client     │  │  ║
║  │  │ Contacts │  │ Timeshts │  │ Expenses │  │  Comms      │  │  ║
║  │  │ Deals    │  │ Delivery │  │ P&L      │  │  History    │  │  ║
║  │  └──────────┘  └──────────┘  └──────────┘  └─────────────┘  │  ║
║  │                                                               │  ║
║  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │  ║
║  │  │ SELLING  │  │  BUYING  │  │    HR    │  │  ANALYTICS  │  │  ║
║  │  │ Quotes   │  │ Vendor   │  │ (future) │  │  Built-in   │  │  ║
║  │  │ Contracts│  │ Tool     │  │ Payroll  │  │  Reports    │  │  ║
║  │  │ Orders   │  │ Costs    │  │ Capacity │  │  100+       │  │  ║
║  │  └──────────┘  └──────────┘  └──────────┘  └─────────────┘  │  ║
║  │                                                               │  ║
║  │              [PostgreSQL — Single Source of Truth]            │  ║
║  └───────────────────────────┬───────────────────────────────────┘  ║
║                              │                                       ║
║                    ┌─────────▼──────────┐                           ║
║                    │     Metabase       │                           ║
║                    │  (intelligence     │                           ║
║                    │   layer)           │                           ║
║                    └────────┬───────────┘                           ║
║                             │                                        ║
║            ┌────────────────┼────────────────┐                      ║
║            ▼                ▼                ▼                      ║
║   ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐           ║
║   │  AGENCY      │ │  CLIENT      │ │  CAMPAIGN        │           ║
║   │  DASHBOARD   │ │  DASHBOARD   │ │  DASHBOARD       │           ║
║   │  (your view) │ │  (they see)  │ │  (ads/SEO/ops)   │           ║
║   └──────────────┘ └──────────────┘ └──────────────────┘           ║
║                                                                      ║
║   ┌───────────────── PARALLEL TOOLS ────────────────────────────┐   ║
║   │  Plane (delivery)   Matomo (web analytics)   DocuSeal (legal│   ║
║   └─────────────────────────────────────────────────────────────┘   ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## DOMAIN COVERAGE MAP
*Zero gaps. Every business domain instrumented.*

| Domain | Covered By | What It Tracks |
|---|---|---|
| **Sales** | ERPNext CRM + Selling | Leads, pipeline, quotes, close rate, CAC |
| **Delivery** | ERPNext Projects + Plane | Tasks, timesheets, deadlines, utilization |
| **Finance** | ERPNext Accounts + Buying | Invoices, expenses, P&L, cash flow, margins |
| **Intelligence** | Metabase (3 dashboards) | Every KPI visualized and queryable |
| **Client** | Metabase links + DocuSeal | Live dashboards + signed contracts |
| **Operations** | n8n + ERPNext timesheets | Automation health, hours, tool costs |
| **Growth** | Metabase LTV:CAC + pipeline | Scaling signals, capacity ceiling, forecast |
| **Legal** | DocuSeal + ERPNext Sales Orders | Contract signing, storage, renewal dates |

---

## THE BUSINESS MATH LAYER
*Define before building any tool. These numbers run everything.*

### Agency Math

| Metric | Formula | Target |
|---|---|---|
| MRR | Sum of all client retainers | Track monthly |
| Cost of Delivery (COD) | Hours × rate + tools + contractors | Per client |
| Gross Profit per Client | Retainer − COD | Must be positive |
| Agency Gross Margin | Total Gross Profit / MRR | > 60% |
| Client LTV | Avg retainer × avg months retained | Maximize |
| Client CAC | Time + spend to close each client | Minimize |
| LTV:CAC Ratio | LTV / CAC | Must exceed 3:1 |
| Capacity Ceiling | Max clients at current team size | Know this number |
| Utilization Rate | Billable hours / total hours worked | > 75% |
| Cash Flow Forecast | Confirmed revenue − confirmed costs | 30/60/90 days |

### Client Math (per client)

| Metric | Formula | Target |
|---|---|---|
| Cost Per Click (CPC) | Ad Spend / Clicks | Platform benchmark |
| Click-Through Rate (CTR) | Clicks / Impressions | > industry average |
| Cost Per Lead (CPL) | Ad Spend / Leads Generated | < Client LTV × 10% |
| Lead-to-Call Rate | Booked Calls / Total Leads | > 20% |
| Close Rate | New Clients / Booked Calls | Track per client |
| Cost Per Acquisition (CPA) | Ad Spend / New Clients Won | < Client LTV × 30% |
| Client ROI | (LTV × New Clients) / Ad Spend | Must exceed 3:1 |
| Ad Burn Rate | Spend to Date / Monthly Budget | Track weekly |

---

## THE 3 METABASE DASHBOARDS

### Dashboard 1 — Agency Command Center
*Your view. Check every Monday morning.*

```
FINANCIAL HEALTH
  ✦ MRR total + trend (↑↓ vs last month)
  ✦ Gross margin % per client + overall
  ✦ Net profit this month
  ✦ Cash in bank + 30-day forecast
  ✦ Outstanding invoices (amount + days overdue)

CLIENT HEALTH
  ✦ Active clients + capacity remaining
  ✦ Client health score (tenure + margin + delivery status)
  ✦ Churn risk flags (no comms >14 days, declining results)
  ✦ Contract renewal dates (next 60 days)

PIPELINE
  ✦ Prospects in pipeline + value
  ✦ Probability-weighted pipeline value
  ✦ Average time to close
  ✦ New revenue needed to hit monthly target

OPERATIONS
  ✦ Hours billed vs. hours worked (utilization rate)
  ✦ Overdue deliverables
  ✦ Tool costs this month vs. budget
  ✦ n8n automation health (running / failed)
```

### Dashboard 2 — Client Performance Dashboard
*Client sees this. Shareable Metabase URL. Updated automatically.*

```
LEAD GENERATION
  ✦ Leads generated this month vs. target
  ✦ Cost Per Lead (CPL) trend
  ✦ Lead source breakdown
  ✦ Lead volume over time (chart)

CAMPAIGN PERFORMANCE
  ✦ Ad spend vs. budget (% burn rate)
  ✦ Impressions → Clicks → Leads funnel
  ✦ CPC and CTR trend
  ✦ Top performing ads and keywords

BUSINESS IMPACT
  ✦ Estimated pipeline value from leads
  ✦ Cost Per Acquisition (CPA)
  ✦ ROI vs. target
  ✦ Month-over-month improvement %
```

### Dashboard 3 — Campaign Operations
*Your internal view. All clients in one place.*

```
  ✦ All clients' ad spend in one view
  ✦ Budget pacing per client (on track / over / under)
  ✦ CPL by client ranked best to worst
  ✦ SEO keyword ranking movements
  ✦ Content publish schedule vs. actual
  ✦ Lead generation pipeline health per client
```

---

## DATA FLOW MAP

### Inbound (into ERPNext + PostgreSQL)

```
Google Ads API
  → n8n pulls nightly
  → Spend, clicks, impressions, conversions per campaign
  → Stored in ERPNext custom fields or PostgreSQL table
  → Feeds Metabase Campaign + Client dashboards

Google Search Console API
  → n8n pulls weekly
  → Keyword rankings, impressions, clicks
  → Stored in PostgreSQL
  → Feeds Metabase Client Dashboard (SEO section)

Matomo
  → Installed on client websites
  → Traffic, sessions, goal conversions, bounce rate
  → Metabase reads Matomo DB directly
  → Feeds Metabase Client Dashboard (traffic section)

Time Tracking
  → ERPNext Timesheets (log hours per client per task)
  → Auto-calculates cost of delivery
  → Feeds profitability per client in real time

Invoicing
  → ERPNext Accounts module
  → Invoice created → sent → paid → reconciled
  → Feeds MRR and cash flow dashboards

Expenses
  → ERPNext Expense module
  → Every cost assigned to a client or overhead
  → Auto-feeds P&L per client
```

### Outbound (from system to world)

```
Metabase  → Shareable URL → Client bookmarks their live dashboard
ERPNext   → Invoice PDF   → Client email (automated on due date)
n8n       → Weekly report → Client inbox every Monday
n8n       → KPI breach alert → Your Telegram/email instantly
n8n       → New lead from Google Ads → ERPNext CRM (auto-created)
DocuSeal  → Contract link → Client signs → stored in ERPNext
```

---

## ERPNext MODULES IN USE

| Module | What You Use It For |
|---|---|
| **CRM** | Lead pipeline, prospect tracking, deal stages |
| **Selling** | Quotations, sales orders, client contracts |
| **Accounts** | Invoicing, expenses, P&L, balance sheet, cash flow |
| **Projects** | Project tracking, timesheets, billing by project |
| **Buying** | Tool subscriptions, contractor costs, vendor management |
| **Support** | Client communication log, tickets, issue tracking |
| **HR** | Capacity planning now, payroll when you hire |
| **Analytics** | 100+ built-in reports, custom report builder |

---

## BUILD SEQUENCE

```
WEEK 1 — FINANCIAL FOUNDATION (spreadsheet first, no tools)
  → Every client: retainer, hours, tool costs, gross margin
  → Identify profitable vs. loss-making clients TODAY
  → Define your hourly cost rate

WEEK 2-3 — ERPNext DEPLOYMENT
  → Deploy via Docker on VPS
  → Configure: company, chart of accounts, tax settings
  → Enter all clients as Customers
  → Set up recurring invoices per client
  → Create one Project per client
  → Begin logging timesheets

WEEK 3-4 — DATA CONNECTIONS
  → n8n: Google Ads API → PostgreSQL (ERPNext DB)
  → n8n: GSC API → PostgreSQL
  → Install Matomo on client websites

MONTH 2 — METABASE DEPLOYMENT
  → Deploy Metabase via Docker
  → Connect to ERPNext PostgreSQL database
  → Build Dashboard 1: Agency Command Center
  → Build Dashboard 2: First client (Roland)
  → Build Dashboard 3: Campaign Operations

MONTH 2 — LEGAL LAYER
  → Deploy DocuSeal
  → Create contract template
  → Connect via n8n: signed → ERPNext deal closed

MONTH 2-3 — AUTOMATION LAYER
  → n8n: nightly Google Ads sync
  → n8n: weekly client report email
  → n8n: KPI breach alerts
  → n8n: new lead → ERPNext CRM auto-create

MONTH 3 — OPTIMIZATION
  → Review all dashboards for missing data
  → Add ERPNext custom fields as needed
  → Refine KPI targets based on real data
  → Build growth forecasting model in Metabase
```

---

## INFRASTRUCTURE

```
1 VPS (~€30-40/month)
  ├── ERPNext (Docker)          — port 8000
  ├── Metabase (Docker)         — port 3000
  ├── n8n (Docker)              — port 5678
  ├── Matomo (Docker)           — port 8080
  ├── Plane (Docker)            — port 3001
  └── DocuSeal (Docker)         — port 3002

All running on Docker Compose.
One server. Zero licensing fees. Full ownership of all data.
```

---

## TOOL REFERENCE (Full Catalog)

### Chosen Stack

| Tool | GitHub | Purpose |
|---|---|---|
| ERPNext | https://github.com/frappe/erpnext | Business OS |
| Metabase | https://github.com/metabase/metabase | BI + Dashboards |
| Matomo | https://github.com/matomo-org/matomo | Web Analytics |
| n8n | https://github.com/n8n-io/n8n | Automation |
| Plane | https://github.com/makeplane/plane | Task Management |
| DocuSeal | https://github.com/docuseal/docuseal | Contract Signing |

### All-in-One Alternatives (if ERPNext is reconsidered)

| Tool | GitHub | Notes |
|---|---|---|
| Odoo Community | https://github.com/odoo/odoo | Most modular |
| Dolibarr | https://github.com/Dolibarr/dolibarr | Lightest, fastest setup |
| YetiForce | https://github.com/YetiForceCompany/YetiForceCRM | Most feature-dense |
| Axelor | https://github.com/axelor/axelor-open-suite | Best workflow automation |
| Twenty | https://github.com/twentyhq/twenty | Best UI, CRM-first |

### Best-of-Breed Alternatives (per component)

| Component | Tool | GitHub |
|---|---|---|
| CRM | Twenty | https://github.com/twentyhq/twenty |
| Finance | Akaunting | https://github.com/akaunting/akaunting |
| Finance alt | Invoice Ninja | https://github.com/invoiceninja/invoiceninja |
| BI alt | Apache Superset | https://github.com/apache/superset |
| BI alt | Grafana | https://github.com/grafana/grafana |
