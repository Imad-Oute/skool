# SEO / GEO / LLM VISIBILITY — FULL INSTALLATION & CONFIGURATION GUIDE
**Project:** RA-Project | **Date:** April 20, 2026 | **Authored by:** CAI + MGI Council
**Website:** Custom-coded | **Stack:** 32 tools across 7 layers

---

## HOW TO USE THIS GUIDE

This guide covers every tool in the SEO/GEO/LLM Visibility ecosystem in exact installation order. Follow the phases sequentially — each phase depends on the previous one being complete. Every step includes exact commands, code snippets, and configurations you can copy directly into your codebase or browser.

**Phase order enforced by dependencies:**
- Layer 1 (Technical Foundation) must be complete before submitting to any search engine
- Layer 2 (Search Engine Presence) must be active before Layer 3 data is meaningful
- Layer 3 (Intelligence) informs Layer 4 (Content) decisions
- Layer 4 produces the content Layer 5 (Authority) amplifies
- Layer 6 (GEO) monitoring starts once you have content live

**Time estimates:**
| Phase | Layer | Time Required |
|-------|-------|---------------|
| Phase 1 — Technical Foundation | L1 | 4–8 hours |
| Phase 2 — Search Engine Presence | L2 | 3–5 hours |
| Phase 3 — Intelligence Setup | L3 | 2–4 hours |
| Phase 4 — Content Architecture | L4 | Ongoing |
| Phase 5 — Authority & Entity | L5 | 3–5 hours setup |
| Phase 6 — GEO & AI Visibility | L6 | 2–3 hours |
| Phase 7 — Analytics & Monitoring | L7 | 1–2 hours |

**Status tracking:**
- `{{Done}}` — completed steps
- `[ ]` — pending steps
- `{{Skip}}` — intentionally skipped

---

## PHASE 1 — TECHNICAL FOUNDATION (LAYER 1)
> Complete this before anything else. Technical errors here invalidate all other work.

---

### STEP 1 — robots.txt

**What you're doing:** Creating and deploying the robots.txt file that controls which crawlers can access which parts of your site. Critical: must allow AI search crawlers, must block AI training crawlers.

**File location:** `yourdomain.com/robots.txt` (must be at root, not /static/robots.txt)

**Create the file:**

```
# ============================================================
# robots.txt — RA-Project | Last updated: April 2026
# Strategy: Allow AI search crawlers, block AI training crawlers
# ============================================================

# ============================================================
# GOOGLE BOTS
# ============================================================
User-agent: Googlebot
Allow: /
Disallow: /admin/
Disallow: /login/
Disallow: /checkout/
Disallow: /api/
Disallow: /private/
Disallow: /internal/
Disallow: /*?*           # Block URL parameters (prevent duplicate indexing)
Disallow: /search        # Block internal search results pages

# Google's AI-search crawler — ALLOW (cites you in AI Overviews)
User-agent: Google-Extended
Allow: /

# Google's image crawler
User-agent: Googlebot-Image
Allow: /

# ============================================================
# BING BOTS (powers ChatGPT Search + Copilot)
# ============================================================
User-agent: Bingbot
Allow: /
Disallow: /admin/
Disallow: /login/
Disallow: /checkout/
Disallow: /api/
Disallow: /private/

# ============================================================
# AI SEARCH CRAWLERS — ALLOW ALL (they cite you in answers)
# ============================================================

# OpenAI — GPT-4 browsing + ChatGPT Search
User-agent: GPTBot
Allow: /

# OpenAI — real-time search component
User-agent: OAI-SearchBot
Allow: /

# Perplexity AI — full AI search engine
User-agent: PerplexityBot
Allow: /

# Anthropic — Claude web search (NOT training — this is retrieval)
User-agent: ClaudeBot
Allow: /

# Anthropic — new search crawler (June 2025+)
User-agent: Claude-SearchBot
Allow: /

# Apple — Siri + Spotlight AI answers
User-agent: Applebot
Allow: /

# Meta AI — Llama-based search
User-agent: FacebookBot
Allow: /

# Amazon — Alexa AI answers
User-agent: Amazonbot
Allow: /

# You.com AI search
User-agent: YouBot
Allow: /

# ============================================================
# AI TRAINING CRAWLERS — BLOCK ALL (scrape content, no citation benefit)
# ============================================================

# Common Crawl — used to train many LLMs
User-agent: CCBot
Disallow: /

# Old Anthropic training crawler (DIFFERENT from ClaudeBot)
# ClaudeBot = retrieval (ALLOW) | anthropic-ai = training (BLOCK)
User-agent: anthropic-ai
Disallow: /

# ByteDance / TikTok training
User-agent: Bytespider
Disallow: /

# Huawei AI training
User-agent: PetalBot
Disallow: /

# Diffbot — web scraping / AI training data
User-agent: Diffbot
Disallow: /

# Omgilibot — AI training data
User-agent: Omgilibot
Disallow: /

# DataForSEO scraper
User-agent: DataForSeoBot
Disallow: /

# ============================================================
# STANDARD SEARCH ENGINES
# ============================================================
User-agent: Slurp          # Yahoo
Allow: /

User-agent: DuckDuckBot    # DuckDuckGo (uses Bing index — Bingbot covers it)
Allow: /

User-agent: ia_archiver    # Internet Archive / Wayback Machine
Allow: /

User-agent: Yandex         # Yandex search
Allow: /

# ============================================================
# DEFAULT RULE (all other bots)
# ============================================================
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /login/
Disallow: /api/
Disallow: /private/

# ============================================================
# SITEMAP DECLARATION
# ============================================================
Sitemap: https://yourdomain.com/sitemap.xml
```

**Deploy to your website:**
```bash
# For static hosting (Nginx/Apache) — place in web root
cp robots.txt /var/www/yourdomain.com/public/robots.txt

# Verify it's live
curl https://yourdomain.com/robots.txt

# Test with Google's robots.txt tester
# → Google Search Console → Settings → robots.txt Tester
```

**Verification checklist:**
```
□ File accessible at yourdomain.com/robots.txt (HTTP 200 response)
□ GPTBot and ClaudeBot listed as ALLOW
□ anthropic-ai and CCBot listed with Disallow: /
□ /admin/ and /api/ blocked for all bots
□ Sitemap URL declared at bottom
□ Test in Google Search Console robots.txt Tester (no errors)
```

---

### STEP 2 — llms.txt

**What you're doing:** Creating the AI-equivalent of a sitemap — a curated Markdown file that tells AI systems which pages on your site matter most and what your site is about.

**File location:** `yourdomain.com/llms.txt` (must be at root)

**Template — customize with your actual content:**

```markdown
# [Your Company Name]

> [One-sentence description of what your company does and who it serves]
> Example: "AI-powered Google Ads management agency specializing in lead generation for B2B service businesses."

## Company Overview

[2-3 sentences about your company — what you do, how long you've been doing it, what makes you different]

## Core Services

- [Service 1]: [Brief description]
- [Service 2]: [Brief description]
- [Service 3]: [Brief description]

## Key Pages

- [Homepage](https://yourdomain.com/): [What it covers]
- [Services](https://yourdomain.com/services/): [What it covers]
- [About](https://yourdomain.com/about/): [What it covers]
- [Contact](https://yourdomain.com/contact/): [Lead inquiry and contact information]

## Content Resources

- [Blog](https://yourdomain.com/blog/): In-depth articles on [your topic]
- [Guide: Topic 1](https://yourdomain.com/blog/topic-1/): [Description]
- [Guide: Topic 2](https://yourdomain.com/blog/topic-2/): [Description]
- [Guide: Topic 3](https://yourdomain.com/blog/topic-3/): [Description]

## Expertise Areas

[List the main topics you have authoritative content on]
- [Topic 1]
- [Topic 2]
- [Topic 3]
- [Topic 4]

## Contact & Engagement

- Website: https://yourdomain.com
- Contact: https://yourdomain.com/contact/
- LinkedIn: https://linkedin.com/company/[your-company]

## Content Licensing

Unless otherwise noted, all content on this site is © [Year] [Company Name].
Content may be cited and quoted with attribution.
Full reproduction requires written permission.
```

**For content-heavy sites — also create `llms-full.txt`:**
```
llms-full.txt → Full text of your top 10 most important pages concatenated together
→ Separate each page with: ---\n[Page Title]\n[URL]\n---
→ Max 100,000 tokens recommended
→ Update monthly
```

**Deploy to your website:**
```bash
cp llms.txt /var/www/yourdomain.com/public/llms.txt

# Verify
curl https://yourdomain.com/llms.txt

# Register at llmstxt.cloud (optional — directory of sites with llms.txt)
# → https://llmstxt.cloud — submit your domain
```

**Update llms.txt when:**
```
□ You publish a major new piece of content
□ You add a new service
□ You change your key pages
□ Quarterly — refresh descriptions and add new guides
```

---

### STEP 3 — XML Sitemap

