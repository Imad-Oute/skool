# SEO / GEO / LLM VISIBILITY — FULL PERFORMANCE MONITORING ECOSYSTEM
**Project:** RA-Project | **Date:** April 20, 2026 | **Authored by:** CAI + MGI Council
**Purpose:** Complete monitoring, tracking, and analytics framework for all 3 search visibility systems

---

## THE CORE PRINCIPLE

You are running three parallel visibility systems simultaneously. Each system has different metrics, different tools, different feedback loops, and different timelines. Monitoring them with one lens (e.g., "just GSC") means you're blind to 66% of your actual performance.

```
SYSTEM 1 — TRADITIONAL SEO
What it measures: Google + Bing blue link rankings
Primary signal: Organic clicks, average position, domain authority
Timeline: Results visible in 30-90 days
Tools: GSC, Bing WMT, Ahrefs, GA4

SYSTEM 2 — GEO (Generative Engine Optimization)
What it measures: AI-generated answer citations across all platforms
Primary signal: Citation frequency, AI impression share
Timeline: Results visible in 14-30 days
Tools: Otterly.AI, Bing AI Performance Dashboard, Semrush AI Toolkit

SYSTEM 3 — LLM BRAND VISIBILITY
What it measures: Brand recognition in AI-direct responses (no search trigger)
Primary signal: Brand mentions in AI answers, entity graph presence
Timeline: Results visible in 60-180 days
Tools: Otterly.AI (brand tracking), Google Alerts, Ahrefs Alerts
```

A brand excelling at all three is nearly impossible to displace. This document gives you the full monitoring infrastructure to run all three in parallel.

---

## ECOSYSTEM MONITORING MAP

```
┌──────────────────────────────────────────────────────────────────────┐
│                    MONITORING COMMAND CENTER                         │
│                                                                      │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │   SYSTEM 1       │  │   SYSTEM 2       │  │   SYSTEM 3       │  │
│  │ Traditional SEO  │  │ GEO / AI Search  │  │ LLM Brand Vis.   │  │
│  │                  │  │                  │  │                  │  │
│  │ • GSC            │  │ • Otterly.AI     │  │ • Otterly.AI     │  │
│  │ • Bing WMT       │  │ • Bing AI Perf.  │  │   (brand mode)   │  │
│  │ • Ahrefs RT      │  │ • Semrush AI     │  │ • Google Alerts  │  │
│  │ • GA4 Organic    │  │ • Manual AI Test │  │ • Ahrefs Alerts  │  │
│  │ • Screaming Frog │  │ • GSC AI Mode    │  │ • Wikidata KP    │  │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘  │
│           │                     │                      │            │
│           └─────────────────────┴──────────────────────┘           │
│                                 │                                   │
│                    ┌────────────▼────────────┐                      │
│                    │  LOOKER STUDIO DASHBOARD │                      │
│                    │  (GSC + GA4 unified)     │                      │
│                    └─────────────────────────┘                      │
└──────────────────────────────────────────────────────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   WEEKLY DECISION LOOP  │
                    │ What to optimize next?  │
                    └─────────────────────────┘
```

---

## COMPLETE METRICS REGISTRY

Every metric you need to track, what it means, what target to aim for, which tool provides it, and how often to check it.

---

### SYSTEM 1 METRICS — TRADITIONAL SEO

#### Tier 1: Business Outcome Metrics (track weekly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **Organic Leads** | Form completions from organic search sessions | GA4 | Growing MoM | Drops >20% week-over-week |
| **Organic Revenue / Pipeline** | Revenue attributed to organic search leads | GA4 + CRM | Growing MoM | Flat for 60+ days |
| **Organic Conversion Rate** | Organic sessions ÷ organic lead form completions | GA4 | 2-5% (varies by industry) | Drops below 1% |
| **Organic CAC** | Total SEO investment ÷ organic leads generated | Manual calc | < Paid CAC | Exceeds paid CAC |

#### Tier 2: Traffic Metrics (track weekly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **Organic Clicks** | Total Google clicks to your site | GSC | Growing MoM | Drops >15% week-over-week |
| **Organic Impressions** | Times your site appeared in Google results | GSC | Growing MoM | Drops >10% week-over-week |
| **Average CTR** | Clicks ÷ Impressions | GSC | 3-5% (varies by position) | Drops below 2% |
| **Average Position** | Mean ranking across all queries | GSC | Declining (lower = better) | Jumps +3 positions suddenly |
| **Organic Sessions** | GA4 sessions from organic search | GA4 | Growing MoM | Drops >15% week-over-week |
| **Engaged Sessions** | Organic sessions with 10s+ engagement | GA4 | >60% of organic sessions | Drops below 50% |
| **Bing Organic Clicks** | Clicks from Bing/Yahoo/DuckDuckGo | Bing WMT | Growing MoM | Flat or declining |

#### Tier 3: Ranking Metrics (track weekly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **Target Keyword Average Position** | Mean position of your tracked keyword set | Ahrefs RT | Declining number = improving | Jumps >5 positions in a week |
| **Keywords in Top 3** | Count of tracked keywords ranking #1-3 | Ahrefs RT | Growing quarterly | Drops significantly |
| **Keywords in Top 10** | Count of tracked keywords on page 1 | Ahrefs RT | Growing quarterly | Drops significantly |
| **Keywords in Positions 4-15** | Quick-win opportunities | Ahrefs RT | Decreasing (moving to top 3) | Growing (means stagnation) |
| **New Keywords Ranking** | New keywords your site appeared for this week | GSC | Growing over time | None — this is informational |

