# FULL GOOGLE ADS LEAD GENERATION ECOSYSTEM — ARCHITECTURE DOCUMENT
**Project:** RA-Project | **Date:** April 20, 2026 | **Designed by:** CAI + MGI Council

---

## ECOSYSTEM MAP — THE 6 LAYERS

```
┌─────────────────────────────────────────────────────────┐
│              LAYER 6: ORCHESTRATION BRAIN               │
│         Claude Code + MCP Servers (AI Command Layer)    │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│              LAYER 5: INTELLIGENCE & OPTIMIZATION       │
│    Dev Assistant + GA4 + Looker Studio + Feedback Loop  │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│              LAYER 4: AUTOMATION ENGINE                  │
│        Google Ads Scripts + Make.com/n8n + Webhooks     │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│              LAYER 3: LEAD CAPTURE & CRM                │
│        Landing Pages + Lead Forms + CRM + Email         │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│              LAYER 2: TRACKING & ATTRIBUTION            │
│        GTM + GA4 + Conversion Tracking + Call Track     │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│              LAYER 1: TRAFFIC ACQUISITION               │
│              Google Ads Platform (Campaigns)            │
└─────────────────────────────────────────────────────────┘
```

---

## THE COMPLETE TOOL LIST

| # | Tool | Layer | Type | Cost |
|---|------|-------|------|------|
| 1 | Google Ads Platform | L1 | SaaS | Pay-per-click |
| 2 | Google Tag Manager | L2 | Free | Free |
| 3 | Google Ads Conversion Tracking | L2 | Free | Free |
| 4 | Google Analytics 4 | L2 | Free | Free |
| 5 | CallRail *(optional)* | L2 | SaaS | ~$45/mo |
| 6 | Landing Page Builder | L3 | SaaS | ~$97-297/mo |
| 7 | CRM (GoHighLevel) | L3 | SaaS | $97-297/mo |
| 8 | Google Ads Scripts | L4 | Free | Free |
| 9 | Make.com or n8n | L4 | SaaS/OSS | $9/mo or free |
| 10 | **Google Ads API Dev Assistant** | L5 | Open Source | **Free** |
| 11 | Google Looker Studio | L5 | Free | Free |
| 12 | Google Search Console | L5 | Free | Free |
| 13 | **Google Ads MCP Server** | L6 | Open Source | **Free** |
| 14 | **Claude Code (this)** | L6 | CLI | Subscription |
| 15 | **Gemini CLI** | L6 | CLI | Free |

---

## LAYER-BY-LAYER BREAKDOWN

---

### LAYER 1 — TRAFFIC ACQUISITION

---

#### 🟥 Tool 1: Google Ads Platform

**What it is:** The core advertising platform — where you create campaigns, write ads, set bids, target audiences, and spend money to generate clicks.

**Why you need it:** This is the engine. Everything else in this ecosystem exists to feed it intelligence, track its results, and optimize its performance. Without this, there's no traffic to convert.

**Role in ecosystem:** The money-in/leads-out machine. It consumes budget and produces clicks → these clicks go to your landing pages → tracked by Layer 2 → optimized by Layer 5 → managed programmatically by Layer 6.

**Campaign types for lead gen:**
- **Search campaigns** — High-intent keywords, people actively searching for your offer
- **Performance Max** — Google's AI-driven multi-channel (Search + Display + YouTube + Gmail)
- **Display remarketing** — Re-engage website visitors who didn't convert
- **Demand Gen** — Visual ads for awareness (YouTube, Discover, Gmail)

**How to use it:**
```
1. Google Ads Account → New Campaign → Lead Generation goal
2. Choose: Search (primary for LeadGen)
3. Set: Budget, bids, target CPA or Maximize Conversions
4. Write: Headlines (15), Descriptions (4) for Responsive Search Ads
5. Target: Keywords + Audiences + Locations
6. Connect: Conversion actions from Layer 2
```

**Where it sits in RA-Project:** `02-slm-machine/traffic/`

---

### LAYER 2 — TRACKING & ATTRIBUTION

> *"You cannot optimize what you cannot measure. And most people measure the wrong things."* — Trace

---

#### 🟧 Tool 2: Google Tag Manager (GTM)

**What it is:** A free tag management system that lets you deploy and manage all tracking scripts on your website from a single interface — without touching code.