**What you're doing:** Generating and structuring a complete XML sitemap that declares all indexable URLs on your site to search engines.

**Sitemap architecture for a lead gen site:**

```
sitemap.xml (index file)
  ├── sitemap-pages.xml     (homepage, services, about, contact)
  ├── sitemap-blog.xml      (all blog/content posts)
  └── sitemap-images.xml    (all images)
```

**sitemap-index.xml (submit this URL to GSC and Bing WMT):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://yourdomain.com/sitemap-pages.xml</loc>
    <lastmod>2026-04-20</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://yourdomain.com/sitemap-blog.xml</loc>
    <lastmod>2026-04-20</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://yourdomain.com/sitemap-images.xml</loc>
    <lastmod>2026-04-20</lastmod>
  </sitemap>
</sitemapindex>
```

**sitemap-pages.xml:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <!-- Homepage -->
  <url>
    <loc>https://yourdomain.com/</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  <!-- Primary Service Page -->
  <url>
    <loc>https://yourdomain.com/services/</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Individual Service Pages -->
  <url>
    <loc>https://yourdomain.com/services/service-1/</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

  <!-- About Page -->
  <url>
    <loc>https://yourdomain.com/about/</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>

  <!-- Contact Page -->
  <url>
    <loc>https://yourdomain.com/contact/</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

  <!-- Author Page(s) -->
  <url>
    <loc>https://yourdomain.com/about/[author-name]/</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>

</urlset>
```

**sitemap-blog.xml (template — generate dynamically):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yourdomain.com/blog/post-slug/</loc>
    <lastmod>2026-04-20</lastmod>   <!-- CRITICAL: update when content changes -->
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>
  <!-- Add one <url> block per blog post -->
</urlset>
```

**Auto-generate sitemap on build (Node.js example):**
```javascript
// scripts/generate-sitemap.js
const fs = require('fs');

const pages = [
  { url: '/', priority: 1.0, changefreq: 'weekly' },
  { url: '/services/', priority: 0.9, changefreq: 'monthly' },
  { url: '/about/', priority: 0.7, changefreq: 'monthly' },
  { url: '/contact/', priority: 0.8, changefreq: 'monthly' },
  // Add all your static pages here
];

// Dynamically add blog posts from your CMS/filesystem
const blogPosts = getBlogPosts(); // implement based on your setup

const allUrls = [...pages, ...blogPosts];

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allUrls.map(page => `  <url>
    <loc>https://yourdomain.com${page.url}</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>${page.changefreq || 'monthly'}</changefreq>
    <priority>${page.priority || 0.6}</priority>
  </url>`).join('\n')}
</urlset>`;

fs.writeFileSync('./public/sitemap-pages.xml', xml);
console.log('Sitemap generated:', allUrls.length, 'URLs');
```

**Sitemap rules:**
```
□ Only include pages that return HTTP 200 (not 301, 404, noindex)
□ Update <lastmod> every time content changes (triggers re-crawl)
□ Do NOT include /admin/, /login/, /thank-you/, /api/ pages
□ Do NOT include pages with <meta name="robots" content="noindex">
□ Maximum 50,000 URLs per sitemap file
□ Submit URL: yourdomain.com/sitemap.xml (or sitemap-index.xml)
```

---

### STEP 4 — Canonical Tags

**What you're doing:** Adding a `<link rel="canonical">` tag to the `<head>` of every single page on your site, declaring the preferred URL for that page.

**Implementation in your HTML template:**
```html
<!-- Add to <head> of your global HTML template -->
<!-- Replace dynamically with each page's actual URL -->

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- CANONICAL TAG — add to EVERY page, including the homepage itself -->
  <link rel="canonical" href="https://yourdomain.com/current-page-url/" />
  
  <!-- All other head tags... -->
</head>
```

**Dynamic canonical generation (JavaScript/Node.js):**
```javascript
// In your page renderer/template system
function generateCanonical(path) {
  // Normalize: always HTTPS, always trailing slash (pick your convention)
  const baseUrl = 'https://yourdomain.com';
  const normalized = path.endsWith('/') ? path : path + '/';
  return `<link rel="canonical" href="${baseUrl}${normalized}" />`;
}

// Usage in template:
// ${generateCanonical(currentPage.slug)}
```

**URL standardization — decide once, never change:**
```
□ Pick: www.yourdomain.com OR yourdomain.com (never both)
□ Pick: trailing slash OR no trailing slash (never both)
□ ALWAYS: HTTPS (never HTTP)
□ Set 301 redirects from non-canonical form to canonical form
   e.g., http://www.yourdomain.com → https://yourdomain.com

Nginx redirect example:
  server {
    listen 80;
    server_name www.yourdomain.com yourdomain.com;
    return 301 https://yourdomain.com$request_uri;
  }
```

**Special cases:**
```
Thank-you pages / confirmation pages:
  → Use <meta name="robots" content="noindex, nofollow"> instead of canonical
  → These should NOT be indexed

Paginated content (/blog/page/2/):
  → Each page self-canonical: <link rel="canonical" href="/blog/page/2/" />
  → DO NOT canonical all pagination to page 1 (that's wrong)

URL parameters (UTM, ref, etc.):
  → Canonical should point to the clean URL (without parameters)
  → /page/?utm_source=email → canonical href="/page/"
```

**Verification:**
```bash
# Check canonical tag on your homepage
curl -s https://yourdomain.com/ | grep -i canonical

# Should return:
# <link rel="canonical" href="https://yourdomain.com/" />

# Check in Google Search Console:
# URL Inspection → enter any URL → "Page indexing" → Canonical URL
```

---

### STEP 5 — JSON-LD Schema Markup

**What you're doing:** Adding structured data to every page that tells search engines and AI systems exactly what your content is.

**Where to add:** Inside `<script type="application/ld+json">` tags in the `<head>` of each page.

---

#### Schema 1: Organization (add to EVERY page — global template)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Your Company Name",
  "url": "https://yourdomain.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://yourdomain.com/images/logo.png",
    "width": 300,
    "height": 60
  },
  "description": "Your company description — what you do and who you serve.",
  "foundingDate": "2023",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "CA"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "hello@yourdomain.com",
    "availableLanguage": ["English", "French"]
  },
  "sameAs": [
    "https://linkedin.com/company/your-company",
    "https://twitter.com/yourcompany",
    "https://www.crunchbase.com/organization/your-company",
    "https://www.wikidata.org/wiki/Q[your-Q-number]"
  ]
}
</script>
```

---

#### Schema 2: WebSite (homepage only)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Your Company Name",
  "url": "https://yourdomain.com",
  "description": "Your company description",
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

---

#### Schema 3: Service (every service page)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Google Ads Management",
  "description": "End-to-end Google Ads campaign management for B2B lead generation, including keyword strategy, ad copywriting, conversion tracking, and monthly optimization.",
  "provider": {
    "@type": "Organization",
    "name": "Your Company Name",
    "url": "https://yourdomain.com"
  },
  "areaServed": {
    "@type": "Country",
    "name": "Canada"
  },
  "serviceType": "Digital Marketing",
  "url": "https://yourdomain.com/services/google-ads-management/"
}
</script>
```

---

#### Schema 4: FAQPage (every service page + blog post)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does Google Ads management cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Google Ads management typically costs between $500-2,000/month for small businesses, depending on ad spend and scope of work. Most agencies charge either a flat monthly fee or a percentage of ad spend (10-20%). At [Company], our management fee starts at $[price]/month for campaigns with up to $[budget] in monthly ad spend."
      }
    },
    {
      "@type": "Question",
      "name": "How long before Google Ads generates leads?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most campaigns begin generating leads within the first 2-4 weeks of launch. The first 30 days are a learning phase where Google's algorithm calibrates to your conversion targets. Optimal performance typically occurs at the 60-90 day mark when Smart Bidding has accumulated sufficient conversion data."
      }
    },
    {
      "@type": "Question",
      "name": "What is a good cost per lead for Google Ads?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A good cost per lead depends on your industry and client lifetime value (LTV). As a benchmark: professional services $50-150/lead, B2B SaaS $75-300/lead, legal services $100-500/lead. The right target is: CPL < LTV × target CAC ratio. If your average client is worth $10,000 over their lifetime, a CPL of $200 with a 10% close rate yields a $2,000 CAC — sustainable if LTV supports it."
      }
    }
  ]
}
</script>
```

---

#### Schema 5: BreadcrumbList (every interior page)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://yourdomain.com/"
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
      "item": "https://yourdomain.com/services/google-ads-management/"
    }
  ]
}
</script>
```

---