#### Tier 4: Authority Metrics (track monthly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **Domain Rating (DR)** | Ahrefs' 0-100 measure of backlink authority | Ahrefs | +5 DR per quarter | Drops (indicates lost links) |
| **Referring Domains** | Count of unique domains linking to you | Ahrefs | +5-10 new domains/month (year 1) | Month-over-month decline |
| **New Backlinks** | New links gained this month | Ahrefs | Growing with PR activity | Not growing after 3 months |
| **Lost Backlinks** | Links removed or gone 404 | Ahrefs | < 20% of gained (natural churn) | High number of high-DR links lost |
| **Organic Pages Indexed** | Count of pages Google has indexed | GSC | Growing with content | Drops (technical issue) |
| **Index Coverage Errors** | Pages Google can't index | GSC | 0 | Any error count > 0 |

#### Tier 5: Technical Performance Metrics (track monthly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **LCP (Largest Contentful Paint)** | Time for largest visible element to load | GSC / PageSpeed | < 2.5s | > 4.0s |
| **INP (Interaction to Next Paint)** | Delay between interaction and visual response | GSC / PageSpeed | < 200ms | > 500ms |
| **CLS (Cumulative Layout Shift)** | Visual stability score | GSC / PageSpeed | < 0.1 | > 0.25 |
| **Good CWV URLs %** | % of pages with all three metrics in "Good" range | GSC | 100% | Drops below 80% |
| **Mobile Performance Score** | Google's composite performance score | PageSpeed | 90+ | Below 70 |
| **Desktop Performance Score** | Google's composite performance score | PageSpeed | 95+ | Below 80 |
| **Crawl Errors (4XX)** | Broken pages found by Screaming Frog | Screaming Frog | 0 | Any 4XX on linked pages |
| **Redirect Chains** | URLs requiring 2+ redirects to reach destination | Screaming Frog | 0 | Any chains found |
| **Missing Title Tags** | Pages without a <title> tag | Screaming Frog | 0 | Any found |
| **Missing H1s** | Pages without an H1 | Screaming Frog | 0 | Any found |
| **Duplicate Title Tags** | Multiple pages with identical titles | Screaming Frog | 0 | Any found |
| **Pages Without Canonical** | Pages missing canonical tag | Screaming Frog | 0 | Any found |
| **Images Without Alt Text** | Images missing descriptive alt attribute | Screaming Frog | 0 | Any found |

---

### SYSTEM 2 METRICS — GEO PERFORMANCE

#### Tier 1: AI Citation Business Metrics (track weekly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **AI Citation Count** | Total times your content cited across all AI platforms | Otterly.AI | Growing weekly | Drops >30% week-over-week |
| **AI-Driven Traffic** | Sessions arriving via AI search platforms | GA4 (source/medium) | Growing MoM | Not growing after 90 days |
| **AI Citation → Lead Rate** | % of AI-cited page visits that convert to leads | GA4 | ≥ Organic avg conversion rate | Significantly below organic rate |

#### Tier 2: Platform-Specific AI Visibility (track weekly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **ChatGPT Citation Count** | Times cited in ChatGPT answers | Otterly.AI | Growing | Declining 2+ weeks |
| **Perplexity Citation Count** | Times cited in Perplexity answers | Otterly.AI | Growing | Declining 2+ weeks |
| **Google AI Overview Citations** | Times cited in Google AI Mode answers | Otterly.AI / Semrush AI | Growing | Not appearing after 90 days |
| **Copilot Citation Count** | Times cited in Microsoft Copilot answers | Bing AI Dashboard | Growing | Declining 2+ weeks |
| **Gemini Citation Count** | Times cited in Google Gemini answers | Otterly.AI | Growing | Not appearing |

#### Tier 3: AI Competitive Metrics (track weekly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **AI Share of Voice** | Your citations ÷ total citations on your target queries | Otterly.AI | Growing vs competitors | Competitors pulling ahead |
| **Competitor Citation Count** | How often competitors are cited on your target queries | Otterly.AI | Your count growing faster | Competitor overtakes you on >5 queries |
| **Uncontested AI Queries** | Your target queries where no one is cited yet | Otterly.AI | Identify and target these | — |
| **AI Impression Share** | % of AI answer appearances you capture | Otterly.AI | Growing | Below 10% on core queries at 90 days |

#### Tier 4: AI Content Performance (track weekly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **Most Cited Pages** | Pages driving the most AI citations | Otterly.AI | Pillar and service pages should top this list | Blog-only citations (content not converting) |
| **Queries Triggering Citations** | Which search queries cause AI to cite your content | Otterly.AI | Expanding to new queries | Stuck on same 3-5 queries |
| **Quick Answer Block Performance** | Whether QAB content appears in AI citations | Manual testing | QABs should appear verbatim | Not appearing — QAB needs rewriting |
| **Schema Impact on Citations** | Correlation between schema-marked pages and citation rate | Cross-reference with Otterly.AI | Schema pages should cite at higher rate | Non-schema pages citing more (schema issue) |

---

### SYSTEM 3 METRICS — LLM BRAND VISIBILITY

#### Tier 1: Brand Recognition Metrics (track monthly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **Brand Mentions in AI Answers** | Times your brand name appears in AI responses | Otterly.AI (brand mode) | Growing after month 3 | Not appearing at 6 months |
| **Knowledge Panel Status** | Whether a Google Knowledge Panel exists for brand search | Manual Google search | Active KP by month 6 | Not appearing at 9 months |
| **Wikidata Entity Status** | Whether your Wikidata entry is live and correct | wikidata.org | Active entry | Data errors found |
| **Unlinked Brand Mentions** | Web mentions of your brand without a backlink | Ahrefs Alerts | Growing with PR activity | Not growing |
| **Linked Brand Mentions** | Web mentions with backlinks | Ahrefs | Growing with PR activity | Flat for 60+ days |

#### Tier 2: Entity Graph Metrics (track monthly)