**Why you need it:** Without GTM, every time you need to add or modify tracking (conversion events, GA4 events, heatmap tools, etc.), you need a developer. With GTM, you manage everything visually. It's also the delivery mechanism for all conversion signals.

**Role in ecosystem:** The tracking infrastructure backbone. It sits between your website and every analytics/tracking tool. GA4 fires through it. Google Ads conversion tags fire through it. Every custom event you define flows through GTM first.

**How to use it:**
```
1. Create GTM account → get container snippet
2. Install snippet in <head> and <body> of landing page
3. Create Tags:
   - GA4 Configuration tag (always fires)
   - Google Ads Conversion tag (fires on thank-you page)
   - Lead form submission event
4. Create Triggers:
   - Page View (all pages)
   - Form Submission (confirmation page or thank-you URL)
   - Button Click (CTA clicks)
5. Publish container
```

**Where it sits in RA-Project:** `00-foundation/tracking/`

---

#### 🟧 Tool 3: Google Ads Conversion Tracking

**What it is:** The conversion measurement system built into Google Ads that attributes leads (form submissions, calls, purchases) back to specific ads, keywords, and campaigns.

**Why you need it:** Without this, Google's algorithm is flying blind. Smart Bidding (Target CPA, Maximize Conversions) requires conversion data to optimize. No conversion tracking = no intelligent bidding = wasted spend.

**Role in ecosystem:** The feedback signal from Layer 3 (lead captured) back to Layer 1 (which ad/keyword/audience generated it). This is what closes the attribution loop.

**How to set up:**
```
1. Google Ads → Tools → Conversions → New Conversion Action
2. Type: Website
3. Name: "Lead Form Submission" or "Phone Call"
4. Value: Assign a value (e.g., $50 per lead)
5. Count: "One" (for lead gen, not e-commerce)
6. Click-through window: 30 days
7. Import Conversion Tag → deploy via GTM
```

**Enhanced Conversions (critical):**
```
Enable enhanced conversions to send hashed email/phone from 
lead forms → dramatically improves attribution accuracy with 
privacy-safe matching
```

**Where it sits in RA-Project:** `00-foundation/tracking/`

---

#### 🟧 Tool 4: Google Analytics 4 (GA4)

**What it is:** Google's behavioral analytics platform. Tracks every user action on your website — page views, scroll depth, form interactions, session duration, traffic sources, user journeys.

**Why you need it:** Google Ads tells you which keywords generate clicks and conversions. GA4 tells you *what happens between the click and the conversion* — bounce rates, time on page, which sections users scroll past, where they drop off. This is your landing page optimization data.

