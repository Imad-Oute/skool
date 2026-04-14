# Protocol: Automated Competitive Intelligence Harvest

## Objective
Systematically extract, analyze, and synthesize competitive data from 20 identified market leaders to inform Rolland Assurances' lead gen strategy.

## 1. The 20-Competitor List (Targeted)

### Mutuelle Santé Sénior (10)
1. Groupe VYV (Harmonie Mutuelle)
2. Malakoff Humanis
3. AXA France
4. Groupama
5. Allianz France
6. April
7. Mutualia
8. Apivia
9. Néoliane
10. Alptis

### Garantie Décennale (10)
1. April (Probat)
2. Entoria
3. Diot-Siaci
4. Verspieren
5. Réassurez-moi
6. Odealim
7. Filhet-Allard
8. Verlingue
9. Simplis
10. Maxance

---

## 2. Recommended Tooling Strategy (Crawl & Harvest)

Given our constraint of **speed and CLI-centric workflows**, I recommend these tools in order of preference:

### Tier 1: The "Surgical" Python Path (Recommended)
*   **BeautifulSoup + Requests:** Best for targeted, low-overhead scraping of known URLs. Allows us to ignore "noise" (ads, third-party trackers) and extract only the H1, H2, and CTA text we need.
*   **Playwright:** Essential if the competitor sites are heavily rendered in JavaScript. Use this if `Requests` returns an empty page.

### Tier 2: The CLI "Power User" Path
*   **`wget` / `curl`:** Use for quick-and-dirty bulk downloading of HTML to your local directory for offline grep/analysis.
*   **`ripgrep` (rg):** Once you have the files, use `rg` to find patterns like "gratuit", "devis", "immédiat", "attestation", "senior" across all 20 files instantly.

### Tier 3: AI-Assisted Synthesis (Our "Brain")
*   **Gemini CLI (This Agent):** Feed the raw HTML content (distilled via `cai-distillator`) directly into me for the **"Incentive Audit"**. I will then generate the structured breakdown.

---

## 3. The Harvest Protocol (Execute Once Weekly)

1.  **Crawl:** Iterate through the 20 URLs. Save locally to `saved/data/raw_harvest/<date>/<competitor>.html`.
2.  **Distill:** Pass the raw HTML to `cai-distillator` to remove bloat, leaving only the "Copy and Call-to-Action" layer.
3.  **Synthesize:** Run a custom Python audit script (I will build this for you) to create a tabular markdown report of:
    *   `Headline`, `Subheadline`, `Primary CTA`, `Trust Signals`, `Pricing Focus`.

---
*Status: Ready for Implementation.*