| Metric | Definition | Tool | Target | Alert If |
|--------|-----------|------|--------|----------|
| **Google Business Profile Rating** | Average star rating | GBP Dashboard | 4.5+ | Below 4.0 |
| **GBP Review Count** | Total reviews collected | GBP Dashboard | +2-3/month | Flat for 60+ days |
| **Clutch/G2 Rating** | Average star rating on review platforms | Platform dashboards | 4.5+ | Below 4.0 |
| **LinkedIn Followers** | Company page followers | LinkedIn Analytics | Growing MoM | Flat for 90+ days |
| **Social Search Impressions** | LinkedIn content impressions | LinkedIn Analytics | Growing | Flat or declining |
| **Brand Search Volume** | Monthly searches for your company name | GSC (branded queries) | Growing quarterly | Flat at 12 months |

---

## MONITORING TOOLS DEEP DIVE

---

### TOOL 1: GOOGLE SEARCH CONSOLE — Primary System 1 Monitor

**Access:** search.google.com/search-console

**Weekly Monitoring Workflow:**

```
STEP 1 — Performance Overview (5 minutes)
→ Performance → Search results → Set date: Last 7 days vs previous 7 days
→ Check four core metrics at top: Clicks, Impressions, CTR, Position
→ If any metric dropped >15%: investigate further before moving on
→ If all metrics up or stable: move to step 2

STEP 2 — Query Mining (10 minutes)
→ Performance → Queries tab → Sort by Impressions (descending)
→ Filter 1: Position > 3 AND Position < 15 (page 1 bottom + page 2 = optimize these)
  → These pages need: better content, more internal links, schema, FAQ sections
  → Each one moved from position 8 → 3 = 3-5x more clicks from same impressions
→ Filter 2: CTR < 2% AND Impressions > 500 (shown a lot but not clicked)
  → Fix: rewrite title tag and meta description to be more compelling
  → The page ranks well but doesn't sell itself in the SERP

STEP 3 — Page Performance (5 minutes)
→ Performance → Pages tab → Sort by Clicks (descending)
→ Your top 10 pages = your revenue pages → protect and grow these
→ Any page with Impressions > 1000 but Clicks < 50: investigate
  → Bad title/meta OR ranking for wrong intent queries

STEP 4 — Coverage Health (3 minutes)
→ Coverage (or Indexing → Pages)
→ Errors: Any new errors this week? Fix immediately
→ Valid count: Is it growing as you publish content? Flat = problem

STEP 5 — New Content Indexing (2 minutes)
→ Any new content published this week?
→ URL Inspection → paste URL → "Request Indexing"
→ Do this for every new page within 24 hours of publishing
```

**Monthly Deep-Dive:**
```
→ Performance → Last 3 months comparison
→ Links report: Top linked pages, top linking sites
→ Core Web Vitals: Good/Needs Improvement/Poor counts
→ Enhancements: FAQ rich results, breadcrumbs — any errors?
→ Export full performance data → save to SS2-performance/gsc-[month]-[year].csv
```

**What the data tells you:**
```
High impressions + low CTR → Title/meta problem (page ranks but doesn't get clicked)
High CTR + low impressions → Good page, needs more authority (link building target)
Dropping impressions → Google reduced your crawl coverage or page lost authority
Dropping position → Competitor improved or you lost a ranking signal
Impressions without clicks on position 1-3 → AI Overview capturing all clicks
```

---

### TOOL 2: BING WEBMASTER TOOLS — System 1 + System 2 Monitor

**Access:** bing.com/webmasters

**Weekly Monitoring Workflow:**
```
STEP 1 — AI Performance Dashboard (5 minutes) ← MOST IMPORTANT in BWT
→ Left sidebar → AI Performance
→ Check: Citation count this week vs last week
→ Check: Which pages are cited in Copilot answers?
→ Check: Which queries trigger Copilot to cite you?
→ Export data weekly → SS2-performance/bing-ai-[week].csv

STEP 2 — Search Performance (3 minutes)
→ Reports → Search Performance
→ Clicks, impressions, CTR, position for Bing
→ Bing traffic should mirror Google trends (if diverges, investigate)

STEP 3 — URL Submission (2 minutes)
→ IndexNow → Check recent submission history
→ All IndexNow pings showing as received? (should all show 200 OK)
```

**Monthly Deep-Dive:**
```
→ SEO Reports → Site Scan → Run new scan
→ Bing sometimes catches technical issues Google doesn't flag
→ Keyword Research → compare Bing-specific search patterns vs Google
→ Backlink Data → export and compare to Ahrefs (find links Ahrefs missed)
```

---

### TOOL 3: AHREFS — System 1 Intelligence + Authority Monitor

**Access:** ahrefs.com

**Weekly Monitoring Workflow:**
```
STEP 1 — Rank Tracker (5 minutes)
→ Rank Tracker → your project
→ Overview: Average position trend (should trend down = improving)
→ Check: Any keywords dropped >5 positions?
  → Click the keyword → see position history
  → Did competitor just publish better content? Did you lose a backlink?
→ Check: Any keywords entered positions 1-3 this week? (celebrate + link build)
→ Check: SERP Features column — are AI Overviews appearing on your keywords?
  → If yes: that query needs GEO optimization (Quick Answer Block + FAQ)

STEP 2 — Backlink Monitor (3 minutes)
→ Site Explorer → your domain → Backlinks → New (last 7 days)
→ Any notable new links? Outreach opportunity to strengthen relationship?
→ Site Explorer → Backlinks → Lost (last 7 days)
→ Any high-DR links lost? Investigate if page still exists on referring site

STEP 3 — Site Audit Status (2 minutes — only if recent changes made)
→ Site Audit → latest crawl → check Health Score
→ Any new errors appeared since last crawl?
```

