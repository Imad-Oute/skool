# SEO / GEO / LLM VISIBILITY — FULL ECOSYSTEM RESEARCH REPORT
**Project:** RA-Project | **Date:** April 20, 2026 | **Researched by:** CAI + MGI Council
**Website:** Custom-coded | **Goal:** Maximize organic traffic + AI citation visibility

---

## EXECUTIVE SUMMARY

In 2026, ranking a website requires operating on **three parallel systems simultaneously**:

1. **Traditional SEO** — Google, Bing, Yandex (blue link rankings)
2. **GEO — Generative Engine Optimization** — AI Overviews, Perplexity, ChatGPT Search, Copilot, Gemini (being cited in AI-generated answers)
3. **LLM Visibility** — Anthropic Claude, GPT-4, Gemini (being cited when AI models answer questions directly)

These three systems share overlapping signals but have distinct requirements. A brand that excels at all three in 2026 is nearly impossible to displace. A brand that only does traditional SEO is already losing ground as AI-generated answers capture 61% more clicks than standard blue links when they appear.

---

## DOMAIN 1: TECHNICAL SEO

**Priority: CRITICAL — Foundation of everything**

### Core Web Vitals (2026 Thresholds)

Google's confirmed ranking signals — all three must be in "Good" range:

| Metric | What It Measures | Good | Needs Improvement | Poor |
|--------|-----------------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | Loading speed of main content | < 2.5s | 2.5–4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | Responsiveness to all user interactions | < 200ms | 200–500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | Visual stability during load | < 0.1 | 0.1–0.25 | > 0.25 |

**INP replaced FID (First Input Delay) in March 2024.** It measures ALL interactions (clicks, taps, key presses), not just the first one. This is the hardest metric for JavaScript-heavy sites.

### INP Optimization (Custom-Coded Website)

```
Problem: Long JavaScript tasks block the main thread → INP increases
Solutions:
1. Break up long tasks into smaller chunks using scheduler.yield()
2. Defer non-critical JavaScript (analytics, chat widgets) with <script defer>
3. Use Island Architecture — only hydrate interactive components, not full page
4. Avoid synchronous operations in event handlers
5. Use requestAnimationFrame() for visual updates
6. Reduce third-party script execution time
```

### LCP Optimization

```
1. Preload your hero image: <link rel="preload" as="image" href="hero.webp">
2. Use WebP format (30-35% smaller than JPEG)
3. Set explicit width/height on images (prevents layout shift too)
4. Implement lazy loading for below-fold images: loading="lazy"
5. Use a CDN for static assets
6. Enable compression (Brotli > Gzip)
7. Eliminate render-blocking resources (defer CSS/JS that aren't needed above fold)
```

### CLS Optimization

```
1. Always set width and height attributes on <img> tags
2. Reserve space for ads/embeds with CSS aspect-ratio
3. Avoid inserting content above existing content
4. Use font-display: swap for custom fonts
5. Preload fonts: <link rel="preload" as="font">
```

### Mobile-First Indexing

```
Google's index is 100% mobile-first as of 2023 — still the standard in 2026:
□ Responsive design — single URL, CSS breakpoints
□ Same content on mobile as desktop (Google crawls mobile version only)
□ Touch targets minimum 48x48px
□ No horizontal scroll
□ Font size minimum 16px for body text
□ Pass Google's Mobile Usability report (Search Console → Core Web Vitals → Mobile)
```

### HTTPS & Security

```
□ SSL certificate on all pages (non-negotiable ranking signal since 2014)
□ Redirect all HTTP → HTTPS (301 redirect)
□ Redirect www → non-www (or vice versa — pick one canonical)
□ Fix all mixed content warnings (HTTP resources on HTTPS pages)
□ Add HSTS header: Strict-Transport-Security: max-age=31536000; includeSubDomains
```

### Robots.txt

```
Location: yourdomain.com/robots.txt
Purpose: Controls which crawlers can access which pages
```

**Template for 2026 (allows AI search crawlers, blocks training crawlers):**

```txt
# Traditional Search Engines — ALLOW ALL
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Slurp
Allow: /

User-agent: DuckDuckBot
Allow: /

# AI SEARCH CRAWLERS — ALLOW (these cite you in answers)
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Applebot
Allow: /

User-agent: YouBot
Allow: /

# AI TRAINING CRAWLERS — BLOCK (they scrape for model training, no SEO benefit)
User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: PetalBot
Disallow: /

User-agent: Diffbot
Disallow: /

User-agent: Omgilibot
Disallow: /

User-agent: magpie-crawler
Disallow: /

# Block irrelevant/abusive crawlers
User-agent: AhrefsBot
Crawl-delay: 10

User-agent: SemrushBot
Crawl-delay: 10

# GLOBAL SETTINGS
User-agent: *
Disallow: /admin/
Disallow: /private/
Disallow: /login/
Disallow: /checkout/
Disallow: /cart/
Disallow: /search?
Disallow: /api/

Sitemap: https://yourdomain.com/sitemap.xml
```

**Key strategic decision — ClaudeBot:**
ClaudeBot is listed under BOTH categories in many guides. The Anthropic-ai agent is the training crawler (block). ClaudeBot is now used for Claude's web retrieval for citations (allow). Separate them in robots.txt.

### XML Sitemaps

```
Types:
□ sitemap.xml — main index sitemap (links to sub-sitemaps)
□ sitemap-pages.xml — all main pages
□ sitemap-blog.xml — all blog posts (if applicable)
□ sitemap-images.xml — for image indexing

Requirements:
□ Maximum 50,000 URLs per sitemap file
□ Maximum 50MB per file
□ Include only canonical, indexable URLs
□ Include <lastmod> for all pages
□ Exclude: paginated pages (except page 1), filtered URLs, /admin/, /private/

Basic template:
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yourdomain.com/</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://yourdomain.com/services/</loc>
    <lastmod>2026-04-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>

Submit to:
→ Google Search Console → Sitemaps
→ Bing Webmaster Tools → Sitemaps
→ IndexNow API (auto-notifies multiple engines)
```

### Canonical URLs

```html
<!-- Add to <head> of every page — points to the preferred version of the URL -->
<link rel="canonical" href="https://yourdomain.com/your-page/" />

Rules:
□ Every page needs a canonical (even if it's self-referencing)
□ Canonical = HTTPS, www or non-www (pick one globally), no trailing query params
□ Paginated pages: page 2+ canonical to page 1 (or self-canonical + rel=next/prev)
□ No canonical for pages you don't want indexed (use noindex instead)
```