#### Schema 6: Article (every blog post)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your Blog Post Title Here",
  "description": "The meta description of this blog post — 155 characters max.",
  "image": {
    "@type": "ImageObject",
    "url": "https://yourdomain.com/images/blog/post-image.webp",
    "width": 1200,
    "height": 630
  },
  "datePublished": "2026-04-20T09:00:00+00:00",
  "dateModified": "2026-04-20T09:00:00+00:00",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://yourdomain.com/about/author-name/",
    "sameAs": "https://linkedin.com/in/author-profile"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Your Company Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://yourdomain.com/images/logo.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://yourdomain.com/blog/post-slug/"
  }
}
</script>
```

---

#### Schema 7: AggregateRating (pages with client testimonials/reviews)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Google Ads Management",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "23",
    "bestRating": "5",
    "worstRating": "1"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5"
      },
      "author": {
        "@type": "Person",
        "name": "Client First Name"
      },
      "reviewBody": "Exact quote from client testimonial here. Keep it real."
    }
  ]
}
</script>
```

---

#### Schema 8: Person (author pages)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Your Full Name",
  "url": "https://yourdomain.com/about/your-name/",
  "image": "https://yourdomain.com/images/team/your-name.webp",
  "jobTitle": "Google Ads Strategist",
  "worksFor": {
    "@type": "Organization",
    "name": "Your Company Name"
  },
  "description": "2-3 sentence bio with specific credentials and expertise.",
  "sameAs": [
    "https://linkedin.com/in/your-profile",
    "https://twitter.com/yourhandle"
  ],
  "knowsAbout": [
    "Google Ads",
    "Lead Generation",
    "PPC Advertising",
    "Marketing Strategy"
  ]
}
</script>
```

**Schema validation — run after every addition:**
```
1. Google Rich Results Test: search.google.com/test/rich-results
   → Enter page URL → Check for errors → Fix any warnings/errors

2. Schema.org Validator: validator.schema.org
   → Paste your JSON-LD code directly

3. Bing Markup Validator: bing.com/toolbox/markup-validator
   → Validates for Bing's understanding too
```

---

### STEP 6 — Core Web Vitals Code Optimization

**What you're doing:** Implementing code-level fixes to achieve Google's performance thresholds: LCP < 2.5s, INP < 200ms, CLS < 0.1

**Run this first — measure before you fix:**
```
1. Go to: pagespeed.web.dev
2. Test your homepage URL on MOBILE (mobile is what Google measures)
3. Screenshot your current scores
4. Note all "Opportunities" and "Diagnostics" listed
5. Then apply fixes below based on your specific issues
```

---

#### Fix 1: LCP — Preload Hero Image

```html
<!-- Add to <head>, BEFORE any other resource loads -->
<!-- Replace hero.webp with your actual above-fold hero image -->
<link rel="preload" as="image" href="/images/hero.webp" fetchpriority="high">

<!-- If your hero is a background-image in CSS, use this instead: -->
<link rel="preload" as="image" href="/images/hero-bg.webp" 
      fetchpriority="high" type="image/webp">
```

#### Fix 2: LCP — Convert Images to WebP

```bash
# Install cwebp (one-time)
sudo apt install webp   # Ubuntu/Debian
brew install webp        # macOS

# Convert a single image
cwebp -q 85 input.jpg -o output.webp

# Convert all JPGs in a directory
for f in images/*.jpg; do cwebp -q 85 "$f" -o "${f%.jpg}.webp"; done
for f in images/*.png; do cwebp -q 85 "$f" -o "${f%.png}.webp"; done

# Average size reduction: 30-35% vs JPEG, 60-70% vs PNG
```

#### Fix 3: LCP — Set Explicit Image Dimensions

```html
<!-- WRONG — browser doesn't know the size until image loads -->
<img src="hero.webp" alt="Hero image">

<!-- CORRECT — browser reserves space, prevents layout shift AND helps LCP -->
<img src="hero.webp" 
     width="1200" 
     height="630" 
     alt="Descriptive alt text for hero image"
     loading="eager"
     fetchpriority="high">

<!-- For below-fold images — use lazy loading -->
<img src="feature.webp" 
     width="600" 
     height="400" 
     alt="Feature description"
     loading="lazy">
```

#### Fix 4: LCP — Defer Non-Critical JavaScript

```html
<!-- In <head> — load critical CSS inline, defer everything else -->

<!-- WRONG — blocks rendering -->
<link rel="stylesheet" href="styles.css">
<script src="app.js"></script>

<!-- CORRECT — only critical CSS blocks, everything else defers -->
<style>
  /* Inline only the CSS needed for above-fold rendering */
  /* Usually: header, hero section, primary nav */
  /* Everything else loads asynchronously */
  body { margin: 0; font-family: sans-serif; }
  header { ... }
  .hero { ... }
</style>
<link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'">
<script src="app.js" defer></script>
<script src="analytics.js" defer></script>
<script src="chat-widget.js" defer></script>
```

#### Fix 5: INP — Break Up Long Tasks

```javascript
// PROBLEM: Long synchronous task blocks user interaction
function processFormData(data) {
  // This might take 200ms — user clicks feel frozen
  validateAllFields(data);
  formatAllData(data);
  buildPayload(data);
  sendToServer(data);
}

// SOLUTION: Use scheduler.yield() to yield between heavy operations
async function processFormData(data) {
  validateAllFields(data);
  await scheduler.yield(); // Yield to browser — handle any pending user events
  
  formatAllData(data);
  await scheduler.yield();
  
  buildPayload(data);
  await scheduler.yield();
  
  await sendToServer(data);
}

// FALLBACK for browsers without scheduler.yield():
function yieldToMain() {
  return new Promise(resolve => setTimeout(resolve, 0));
}
```

#### Fix 6: INP — Defer Event Handler Heavy Operations

```javascript
// WRONG — runs synchronously in click handler, blocks INP
button.addEventListener('click', () => {
  const result = heavyComputation(); // Blocks for 150ms
  updateUI(result);
});

// CORRECT — immediate visual feedback, defer heavy work
button.addEventListener('click', () => {
  button.textContent = 'Processing...'; // Immediate feedback
  button.disabled = true;
  
  // Defer the heavy computation
  requestAnimationFrame(() => {
    const result = heavyComputation();
    updateUI(result);
    button.disabled = false;
  });
});
```

#### Fix 7: CLS — Reserve Space for Images and Embeds

```css
/* Every image must have explicit width/height OR use aspect-ratio */

/* Option A: Set in HTML (preferred — add width/height attributes to <img>) */
/* <img src="photo.jpg" width="800" height="450" alt="..."> */

/* Option B: CSS aspect-ratio (for responsive images) */
.blog-thumbnail {
  aspect-ratio: 16 / 9;
  width: 100%;
  object-fit: cover;
}

/* Video/iframe embeds */
.video-container {
  position: relative;
  aspect-ratio: 16 / 9;
  width: 100%;
}
.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Cookie banners, notification bars — prevent layout shift */
.cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  /* Never inject ABOVE existing content — always fixed/sticky at bottom */
}
```

#### Fix 8: CLS — Font Loading

```html
<!-- In <head> — preload custom fonts -->
<link rel="preload" 
      href="/fonts/your-font.woff2" 
      as="font" 
      type="font/woff2" 
      crossorigin>