**Monthly Deep-Dive:**
```
→ Domain Rating: Trending up? Target +5 DR per quarter
→ Referring Domains: New domains count vs last month
→ Top Pages: Which pages attract the most backlinks?
   → These are your "link magnets" → build more content like them
→ Competitor Analysis: Run Content Gap vs top 3 competitors
   → New gaps this month = new content opportunities
→ Run Site Audit → export errors → fix in priority order
```

**The Key Ahrefs Weekly Report to Build:**
```
Every Monday, in Ahrefs, check:
1. Keywords moved out of positions 4-15 → WINS (moved to top 3)
2. Keywords moved INTO positions 4-15 → OPPORTUNITIES (target these)
3. Keywords dropped out of top 20 → LOSSES (investigate why)

This three-bucket system tells you the exact state of your SEO momentum.
```

---

### TOOL 4: GOOGLE ANALYTICS 4 — Business Outcome Monitor

**Access:** analytics.google.com

**Weekly Monitoring Workflow:**
```
STEP 1 — Organic Traffic Overview (5 minutes)
→ Reports → Acquisition → Traffic Acquisition
→ Filter: Session default channel group = "Organic Search"
→ Date: This week vs last week
→ Key metrics: Sessions, Engaged Sessions, Key Events (conversions)
→ Is organic traffic up or down vs last week?

STEP 2 — Organic Conversions (5 minutes)
→ Same report → add "Key events" column
→ Filter to Organic Search only
→ How many leads from organic this week?
→ Conversion rate = Key Events ÷ Sessions (target: 2-5%)

STEP 3 — Top Organic Landing Pages (3 minutes)
→ Reports → Engagement → Landing Page
→ Add filter: First user default channel group = Organic Search
→ Sort by: Sessions descending
→ These are your money pages → any dropping traffic? Investigate
```

**Monthly Deep-Dive:**
```
→ Explore → Free Form → set up organic keyword → landing page → conversion report
  (requires GSC link to be active)
→ This shows: which keywords drive converting traffic vs just traffic
→ Funnel Exploration: Where do organic visitors drop off before converting?
  → Fix the page that's leaking the most potential leads

The Ultimate GA4 Organic Question:
"Which pages bring organic visitors who become leads?"
→ That's what to protect, expand, and create more of.
```

---

### TOOL 5: OTTERLY.AI — System 2 + System 3 Primary Monitor

**Access:** otterly.ai

**Weekly Monitoring Workflow:**
```
STEP 1 — Citation Dashboard (10 minutes)
→ Dashboard: Total citations this week vs last week
→ Platform breakdown:
  • ChatGPT: up or down?
  • Perplexity: up or down?
  • Google AI Mode: up or down?
  • Copilot: up or down (cross-reference with Bing WMT)
  • Gemini: up or down?

STEP 2 — Query Analysis (10 minutes)
→ Queries section: Which queries triggered your citations?
→ NEW this week: Are you appearing in queries you weren't before?
  → Growing query diversity = GEO content is working
→ Competitor queries: Which queries cite competitors but not you?
  → Each one = a content gap to fill OR content to restructure

STEP 3 — Page-Level Citation Data (5 minutes)
→ Pages section: Which specific pages on your site are cited?
→ Are your pillar pages and service pages getting cited?
  OR are only blog posts getting cited?
  → Service page citations = direct commercial intent = high value
  → Blog-only citations = awareness but no commercial pull = expand content strategy
→ Pages with zero citations after 90 days → need GEO optimization

STEP 4 — Brand Tracking (3 minutes)
→ Brand mentions: Is your brand name appearing in AI answers?
  (This is System 3 — LLM Visibility)
→ Brand sentiment: positive/neutral/negative framing in citations?
```

**Export and save:**
```
Weekly: Export citation report → SS2-performance/otterly-[week].csv
Monthly: Export competitor comparison → SS1-market/competitor-ai-presence-[month].csv
```

---

### TOOL 6: SCREAMING FROG — Monthly Technical Health Monitor

**Access:** Desktop app (screamingfrog.co.uk/seo-spider)

**Monthly Crawl Workflow:**
```
1. Open Screaming Frog
2. Enter yourdomain.com → Start
3. Wait for crawl to complete

REPORT CHECKLIST (run each, note counts):

Response Codes:
□ 4XX count: (target 0) → fix all broken internal links
□ 3XX count: (reduce over time) → flatten redirect chains

Page Titles:
□ Missing: (target 0)
□ Duplicate: (target 0)
□ Over 60 chars: (fix — gets truncated in SERP)

Meta Descriptions:
□ Missing: (target 0)
□ Duplicate: (target 0)
□ Over 160 chars: (fix — gets truncated in SERP)

H1:
□ Missing: (target 0)
□ Multiple: (target 0)

Images:
□ Missing Alt Text: (target 0)
□ Over 100KB: (target 0 — all should be WebP)

Canonical:
□ Missing: (target 0)
□ Non-indexable canonicals ranking: (investigate each)

Internal Links:
□ Orphan pages (0 inlinks): (target 0 — every page needs at least 1 link)

SAVE EXPORT:
File → Export → All Tabs → Save to:
SS2-performance/screaming-frog/crawl-[YYYY-MM].xlsx

MONTH-OVER-MONTH COMPARISON:
Open last month's export alongside this month's
Target: Error count decreasing, page count growing
```

---

## THE LOOKER STUDIO MASTER DASHBOARD

**What you're building:** A single, always-live URL showing your complete SEO performance from GSC + GA4 in one place. Checks in 5 minutes instead of 20.

**Setup steps:**

```
1. Go to: lookerstudio.google.com
2. Create → Blank Report
3. Rename: "SEO Performance Dashboard — [Your Site]"

DATA SOURCES TO ADD:
→ Click "Add data" → Select "Search Console"
  → Connect: your GSC property
  → Import type: Site Impression (all data)
→ Click "Add data" → Select "Google Analytics 4"
  → Connect: your GA4 property
```

**Build these 10 report cards:**