### Site Architecture

```
Golden rule: Every page reachable within 3 clicks from homepage

Recommended structure for lead gen site:
Homepage (1)
├── Services/ (pillar pages)
│   ├── service-a/ (cluster)
│   ├── service-b/ (cluster)
│   └── service-c/ (cluster)
├── Blog/ (topical authority)
│   ├── category-a/ (pillar)
│   │   ├── article-1/ (cluster)
│   │   └── article-2/ (cluster)
├── About/
├── Contact/
└── [Thank-you/] (noindex)

Internal linking rules:
□ Every cluster page links back to its pillar page
□ Pillar pages link to all cluster pages
□ Homepage links to all pillar pages
□ Use descriptive anchor text (not "click here")
□ 3-5 internal links per page minimum
```

### JavaScript SEO (Critical for Custom-Coded Sites)

```
Google uses a two-wave rendering process:
Wave 1: Crawls raw HTML (immediate)
Wave 2: Renders JavaScript (delayed — hours to days later)

Best practice: Critical SEO content in raw HTML, not JS-rendered
□ Main headings (H1, H2) in HTML
□ Body text in HTML
□ Internal links in HTML (not JS-added)
□ Meta tags in <head> — not dynamically injected by JS

Test with: Google Search Console → URL Inspection → View Crawled Page
Also: Search Console → URL Inspection → Test Live URL
```

---

## DOMAIN 2: ON-PAGE SEO

**Priority: CRITICAL**

### Title Tags

```
Format: Primary Keyword | Brand Name
Or: Primary Keyword — Secondary Keyword | Brand Name

Rules:
□ 50-60 characters (longer gets truncated in SERPs)
□ Primary keyword toward the beginning
□ Every page has unique title
□ Do NOT repeat titles across pages

Examples:
✓ "Google Ads Management for Contractors | RA Agency"
✓ "Lead Generation Services — Performance Marketing | RA Agency"
✗ "Home | RA Agency" (no keyword value)
✗ "Services" (too vague, too short)
```

### Meta Descriptions

```
Purpose: Not a direct ranking signal, but drives CTR from SERPs
Format: 150-160 characters, include primary keyword, clear CTA

Example:
"Generate high-quality leads for your business with our Google Ads 
management service. Guaranteed performance. Book a free audit today."

Rules:
□ Unique for every page
□ Active voice, action verbs
□ Include a value proposition
□ Match search intent (don't bait-and-switch)
```

### Header Hierarchy

```html
<h1>One H1 per page — primary topic (matches title intent)</h1>
  <h2>Major section heading — secondary keywords</h2>
    <h3>Sub-section — long-tail keywords</h3>
      <h4>Detail level (use sparingly)</h4>

Rules:
□ Exactly ONE H1 per page
□ H1 must contain or closely match the primary target keyword
□ H2s should cover major subtopics (think: table of contents)
□ Don't skip levels (H1 → H3 with no H2)
□ Headers should read naturally — not keyword-stuffed
```

### E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

Google's quality evaluator framework — significantly amplified in March 2026 core update.

```
EXPERIENCE:
□ First-hand content: "I tested X and found Y"
□ Case studies with real results (including yours)
□ Screenshots, data, specific numbers
□ Author bio with verifiable credentials
□ Date of experience noted

EXPERTISE:
□ Author pages with credentials, portfolio, LinkedIn
□ Content depth — covers topic comprehensively, not superficially
□ Cites authoritative sources (link out to research, data)
□ Demonstrates knowledge competitors don't have

AUTHORITATIVENESS:
□ Backlinks from recognized sites in your industry
□ Brand mentions on other authoritative sites
□ Speaking/press mentions
□ Social proof (awards, certifications, case studies)
□ Google Knowledge Panel (entity recognition)

TRUSTWORTHINESS:
□ HTTPS
□ Privacy policy, terms of service, contact page
□ Physical address (if local)
□ Clear authorship on all content
□ No deceptive content, misleading claims
□ Positive reviews and testimonials
□ Updated "Last modified" dates on content
```

### Keyword Research Framework

```
INTENT CATEGORIES:
□ Informational: "how to generate leads" → blog content
□ Commercial Investigation: "best lead gen agency" → comparison/service pages
□ Transactional: "hire lead gen agency" → landing pages, service pages
□ Navigational: "RA Agency contact" → brand pages

TARGETING STRATEGY:
□ Head terms (1-2 words): high volume, high competition → pillar pages
□ Middle tail (2-3 words): medium volume, medium competition → service pages
□ Long tail (4+ words): lower volume, low competition → blog posts, FAQs

PRIMARY RESEARCH TOOLS:
□ Google Search Console → Queries (what you already rank for — gold)
□ Google Keyword Planner (free in Google Ads account)
□ Ahrefs / Semrush (paid — most complete data)
□ "People Also Ask" boxes (Google SERPs — free insight into related questions)
□ Answer The Public / AlsoAsked.com (question-based keyword discovery)

COMPETITIVE ANALYSIS:
□ Ahrefs → Site Explorer → Enter competitor → Organic keywords
□ Find pages ranking #4-15 (you can beat them)
□ Find keywords they rank for that you don't → content gaps
```

---

## DOMAIN 3: SCHEMA MARKUP & STRUCTURED DATA

**Priority: HIGH — Required for Rich Results + AI citation**

### Why Schema Matters in 2026

Beyond rich results (star ratings, FAQ dropdowns in SERPs), Google's Gemini-powered AI Mode uses schema markup to verify claims, establish entity relationships, and assess source credibility. Schema that accurately describes content **increases AI citation probability** even when no traditional rich result is displayed.

### Core Schema Types for a Lead Gen Website

**1. Organization Schema (Every Site)**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Your Company Name",
  "url": "https://yourdomain.com",
  "logo": "https://yourdomain.com/logo.png",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-XXX-XXX-XXXX",
    "contactType": "customer service",
    "availableLanguage": "English"
  },
  "sameAs": [
    "https://linkedin.com/company/yourcompany",
    "https://twitter.com/yourhandle"
  ]
}
</script>
```

**2. WebSite Schema (Homepage only — enables Sitelinks Search Box)**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Your Company Name",
  "url": "https://yourdomain.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://yourdomain.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
</script>
```