**Role in ecosystem:** The behavioral intelligence layer. Feeds insights to the Dev Assistant for analysis, feeds audiences back to Google Ads for remarketing, and feeds the feedback loop (Trace's 3-layer diagnosis) for body/page optimization.

**Key configurations:**
```
1. Create GA4 property → link to Google Ads account
2. Configure events:
   - page_view (automatic)
   - scroll (automatic)
   - form_start (custom)
   - form_submit (custom → mark as conversion)
   - click (automatic for outbound)
3. Import GA4 audiences into Google Ads:
   - "Visited pricing page, no conversion" → remarketing
   - "High engagement (2min+ on page)" → bid boost
4. Enable Google Signals for cross-device tracking
```

**Where it sits in RA-Project:** `01-intelligence/SS2-performance/`

---

#### 🟧 Tool 5: CallRail *(Conditional — if you run call-based leads)*

**What it is:** Call tracking platform that assigns unique phone numbers to traffic sources, so you know which campaign/keyword/ad generated a phone call lead.

**Why you need it:** If your lead gen includes phone calls (high-ticket services, medical, legal, home services), Google's native call tracking only tells you a call happened. CallRail tells you the keyword, duration, recording, and whether it was a qualified lead.

**Role in ecosystem:** Closes attribution for call leads. Sends conversion data back to Google Ads. Feeds call quality data for bid optimization.

**Only install if:** Your offer generates phone call leads. Otherwise skip.

---

### LAYER 3 — LEAD CAPTURE & CRM

> *"The click is just the start. The landing page is where the money is made or lost."* — Aura

---

#### 🟨 Tool 6: Landing Page Builder

**What it is:** A dedicated tool for building high-converting, fast-loading landing pages that are separate from your main website.

**Why you need it:** Your main website is built for many goals (brand, SEO, navigation). A landing page is built for ONE goal: get the visitor to submit their information. Dedicated landing pages convert 3-5x better than directing ads to homepages.

**Recommended options:**

| Tool | Best For | Price |
|------|---------|-------|
| **Unbounce** | A/B testing, AI copy | $99/mo |
| **Leadpages** | Simple, fast deployment | $49/mo |
| **ClickFunnels** | Full funnel building | $97/mo |
| **GoHighLevel** | All-in-one (includes CRM) | $97/mo |
| **Framer/Webflow** | Custom, developer-grade | $20-39/mo |

**Role in ecosystem:** The conversion point between ad click (Layer 1) and lead data (Layer 3). Must fire GTM tracking on form submission. Must load under 2 seconds. Must have one CTA.

**Page anatomy for lead gen:**
```
1. Headline → matches ad message exactly (message match)
2. Sub-headline → specific benefit/outcome
3. Hero image or video (social proof or product demo)
4. Benefit bullets (3-5 max)
5. Lead form (Name + Email + Phone minimum)
6. Trust signals (logos, reviews, certifications)
7. CTA button (contrast color, action verb)
```

**Where it sits in RA-Project:** `02-slm-machine/funnels/`

---

#### 🟨 Tool 7: CRM — GoHighLevel (Recommended)

**What it is:** Customer Relationship Management platform that captures lead data, manages follow-up, and tracks lead status through your sales pipeline.

**Why you need it (non-negotiable):** When a lead submits a form, that data must go somewhere actionable. A CRM: captures the lead, assigns it to a sales rep, triggers automated follow-up (email/SMS), tracks deal stage, and reports on conversion rate from lead to customer.

**Why GoHighLevel specifically:**
- All-in-one: CRM + landing pages + email + SMS + pipeline
- Native webhook integrations with Google Ads (offline conversions)
- White-label capable for agency use
- Replace 5+ separate tools with one

**Role in ecosystem:** The lead repository and nurture engine. All form submissions flow here. Closed deals feed back to Google Ads as offline conversions (critical for smart bidding optimization on *quality* leads, not just form fills).

**Critical integration — Offline Conversion Imports:**
```
Lead submits form → CRM records lead
Sales rep marks lead as "Closed Won" → 
CRM sends offline conversion event back to Google Ads →
Google Ads learns which keywords generate PAYING customers,
not just form fills → bids optimize for revenue, not leads
```

**How to set up:**
```
1. GHL → Pipelines → Create "Google Ads Leads" pipeline
2. Stages: New Lead → Contacted → Qualified → Proposal → Closed
3. Connect form webhook from landing page
4. Set up automation: 
   - Immediate email: "We received your request"
   - 5-min SMS: "Hi [name], saw your inquiry..."
   - Day 1 email: Value content
5. Connect "Closed Won" trigger → Google Ads Offline Import
```

**Where it sits in RA-Project:** `02-slm-machine/conversion/`

---

### LAYER 4 — AUTOMATION ENGINE

> *"Automation isn't about replacing people. It's about making the machine run while you sleep."* — Felix

---

#### 🟩 Tool 8: Google Ads Scripts

**What it is:** JavaScript-based automation built directly into Google Ads. Runs on a schedule (hourly/daily/weekly) to perform automated actions — pausing underperformers, adjusting bids, sending alerts, generating reports.

**Why you need it:** Manual Google Ads management doesn't scale. Scripts let you automate repetitive optimization tasks inside the platform itself without API credentials or external infrastructure.

**Role in ecosystem:** In-platform automation. Executes changes directly in Google Ads without needing external API calls. Lighter weight than the full API for routine tasks.

**Essential scripts to deploy:**

```javascript
// 1. AUTOMATED BUDGET ALERTS
// Fires email if daily spend exceeds threshold
function checkBudget() {
  var campaign = AdsApp.campaigns().get().next();
  if (campaign.getStats().getCost() > 500) {
    MailApp.sendEmail("you@email.com", "Budget Alert", "Over $500 today");
  }
}

// 2. PAUSE LOW-QUALITY SEARCH TERMS
// Pauses keywords with 100+ clicks and 0 conversions
function pauseWastedSpend() {
  var keywords = AdsApp.keywords()
    .withCondition("Clicks > 100")
    .withCondition("Conversions < 1")
    .get();
  while (keywords.hasNext()) {
    keywords.next().pause();
  }
}

// 3. DAYPARTING AUTOMATION
// Reduce bids 50% during low-converting hours
```

**Where to find scripts:** `scripts.google.com/ads` library

**Where it sits in RA-Project:** `03-automation/v1-deployment/`

---

#### 🟩 Tool 9: Make.com (or n8n for self-hosted)

**What it is:** Visual workflow automation platform. Connect any tools that have APIs or webhooks — Google Ads, GoHighLevel, Slack, Google Sheets, email — into automated flows triggered by events.

**Why you need it:** The glue between tools. When a lead converts in CRM → Make sends offline conversion to Google Ads. When performance drops below threshold → Make sends Slack alert and drafts diagnostic report. When new campaign launches → Make creates tracking spreadsheet. The automation infrastructure that connects all layers.

**Role in ecosystem:** The inter-layer data bus. Moves data between Layer 2 (tracking), Layer 3 (CRM), Layer 5 (reporting), and Layer 6 (AI tools). Eliminates manual data transfer between platforms.

**Key flows to build:**

```
FLOW 1: Lead Capture → CRM → Notification
Trigger: New form submission (Webhook)
Action 1: Create contact in GoHighLevel
Action 2: Send SMS to lead (GHL)
Action 3: Post to Slack #new-leads

FLOW 2: Closed Deal → Google Ads Offline Conversion
Trigger: Deal stage = "Closed Won" in GHL
Action 1: Format conversion data
Action 2: Upload to Google Ads Conversions API
Action 3: Log to Google Sheets

FLOW 3: Weekly Performance Pull
Trigger: Every Monday 8am
Action 1: Run query via Dev Assistant (read performance)
Action 2: Format into report
Action 3: Email to client/team

FLOW 4: Budget Threshold Alert
Trigger: Google Ads spend > 80% of daily budget
Action 1: Slack alert with spend breakdown
Action 2: Log to report dashboard
```

**Make vs n8n:**
- **Make.com**: Easier visual interface, hosted, $9/mo → Best for most users
- **n8n**: Self-hosted, unlimited runs, more technical → Best if you want full control

**Where it sits in RA-Project:** `03-automation/v1-deployment/`

---

### LAYER 5 — INTELLIGENCE & OPTIMIZATION

> *"Data without a feedback loop is just expensive history."* — Trace

---

#### 🔵 Tool 10: Google Ads API Developer Assistant *(Already Installed)*

**What it is:** Open-source Gemini CLI extension that converts natural language to executable GAQL queries and client library code.

**Why you need it:** The Google Ads UI only shows you what Google wants you to see. The API gives you raw access to everything — every keyword, bid, impression, conversion, quality score — and the Developer Assistant makes that access conversational.

**Role in ecosystem:** The data interrogation layer. Instead of manually navigating through the Google Ads UI to find performance insights, you ask questions in plain English and receive executable queries and data. Feeds insights to the optimization loop and generates code for the automation layer.

**How it integrates with RA-Project:**

```bash
# From your RA-Project directory (already cloned):
cd google-ads-api-developer-assistant
gemini

# Example queries you'll run:
"Show me all keywords with Quality Score below 5 and spend above $20"
"What campaigns had CPA above $80 last 14 days?"
"Compare CTR by ad group this week vs last week"
"Show me search terms that triggered 'broad match' keywords with 0 conversions"
"Which audiences have the highest conversion rate on remarketing campaigns?"
```

**Output feeds to:**
- `output/reports/` — performance analysis
- `03-automation/v2-reporting/` — automated reporting
- Layer 6 (Claude Code) for agentic decision-making

**Where it sits in RA-Project:** `/google-ads-api-developer-assistant/` (root)

---

#### 🔵 Tool 11: Google Looker Studio

**What it is:** Free Google-native data visualization and dashboard tool. Connects to Google Ads, GA4, Google Sheets, BigQuery, and dozens of other sources to build live reporting dashboards.

**Why you need it:** Raw data in spreadsheets or API outputs is not usable for decisions at a glance. Looker Studio turns that data into visual dashboards — campaign performance, lead volume trends, CPA by channel, ROAS over time — updated in real-time.

**Role in ecosystem:** The visualization layer for Layer 5 intelligence. Takes data from Google Ads (direct connector), GA4, and Google Sheets (Make.com outputs) and presents it as the operational dashboard you and clients see daily.

**Dashboard to build:**

```
DASHBOARD 1: Campaign Performance (Daily)
- Total spend | Impressions | Clicks | CTR | Avg CPC
- Conversions | CPA | Conversion Rate
- Campaign-level breakdown table
- 30-day trend chart

DASHBOARD 2: Lead Quality (Weekly)
- Leads generated | Leads qualified | Leads closed
- Cost per qualified lead | Cost per acquisition
- Top-performing keywords by closed revenue
- Geographic heatmap

DASHBOARD 3: Account Health (Weekly)
- Quality Score distribution
- Budget utilization
- Search Impression Share
- Auction insights (vs competitors)
```

**Where it sits in RA-Project:** `03-automation/v2-reporting/`

---

#### 🔵 Tool 12: Google Search Console

**What it is:** Google's free tool showing how your website appears in organic search — queries, clicks, impressions, average position, and crawl/indexing status.

**Why you need it in a paid ads ecosystem:** Most people ignore Search Console for paid ads. Mistake. It shows you what search queries people are using to find you organically — which is a goldmine for paid keyword discovery. If you're ranking organically for a keyword, you can choose to NOT bid on it (save budget) or bid on it anyway (dominate the SERP). It also reveals negative keyword opportunities.

**Role in ecosystem:** Intelligence feeder. Queries from Search Console → keyword research for Google Ads campaigns. Top-performing organic pages → landing page templates for paid campaigns.

**Where it sits in RA-Project:** `01-intelligence/SS1-market/`

---

### LAYER 6 — ORCHESTRATION BRAIN (AI Command Layer)

> *"This is where the machine becomes intelligent. Not just automated — intelligent."* — CEO

---

#### 🟣 Tool 13: Google Ads MCP Server

**What it is:** Open-source Model Context Protocol server that gives AI assistants (Claude, Gemini, ChatGPT) structured, authenticated access to the Google Ads API as callable tools.

**GitHub:** https://github.com/google-marketing-solutions/google_ads_mcp

**Why you need it:** The Developer Assistant is for humans using Gemini CLI interactively. The MCP Server is for AI agents (Claude Code) to call Google Ads API operations programmatically as part of multi-step agentic workflows.

**Role in ecosystem:** The AI-to-API bridge. With MCP installed and configured, Claude Code can:
- Query campaign performance data in real-time
- Identify underperforming campaigns autonomously
- Generate optimization recommendations
- Trigger Make.com automations via API
- Write analysis reports directly to `output/reports/`

**How it differs from Developer Assistant:**

| | Dev Assistant | MCP Server |
|--|---------------|------------|
| **Used by** | Human via Gemini CLI | AI agents (Claude, Gemini) |
| **Interface** | Interactive terminal | Tool calls from AI |
| **Trigger** | Manual prompt | Autonomous or commanded |
| **Execution** | Gemini CLI runtime | Agent runtime |
| **Best for** | Developer workflows | Agentic automation |

**Installation:**
```bash
# Clone
git clone https://github.com/google-marketing-solutions/google_ads_mcp
cd google_ads_mcp

# Install dependencies
pip install -r requirements.txt

# Configure credentials (same OAuth as Dev Assistant)
cp .env.example .env
# Edit .env with your developer token + OAuth credentials

# Add to Claude Code's MCP config
# ~/.claude/settings.json → mcpServers section:
{
  "mcpServers": {
    "google-ads": {
      "command": "python",
      "args": ["/path/to/google_ads_mcp/server.py"]
    }
  }
}
```

**Agentic workflows you'll enable:**
```
"Analyze last week's campaigns and identify the 3 worst 
performing ad groups by CPA. Pause them and write a 
diagnostic report to output/reports/"

"Pull all active keywords, flag any with Quality Score < 4, 
generate a list of recommended negative keywords, and save 
to output/ads/negative-keywords-[date].csv"

"Compare this month vs last month performance across all 
campaigns and generate a client-ready report"
```

**Where it sits in RA-Project:** `03-automation/v3-advanced/`

---

#### 🟣 Tool 14: Claude Code

**What it is:** The AI orchestration brain of the entire ecosystem when connected to MCP servers.

**Why it's in the ecosystem:** With the Google Ads MCP installed, Claude Code becomes a fully autonomous Google Ads operator — it can query data, analyze it, generate optimization recommendations, write reports, create campaign scripts, and trigger automations, all within a single conversation or scheduled workflow.

**Role in ecosystem:** The central intelligence and decision-making layer. Consumes data from all layers (GA4 via API, Google Ads via MCP, CRM data via webhooks), processes it through CAI agents (Trace for diagnosis, Felix for financial modeling, Aura for creative optimization), and produces actionable outputs.

**Combined with your CAI agents:**
```
Claude Code → calls Google Ads MCP → gets performance data
→ feeds to Trace (3-layer diagnosis: Hook / Body / CTA)
→ feeds to Felix (LTGP:CAC analysis, scale/kill decision)
→ feeds to Aura (creative optimization recommendations)
→ feeds to CEO (strategic direction)
→ outputs to output/reports/ + output/plans/
```

**Where it sits in RA-Project:** Runs at project root level, orchestrates all layers.

---

#### 🟣 Tool 15: Gemini CLI

**What it is:** Google's AI CLI tool — the runtime environment for the Developer Assistant. Also has its own agentic capabilities for Google Workspace, Drive, Gmail, and web search.

**Why you need it:** Required to run the Developer Assistant (Tool 10). But beyond that, it provides complementary AI capabilities — especially for Google-ecosystem tasks (Drive, Docs, Sheets automation).

**Role in ecosystem:** Runtime for Developer Assistant. Secondary AI agent for Google Workspace automation. Can run scheduled queries and dump results to Sheets for Looker Studio dashboards.

**Where it sits in RA-Project:** System-level CLI (runs from `google-ads-api-developer-assistant/`)

---

## FULL DATA FLOW DIAGRAM

```
SEARCH QUERY (User types in Google)
          ↓
[GOOGLE ADS PLATFORM] — serves ad
          ↓
[LANDING PAGE] — GTM fires tracking
          ↓ (click)      ↓ (no click)
[GA4 + CONVERSION TAG]  [REMARKETING AUDIENCE]
          ↓                    ↓ (loops back to Google Ads)
[LEAD FORM SUBMITTED]
          ↓
[GTM → Google Ads Conversion + GA4 Event]
          ↓
[CRM / GoHighLevel]
          ↓ (webhook)
[MAKE.COM]
    ↓           ↓
[Slack Alert] [Google Sheets log]
          ↓ (deal closed)
[OFFLINE CONVERSION → Google Ads]
          ↓
[SMART BIDDING LEARNS from closed revenue]
          
─── INTELLIGENCE LOOP ───────────────────

[Dev Assistant / MCP] ← queries Google Ads API
          ↓
[Claude Code] — analyzes via CAI agents
          ↓
[Looker Studio Dashboard] ← reads Sheets/GA4/Ads
          ↓
[Optimization Recommendations]
          ↓
[Google Ads Scripts / Make.com] — execute changes
          ↓
[Back to Google Ads Platform]
```

---

## IMPLEMENTATION PRIORITY ORDER

### Phase 1 — Foundation (Week 1-2)
```
✅ Google Ads Platform (campaign live)
✅ Google Tag Manager (install on landing page)
✅ Google Ads Conversion Tracking (form submission event)
✅ Google Analytics 4 (behavioral data)
✅ Landing Page (basic, one CTA)
✅ CRM / GoHighLevel (lead capture)
```

### Phase 2 — Intelligence (Week 3-4)
```
□ Google Ads API Developer Assistant (already cloned — configure credentials)
□ Google Looker Studio (connect Ads + GA4)
□ Google Search Console (connect to property)
□ Make.com (lead → CRM → Slack flow)
```

### Phase 3 — Automation (Week 5-6)
```
□ Google Ads Scripts (budget alerts, negative keyword automation)
□ Make.com offline conversion flow (CRM closed → Ads)
□ Automated weekly reporting flow
□ Enhanced Conversions (hash email/phone from form)
```

### Phase 4 — Agentic AI Layer (Week 7-8)
```
□ Google Ads MCP Server (install + configure)
□ Connect MCP to Claude Code settings
□ Build first agentic workflow (performance audit + report)
□ Gemini CLI scheduled queries → Sheets → Looker Studio
```

---

## COST SUMMARY

| Tool | Monthly Cost |
|------|-------------|
| Google Ads Platform | Your ad budget |
| Google Tag Manager | Free |
| Google Analytics 4 | Free |
| Google Ads Conversion Tracking | Free |
| Google Search Console | Free |
| Google Looker Studio | Free |
| Google Ads API Dev Assistant | Free |
| Google Ads MCP Server | Free |
| Gemini CLI | Free |
| Google Ads Scripts | Free |
| **GoHighLevel** | **$97/mo** |
| **Make.com** | **$9/mo** |
| **Landing Page (if not GHL)** | **$49-97/mo** |
| **Claude Code** | **Your subscription** |
| **Total non-ad cost** | **~$155-200/mo** |

---

## MAPPING TO YOUR RA-PROJECT STRUCTURE

```
RA-Project/
├── 00-foundation/
│   ├── credentials/        ← OAuth tokens for Ads API, GHL API keys
│   ├── legal/              ← Privacy policy, terms (required for Google Ads)
│   └── tracking/           ← GTM container export, conversion tag IDs
│
├── 01-intelligence/
│   ├── SS1-market/         ← Search Console data, keyword research
│   └── SS2-performance/    ← GA4 reports, Ads performance exports
│
├── 02-slm-machine/
│   ├── traffic/            ← Campaign structures, keyword lists, ad copy
│   ├── funnels/            ← Landing page templates + variants
│   ├── conversion/         ← CRM pipeline configs, form templates
│   ├── persuasion-core/    ← Ad copy frameworks, VSL scripts
│   └── looping/            ← Remarketing audiences, email sequences
│
├── 03-automation/
│   ├── v1-deployment/      ← Google Ads Scripts + Make.com flows
│   ├── v2-reporting/       ← Looker Studio templates, report automation
│   └── v3-advanced/        ← Google Ads MCP Server, agentic workflows
│
├── google-ads-api-developer-assistant/  ← Already here (Layer 5)
└── output/
    ├── ads/                ← Generated ad copy, campaign briefs
    ├── reports/            ← AI-generated performance reports
    └── plans/              ← Strategic optimization plans
```

---

## AGENT STRATEGIC ASSESSMENTS

### 📈 Felix — Financial Verdict

The non-ad cost of this entire ecosystem is ~$155-200/month. If your campaigns are generating leads at even $50 CPA and closing at 20%, the LTGP:CAC math justifies every dollar of this infrastructure on campaign #1. The only waste here would be building Layer 6 before Layer 1 is converting. Sequence matters.

### 🔄 Trace — Critical Diagnostic Note

Instrument the offline conversion import (CRM → Google Ads) before you scale. Most operators optimize for form fills. The smart move is optimizing for *closed revenue*. That one configuration change is worth more than any other optimization in this stack.

### 🧠 Thinker — Structural Observation

Note that Tools 2, 3, 4, 11, 12, 13, 14, and 15 are entirely free. The intelligence and AI orchestration layer of this ecosystem costs you nothing but setup time. The only real costs are the tools that hold human-managed data (CRM) and automate between platforms (Make). That's a remarkably lean infrastructure for what it produces.

### 🎯 CEO — Strategic Context

The fatal mistake most people make is building tools that don't talk to each other. Every layer in this architecture has a defined data handoff to the next layer. No orphan tools. The first-principles question: what does a lead generation machine actually need? (1) traffic acquisition, (2) conversion of that traffic, (3) data capture, (4) data analysis → optimization loop, (5) scale. Every tool listed serves one of those five. If it doesn't, it's overhead.

---

## QUICK REFERENCE — TOOL ROLES SUMMARY

| Tool | Primary Role | Feeds Into |
|------|-------------|-----------|
| Google Ads Platform | Traffic source | Landing Page |
| Google Tag Manager | Tracking delivery | GA4, Conversion Tracking |
| Google Ads Conversion Tracking | Attribution signal | Google Ads Smart Bidding |
| Google Analytics 4 | Behavioral data | Remarketing, Optimization |
| CallRail | Call attribution | Google Ads Conversions |
| Landing Page Builder | Lead capture UI | CRM, GTM |
| GoHighLevel CRM | Lead management | Google Ads Offline Conversions |
| Google Ads Scripts | In-platform automation | Google Ads (direct) |
| Make.com / n8n | Inter-tool automation | All layers |
| Dev Assistant | Data interrogation | Reports, Automation code |
| Looker Studio | Dashboard visualization | Decision-making |
| Search Console | Keyword intelligence | Campaign planning |
| Google Ads MCP | AI-to-API bridge | Claude Code agents |
| Claude Code | Orchestration brain | All outputs |
| Gemini CLI | Dev Assistant runtime | Dev Assistant |

---

*Document generated by CAI + MGI Council | RA-Project | April 20, 2026*