```
PAGE 1: WEEKLY OVERVIEW

Card 1: Scorecard — Organic Clicks (last 28 days vs previous 28 days)
→ Data source: Search Console
→ Metric: Clicks
→ Comparison: vs previous period
→ Style: Green arrow if up, red if down

Card 2: Scorecard — Average Position (last 28 days vs previous 28 days)
→ Metric: Average Position
→ Note: LOWER is better — flip comparison arrow direction

Card 3: Scorecard — Organic Sessions from GA4
→ Data source: GA4
→ Metric: Sessions
→ Filter: Session default channel group = "Organic Search"

Card 4: Scorecard — Organic Conversions (Leads)
→ Data source: GA4
→ Metric: Key Events (or Conversions)
→ Filter: Session default channel group = "Organic Search"

Card 5: Line Chart — Organic Clicks Trend (last 90 days)
→ Dimension: Date
→ Metric: Clicks
→ Date range: Last 90 days
→ Shows: Is traffic growing over time?

Card 6: Line Chart — Average Position Trend (last 90 days)
→ Dimension: Date
→ Metric: Average Position
→ Shows: Are rankings improving over time?

Card 7: Table — Top 10 Organic Pages by Clicks
→ Dimension: Landing Page
→ Metrics: Clicks, Impressions, CTR, Average Position
→ Sort: Clicks descending
→ These are your revenue pages

Card 8: Table — Top 10 Queries Driving Clicks
→ Dimension: Query
→ Metrics: Clicks, Impressions, CTR, Average Position
→ Sort: Clicks descending

Card 9: Table — Quick-Win Keywords (Position 4-15)
→ Dimension: Query
→ Metrics: Clicks, Impressions, CTR, Average Position
→ Filter: Average Position > 3 AND Average Position < 16
→ Sort: Impressions descending
→ These are optimization priorities — high impressions, not yet on page 1 top 3

Card 10: Scorecard — Pages Indexed Count
→ Data source: Search Console (URL inspection data or coverage)
→ Metric: Valid indexed pages count
→ Should grow with content publication
```

```
PAGE 2: ORGANIC TRAFFIC DEEP DIVE

Card 1: Table — Organic Landing Pages with Conversions
→ GA4 data source
→ Dimensions: Landing page
→ Metrics: Sessions, Engaged Sessions, Conversions
→ Filter: Organic Search only
→ This answers: "Which content actually generates leads?"

Card 2: Bar Chart — Organic Sessions by Month (last 12 months)
→ Shows: Long-term organic growth trajectory

Card 3: Table — Low CTR Opportunities
→ Dimension: Query
→ Metrics: CTR, Impressions, Average Position
→ Filter: CTR < 2% AND Impressions > 200
→ Sort: Impressions descending
→ These pages rank but aren't compelling in SERPs
→ Fix their title tags and meta descriptions

Card 4: Geographic breakdown
→ Dimension: Country
→ Metric: Organic Sessions
→ Shows: Where your organic audience comes from
```

**Share your dashboard:**
```
→ Top right → Share → "Anyone with the link can view"
→ Bookmark the URL
→ Add to Monday morning routine
```

---

## PERFORMANCE BENCHMARKS

What "good" looks like at each stage of building this ecosystem:

---

### Month 1-2: Foundation Stage

```
SYSTEM 1 TARGETS:
□ Google Search Console verified + sitemap submitted ✓
□ First GSC data appearing (clicks, impressions, position)
□ Core Web Vitals: 0 "Poor" pages
□ Screaming Frog: 0 4XX errors, 0 missing titles, 0 missing H1s
□ Indexed page count: All site pages indexed (no missing pages)
□ Ahrefs DR: Baseline established (whatever it starts at)

SYSTEM 2 TARGETS:
□ Otterly.AI showing first citations (even if low count)
□ Bing AI Dashboard showing first Copilot citation data
□ At least 1 pillar page live with Quick Answer Block + FAQPage schema
□ Schema validated in Google Rich Results Test (no errors)

SYSTEM 3 TARGETS:
□ Google Business Profile active
□ LinkedIn Company Page 100% complete
□ Crunchbase profile live
□ Wikidata entry submitted (may still be under review)
□ Google Alerts for brand name active

NOTE: Organic traffic at month 1-2 is often flat. This is normal.
The ecosystem is being built — it is not yet producing results.
The absence of traffic at month 1 is not failure. It is foundation.
```

---

### Month 3: First Signal Stage

```
SYSTEM 1 TARGETS (baseline established):
□ Organic clicks: 50-200/month (highly variable by niche)
□ Indexed pages: Growing with every content publish
□ At least 1 target keyword in positions 4-20
□ Referring domains: Baseline established (even if low)
□ Ahrefs DR: Any DR above 0 means backlinks exist

SYSTEM 2 TARGETS:
□ Otterly.AI: At least 10 citations/week across all platforms
□ At least 1 page cited by 2+ AI platforms
□ Bing AI: At least 1 Copilot citation tracked

SYSTEM 3 TARGETS:
□ First external brand mention (from digital PR or directory)
□ GBP: First reviews appearing

KEY INSIGHT AT MONTH 3:
If citations are growing but organic clicks are flat:
→ GEO is working before traditional SEO (normal — AI indexes faster)
→ Continue content + technical work — rankings follow
```

---

### Month 6: Momentum Stage