**3. Service Schema (Each Service Page)**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Google Ads Management",
  "serviceType": "Digital Marketing",
  "provider": {
    "@type": "Organization",
    "name": "Your Company Name"
  },
  "description": "Full-service Google Ads management for lead generation.",
  "areaServed": {
    "@type": "Country",
    "name": "United States"
  },
  "offers": {
    "@type": "Offer",
    "price": "500",
    "priceCurrency": "USD"
  }
}
</script>
```

**4. FAQPage Schema (Service pages, blog posts — critical for AI citation)**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does it take to see results from Google Ads?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most campaigns see initial data within 7-14 days. Meaningful optimization data typically requires 30-90 days and 30+ conversions."
      }
    },
    {
      "@type": "Question",
      "name": "What is the minimum budget for Google Ads?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There is no official Google Ads minimum budget. However, we recommend a minimum of $1,000/month for meaningful data collection and optimization."
      }
    }
  ]
}
</script>
```

**5. BreadcrumbList Schema (Every interior page)**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://yourdomain.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Services",
      "item": "https://yourdomain.com/services/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Google Ads Management",
      "item": "https://yourdomain.com/services/google-ads/"
    }
  ]
}
</script>
```

**6. Article Schema (Blog posts)**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your Article Title",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://yourdomain.com/about/author/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Your Company",
    "logo": "https://yourdomain.com/logo.png"
  },
  "datePublished": "2026-04-20",
  "dateModified": "2026-04-20",
  "image": "https://yourdomain.com/blog/article-image.jpg"
}
</script>
```

**7. Review / AggregateRating (if you have testimonials)**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Your Company",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "47"
  }
}
</script>
```

### Testing Tools

```
□ Google Rich Results Test: search.google.com/test/rich-results
□ Schema Markup Validator: validator.schema.org
□ Google Search Console → Enhancements (see which rich results are active)
```

---

## DOMAIN 4: LLMS.TXT — THE AI VISIBILITY STANDARD

**Priority: HIGH — Low effort, growing impact**

### What It Is

llms.txt is a plain text Markdown file placed at your website root (`yourdomain.com/llms.txt`) that curates a shortlist of your most important pages specifically for AI/LLM consumption. Think of it as a sitemap, but written for AI systems rather than search engine crawlers.

**Adoption status (April 2026):** Anthropic, Stripe, Zapier, Cloudflare, and hundreds of developer-tool companies have adopted it. Developer-facing AI tools (Cursor, Continue, Aider, RAG frameworks) actively read it. No major consumer AI platform has officially committed to reading it as a first-class input — but it's a zero-cost signal worth implementing.

### Full Specification

```markdown
# [Your Site/Company Name]

[1-3 sentence description of what the site is, who it serves, and what value it provides. Be direct and specific — this is read by AI, not humans.]

## Core Services