```

```css
/* In CSS — font-display: swap prevents FOIT (flash of invisible text) */
@font-face {
  font-family: 'YourFont';
  src: url('/fonts/your-font.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap; /* Critical: prevents CLS from font loading */
}
```

**After applying all fixes:**
```
□ Run PageSpeed Insights again on mobile
□ Target: Performance 90+
□ If still failing: check "Opportunities" section for remaining issues
□ Run on 3 pages: Homepage, primary service page, contact page
□ Document scores in: 01-intelligence/SS2-performance/cwv-baseline-[date].md
```

---

## PHASE 2 — SEARCH ENGINE PRESENCE (LAYER 2)
> Register your website with every major search engine and AI platform.

---

### STEP 7 — Google Search Console

**What you're doing:** Verifying your website with Google and submitting your sitemap.

**Setup steps:**

```
1. Go to: search.google.com/search-console
2. Click "Add property"
3. Choose "Domain" (not URL prefix — Domain covers all subdomains and protocols)
4. Enter: yourdomain.com (without https://)

DOMAIN VERIFICATION (via DNS):
5. Copy the TXT record provided (e.g., google-site-verification=abc123...)
6. Go to your DNS provider (Cloudflare, NameCheap, etc.)
7. Add a TXT record:
   Name: @ (or blank)
   Type: TXT
   Value: google-site-verification=abc123...
   TTL: 3600
8. Click "Verify" in GSC (can take 5-30 minutes for DNS to propagate)
```

**Submit sitemap:**
```
After verification:
1. Left sidebar → Sitemaps
2. Enter: sitemap.xml (or sitemap-index.xml if using index file)
3. Click Submit
4. Status should change from "Pending" to "Success" within 24 hours
5. Note the number of "Discovered URLs" — verify it matches your page count
```

**Link GSC to GA4 (if not done already in Google Ads install guide):**
```
GSC → Settings → Associations → Google Analytics
→ Select your GA4 property
→ Click "Associate"
→ This unlocks Search Console data inside GA4 reports
```

**Critical initial checks:**
```
□ Coverage report → check "Error" count (should be 0 or investigate each)
□ Core Web Vitals → check "Poor URLs" list
□ Enhancements → check if any rich result types detected
□ Performance → check if any queries/clicks appearing (may take 2-4 weeks)
```

**Weekly GSC workflow (set a calendar reminder):**
```
Every Monday:
□ Performance → last 7 days vs previous 7 days
  → Any clicks/impressions drop? Investigate pages
□ Coverage → any new Errors? Fix immediately
□ Core Web Vitals → any new "Poor" pages? Prioritize for fix
□ URL Inspection → paste any newly published URL → "Request indexing"
```

---

### STEP 8 — Bing Webmaster Tools

**What you're doing:** Registering your site with Bing (which powers Bing, Yahoo, DuckDuckGo, Ecosia, ChatGPT Search, and Microsoft Copilot).

**Setup steps:**

```
1. Go to: bing.com/webmasters
2. Sign in with Microsoft account (create one if needed)
3. Click "Add your site"
4. Enter: https://yourdomain.com

VERIFICATION — choose one method:

Method A: Import from Google Search Console (fastest)
→ "Import from GSC" → Sign in with Google → select GSC property → Done
→ This imports your sitemap too

Method B: XML file
→ Download the verification XML file provided
→ Upload to: yourdomain.com/BingSiteAuth.xml
→ File must be publicly accessible
→ Click Verify

Method C: Meta tag
→ Add to <head> of homepage: <meta name="msvalidate.01" content="[code]">
→ Click Verify
```

**Submit sitemap to Bing:**
```
Left sidebar → Sitemaps → Submit sitemap
Enter: https://yourdomain.com/sitemap.xml
Click Submit
→ Bing will begin crawling your site within 24-48 hours
```

**IndexNow setup in Bing WMT:**
```
Left sidebar → IndexNow
→ This is where you'll monitor IndexNow submissions from your site
→ Also allows manual URL submission
→ Keep this tab open — you'll return after Step 9
```

**Check AI Performance Dashboard (new Feb 2026):**
```
Left sidebar → AI Performance
→ If you just registered, data will populate over the first 2-4 weeks
→ Bookmark this — check every Monday
```

---

### STEP 9 — IndexNow Protocol

**What you're doing:** Implementing automatic real-time notifications to search engines (Bing, Yandex, Seznam) whenever you publish or update content. This accelerates indexing from weeks to hours.

**Step 9.1 — Generate your API key:**
```bash
# Your IndexNow API key must be a random alphanumeric string (min 8 chars)
# Generate one:
openssl rand -hex 32

# Example output: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6

# Save this key — you'll use it in multiple places
YOUR_INDEXNOW_KEY="a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
```

**Step 9.2 — Create verification file:**
```bash
# Create a text file with ONLY your API key as the content (nothing else)
# File must be at: yourdomain.com/[your-key].txt

echo "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6" > public/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6.txt

# Verify it's accessible:
curl https://yourdomain.com/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6.txt
# Should return ONLY: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

**Step 9.3 — Implement the IndexNow notification function:**

```javascript
// lib/indexnow.js
// Call this function every time you publish or update a page

const INDEXNOW_KEY = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6';
const SITE_HOST = 'yourdomain.com';

/**
 * Notify search engines of new/updated URLs via IndexNow
 * @param {string|string[]} urls - Single URL or array of URLs to submit
 */
async function notifyIndexNow(urls) {
  // Normalize to array
  const urlList = Array.isArray(urls) ? urls : [urls];
  
  // IndexNow accepts up to 10,000 URLs per batch
  const payload = {
    host: SITE_HOST,
    key: INDEXNOW_KEY,
    keyLocation: `https://${SITE_HOST}/${INDEXNOW_KEY}.txt`,
    urlList: urlList
  };
  
  try {
    // Submit to Bing (which relays to all IndexNow partners)
    const response = await fetch('https://api.indexnow.org/indexnow', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(payload)
    });
    
    if (response.status === 200) {
      console.log(`✅ IndexNow: Submitted ${urlList.length} URL(s)`);
    } else if (response.status === 202) {
      console.log(`✅ IndexNow: Accepted (queued for processing)`);
    } else {
      console.error(`❌ IndexNow Error: ${response.status}`, await response.text());
    }
    
    return response.status;
  } catch (error) {
    console.error('IndexNow submission failed:', error);
  }
}

// USAGE EXAMPLES:

// Single URL (after publishing a blog post):
// notifyIndexNow('https://yourdomain.com/blog/new-post-slug/');

// Multiple URLs (after a site-wide update):
// notifyIndexNow([
//   'https://yourdomain.com/',
//   'https://yourdomain.com/services/',
//   'https://yourdomain.com/blog/updated-post/'
// ]);

module.exports = { notifyIndexNow };
```

**Step 9.4 — Integrate into your publish workflow:**

```javascript
// In your content publish script / deployment pipeline:
const { notifyIndexNow } = require('./lib/indexnow');

// After publishing a new blog post:
async function publishBlogPost(post) {
  // ... your existing publish logic ...
  
  // After successful publish:
  const postUrl = `https://yourdomain.com/blog/${post.slug}/`;
  
  // Notify IndexNow (automatically notifies Bing, Yandex, Seznam, Naver)
  await notifyIndexNow([
    postUrl,
    'https://yourdomain.com/blog/', // Blog index page updated too
    'https://yourdomain.com/sitemap.xml' // Sitemap updated
  ]);
  
  console.log(`Published and IndexNow submitted: ${postUrl}`);
}
```

**Step 9.5 — Manual bulk submission (first-time, for existing pages):**
```bash
# Submit all existing pages at once (first-time setup)
curl -X POST https://api.indexnow.org/indexnow \
  -H "Content-Type: application/json" \
  -d '{
    "host": "yourdomain.com",
    "key": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    "keyLocation": "https://yourdomain.com/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6.txt",
    "urlList": [
      "https://yourdomain.com/",
      "https://yourdomain.com/services/",
      "https://yourdomain.com/about/",
      "https://yourdomain.com/contact/"
    ]
  }'

# Expected response: HTTP 200 (OK) or 202 (Accepted)
```

**Save to RA-Project:**
```bash
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/03-automation/v1-deployment/
# Save indexnow.js to this directory
```

---

### STEP 10 — Yandex Webmaster (Optional)

```
Skip unless targeting Russian-speaking market.

If needed:
1. Go to: webmaster.yandex.com
2. Add site → enter yourdomain.com
3. Choose verification method: meta tag or TXT record
4. Submit sitemap

Note: IndexNow (Step 9) automatically notifies Yandex on each publish.
Yandex Webmaster is just for monitoring — not required for IndexNow to work.
```

---

### STEP 11 — Google Business Profile

**What you're doing:** Creating your Google Business Profile to establish your business as a verified entity in Google's Knowledge Graph.

**Setup:**
```
1. Go to: business.google.com
2. Click "Manage now" or "Add your business"
3. Enter your business name exactly as it appears on your website
4. Select your business category:
   → Primary: "Marketing Agency" or your relevant category
   → Add secondary categories where applicable
5. Choose: "No — I don't have a physical location customers visit"
   → Enter your service area (city/region/country you serve)
6. Add contact info:
   → Phone number (must be real and active)
   → Website: https://yourdomain.com
7. Finish and claim

VERIFICATION:
→ Google will mail a postcard to your address (5-14 days)
   OR
→ Video verification (available for some accounts — faster)
→ Phone verification (available if you have a Google Ads account linked)
```

**After verification — complete your profile (critical for entity signals):**
```
□ Business description: 750-character description (use keywords naturally)
□ Hours: Add business hours (even "by appointment" works)
□ Photos: Upload minimum 5 photos (logo, team, office, work samples)
□ Services: Add all your service offerings with descriptions and prices (optional)
□ Products: Add if applicable
□ Posts: Publish 1 post per week (updates, offers, blog highlights)
□ Get first reviews: Ask 5 past clients to leave a Google review
□ Q&A: Add common questions + answers yourself proactively
```

**Link website to GBP:**
```
Add this to your website's About or Footer:
<a href="https://g.page/your-business-profile" rel="noopener">
  Google Business Profile
</a>

Also add your GBP URL to the Organization schema sameAs array (Step 5)
```

---

### STEP 12 — Brave Search Webmaster

```
10-minute setup. One-time task.

1. Go to: search.brave.com/webmaster
2. Sign in with email
3. Add your website
4. Verify via meta tag or DNS TXT record
5. Submit sitemap URL

That's it. Brave Search has its own independent index.
Monitor quarterly — no regular action needed.
```

---

## PHASE 3 — INTELLIGENCE & RESEARCH (LAYER 3)

---

### STEP 13 — Ahrefs Setup

**What you're doing:** Setting up your primary SEO intelligence platform and running first critical research workflows.

**Account setup:**
```
1. Go to: ahrefs.com
2. Sign up for Lite plan ($129/mo) — sufficient for one website
3. Add your project:
   → Workspace → Add project → yourdomain.com
   → Connect to GSC property (grants Ahrefs access to your GSC data)