```
SYSTEM 1 TARGETS:
□ Organic clicks: 300-1,000+/month (depends on content volume)
□ At least 3-5 target keywords in top 10
□ DR: +3-5 from starting baseline
□ Referring domains: +15-30 new domains
□ Organic leads: 5-15/month minimum
□ Organic conversion rate: 2%+ of organic sessions

SYSTEM 2 TARGETS:
□ Otterly.AI: 50+ citations/week across all platforms
□ 3+ pages being cited regularly
□ Brand appearing in answers to direct "who is the best..." queries
□ AI-driven traffic: measurable in GA4 (separate source/medium)

SYSTEM 3 TARGETS:
□ Google Knowledge Panel appearing for brand search (may take longer)
□ Brand mentioned in 2+ external publications
□ GBP: 5+ reviews, 4.5+ average rating

KEY INSIGHT AT MONTH 6:
This is where you should see the first compounding effects.
Content published in Month 1 is now mature and ranking.
The cluster architecture should show: pillar page ranking + clusters appearing.
```

---

### Month 12: Compounding Stage

```
SYSTEM 1 TARGETS:
□ Organic clicks: 1,000-5,000+/month
□ 10+ target keywords in top 5
□ DR: 25+ (meaningful authority)
□ Referring domains: 50+ total
□ Organic leads: 20-50+/month
□ Organic traffic covering a meaningful % of total lead volume

SYSTEM 2 TARGETS:
□ Otterly.AI: 100+ citations/week
□ Featured as primary source on 2+ high-volume AI queries
□ AI-driven traffic: 10-20% of total organic sessions

SYSTEM 3 TARGETS:
□ Active Google Knowledge Panel
□ Wikidata entry stable with multiple sameAs connections
□ Brand search volume: measurable (people searching your brand name)
□ GBP: 15+ reviews

COMPETITIVE MOAT SIGNAL:
At month 12, the combination of:
→ 50+ referring domains (authority)
→ Full content cluster published (topical authority)
→ 100+ AI citations/week (GEO authority)
→ Active entity presence (brand authority)

...creates a competitive position that a new entrant cannot replicate in less than 12 months.
This is the moat.
```

---

## ALERT SYSTEM — WHEN TO INVESTIGATE IMMEDIATELY

These are the signals that require same-day investigation, not weekly review:

```
CRITICAL ALERTS (investigate within 24 hours):

1. Organic clicks drop >30% week-over-week
   → Could be: Google algorithm update, manual penalty, technical issue (robots.txt blocking)
   → First check: Is the site still indexable? (GSC → Coverage → Valid count)
   → Second check: robots.txt changes? (did something accidentally block Googlebot?)
   → Third check: Google Search Status Dashboard for algorithm updates

2. Indexed pages count drops significantly
   → Could be: noindex tag accidentally added, server returning 5XX errors
   → First check: GSC → Coverage → Errors
   → Screaming Frog crawl immediately

3. Core Web Vitals suddenly show 100+ "Poor" URLs
   → Could be: New JavaScript deployment broke performance
   → Test immediately: pagespeed.web.dev on homepage

4. 4XX errors spike in Screaming Frog
   → Could be: URL restructuring broke internal links
   → Map all broken URLs → create 301 redirects to correct destinations

MODERATE ALERTS (investigate within 72 hours):

5. Average position drops >5 positions across multiple keywords
   → Could be: Major competitor published better content
   → Audit their new content → update yours to be more comprehensive

6. Otterly.AI citations drop >50% in one week
   → Could be: AI platform changed citation algorithm
   → Could be: Competitor published strongly optimized content
   → Check competitor pages on your core queries

7. Ahrefs shows significant lost referring domains
   → High-DR links lost = authority loss
   → Find the referring pages → contact site owner if link was removed

WARNING SIGNALS (note and monitor):

8. CTR drops on ranking pages (impressions stable, clicks falling)
   → Competitor improved their meta title/description
   → Google now showing AI Overview for that query
   → Rewrite your title and meta for that page

9. AI citations flat for 4+ weeks despite new content
   → Content not meeting AI citation criteria
   → Review: Quick Answer Blocks present? FAQPage schema valid? Author signals?

10. Engagement rate on organic sessions dropping
   → Content attracting wrong-intent visitors
   → OR page load speed degraded
   → Check PageSpeed + re-read the page for search intent alignment
```

---

## WEEKLY OPERATING ROUTINE — EXACT SCHEDULE

**Monday — Data Review (45–60 minutes)**
```
09:00 — GSC Weekly Check (15 min)
→ Performance → Last 7 days vs previous 7 days
→ Note: Clicks, Impressions, CTR, Position changes
→ Flag any >15% drops → investigate root cause
→ Check Coverage for new errors

09:15 — Bing AI Performance Dashboard (10 min)
→ Check Copilot citation count vs last week
→ Note: Which pages cited? Which queries?

09:25 — Otterly.AI Weekly Report (15 min)
→ Total citations: up or down?
→ Platform breakdown: which platform growing/declining?
→ Competitor queries: any new gaps to target?
→ Page-level: which pages being cited?

09:40 — Ahrefs Rank Tracker (10 min)
→ Position changes since last Monday
→ Keywords moved into/out of top 10 (wins and losses)
→ Any significant drops to investigate?

09:50 — GA4 Organic Overview (10 min)
→ Organic sessions: this week vs last week
→ Organic leads: this week vs last week
→ Any anomalies in behavior?
```

**Wednesday — Content Publish Day (varies)**
```
→ Publish or update 1 content piece
→ Apply GEO checklist before hitting publish
→ Validate schema: search.google.com/test/rich-results
→ Submit via IndexNow immediately after publishing
→ Request indexing in GSC (URL Inspection → Request Indexing)
→ Share to LinkedIn
→ Update 2 existing pages to link to new content
```

**Friday — Authority Building (30 minutes)**
```
→ Check HARO/Connectively for relevant journalist queries
  → Respond to any relevant ones (3-4 sentences, credentials first)
→ Check Google Alerts for brand mentions
  → Any unlinked mentions? Send link reclamation email
→ Check Ahrefs Alerts for new backlinks or mentions
→ Add any new content to llms.txt if it's a key resource page
```

---

## MONTHLY AUDIT ROUTINE — EXACT SCHEDULE