- [Service Page Title](https://yourdomain.com/services/google-ads/): Full-service Google Ads management for lead generation businesses.
- [Service Page Title](https://yourdomain.com/services/seo/): SEO strategy and implementation for organic traffic growth.

## Guides & Resources

- [Guide Title](https://yourdomain.com/blog/google-ads-guide/): Comprehensive guide to setting up Google Ads for lead generation.
- [Guide Title](https://yourdomain.com/blog/lead-gen-strategy/): Complete lead generation strategy for service businesses.

## About

- [About Us](https://yourdomain.com/about/): Company background, team, and approach to digital marketing.
- [Case Studies](https://yourdomain.com/case-studies/): Real client results with data and methodology.
- [Contact](https://yourdomain.com/contact/): Get in touch for a free consultation.

## Tools & Resources

- [Free Audit](https://yourdomain.com/free-audit/): Free Google Ads account audit.
```

### llms-full.txt Variant

Some sites create an optional `llms-full.txt` at the root — it contains the **full concatenated text** of key pages, allowing AI systems to access comprehensive content in a single request without crawling multiple pages.

```
yourdomain.com/llms.txt       ← Curated index (always create this)
yourdomain.com/llms-full.txt  ← Full text dump (optional, for content-heavy sites)
```

### What NOT to Include

```
□ Login, checkout, or cart pages
□ Legal boilerplate (privacy policy, terms)
□ Thin or duplicate content
□ Internal search results (/search?q=...)
□ Admin or private areas
□ Paginated results
```

### Relationship to Other Files

| File | Purpose | Audience |
|------|---------|---------|
| `robots.txt` | Access control — what crawlers can/cannot visit | All crawlers |
| `sitemap.xml` | Complete URL map for indexing | Search engine crawlers |
| `llms.txt` | Curated content guide for AI | AI/LLM systems |
| `llms-full.txt` | Full text of key pages for AI | AI/LLM systems (RAG) |

---

## DOMAIN 5: GEO — GENERATIVE ENGINE OPTIMIZATION

**Priority: CRITICAL — This is where search is going**

### What GEO Is

Generative Engine Optimization (GEO) is the practice of optimizing content to be cited by AI search engines: ChatGPT Search, Perplexity, Google AI Overviews, Google AI Mode, Microsoft Copilot, Claude, and Gemini. Traditional SEO gets you ranked in a list of blue links. GEO gets you cited inside the AI-generated answer itself.

**Key market shift (2026):** Organic CTR drops by **61%** on searches that trigger AI Overviews. BUT — if your content is cited inside an AI Overview, cited pages earn **35% more clicks** than standard organic results. The game has changed: be cited or be irrelevant.

### Google AI Overviews / AI Mode Optimization

**44% of AI Overview citations come from the first 30% of a page.** Your introduction is your most valuable AI real estate.

```
OPTIMIZATION CHECKLIST:

□ "Quick Answer Block" above the fold:
  Write a 134-167 word self-contained answer to the page's primary question
  at the very top of the page, before any other content.
  This is what AI systems extract for citations.

□ Semantic Completeness Score:
  Content scoring 8.5/10+ on semantic completeness is 4.2x more likely to be cited.
  Cover the full topic — don't leave obvious subtopics out.

□ FAQ Sections:
  Add a structured FAQ at the bottom of every service page and blog post.
  Use Question/Answer format explicitly. Match "People Also Ask" questions.
  Implement FAQPage schema (see Domain 3).

□ Author Credentials:
  Add an author byline with verifiable credentials on all content.
  Link to author page with LinkedIn, published work, professional affiliations.
  Google AI Mode prioritizes content from identifiable, credentialed authors.

□ Data & Statistics:
  Include specific numbers, percentages, and dates.
  Cite authoritative sources (link out to research papers, gov data, industry reports).
  Original data/research cited by others = highest AI citation probability.

□ Content Freshness:
  Update key pages every 7-14 days for active AI citation.
  Update <lastmod> in sitemap when content changes.
  Add "Last updated: [date]" visibly on page.

□ Entity Optimization:
  Mention your brand name, key people, location, and service names clearly.
  Use consistent naming across all pages.
  Link to your own LinkedIn, Crunchbase, Wikipedia (if applicable).
```

### Perplexity AI Optimization

```
Perplexity indexes the web in real-time and heavily favors:
□ Primary sources and original research
□ Specific, data-backed claims with citations
□ Content that directly answers questions (no preamble)
□ Well-structured pages with clear headers
□ Fast-loading pages (they crawl frequently)

Perplexity's own crawler: PerplexityBot — ensure allowed in robots.txt
New content enters Perplexity citation pool within 3-5 business days.
```

### ChatGPT Search Optimization

```
ChatGPT Search is powered by Bing's index.
Optimizing for Bing = optimizing for ChatGPT Search.

Key signals:
□ Strong Bing Webmaster Tools setup (see Domain 7)
□ IndexNow implementation (notifies Bing instantly)
□ Social media signals (Bing weights these)
□ Exact-match keyword optimization
□ Fast page speed
□ Quality backlinks
```

### Microsoft Copilot Optimization

```
Copilot draws from:
□ Bing's main search index
□ Bing's AI Performance data (new Feb 2026 feature in Bing Webmaster Tools)
□ LinkedIn content (Microsoft owns LinkedIn)

Actions:
□ Bing Webmaster Tools → AI Performance dashboard (new Feb 2026)
   Shows how often your content appears in Copilot answers
□ Optimize LinkedIn company page and publish articles there
□ Submit all pages via IndexNow
```

### Content Patterns That Get AI Citations

```
HIGH CITATION PROBABILITY:
✓ Numbered lists with specific facts ("7 types of...", "3 reasons why...")
✓ Comparison tables (X vs Y)
✓ Step-by-step instructions with numbered steps
✓ Definition paragraphs ("X is defined as...")
✓ Data-backed claims with citations ("According to [source], X%...")
✓ Quick answer summaries (134-167 words)
✓ FAQ blocks (Q&A format)
✓ "Best X for Y" listicles
✓ Original research with specific statistics

LOW CITATION PROBABILITY:
✗ Pure opinion without data
✗ Vague claims ("many businesses find that...")
✗ Long paragraphs without structure
✗ Content without author attribution
✗ Outdated information (no "last updated" date)
✗ Thin content (under 800 words for competitive topics)
```

### GEO Measurement Tools

```
□ Semrush AI Toolkit — tracks AI Overview presence per keyword
□ Otterly.AI — dedicated AI visibility tracking (ChatGPT, Perplexity, Gemini)
□ Profound — enterprise AI citation monitoring
□ BrandMentions — tracks brand mentions across AI outputs
□ Manual testing: search your target queries in each AI tool, check if cited
```

---

## DOMAIN 6: AI CRAWLERS — COMPLETE REFERENCE

**Priority: HIGH — Configure robots.txt correctly or lose AI visibility**

### AI Search/Browse Crawlers (ALLOW — these cite you)

| Bot | Company | User-Agent String | Purpose |
|-----|---------|-----------------|---------|
| GPTBot | OpenAI | `GPTBot` | ChatGPT Search + retrieval |
| OAI-SearchBot | OpenAI | `OAI-SearchBot` | SearchGPT indexing |
| ChatGPT-User | OpenAI | `ChatGPT-User` | Real-time browsing for users |
| PerplexityBot | Perplexity AI | `PerplexityBot` | Perplexity answer generation |
| Perplexity-User | Perplexity AI | `Perplexity-User` | User-triggered fetches |
| Google-Extended | Google | `Google-Extended` | Gemini AI features |
| Bingbot | Microsoft | `bingbot` | Bing + Copilot retrieval |
| ClaudeBot | Anthropic | `ClaudeBot` | Claude web retrieval |
| Applebot | Apple | `Applebot` | Siri knowledge |
| Applebot-Extended | Apple | `Applebot-Extended` | Apple AI features |
| YouBot | You.com | `YouBot` | You.com AI search |
| PhindBot | Phind | `PhindBot` | Phind developer search |
| DuckDuckBot | DuckDuckGo | `DuckDuckBot` | DDG AI integrations |

### AI Training Crawlers (BLOCK — scrape for training data, no citation benefit)

| Bot | Company | User-Agent String |
|-----|---------|-----------------|
| CCBot | Common Crawl | `CCBot` |
| anthropic-ai | Anthropic | `anthropic-ai` |
| Bytespider | ByteDance (TikTok) | `Bytespider` |
| PetalBot | Huawei | `PetalBot` |
| Diffbot | Diffbot | `Diffbot` |
| Omgilibot | Webz.io | `Omgilibot` |
| magpie-crawler | Magpie | `magpie-crawler` |
| DataForSeoBot | DataForSEO | `DataForSeoBot` |

**Note on ClaudeBot:** Anthropic deprecated `anthropic-ai` in 2024 in favor of `ClaudeBot`. The `anthropic-ai` agent was the training crawler; `ClaudeBot` is now the retrieval crawler for Claude's web search. Block `anthropic-ai`, allow `ClaudeBot`.

**ClaudeBot activity (Q1 2026):** ClaudeBot has approximately doubled its crawl rate between Q3 2025 and Q1 2026, indicating significant scaling of Anthropic's retrieval infrastructure.

---

## DOMAIN 7: WEBMASTER TOOLS & SEARCH ENGINE SUBMISSION

**Priority: CRITICAL**

### Google Search Console

**URL:** search.google.com/search-console
**Cost:** Free

Key features:
```
□ Performance → Queries: Real keyword data (impressions, clicks, CTR, position)
□ Performance → Pages: Which pages drive organic traffic
□ Performance → Devices: Mobile vs desktop performance
□ URL Inspection: Check indexing status of any URL
□ Coverage → Errors: Pages Google can't index (404s, redirect errors, noindex)
□ Sitemaps: Submit and monitor sitemap status
□ Core Web Vitals: LCP/CLS/INP data from real users (field data)
□ Mobile Usability: Mobile-specific issues
□ Enhancements: Rich results status (FAQ, breadcrumbs, etc.)
□ Security: Manual actions, security issues
□ Links: Your top linked pages (internal + external)
```

**New in 2026:**
- AI Mode visibility data (showing when your content appears in Google AI Mode)
- Search Generative Experience (SGE) citation tracking

### Bing Webmaster Tools

**URL:** bing.com/webmasters
**Cost:** Free
**Why it matters:** Bing powers ChatGPT Search + Microsoft Copilot. Combined market share ~33% in 2026.

Key features:
```
□ Dashboard: Clicks, impressions, crawl status
□ Search Performance: Keyword data (like Google Search Console for Bing)
□ URL Submission: Submit individual URLs instantly (manual + API)
□ Sitemaps: Submit and monitor
□ Site Explorer: See Bing's view of your site
□ SEO Reports: Automated technical SEO analysis (Bing's own audit)
□ Keyword Research Tool: Built-in keyword data
□ Backlink Data: See who links to you according to Bing
□ Crawl Control: Set crawl rate and preferences
□ IndexNow: Direct integration (the easiest way to submit)

NEW Feb 2026:
□ AI Performance Dashboard: Shows how often your content appears in
  Copilot and Bing AI-generated summaries. UNIQUE TO BING — Google
  doesn't have this yet. Monitor this weekly.
```

**Setup steps:**
```
1. bing.com/webmasters → Sign in with Microsoft account
2. Add site → Enter domain
3. Verify ownership:
   □ XML file method: Download verification file → upload to root
   □ Meta tag: Add <meta name="msvalidate.01" content="XXXXX"> to <head>
   □ CNAME record in DNS
4. Submit sitemap
5. Enable IndexNow (see below)
```

### IndexNow Protocol

**URL:** indexnow.org
**Cost:** Free
**Supported by:** Bing, Yandex, Seznam.cz, Naver, DuckDuckGo (via Bing)
**Google status:** Testing, not yet officially adopted (but doesn't ignore it either)

**What it does:** Instantly notifies search engines when a URL is added, updated, or deleted. Content indexed in **minutes**, not days/weeks.

**Implementation for custom-coded website:**

**Step 1 — Generate API Key**
```
Any random unique string works:
Example: 8f3a9d1b4e2c7f6a0d5b8e3c1a4f7d2b

Or generate via:
□ bing.com/webmasters → IndexNow → Generate Key
□ Online UUID generator
```

**Step 2 — Create Key Verification File**
```
Create a file named exactly: [your-key].txt
Content of file: [your-key]

Example:
Filename: 8f3a9d1b4e2c7f6a0d5b8e3c1a4f7d2b.txt
Content: 8f3a9d1b4e2c7f6a0d5b8e3c1a4f7d2b

Upload to: yourdomain.com/8f3a9d1b4e2c7f6a0d5b8e3c1a4f7d2b.txt
```

**Step 3 — Submit URLs**

Single URL (immediate, for new/updated pages):
```bash
curl "https://www.bing.com/indexnow?url=https://yourdomain.com/new-page/&key=YOUR_KEY"
```

Bulk submission (up to 10,000 URLs per request):
```bash
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "host": "yourdomain.com",
    "key": "YOUR_KEY",
    "keyLocation": "https://yourdomain.com/YOUR_KEY.txt",
    "urlList": [
      "https://yourdomain.com/page-1/",
      "https://yourdomain.com/page-2/",
      "https://yourdomain.com/page-3/"
    ]
  }'
```

**Step 4 — Automate (Critical)**

For custom-coded sites, trigger IndexNow submission automatically when content changes:

```javascript
// indexnow.js — call this function whenever you publish/update a page
async function notifyIndexNow(urls) {
  const API_KEY = 'YOUR_INDEXNOW_KEY';
  const HOST = 'yourdomain.com';
  
  // Single URL shorthand
  if (typeof urls === 'string') {
    const response = await fetch(
      `https://www.bing.com/indexnow?url=${encodeURIComponent(urls)}&key=${API_KEY}`
    );
    return response.status; // 200 = success
  }
  
  // Bulk submission
  const response = await fetch('https://api.indexnow.org/indexnow', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
    body: JSON.stringify({
      host: HOST,
      key: API_KEY,
      keyLocation: `https://${HOST}/${API_KEY}.txt`,
      urlList: urls
    })
  });
  
  return response.status; // 200 = success, 202 = accepted
}

// Usage:
// On new page publish:
notifyIndexNow('https://yourdomain.com/new-page/');

// On batch update (e.g., site redesign):
notifyIndexNow([
  'https://yourdomain.com/',
  'https://yourdomain.com/services/',
  'https://yourdomain.com/about/'
]);
```

**Response codes:**
```
200 OK — URL submitted successfully
202 Accepted — URL will be submitted (queued)
400 Bad Request — Invalid URL format or key
403 Forbidden — Key doesn't match verification file
422 Unprocessable Entity — URL not from same host as key
429 Too Many Requests — Rate limited
```

### Yandex Webmaster

**URL:** webmaster.yandex.com
**Relevant if:** You have Russian-speaking audience
**Setup:** Same as Google Search Console process — verify domain, submit sitemap

### DuckDuckGo

DuckDuckGo does not have its own web index. It aggregates results primarily from:
- Bing (main source)
- Yahoo
- Its own DuckDuckBot crawler (for some results)

**Action:** Optimize for Bing → DuckDuckGo follows automatically.

### Ecosia, Brave Search, Startpage

```
Ecosia → powered by Bing → Bing Webmaster Tools = Ecosia coverage
Startpage → powered by Google → Google Search Console = Startpage coverage

Brave Search → Independent index (unique)
  URL: search.brave.com/goggles (for publisher tools)
  Submit via: brave.com/search/webmaster
  Brave's own crawler: Brave Search Bot

Action: Submit to Bing + Google → covers ~95% of all search traffic
Brave Search is growing but still ~3-5% market share — low priority initially
```

---

## DOMAIN 8: BING-SPECIFIC SEO

**Priority: HIGH (often overlooked, high ROI)**

### Why Bing Matters More Than Most Realize

```
Market share breakdown (2026):
□ Google: ~89%
□ Bing: ~8%
□ Yahoo: ~2% (uses Bing results)
□ DuckDuckGo: ~1% (uses Bing results)
□ Ecosia: <1% (uses Bing results)

Effective Bing coverage: ~11% of all search traffic

PLUS:
□ Bing powers ChatGPT Search (400M+ users)
□ Bing powers Microsoft Copilot (integrated in Windows 11)
□ Bing has older, higher-income demographic — higher value leads
□ Bing traffic often converts at higher rates than Google for B2B
```

### Bing-Specific Ranking Factors (Different from Google)

```
1. EXACT-MATCH KEYWORDS
   Bing weights exact keyword matches more heavily than Google.
   Include exact target keyword in: title tag, meta description, H1, first paragraph, URL.
   
2. SOCIAL MEDIA SIGNALS (UNIQUE TO BING)
   Bing officially weights social signals — shares, likes, engagement.
   LinkedIn signals are especially strong (Microsoft owns both).
   
3. DOMAIN AGE & AUTHORITY
   Bing favors older, established domains more explicitly than Google.
   .edu and .gov links carry particular weight.
   
4. META DESCRIPTION AS RANKING SIGNAL
   Unlike Google, Bing uses meta description for relevance assessment.
   Include primary keyword in meta description.
   
5. LINK QUANTITY MATTERS MORE
   Bing weights link volume more than Google (Google is more about quality).
   More links from relevant (not necessarily top-tier) sites helps.
   
6. MULTIMEDIA CONTENT
   Bing favors pages with images and video, especially with descriptive alt text.
   Bing has its own image and video search — optimize for these.
   
7. CLICK-THROUGH RATE
   Bing explicitly uses CTR as a ranking signal — title/meta optimization matters.
```

### Bing Webmaster Tools SEO Reports

```
Unique to Bing — no Google equivalent:
□ SEO Reports → Site Scan: Automated crawl of your site with specific recommendations
□ SEO Reports → Inbound Links: Link profile analysis
□ SEO Reports → Keyword Research: Search volume data
□ New: AI Performance (Feb 2026) → Copilot citation tracking
```

---

## DOMAIN 9: CONTENT SEO STRATEGY

**Priority: HIGH**

### Topical Authority & Content Clusters

**Performance data (2026):**
- Sites sustaining cluster publishing for 12+ months see **40% higher organic traffic** than single-page strategies
- Content clusters show 30% more organic traffic, 2.5x longer rankings, 4.7x more link equity on priority pages
- AI citation rate can increase from 12% to 41% with proper cluster architecture

**Structure:**
```
PILLAR PAGE (3,000-5,000 words):
□ Comprehensive coverage of the main topic
□ Links to ALL cluster pages
□ Optimized for head-term keyword
□ Acts as the canonical authority on the subject

CLUSTER PAGES (1,000-2,000 words each):
□ Each covers one specific subtopic in depth
□ Links back to pillar page
□ Links to 2-3 related cluster pages
□ Optimized for long-tail keywords

EXAMPLE:
Pillar: "Google Ads Management — Complete Guide"
Clusters:
  → "Google Ads Keyword Research Guide"
  → "Google Ads Bidding Strategies Explained"  
  → "Google Ads Quality Score: How to Improve It"
  → "Google Ads Conversion Tracking Setup"
  → "Google Ads Budget Optimization"
  → "Search vs. Display vs. Performance Max Campaigns"
```

### E-E-A-T Content Framework

```
Every piece of content should answer these before publishing:
□ Who wrote this? (Author byline with credentials)
□ When was this written/updated? (Visible date + lastmod in sitemap)
□ Why should I trust this? (Data, citations, case studies)
□ What first-hand experience informs this? (Real examples, results)
```

### Featured Snippets Optimization

```
Snippet types and how to target each:

PARAGRAPH SNIPPETS (most common):
→ Write a 40-60 word direct answer immediately after the relevant H2
→ Start the answer with the question's keywords
→ Example H2: "What Is Google Ads Quality Score?"
→ Immediately below: "Google Ads Quality Score is a 1-10 rating that..."

LIST SNIPPETS:
→ Use numbered or bulleted lists for process/step content
→ Keep list items concise (5-10 words each)
→ Use H2 "How to [X]" or "Top [X] ways to..."

TABLE SNIPPETS:
→ Use HTML <table> elements for comparison content
→ Include headers and keep cells concise
→ Google extracts these directly for table snippets

KEY: Your page must already rank in top 10 for that query to get the snippet
```

### People Also Ask (PAA) Targeting

```
Strategy:
1. Search your target keyword in Google
2. Note all PAA questions that appear
3. Create FAQ sections that answer each PAA question
4. Use the exact question text as the FAQ question
5. Answer in 40-80 words, directly and completely
6. Add FAQPage schema (see Domain 3)

This creates a self-reinforcing loop:
Answer PAA → Google pulls your answer → More visibility → Higher CTR → Better ranking
```

### Content Freshness

```
Google's freshness algorithm favors recently updated content for:
□ News and time-sensitive topics (update constantly)
□ "Best X" and comparison pages (update quarterly)
□ How-to guides and tutorials (update annually minimum)
□ Landing pages and service pages (update when services change)

Freshness signals:
□ <lastmod> in sitemap.xml (update every time content changes)
□ Visible "Last updated: [date]" on page
□ Adding new data, sections, or statistics
□ Updating outdated statistics to current year
```

---

## DOMAIN 10: OFF-PAGE SEO & LINK BUILDING

**Priority: HIGH**

### What Works in 2026

Survey of 518 SEOs: **48.6% say digital PR is the most effective tactic** — replacing guest posting as the top strategy.

**New key metric (2026):** Brand mentions correlate **3x more strongly with AI search visibility** than traditional backlinks (0.664 vs 0.218 correlation). 66.2% of practitioners now track AI citation as a primary KPI.

### Digital PR (Top Priority)

```
Definition: Earning media coverage and high-authority backlinks from reputable 
online publications by creating genuinely newsworthy content.

What journalists link to:
□ Original research with surprising statistics
□ Data studies using proprietary data
□ Expert opinions on trending topics
□ Visual content (infographics, data visualizations)
□ Controversial-but-defensible takes on industry topics
□ Localized versions of national stories

Process:
1. Identify 20-30 target publications your audience reads
2. Identify journalists who cover your industry (use Hunter.io, Journalist.ai)
3. Create newsworthy asset (original data, research, tool)
4. Craft pitch: Subject line = headline, body = 3 sentences max
5. Follow up once (3-5 days later)
6. Track placements → monitor for unlinked mentions → request link
```

### Content Gap Link Building

```
1. Identify competitor pages with most backlinks (Ahrefs → Site Explorer → Top Pages)
2. Create substantially better version of that content
3. Find sites linking to competitor's version (Ahrefs → Backlinks)
4. Reach out: "You linked to [X] — we've created [better resource] — would you update?"
```

### Unlinked Brand Mention Reclamation

```
1. Set up Google Alerts for your brand name
2. Use Ahrefs Alerts or Mention.com for monitoring
3. When you find a mention without a link → reach out to author
4. "Thanks for mentioning us in your article — would you mind adding a link back to [URL]?"
5. Success rate: ~30-40% for politely requested reclamations
```

### Guest Posting (Still Works with Conditions)

```
GOOGLE VALUES:
✓ Target publications your audience actually reads
✓ Content is genuinely useful and high-quality
✓ Link is contextually relevant to the article
✓ Author bio is real (your real name, real credentials)

GOOGLE DISCOUNTS/PENALIZES:
✗ Mass guest post factories
✗ Links in author bio to keyword-rich anchor text
✗ Off-topic publications
✗ Obviously paid placements with commercial anchor text
```

---

## DOMAIN 11: INDEXING SPEED

**Priority: HIGH**

### Multi-Engine Submission Strategy

```
When you publish or update a page, submit to ALL of these:

IMMEDIATE:
□ IndexNow API → notifies Bing, Yandex, Seznam, Naver simultaneously
□ Google Search Console → URL Inspection → Request Indexing (manual, 1 URL at a time)

AUTOMATED:
□ Dynamic sitemap with <lastmod> → search engines check this regularly
□ IndexNow in your build/publish pipeline (auto-fires on content change)

MONITORING:
□ Google Search Console → URL Inspection (check indexed status)
□ Bing Webmaster Tools → URL Submission → check status
```

### Google Indexing API

```
Google's Indexing API is officially for pages with JobPosting or BroadcastEvent schema.
However, Google says it may crawl pages notified via the API.

Access requirements:
□ Google Cloud project with Indexing API enabled
□ Service account with "Owner" permission on your Google Search Console property
□ Maximum 200 URL submissions per day

For most sites: IndexNow + sitemap + manual URL inspection is sufficient.
The Indexing API is best for sites with very frequently updated content.
```

---

## DOMAIN 12: SEO TOOLS ECOSYSTEM

**Priority: MEDIUM (need at least one of each category)**

### Tool Categories & Recommendations

**TIER 1 — FREE, USE ALWAYS:**

| Tool | Purpose | URL |
|------|---------|-----|
| Google Search Console | Real performance data, indexing | search.google.com/search-console |
| Bing Webmaster Tools | Bing data + AI Performance | bing.com/webmasters |
| Google PageSpeed Insights | Core Web Vitals measurement | pagespeed.web.dev |
| Google Rich Results Test | Schema validation | search.google.com/test/rich-results |
| Schema Validator | Schema markup testing | validator.schema.org |
| Ahrefs Webmaster Tools | Free backlink + SEO audit for your own site | ahrefs.com/webmaster-tools |

**TIER 2 — PAID, CHOOSE ONE (Primary Platform):**

| Tool | Best For | Price | Verdict |
|------|---------|-------|---------|
| **Semrush** | Agency work, full suite (keywords, audit, PPC, content) | $129/mo | Best all-rounder |
| **Ahrefs** | Backlink analysis, content research | $129/mo | Best backlink data |
| Moz Pro | Beginner-friendly, domain authority | $99/mo | Good for basics |

**Recommendation for RA-Project:** Start with Ahrefs ($129/mo) for backlink analysis and keyword research. Add Semrush later if you need PPC keyword data alongside SEO.

**TIER 3 — TECHNICAL AUDIT:**

| Tool | Purpose | Price |
|------|---------|-------|
| **Screaming Frog** | Deep technical crawl, 500-URL free | $259/year |
| Sitebulb | Visual crawl reports, good for presentations | $179/year |
| Google Lighthouse | Page-level performance + SEO audit | Free (Chrome DevTools) |

**TIER 4 — AI VISIBILITY TRACKING (NEW 2026):**

| Tool | Purpose | Price |
|------|---------|-------|
| Semrush AI Toolkit | Google AI Overview tracking | Included in Semrush |
| Otterly.AI | Multi-platform AI citation monitoring | ~$49/mo |
| Profound | Enterprise AI visibility | Custom |
| BrandMentions | AI brand mention tracking | ~$99/mo |

**TIER 5 — KEYWORD RESEARCH SUPPLEMENTARY (FREE):**

```
□ Answer The Public (answerthepublic.com) — question-based keyword discovery
□ AlsoAsked.com — People Also Ask keyword mapping
□ Google Keyword Planner — volume data (free with Google Ads account)
□ Ubersuggest — free tier with limited queries
□ Google Trends — trending topics and seasonal patterns
```

---

## DOMAIN 13: ENTITY SEO & BRAND SIGNALS

**Priority: HIGH — Foundation for AI citation**

### What Entity SEO Is

Search engines (and AI systems) think in terms of entities — real-world people, places, organizations, concepts — not just keywords. Building your brand as a recognized entity in Google's Knowledge Graph and across the web dramatically increases both traditional ranking signals and AI citation probability.

### Entity Building Checklist

```
DIGITAL FOOTPRINT (create consistent NAP: Name, Address, Phone across all):
□ Google Business Profile (maps.google.com/business) — even for non-local
□ LinkedIn Company Page (fill 100% — most important)
□ Crunchbase Company Profile
□ Wikipedia (if notable enough — very powerful, hard to get)
□ Wikidata entry (easier than Wikipedia, feeds knowledge graphs)
□ GitHub profile (if tech company)
□ Twitter/X business account
□ Facebook Business Page
□ Industry-specific directories (Clutch, G2, Trustpilot, etc.)

CONSISTENCY RULES:
□ Company name: exactly the same everywhere
□ URL: exactly the same everywhere (with or without www, https)
□ Description: same core description across all platforms
□ Logo: same logo image

KNOWLEDGE PANEL TRIGGERS:
□ Consistent brand mentions across authoritative sites
□ Wikipedia/Wikidata presence
□ Google Business Profile
□ Structured data (Organization schema with sameAs links)
□ Brand searches increasing over time

sameAs LINKS in Organization schema:
"sameAs": [
  "https://linkedin.com/company/[your-company]",
  "https://twitter.com/[handle]",
  "https://en.wikipedia.org/wiki/[Company]",  (if exists)
  "https://www.wikidata.org/wiki/Q[number]"   (if exists)
]
```

---

## DOMAIN 14: FULL TOOL LIST BY SEARCH ENGINE

### Submission & Management by Engine

| Search Engine | Market Share | Tool | URL | Notes |
|---------------|-------------|------|-----|-------|
| Google | ~89% | Google Search Console | search.google.com/search-console | Primary |
| Bing | ~8% | Bing Webmaster Tools | bing.com/webmasters | Covers Yahoo, DuckDuckGo, Ecosia, Copilot, ChatGPT |
| Yandex | ~2% (global) | Yandex Webmaster | webmaster.yandex.com | Russian market |
| DuckDuckGo | ~1% | Via Bing | — | No separate submission |
| Yahoo | ~1% | Via Bing | — | No separate submission |
| Ecosia | <1% | Via Bing | — | No separate submission |
| Brave Search | <1% | Brave Webmaster | search.brave.com/webmaster | Independent index |
| Baidu | Dominant in China | Baidu Webmaster | zhanzhang.baidu.com | If targeting China |
| Naver | Dominant in Korea | Naver Search Advisor | searchadvisor.naver.com | If targeting Korea |
| ChatGPT Search | Via Bing index | Bing Webmaster | — | Optimize for Bing |
| Perplexity | Direct crawl | PerplexityBot | — | Allow in robots.txt |
| Google AI Mode | Via Google | Search Console | — | AI Performance data |
| Microsoft Copilot | Via Bing | Bing AI Performance | bing.com/webmasters | Feb 2026 feature |

---

## PRIORITY MATRIX — WHERE TO START

| Priority | Domain | Effort | Impact | Do This |
|----------|--------|--------|--------|---------|
| 🔴 CRITICAL | Technical SEO Foundation | Medium | Very High | Week 1 |
| 🔴 CRITICAL | Google Search Console | Low | Very High | Week 1 |
| 🔴 CRITICAL | Bing Webmaster Tools | Low | High | Week 1 |
| 🔴 CRITICAL | IndexNow Implementation | Low | High | Week 1 |
| 🔴 CRITICAL | robots.txt Configuration | Low | High | Week 1 |
| 🟠 HIGH | Schema Markup (Org + FAQ + Service) | Medium | High | Week 2 |
| 🟠 HIGH | llms.txt Creation | Very Low | Growing | Week 2 |
| 🟠 HIGH | Core Web Vitals Optimization | Medium-High | High | Week 2-3 |
| 🟠 HIGH | Canonical Tags on All Pages | Low | High | Week 2 |
| 🟠 HIGH | On-Page SEO (Title, Meta, H1) | Medium | High | Week 2-3 |
| 🟡 MEDIUM | Content Cluster Strategy | High | Very High (long-term) | Month 1-2 |
| 🟡 MEDIUM | GEO Content Optimization | Medium | High | Month 1-2 |
| 🟡 MEDIUM | Topical Authority Building | Very High | Very High (long-term) | Ongoing |
| 🟡 MEDIUM | AI Visibility Tracking Setup | Low | Medium | Month 1 |
| 🟢 LOWER | Digital PR / Link Building | Very High | High (long-term) | Month 2+ |
| 🟢 LOWER | Entity Building (Wikidata, GBP) | Medium | Medium | Month 2+ |
| 🟢 LOWER | Brave Search Submission | Very Low | Low | Month 2 |

---

## EMERGING FACTORS 2026

### AI-Generated Content Policy

```
Google's stance (2026): Content quality matters, not content origin.
AI content is allowed if it demonstrates genuine E-E-A-T signals.
Pure AI-generated content without human expertise/review = at risk.

Best practice:
□ Human expert writes or substantially reviews all content
□ Author byline = real person with verifiable credentials
□ Content includes first-hand experience (what AI alone cannot provide)
□ Add original data, screenshots, or examples to AI-drafted content
```

### Google Helpful Content System

```
Ongoing algorithm (not a one-time update) running continuously.
Penalizes: Content created primarily for search engines, not humans.
Rewards: Content that satisfies the reader's full intent.

Self-audit questions:
□ Does this content provide original information/research?
□ Does the main heading/title match what the page actually delivers?
□ Would someone read this and feel they've learned something?
□ Would someone want to bookmark or share this?
□ Does this content compare favorably to other results for the same query?
```

### Zero-Click Searches

```
~60% of Google searches now end without a click (featured snippets, AI answers).
Adaptation strategy:
□ If your content gets featured (even without click) → brand awareness builds
□ Target informational queries where citation = brand building
□ For commercial queries, optimize for CTR (meta, title) not just ranking
□ Build email list from organic visitors → reduce dependency on search clicks
```

### Voice Search

```
Voice queries are conversational, longer, and question-based.
Optimization:
□ Use natural language in H2s/H3s ("How do I...", "What is the best...")
□ FAQ sections (voice assistants read FAQ answers directly)
□ Answer in first sentence after question heading
□ Target featured snippets (most voice answers come from position 0)
□ Local optimization (voice search is heavily local: "near me" queries)
```

---

## SOURCES

- [What is llms.txt? Complete Guide 2026](https://webaloha.co/llms-txt-complete-guide/)
- [AI Crawler User Agents Complete Reference 2026](https://pulserank.ai/ai-crawlers-user-agents/)
- [GEO Complete Guide — Search Engine Land](https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142)
- [GEO Definitive Guide — Enrich Labs](https://www.enrichlabs.ai/blog/generative-engine-optimization-geo-complete-guide-2026)
- [Core Web Vitals 2026 — W3Era](https://www.w3era.com/blog/seo/core-web-vitals-guide/)
- [Technical SEO Checklist 2026 — Kerkarmedia](https://kerkarmedia.com/technical-seo-checklist/)
- [Bing AI Performance Feature Announcement — Bing Blog](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- [IndexNow Documentation](https://www.indexnow.org/documentation)
- [Bing Webmaster Tools Setup 2026](https://jetfuel.agency/bing-webmaster-tools-setup-2026/)
- [Google AI Overviews Optimization — Semrush](https://www.semrush.com/blog/how-to-optimize-content-for-ai-search-engines/)
- [Schema Markup 2026 — Rankeo](https://rankeo.io/blog/schema-markup-complete-guide)
- [Schema Markup After March 2026 — Digital Applied](https://www.digitalapplied.com/blog/schema-markup-after-march-2026-structured-data-strategies)
- [Topical Authority SEO 2026 — ClickRank](https://www.clickrank.ai/topical-authority/)
- [Link Building 2026 — Sky SEO Digital](https://skyseodigital.com/link-building-strategies-that-actually-work-in-2026/)
- [Digital PR Link Building Guide](https://www.reporteroutreach.com/blog/digital-pr-link-building)
- [Bing SEO Ranking Factors 2026](https://seosherpa.com/bing-seo/)
- [Robots.txt Strategy 2026 for AI Crawlers](https://witscode.com/blogs/robots-txt-strategy-2026-managing-ai-crawlers/)
- [SEO Tools Comparison 2026 — Nucleo Analytics](https://nucleoanalytics.com/which-seo-tools-actually-perform-best-in-2026-we-tested-11/)
- [llms.txt Skepticism Analysis — Longato](https://www.longato.ch/llms-recommendation-2025-august/)

---

*Research compiled by CAI + MGI Council | RA-Project | April 20, 2026*
*Next step: Architecture design document based on this research*