```

**Free alternative — Ahrefs Webmaster Tools:**
```
If not ready to pay, start with Ahrefs Webmaster Tools (free):
1. Go to: ahrefs.com/webmaster-tools
2. Verify your site via GSC or DNS
3. Gets you:
   → Full backlink report for YOUR site
   → Site Audit for YOUR site
   → Organic keyword data for YOUR site
4. Limitation: Cannot analyze competitor sites
5. Upgrade to paid when ready for competitor analysis
```

**First run — Site Audit:**
```
Ahrefs → Site Audit → New project → Enter yourdomain.com
→ Run audit
→ Fix all "Errors" (red) before anything else
→ Review "Warnings" (orange)
→ Save crawl report to: 01-intelligence/SS2-performance/ahrefs-audit-[date].csv
```

**First run — Keyword Research:**
```
WORKFLOW:
1. Ahrefs → Keywords Explorer
2. Enter your primary service keyword (e.g., "google ads management")
3. Apply filters:
   → Keyword Difficulty: Max 30 (easier to rank for)
   → Volume: Min 100/month
4. Review tabs:
   → "Questions" tab → long-tail FAQ and blog opportunities
   → "Also rank for" tab → related terms your pillar should cover
   → "Having same terms" → variations to target in content
5. Export all results → save to 01-intelligence/SS1-market/keyword-research/

BUILD YOUR KEYWORD MAP:
→ Pillar keyword: high volume head term (e.g., "google ads management")
→ Cluster keywords: everything else (lower volume, more specific)
→ Map clusters to specific blog posts in your content calendar
```

**First run — Competitor Analysis:**
```
1. Ahrefs → Site Explorer → Enter top competitor's domain
2. "Organic Keywords" tab → keywords they rank for
3. "Top Pages" tab → their highest-traffic pages
4. "Backlinks" tab → who links to them
5. Site Explorer → your domain → "Content Gap":
   → Enter 3 competitor domains
   → See all keywords they rank for that you don't
   → Priority: highest volume gaps = first content to create
```

---

### STEP 14 — Screaming Frog Setup

**What you're doing:** Installing the desktop crawler and running your first technical audit.

**Install:**
```bash
# Linux
wget https://www.screamingfrog.co.uk/screamingfrogseospider/ScreamingFrogSEOSpider.deb
sudo dpkg -i ScreamingFrogSEOSpider.deb

# macOS
# Download .dmg from screamingfrog.co.uk/seo-spider

# Windows
# Download .exe from screamingfrog.co.uk/seo-spider

# License key: Enter in app → Help → Enter License
# Free version: crawls up to 500 URLs (sufficient for early-stage site)
```

**First crawl:**
```
1. Open Screaming Frog
2. Enter: https://yourdomain.com
3. Click Start
4. Wait for crawl to complete

CRITICAL REPORTS TO CHECK:
Response Codes tab:
□ Filter: 4XX → fix all broken links (redirect or remove)
□ Filter: 3XX → check for redirect chains (A→B→C = bad; flatten to A→C)

Page Titles tab:
□ Filter: Missing → add title to every page
□ Filter: Duplicate → make unique (every page needs unique title)
□ Filter: Over 60 chars → shorten

Meta Description tab:
□ Filter: Missing → add meta description to every page
□ Filter: Duplicate → make unique
□ Filter: Over 160 chars → shorten

H1 tab:
□ Filter: Missing → add H1 to every page
□ Filter: Multiple → fix to exactly one H1 per page

Images tab:
□ Filter: Missing Alt Text → add alt text
□ Filter: Over 100KB → compress to WebP

Canonical tab:
□ Filter: Missing → add canonical to every page (you did this in Step 4)

Schema tab (requires configuration):
□ Configuration → Spider → Extraction → Add custom extraction for schema

EXPORT ALL REPORTS:
File → Export → Save to: 01-intelligence/SS2-performance/screaming-frog-[date]/
```

**Set monthly reminder:**
```
Run Screaming Frog the first Monday of every month
Compare to previous month's crawl
Track: Did error count decrease? Did page count grow correctly?
```

---

### STEP 15 — Google PageSpeed Insights

**What you're doing:** Establishing Core Web Vitals baseline scores and identifying specific fixes needed.

```
URL: pagespeed.web.dev

Test these 4 pages on MOBILE first, then desktop:
□ Homepage: https://yourdomain.com/
□ Primary service page: https://yourdomain.com/services/
□ Contact/lead form page: https://yourdomain.com/contact/
□ Best blog post (if any): https://yourdomain.com/blog/[post]

For each page, record in a document:
→ Performance score (target: 90+)
→ LCP value (target: < 2.5s)
→ INP value (target: < 200ms)
→ CLS value (target: < 0.1)
→ Top 3 "Opportunities" listed

Save baseline document:
01-intelligence/SS2-performance/cwv-baseline-[date].md

After applying Step 6 fixes, re-run and compare scores.
```

---

### STEP 16 — Answer The Public + AlsoAsked

**What you're doing:** Building your complete FAQ question library that will fuel all content in Layer 4.

**Answer The Public:**
```
1. Go to: answerthepublic.com
2. Enter your primary keyword (e.g., "google ads")
3. Select language/country
4. Download the question map
5. Open CSV export → filter for:
   → Questions starting with: "what", "how", "why", "which", "can", "when", "where"
6. Repeat for each major service/topic you want to write about