**First Monday of Every Month (2–3 hours)**

```
TECHNICAL AUDIT:
□ Run Screaming Frog crawl → compare to last month
  → Error count decreased? Page count grew correctly?
□ GSC → Core Web Vitals → Good/Poor URL counts vs last month
□ PageSpeed Insights: Test homepage + primary service page
  → Record scores in SS2-performance/cwv-monthly-[YYYY-MM].md
□ GSC → Coverage → Valid indexed pages count vs last month

AUTHORITY AUDIT:
□ Ahrefs: Domain Rating vs last month
□ Ahrefs: New referring domains vs last month
□ Ahrefs: Lost referring domains — any significant losses?
□ Ahrefs: Top linked pages — any changes?

CONTENT AUDIT:
□ Cluster progress: How many cluster pages published this month?
□ GSC: Top pages report — any previously strong pages losing impressions?
  → Pages dropping = need refresh (update content, add data, re-date)
□ Update at least 2 older pages with new data/stats
  → Re-date → submit via IndexNow → request indexing in GSC

GEO AUDIT:
□ Otterly.AI: Monthly citation trend — is it growing?
□ Manual AI testing: Ask ChatGPT, Perplexity, Claude about your topic
  → Are you mentioned? If not, what competitor is? Why?
□ Bing AI Dashboard: Month-over-month Copilot citations

ENTITY AUDIT:
□ Google search your brand name → Knowledge Panel status?
□ GBP: New reviews this month? Respond to all
□ Wikidata: Any data quality issues flagged?
□ Clutch/G2: New reviews? Any negative to address?

REPORT:
□ Complete monthly SEO report → SS2-performance/monthly-report-[YYYY-MM].md
  (template below)
```

---

## MONTHLY REPORT TEMPLATE

Save a copy of this every month in `01-intelligence/SS2-performance/`

```markdown
# SEO Monthly Report — [Month Year]

## Executive Summary
[2-3 sentence summary of the month's performance]

## System 1: Traditional SEO

### Traffic
| Metric | This Month | Last Month | Change |
|--------|-----------|-----------|--------|
| Organic Clicks (GSC) | | | |
| Organic Sessions (GA4) | | | |
| Organic Leads (GA4) | | | |
| Organic Conversion Rate | | | |

### Rankings
| Metric | This Month | Last Month | Change |
|--------|-----------|-----------|--------|
| Keywords in Top 3 | | | |
| Keywords in Top 10 | | | |
| Average Position | | | |

### Authority
| Metric | This Month | Last Month | Change |
|--------|-----------|-----------|--------|
| Domain Rating | | | |
| Referring Domains | | | |
| New Backlinks | | | |
| Lost Backlinks | | | |

### Technical
| Metric | This Month | Status |
|--------|-----------|--------|
| Good CWV URLs % | | |
| Screaming Frog Errors | | |
| Indexed Pages Count | | |
| Mobile Performance Score | | |

## System 2: GEO Performance

| Metric | This Month | Last Month | Change |
|--------|-----------|-----------|--------|
| Total AI Citations (Otterly) | | | |
| ChatGPT Citations | | | |
| Perplexity Citations | | | |
| Google AI Mode Citations | | | |
| Copilot Citations (Bing) | | | |
| Gemini Citations | | | |

## System 3: LLM Brand Visibility

| Metric | This Month | Status |
|--------|-----------|--------|
| Brand Mentions in AI Answers | | |
| GBP Reviews (total) | | |
| GBP Average Rating | | |
| Knowledge Panel Active | Yes / No / Not Yet |
| Wikidata Entry Status | Active / Pending |
| Clutch/G2 Reviews (total) | | |

## Content Published This Month
| Title | URL | Type | Published Date |
|-------|-----|------|---------------|
| | | | |

## Top Wins
1. 
2. 
3. 

## Problems Found + Fixes Applied
1. 
2. 

## Priority Actions for Next Month
1. 
2. 
3. 
```

---

## QUARTERLY STRATEGY REVIEW

Every 3 months, run a deeper strategic review beyond the monthly metrics:

```
QUARTERLY QUESTIONS TO ANSWER:

1. CONTENT STRATEGY:
□ Which content cluster generated the most organic traffic?
   → Create more content in this cluster
□ Which content cluster has the lowest performance despite publication?
   → Investigate: keyword difficulty too high? Search intent mismatch?
□ What are the 5 highest-volume keywords we still have no content for?
   → These are the next content priorities

2. COMPETITIVE ANALYSIS:
□ Run Ahrefs Content Gap: What do top 3 competitors rank for that we don't?
□ Run Ahrefs Backlink Gap: Who links to competitors but not us?
   → Outreach targets for next quarter
□ Which competitors gained the most domain authority this quarter?
   → Study what they published and linked to

3. GEO STRATEGY:
□ Which AI platforms are generating the most citations?
   → Double down on that platform's citation triggers
□ Which queries trigger AI Overviews on our target keywords? (Semrush AI Toolkit)
   → These queries need Quick Answer Blocks + strong FAQPage schema
□ Manual AI test: Ask 10 core questions in ChatGPT, Perplexity, Claude
   → Are we cited? Who is cited instead?

4. AUTHORITY STRATEGY:
□ How many new referring domains this quarter?
   → If <10: accelerate digital PR (publish research asset)
□ What is Domain Rating now vs 90 days ago?
   → If < +3: link acquisition needs more attention
□ How many Clutch/G2/GBP reviews acquired?
   → If <5: implement systematic review request process

5. TECHNICAL STRATEGY:
□ Any Core Web Vitals regressions?
□ Any Screaming Frog errors that reoccur monthly?
   → Find and fix the root cause, not just the symptom
□ Any schema types still not implemented?
□ Is llms.txt up to date with latest content?

QUARTERLY REPORT OUTPUT:
→ Save to: output/reports/quarterly-seo-review-[YYYY-Q#].md
→ Update content cluster map with performance data
→ Update content calendar with next quarter's priorities
```