Save to: 01-intelligence/SS1-market/question-maps/[keyword]-questions.csv
```

**AlsoAsked:**
```
1. Go to: alsoasked.com
2. Enter your primary keyword
3. Click "Search"
4. Explore the question tree (these are EXACTLY what Google's PAA shows)
5. Download CSV
6. These questions = your FAQ section questions AND individual blog post topics

For each question ask:
→ Is this a standalone blog post? (1,000-2,500 words)
→ Is this a FAQ entry on a service page? (40-80 word answer)
→ Does this become a section header in the pillar page?
```

**Build the master question library:**
```
Create: 01-intelligence/SS1-market/faq-master-library.md

Format:
## Topic: Google Ads

### Blog Post Topics (1,000-2,500 words each)
- How to set up Google Ads conversion tracking
- Google Ads quality score: what it is and how to improve it
- [etc.]

### FAQ Questions (40-80 word answers)
- What is a good Google Ads quality score?
- How long does it take for Google Ads to work?
- [etc.]

### Quick Answer Block Topics (134-167 word featured snippet answers)
- What is Google Ads?
- How does Google Ads bidding work?
- [etc.]
```

---

## PHASE 4 — CONTENT & ON-PAGE SEO (LAYER 4)

---

### STEP 17 — Content Cluster Architecture

**What you're doing:** Planning your entire topical authority content system before writing a single word.

**Create your content cluster map:**
```
Document: 02-slm-machine/content/content-cluster-map.md

STRUCTURE:
For each major topic/service:

## CLUSTER 1: [Primary Topic] — e.g., "Google Ads Management"

Pillar Page:
- Title: "Google Ads Management: The Complete 2026 Guide"
- Target keyword: "google ads management"
- URL: /blog/google-ads-management-guide/
- Length: 4,000-5,000 words
- Status: [ ] Planning | [ ] Written | [ ] Published

Cluster Pages (1,000-2,500 words each):
1. "Google Ads Keyword Research: How to Find Winning Keywords"
   - Target keyword: "google ads keyword research"
   - URL: /blog/google-ads-keyword-research/
   - Status: [ ]

2. "Google Ads Quality Score: What It Is and How to Improve It"
   - Target keyword: "google ads quality score"
   - URL: /blog/google-ads-quality-score/
   - Status: [ ]

[Continue for 7-12 cluster pages per pillar]
```

**Content brief template (use for every piece):**
```
## Content Brief: [Page Title]

TARGET KEYWORD: 
SECONDARY KEYWORDS: 
URL SLUG: 
CONTENT TYPE: [Pillar | Cluster | Service Page | FAQ]
TARGET WORD COUNT: 

SEARCH INTENT: [Informational | Commercial | Transactional]
FUNNEL STAGE: [Awareness | Consideration | Decision]

QUICK ANSWER BLOCK TOPIC: 
(The single most important question this page answers in 134-167 words)

OUTLINE:
H1: 
H2: (Quick Answer Block section)
H2: 
  H3: 
  H3: 
H2: 
H2: FAQ Section
  Q: 
  Q: 
  Q: 
  Q: 
  Q: 

SCHEMA TO ADD: [Organization | FAQPage | Article | BreadcrumbList | Service]
INTERNAL LINKS FROM THIS PAGE: 
INTERNAL LINKS TO THIS PAGE FROM:
```

**Publication cadence:**
```
Week 1: Publish Pillar Page
Week 2: Publish 2 cluster pages
Week 3: Publish 2 cluster pages
Week 4: Publish 2 cluster pages + update pillar with links
Week 5: Publish 2 cluster pages
[Repeat until all clusters published]

After full cluster published:
→ Set quarterly reminder to refresh and expand each page
→ Add new data, statistics, update dates
→ Submit updated URLs via IndexNow
```

---

### STEP 18 — Quick Answer Blocks + FAQ Setup

**Template: Quick Answer Block (place at TOP of every page, above all other content):**

```html
<!-- Place this IMMEDIATELY after the H1 heading, before any other content -->
<div class="quick-answer" itemscope itemtype="https://schema.org/Answer">
  <div class="quick-answer-label">Quick Answer</div>
  <div itemprop="text">
    <p>
      [134-167 word self-contained answer to the primary question of this page.
      Write this to be 100% standalone — the reader should not need to scroll
      further to understand the answer.
      
      Include: Definition → Core mechanism → Key numbers/data → Practical implication.
      
      Example for "What is Google Ads Quality Score?":
      
      "Google Ads Quality Score is a 1–10 rating assigned by Google to each 
      keyword in your account, measuring how relevant your keyword, ad, and 
      landing page are to the user's search intent. A score of 7–10 indicates 
      strong relevance and earns lower CPCs and better ad positions. A score 
      of 1–4 signals misalignment between what users search, what your ad 
      promises, and what your landing page delivers. Quality Score is 
      calculated from three components: Expected CTR (40% weight), Ad 
      Relevance (40%), and Landing Page Experience (20%). Improving Quality 
      Score reduces what you pay per click — a score of 10 vs 4 on the same 
      keyword can reduce CPC by 30-50%, directly lowering your cost per lead."]
    </p>
  </div>
</div>
```

```css
/* Style the Quick Answer Block to be visually distinct */
.quick-answer {
  background: #f8f9fa;
  border-left: 4px solid #0066cc;
  padding: 20px 24px;
  margin: 24px 0 32px 0;
  border-radius: 0 4px 4px 0;
}

.quick-answer-label {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #0066cc;
  margin-bottom: 8px;
}

.quick-answer p {
  font-size: 16px;
  line-height: 1.65;
  color: #333;
  margin: 0;
}
```

**FAQ Section (place at BOTTOM of every page):**
```html
<!-- Before closing </article> or </main> -->
<section class="faq-section" itemscope itemtype="https://schema.org/FAQPage">
  <h2>Frequently Asked Questions</h2>
  
  <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">Your question here?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">
        40-80 word answer. Complete, standalone. Must answer the question
        without requiring the reader to read anything else on the page.
        Include a specific number, percentage, or timeframe where possible.
        End with what the reader should do or expect next.
      </p>
    </div>
  </div>
  
  <!-- Repeat .faq-item for 5-10 questions per page -->
  
</section>
```

**Also add the FAQPage JSON-LD schema (from Step 5, Schema 4) matching the same questions.**

---

### STEP 19 — Author Pages Setup

**What you're doing:** Creating author page(s) with verified credentials to establish E-E-A-T signals.

**Create the author page:**
```
URL: yourdomain.com/about/[your-name]/

Content requirements:
□ Full legal name
□ Professional headshot (400x400px minimum, WebP format)
□ Professional title ("Google Ads Strategist", "Founder & Lead Consultant")
□ 3-5 sentence bio with SPECIFIC credentials:
   → Years of experience (specific number)
   → Industries worked in
   → Specific results achieved ("managed $2M+ in Google Ads spend")
   → Certifications (Google Ads Certified, Meta Blueprint, etc.)
□ LinkedIn profile link (must be active, complete profile)
□ Published work / portfolio samples with links
□ "Expert in:" list (your core topic areas)
□ Person schema markup (Schema 8 from Step 5)
```

**Add byline to every content page:**
```html
<!-- Below H1 or below the article header -->
<div class="article-meta">
  <a href="https://yourdomain.com/about/your-name/" class="author-byline">
    <img src="/images/team/your-name.webp" 
         width="40" 
         height="40" 
         alt="Your Name"
         loading="lazy">
    <span>By <strong>Your Name</strong></span>
  </a>
  <span class="article-dates">
    <time datetime="2026-04-20">Published April 20, 2026</time>
    <time datetime="2026-04-20">· Updated April 20, 2026</time>
  </span>
</div>
```

---

### STEP 20 — Internal Linking Architecture

**What you're doing:** Creating a deliberate map of how pages link to each other to distribute authority across your site.

**Build the internal linking map:**
```
Document: 02-slm-machine/content/internal-linking-map.md

FORMAT:

Page: /services/google-ads-management/
→ Links TO: 
  - /blog/google-ads-keyword-research/ ("keyword research strategy")
  - /blog/google-ads-quality-score/ ("quality score optimization")
  - /blog/google-ads-conversion-tracking/ ("conversion tracking setup")
  - /contact/ ("get a free audit")
→ Linked FROM:
  - Homepage: nav and featured services section
  - /blog/google-ads-management-guide/ (pillar → service page)
  - /about/ (mention of expertise)
```

**Implementation rules:**
```
When publishing any new page:
□ Add minimum 3 outbound links to related pages
   → Use descriptive anchor text (not "click here")
   → Example: "complete keyword research strategy" → link to keyword guide
□ Update at least 2 existing pages to link TO the new page
   → Choose pages most topically related
   → Find natural places to mention the new page's topic
□ Always link cluster pages → their pillar page
□ Pillar pages → all cluster pages in their cluster
□ All important pages → homepage (usually via navigation — no extra work needed)
```

**Orphan page check:**
```
Monthly: Run Screaming Frog → Inlinks report
→ Filter: Pages with 0 inlinks = orphan pages
→ Every orphan page needs at least 1 link from a related page
→ No page should require a sitemap to discover
```

---

## PHASE 5 — AUTHORITY & ENTITY BUILDING (LAYER 5)

---

### STEP 21 — Wikidata Entity Entry

**What you're doing:** Adding your company to Wikidata — the structured knowledge base that powers Google's Knowledge Graph.

**Prerequisites before applying:**
```
□ Your company has been mentioned in at least 1 independent, reliable source
  (news article, industry publication, directory — anything external)
□ If not yet: complete a digital PR placement first (Step 25 below)
   then return here

Notable = external coverage exists about your company
Not just your own website, social media, or paid listings
```

**Create Wikidata entry:**
```
1. Go to: wikidata.org
2. Create an account (use a professional email)
3. Click "Create a new item"
4. Label: Your company's full legal name
5. Description: Short description (e.g., "Canadian digital marketing agency")
6. Add statements (the most important ones):

Property P31 (instance of): Q4830453 (business)
Property P856 (official website): https://yourdomain.com
Property P571 (inception): [founding year]
Property P17 (country): Q16 (Canada) or your country
Property P452 (industry): Q11020 (advertising) or your relevant industry
Property P159 (headquarters): your city
Property P1813 (short name): abbreviated name if any
Property P18 (image): your logo (upload to Wikimedia Commons first)
Property P856 (official website): add language variants if multilingual

SAMEÂS properties (critical — these create entity graph connections):
Property P856 (official website): https://yourdomain.com
Property P4264 (LinkedIn): company LinkedIn URL
Property P2088 (Crunchbase): company Crunchbase URL
Property P6262 (official website/Fandom): [if applicable]
```

**After submission:**
```
□ Note your Wikidata Q-number (e.g., Q12345678)
□ Add Q-number to Organization schema sameAs array:
   "sameAs": ["https://www.wikidata.org/wiki/Q12345678", ...]
□ Save Q-number to: 01-intelligence/SS1-market/entity-profile.md
□ Monitor Google for Knowledge Panel appearance (may take 4-12 weeks)
```

---

### STEP 22 — LinkedIn Company Page

**Setup (if not already done):**
```
1. linkedin.com → Work → Create a Company Page
2. Company type: Small Business
3. Fill all fields:
   □ Company name (match exactly to website + Wikidata)
   □ Website URL: https://yourdomain.com
   □ Industry: Marketing Services (or your relevant industry)
   □ Company size: 1-10 employees
   □ Founded year
   □ Logo (400x400px, high quality)
   □ Cover image (1128x191px)
   □ About section: 2,000 characters — use keywords naturally
   □ Specialties: List your service keywords (these are indexed by Bing)
4. Target: 100% profile completion
```

**Ongoing (weekly):**
```
□ Post 2-3 times per week
   → Share blog posts with LinkedIn-native text (not just a link)
   → Post industry insights, data, commentary
   → Share client results (anonymized if needed)
□ Articles > Posts for authority signals (LinkedIn articles are indexed by Bing)
□ Ask team members / contractors to list your company in their profiles
□ Add LinkedIn company page URL to Organization schema sameAs
```

---

### STEP 23 — Crunchbase Profile

```
1. Go to: crunchbase.com
2. Click "Add your company"
3. Fill all fields:
   □ Legal company name (exact match to website + Wikidata)
   □ Short description
   □ Website: https://yourdomain.com
   □ Founded date
   □ Category groups: Advertising, Marketing (or your industry)
   □ HQ location
   □ Employee count range
   □ LinkedIn URL
4. Claim the profile (verify you're an authorized representative)
5. Add company URL to Organization schema sameAs array

Cost: Free basic listing
Premium ($29/mo): Not required — basic listing is sufficient for entity signals
```

---

### STEP 24 — Industry Directories

**Priority directories — submit in this order:**

```
FOR MARKETING/AGENCY:

1. Clutch.co (highest authority — DR 91)
   → clutch.co → List Your Company
   → Complete full profile: services, team size, clients, portfolio
   → Request reviews from 3+ past clients (Clutch sends them an email)
   → Clutch verification call required (20 min) — worth it

2. DesignRush
   → designrush.com → List Your Agency
   → Free listing available
   → Add portfolio samples

3. G2 (for SaaS/software companies)
   → g2.com → Get listed

4. Trustpilot
   → trustpilot.com → Get started for free
   → Invite past clients to review via email

FOR ALL BUSINESSES:

5. Google Business Profile (already done in Step 11)

DIRECTORY TRACKER — maintain this document:
01-intelligence/SS1-market/directory-submissions.md

Format:
| Directory | Status | Profile URL | Reviews | Notes |
|-----------|--------|-------------|---------|-------|
| Clutch | Active | clutch.co/profile/... | 3 | Verified |
| Google BP | Active | g.page/... | 12 | |
```

---

### STEP 25 — Digital PR Setup

**What you're doing:** Setting up the systems that enable ongoing link acquisition and brand mention monitoring.

**Set up monitoring:**
```
1. Google Alerts (free):
   → alerts.google.com
   → Create alerts for:
     □ "your company name" (brand mentions)
     □ "your founder/CEO name"
     □ [your main service keyword] (industry news to comment on)
   → Delivery: Daily digest, to your email
   → Result type: News

2. HARO/Connectively (free — journalists seeking expert sources):
   → connectively.us
   → Sign up as a Source (not a journalist)
   → Category: select your relevant industry categories
   → Check daily — respond within 2 hours for best chance of citation
   → Format: Subject = your credentials + answer, Body = 3-4 sentences maximum

3. Ahrefs Alerts (if using paid Ahrefs):
   → Ahrefs → Alerts → Mentions
   → Add your brand name → monitor unlinked mentions
   → When you find unlinked mentions → email the author requesting a link
```

**First digital PR asset — create within first month:**
```
EASIEST HIGH-VALUE ASSET: Industry Statistics Roundup

Process:
1. Google "[your industry] statistics 2026"
2. Find 15-20 statistics from authoritative sources
3. Compile into: "25 [Your Industry] Statistics That Will Change How You Think About [Topic]"
4. Add your own commentary/analysis to each stat
5. Publish as a pillar-length piece (3,000+ words)
6. Submit to:
   → Product Hunt (if digital tool adjacent)
   → Reddit relevant subreddit
   → LinkedIn as a LinkedIn Article
   → Email to 5-10 journalists who write about your industry

This type of content earns links passively — journalists cite statistics roundups
regularly. Target: 5-10 backlinks from this asset in the first 90 days.
```

---

## PHASE 6 — GEO & AI VISIBILITY (LAYER 6)

---

### STEP 26 — GEO Content Optimization

**What you're doing:** Applying the AI citation optimization checklist to every content page you have and every new page you create.

**Apply this checklist to every page (before publishing):**

```
STRUCTURE CHECKLIST:
□ Quick Answer Block at top (134-167 words) — answers the page's primary question
□ H1: Clear, keyword-containing, matches search intent
□ H2s: Cover all major subtopics (semantic completeness)
□ FAQ section at bottom: minimum 5 questions matching "People Also Ask"
□ Lists/bullets used for any process, ranking, or comparison content
□ Comparison tables for any "X vs Y" content
□ Data table where statistical data can be presented

CONTENT QUALITY CHECKLIST:
□ At least 2 specific statistics with cited sources (link to the study)
□ At least 1 first-hand example or case study
□ Original data or proprietary analysis (highest citability)
□ Every claim supported by evidence (not "many experts say")
□ Specific numbers, not ranges (say "47% increase", not "significant increase")
□ Publication date + last updated date visible on page

AUTHOR SIGNALS:
□ Author byline with name + credentials + link to author page
□ Author photo visible
□ Author's LinkedIn in their author page profile

FRESHNESS:
□ "Last updated: [date]" visible near the top of every content page
□ Update schedule in your calendar: every 7-14 days for high-priority pages

AFTER PUBLISHING:
□ Submit URL via IndexNow immediately
□ Request indexing in Google Search Console (URL Inspection → Request Indexing)
□ Share to LinkedIn (signals freshness and authority)
□ Update internal links from related pages to include this new content
```

---

### STEP 27 — Otterly.AI Setup

**What you're doing:** Setting up AI citation monitoring across ChatGPT, Perplexity, Google AI Mode, Gemini, and Copilot.

```
1. Go to: otterly.ai
2. Sign up (email + password)
3. Connect your brand:
   → Brand name: Your company name
   → Website: https://yourdomain.com
   → Competitors: Add 3-5 competitor domains to track alongside yours
4. Add tracked queries (keywords you want to monitor in AI answers):
   → Start with 10-20 your most important service keywords
   → Example: "google ads management agency", "best google ads consultant"
   → Add industry questions: "how to improve google ads performance"
5. Choose monitoring frequency: Daily (recommended to start)
6. Set up email alerts for:
   → New citations of your content
   → Competitor citations on your target queries

WEEKLY WORKFLOW (Monday):
□ Open Otterly.AI dashboard
□ Check: Citation count vs previous week (up or down?)
□ Check: Which pages are being cited most?
□ Check: Which queries generate citations for competitors but not you?
   → These are your highest-priority GEO content opportunities
□ Export weekly report → save to 01-intelligence/SS2-performance/

COST: ~$49/month (entry plan)
ROI TEST: If you're running paid ads too, compare:
  → Clicks from AI citations × conversion rate = leads from GEO
  → If GEO generates even 5 leads/month, Otterly pays for itself 3-4x
```

---

### STEP 28 — Bing AI Performance Dashboard

```
No separate setup required — it's inside Bing Webmaster Tools (Step 8)

Access:
1. bing.com/webmasters
2. Left sidebar → AI Performance
3. Data will start populating after 2-4 weeks of being registered

WHAT TO MONITOR:
□ AI citation count (should grow over time with better GEO content)
□ Which pages are cited most in Copilot answers
□ Which queries trigger Copilot answers citing your content
□ CTR from Copilot citations → compare to traditional Bing CTR

Note: This is currently the ONLY free tool showing AI search citation data.
Google Search Console is beginning to add similar data — watch for it.

Add to Monday monitoring routine alongside Otterly.AI.
```

---

### STEP 29 — Semrush AI Toolkit

```
Only relevant if you choose Semrush over Ahrefs as your primary SEO tool.

If using Semrush (included in all paid plans):
1. Semrush → left sidebar → AI Toolkit
2. Enter your target keywords
3. See:
   → Which keywords trigger Google AI Overviews
   → Who is cited in AI Overviews for each keyword
   → Your presence vs competitors in AI Overviews

If using Ahrefs as primary tool:
→ Skip Semrush AI Toolkit
→ Otterly.AI covers Google AI Mode tracking (Step 27)
```

---

## PHASE 7 — ANALYTICS & MONITORING (LAYER 7)

---

### STEP 30 — GA4 Organic Traffic Configuration

**What you're doing:** Configuring GA4 to properly isolate and analyze organic search traffic.

**Prerequisite:** GA4 already set up and linked to GSC (completed in Google Ads install guide Steps 2 and 7)

**Create organic traffic exploration:**
```
GA4 → Explore → + New exploration → Free Form

Configuration:
Dimensions: Landing page, Session default channel group, City
Metrics: Sessions, Engaged sessions, Engagement rate, Conversions, Key events

Add segment:
→ + Add segment → User segment → "Organic Search Only"
→ Filter: Session channel group → exactly matches → "Organic Search"
→ Save

REPORTS TO RUN WEEKLY:

Report 1: Which pages drive the most organic sessions?
→ Dimension: Landing page
→ Metric: Sessions
→ Segment: Organic Search Only
→ Sort: Sessions descending
→ Shows: Your top organic traffic pages

Report 2: Which organic pages convert to leads?
→ Same as above + add Conversions column
→ This shows which content drives actual business value

Report 3: Organic traffic trend
→ Reports → Acquisition → Traffic Acquisition
→ Filter: Session default channel group = "Organic Search"
→ Date: Last 90 days
→ Shows: Organic growth trend (should grow over time)
```

**Set up a dedicated Organic Traffic dashboard:**
```
GA4 → Reports → Library → Create Report → Blank

Add these cards:
1. Organic sessions (last 30 days vs previous 30 days)
2. Organic conversion rate
3. Top 10 organic landing pages by sessions
4. Organic sessions by city/country
5. Organic traffic over time (line chart, 90 days)

Share this dashboard link with yourself
→ Check every Monday morning
```

---

### STEP 31 — Rank Tracker Setup

**What you're doing:** Setting up automated weekly keyword rank monitoring.

**In Ahrefs:**
```
1. Ahrefs → Rank Tracker → + New project
2. Enter: yourdomain.com
3. Add competitors: Add 3 competitor domains to track alongside yours
4. Location: Your target country/city (important for local targeting)
5. Add keywords:
   → Start with 30-50 keywords
   → Include: Your pillar page keywords, primary service keywords
   → Include: Long-tail keywords you're targeting with cluster pages
   → Include: 5-10 branded keywords (your company name + variations)
6. Update frequency: Weekly
7. Set up email alerts:
   → Large position changes (+ or - 5+ positions)
   → Position 1-3 new rankings (celebrate wins)

Tag your keywords by topic cluster:
→ Tag: "Pillar 1 - Google Ads" → all Google Ads keywords
→ Tag: "Pillar 2 - [Next Topic]" → all next topic keywords
→ Allows you to see cluster-level performance, not just individual keywords

WEEKLY ROUTINE (Wednesday — 2 days after Monday GSC check):
□ Any keywords dropped 5+ positions? → Investigate page (content still there? tech issue?)
□ Any keywords moved to position 4-15? → Optimize that page (highest ROI)
□ Any new rankings appearing? → Note and build internal links to that page
□ Overall: Is tracked keyword average position trending down (good) over time?
```

---

### STEP 32 — Core Web Vitals Monitoring in GSC

**What you're doing:** Setting up continuous real-user performance monitoring from Google's data.

```
This is already accessible from Step 7 (GSC setup) — no additional setup needed.

MONTHLY ROUTINE (first Monday of month):
1. GSC → Core Web Vitals → Web (desktop separate)
2. Check "Poor URLs" count:
   → Should be 0 or trending toward 0
   → If new "Poor" pages appear: click through → see which metric failing
3. Check "Needs Improvement" count:
   → Set a quarterly target to move these to "Good"
4. Click any URL group → identify specific pages
5. Run those pages through pagespeed.web.dev for fix recommendations
6. Implement fixes in website code
7. After fixing: GSC → URL Inspection → paste URL → "Request re-evaluation"

EXPORT MONTHLY SCORES:
Save to: 01-intelligence/SS2-performance/cwv-monthly-[YYYY-MM].md

Track over time:
| Month | Good URLs | Needs Improvement | Poor URLs | LCP avg | INP avg | CLS avg |
|-------|-----------|-------------------|-----------|---------|---------|---------|
| Apr 2026 | X | X | X | Xs | Xms | X |
| May 2026 | | | | | | |
```

---

## WEEKLY OPERATING ROUTINE

Once all steps are complete, this is your weekly SEO operations cadence:

```
MONDAY — Data Review (45 minutes)
□ GSC: Check clicks/impressions vs last week. Any drops? Investigate.
□ Bing WMT AI Performance: Check Copilot citation count
□ Otterly.AI: Check AI citations. What queries is competition winning?
□ Rank Tracker: Review significant ranking changes

WEDNESDAY — Content (varies)
□ Publish or update 1 content piece
□ Apply GEO checklist before publishing
□ Submit via IndexNow immediately after publishing
□ Request indexing in GSC

FRIDAY — Link Building & Authority
□ Check HARO/Connectively — respond to relevant queries
□ Check Google Alerts for brand mentions
□ Any unlinked mentions from the week? Send reclamation email
□ Update 1-2 existing pages with links to new content
```

---

## MONTHLY AUDIT ROUTINE

```
First Monday of every month:
□ Run Screaming Frog crawl → compare to last month
□ Check Core Web Vitals in GSC → any new Poor pages?
□ Run PageSpeed Insights on top 3 pages → scores trending up?
□ Ahrefs: Check domain rating and referring domain count
□ Ahrefs: Run Site Audit → new errors to fix?
□ Export GSC Performance report → save to performance folder
□ Review content cluster progress: How many cluster pages published?
□ Review backlink growth: New referring domains vs last month?
```

---

## COST SUMMARY

| Tool | Monthly Cost | Status |
|------|-------------|--------|
| robots.txt | Free | Implement now |
| llms.txt | Free | Implement now |
| XML Sitemap | Free | Implement now |
| Canonical Tags | Free | Implement now |
| JSON-LD Schema | Free | Implement now |
| Core Web Vitals fixes | Free (dev time) | Implement now |
| Google Search Console | Free | Set up now |
| Bing Webmaster Tools | Free | Set up now |
| IndexNow Protocol | Free | Implement now |
| Yandex Webmaster | Free | Optional |
| Google Business Profile | Free | Set up now |
| Brave Search Webmaster | Free | Set up (10 min) |
| Ahrefs (or free tier) | $129/mo (or free) | Set up now |
| Screaming Frog | $21.58/mo (billed annually) | Install |
| Google PageSpeed | Free | Use now |
| Answer The Public | Free (3/day) | Use now |
| AlsoAsked | Free (limited) | Use now |
| Wikidata | Free | Week 4 |
| LinkedIn Company Page | Free | Set up now |
| Crunchbase | Free | Set up now |
| Clutch / G2 | Free (basic) | Set up now |
| Digital PR | Time only | Month 2+ |
| GEO Content Optimization | Free (process) | Ongoing |
| Otterly.AI | ~$49/mo | Month 2 |
| Bing AI Performance Dashboard | Free | Included in BWT |
| Semrush AI Toolkit | Included (if using Semrush) | Optional |
| GA4 Organic Analysis | Free | Already set up |
| Rank Tracker (Ahrefs) | Included | Set up now |
| CWV Monitoring (GSC) | Free | Included in GSC |
| **TOTAL HARD COST** | **~$215–225/mo** | |

---

## RA-PROJECT FOLDER SETUP

```bash
# Create all required directories
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/00-foundation/tracking/schema
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/00-foundation/legal
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/01-intelligence/SS1-market/keyword-research
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/01-intelligence/SS1-market/question-maps
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/01-intelligence/SS2-performance
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/02-slm-machine/content
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/03-automation/v1-deployment
mkdir -p /home/sog/skool/05-Client-OS/RA-Project/03-automation/v2-reporting

# Files to create in 00-foundation/tracking/:
# robots.txt          ← Step 1 (deploy to website root)
# llms.txt            ← Step 2 (deploy to website root)
# sitemap-config.md   ← Step 3 (sitemap architecture documentation)
# canonical-rules.md  ← Step 4 (canonical URL format decision)
# schema/org.json     ← Step 5 - Organization schema
# schema/website.json ← Step 5 - WebSite schema
# schema/service.json ← Step 5 - Service schema template
# schema/faq.json     ← Step 5 - FAQPage schema template
# schema/article.json ← Step 5 - Article schema template
# schema/person.json  ← Step 5 - Person schema template

# Files to create in 03-automation/v1-deployment/:
# indexnow.js         ← Step 9 - IndexNow notification function
```

---

## VERIFICATION CHECKLIST — PHASE 1 COMPLETE

Run this before moving to Phase 2:

```
TECHNICAL FOUNDATION:
□ robots.txt accessible at yourdomain.com/robots.txt
□ robots.txt tested in GSC robots.txt tester (no errors)
□ GPTBot and ClaudeBot allowed in robots.txt
□ anthropic-ai and CCBot blocked in robots.txt
□ llms.txt accessible at yourdomain.com/llms.txt
□ sitemap.xml (or sitemap-index.xml) accessible and valid
□ Canonical tag present in <head> of every page
□ Canonical always points to HTTPS version of URL
□ Organization schema on every page (validated in Rich Results Test)
□ WebSite schema on homepage (validated)
□ FAQPage schema on at least 1 service page (validated)
□ BreadcrumbList schema on all interior pages
□ Core Web Vitals: Performance score 90+ on mobile (or work in progress)
□ All images have explicit width and height attributes
□ Hero image uses fetchpriority="high" and rel="preload"
□ All <script> tags use defer attribute (except inline critical scripts)

SEARCH ENGINE PRESENCE:
□ Google Search Console: property verified, sitemap submitted
□ Bing Webmaster Tools: property verified, sitemap submitted
□ IndexNow API key file live at yourdomain.com/[key].txt
□ IndexNow automated function integrated into publish pipeline
□ Google Business Profile: created and verification pending/complete
□ Brave Search: site submitted

YOU ARE READY TO MOVE TO PHASE 2 →
```

---

*Installation guide generated by CAI + MGI Council | RA-Project | April 20, 2026*
*Reference document: seo-geo-llm-ecosystem-architecture.md*
*For Google Ads ecosystem setup: see google-ads-ecosystem-install-guide.md*