---

## DATA FLOW: HOW MONITORING FEEDS DECISIONS

```
MONITORING DATA → ACTION DECISION MATRIX

GSC: High impressions, low CTR (CTR < 2%)
→ Action: Rewrite title tag and meta description for that query
→ Goal: Increase CTR by 1-2% = 50-100% more clicks with no ranking change

GSC: Keyword ranking position 4-15
→ Action: Expand content (add FAQ section, Quick Answer Block, more detail)
→ Action: Add internal links from related pages to this page
→ Action: Add FAQPage schema if not present
→ Goal: Move to position 1-3 = 3-5x more clicks

Ahrefs: Competitor ranks for keyword you don't have content for
→ Action: Create cluster page targeting that keyword
→ Priority: Higher volume gaps first

Otterly.AI: Competitor cited on queries you target, you are not
→ Action: Add Quick Answer Block to relevant page
→ Action: Restructure page with H2s matching the query pattern
→ Action: Add more specific data and statistics
→ Goal: Enter AI citation pool for that query

GSC: Core Web Vitals showing new "Poor" pages
→ Action: PageSpeed Insights on those specific pages
→ Action: Fix highest-impact opportunity first (usually image/JS issue)
→ Goal: Return to "Good" before next GSC scan cycle

Ahrefs: Lost high-DR referring domain
→ Action: Check if the linking page still exists
→ Action: If removed: contact site owner for reinstatement request
→ Action: If gone: check if content is linkworthy enough to replace

Screaming Frog: New 4XX errors
→ Action: 301 redirect each broken URL to most relevant live page
→ Priority: Pages with backlinks or high organic traffic first

GA4: Organic sessions growing but leads flat
→ Action: Conversion rate optimization on top organic landing pages
→ Check: Is the lead form visible above the fold?
→ Check: Is the CTA compelling and action-oriented?
→ Check: Does the page match the search intent of the query bringing traffic?
```

---

## RA-PROJECT MONITORING FOLDER STRUCTURE

```
RA-Project/
├── 01-intelligence/
│   └── SS2-performance/
│       ├── gsc/
│       │   ├── gsc-[YYYY-MM]-performance.csv    ← Monthly GSC exports
│       │   └── gsc-[YYYY-MM]-queries.csv         ← Top queries export
│       ├── ahrefs/
│       │   ├── rank-tracker-[YYYY-MM].csv        ← Monthly rank export
│       │   ├── backlinks-[YYYY-MM].csv           ← Monthly backlink export
│       │   └── site-audit-[YYYY-MM].csv          ← Monthly audit export
│       ├── screaming-frog/
│       │   └── crawl-[YYYY-MM]/                  ← Monthly crawl exports
│       ├── otterly-ai/
│       │   ├── citations-weekly-[date].csv       ← Weekly citation exports
│       │   └── competitor-ai-[YYYY-MM].csv       ← Monthly competitor AI data
│       ├── bing/
│       │   ├── bing-ai-performance-[YYYY-MM].csv ← Copilot citations
│       │   └── bing-search-[YYYY-MM].csv         ← Bing organic data
│       ├── cwv/
│       │   └── cwv-monthly-[YYYY-MM].md          ← Core Web Vitals scores
│       └── reports/
│           ├── monthly-report-[YYYY-MM].md       ← Monthly report (template above)
│           └── quarterly-review-[YYYY-Q#].md     ← Quarterly strategy review
```

---

## AGENT STRATEGIC ASSESSMENTS

### 🎯 CEO — Monitoring Philosophy

There is a difference between monitoring and intelligence. Monitoring tells you what happened. Intelligence tells you why it happened and what to do next. Build monitoring first (this document) — then graduate to intelligence by developing the habit of asking "why" after every metric change before acting. A 20% drop in organic clicks is not a decision — it is a question. Only after you know why it dropped can you decide what to do. The teams that win in SEO are not the ones who check metrics most often. They are the ones who ask the best questions when metrics change.

### 🔄 Trace — Diagnostic Framework

The most common monitoring failure I see: measuring output metrics only. Clicks, leads, citations — these are outputs. They tell you results. But they don't tell you what to fix. Add input metrics to your weekly routine: How many new content pieces published? How many new backlinks acquired? How many schema validations passed? The ratio of input metrics to output metrics tells you whether you're executing or just hoping. Track both. When outputs decline, check inputs first — often the execution slowed down weeks before the traffic dropped.

### 📊 Analyst — The One Number That Matters

Every week, compute this: Organic Leads ÷ SEO Investment (time + tool cost). This is your organic ROAS. If it's improving month-over-month, the ecosystem is working and you should double down on what's producing leads. If it's flat, the traffic is coming but not converting — conversion optimization, not more content. If it's declining, either the investment grew faster than results (early stage — acceptable) or a systemic issue exists (algorithm change, technical problem, wrong content strategy). Everything in this document serves one number: organic leads per dollar invested.

### 🧠 Thinker — The Counterintuitive Insight

The most important metric in this entire document is not in any tool. It is: **content compound rate** — how many of your published pages are still generating traffic 12 months after publication. A blog post that drives traffic today and in year three is the entire thesis of organic SEO. A blog post that drove traffic for 90 days and then decayed is content without compounding. Track this manually at the 6-month and 12-month mark for every content piece you publish. The posts that compound deserve more: updates, more links, more GEO optimization. The posts that decayed deserve diagnosis: wrong keyword intent, or content quality too low to sustain ranking against newer competitors.

---

*Performance monitoring framework generated by CAI + MGI Council | RA-Project | April 20, 2026*
*Reference documents: seo-geo-llm-ecosystem-architecture.md | seo-geo-llm-ecosystem-install-guide.md*
