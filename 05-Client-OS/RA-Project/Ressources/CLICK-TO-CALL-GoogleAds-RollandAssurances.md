# STRATÉGIE CLICK-TO-CALL — GOOGLE ADS UNIQUEMENT
## Rolland Assurances | rollandassurances.com | Budget 1 500 €/mois
### Rapport généré le 11 Avril 2026

---

> **Format exclusif** : Call-Only Ads + Extensions d'appel sur Search.
> Aucune landing page chargée — les prospects appellent directement depuis l'annonce.
> SSL valide sur `https://rollandassurances.com` ✓

---

## SYNTHÈSE EXÉCUTIVE

| Paramètre | Valeur |
|---|---|
| Domaine | https://rollandassurances.com |
| SSL | ✅ Valide |
| Budget mensuel | 1 500 € |
| Segments | A — Seniors 55+ Mutuelle Santé / B — BTP Assurance Décennale |
| Format principal | Call-Only Search Ads |
| Plateforme | Google Ads uniquement |
| Horaires diffusion | Lundi–Vendredi 09:00–18:30 |
| Jours exclus | Samedi, Dimanche |
| Objectif principal | Appels entrants qualifiés (durée ≥ 60 secondes) |
| CPL cible Segment A | < 35 € par appel qualifié |
| CPL cible Segment B | < 55 € par appel qualifié |

---

## ⚙️ CONFIGURATION TECHNIQUE — PRÉREQUIS AVANT LANCEMENT

### Checklist obligatoire (à compléter avant toute dépense)

- [ ] **Numéro de Transfert Google activé** dans Google Ads → Outils → Conversions → Appels
  - Activer "Numéro Google de transfert d'appel"
  - Durée minimale de l'appel pour conversion : **60 secondes**
  - Compter comme conversion : **1 fois par appel**
- [ ] **Segment de conversion créé** : "Appel depuis annonce" (catégorie : Appels téléphoniques)
- [ ] **Liaison Google Ads ↔ Google Analytics 4** (import des conversions GA4 → Ads)
- [ ] **Extensions d'appel configurées** sur toutes les campagnes avec le numéro principal
- [ ] **Google Business Profile** créé et vérifié (bonus : éligibilité aux Local Service Ads)
- [ ] **Tag de conversion Google Ads** installé sur rollandassurances.com via Google Tag Manager

> **Avantage SSL** : Le certificat valide sur `https://rollandassurances.com` permet d'utiliser l'URL finale dans les extensions d'annonces. Pour les Call-Only Ads purs, la page n'est pas chargée mais l'URL affichée doit correspondre à un domaine HTTPS valide. ✅

---

## 📐 STRUCTURE DU COMPTE GOOGLE ADS

```
COMPTE : Rolland Assurances
│
├── CAMPAGNE 1 — [SENIOR] Mutuelle Santé | Call-Only | 750 €/mois
│   ├── Groupe S1 : Changement de mutuelle
│   ├── Groupe S2 : Urgence soins / remboursements
│   └── Groupe S3 : Hausse cotisation / résiliation Châtel
│
└── CAMPAGNE 2 — [BTP] Assurance Décennale | Call-Only | 750 €/mois
    ├── Groupe D1 : Urgence attestation
    ├── Groupe D2 : Création / première décennale
    ├── Groupe D3 : Changement assureur / moins cher
    └── Groupe D4 : Profils complexes / refusés ailleurs
```

---

## 🗓️ PARAMÈTRES DE DIFFUSION (COMMUNS AUX 2 CAMPAGNES)

### Planification horaire — Ad Schedule

| Jour | Statut | Plage de diffusion |
|---|---|---|
| Lundi | ✅ Actif | 09:00 → 18:30 |
| Mardi | ✅ Actif | 09:00 → 18:30 |
| Mercredi | ✅ Actif | 09:00 → 18:30 |
| Jeudi | ✅ Actif | 09:00 → 18:30 |
| Vendredi | ✅ Actif | 09:00 → 18:30 |
| Samedi | ❌ Suspendu | — |
| Dimanche | ❌ Suspendu | — |

> **Règle critique** : Ne jamais diffuser en dehors des heures d'ouverture. Un appel sans réponse = budget brûlé + prospect perdu définitivement. Configurer l'Ad Schedule exactement sur les plages ci-dessus.

### Réglages appareils

| Appareil | Ajustement d'enchère | Justification |
|---|---|---|
| Mobile | **+40%** (priorité absolue) | Click-to-call = usage mobile natif |
| Desktop | Référence (0%) | Appel possible via Google Chrome |
| Tablette | **-30%** | Moins d'appels spontanés depuis tablette |

### Ciblage géographique

| Paramètre | Valeur recommandée |
|---|---|
| Zone | France entière (ou rayon autour de l'agence) |
| Exclusions | Territoires d'outre-mer si hors zone de service |
| Option cible | "Personnes situées dans la zone cible" (pas "intérêt pour") |

---

## CAMPAGNE 1 — SEGMENT A : SENIORS 55+ / MUTUELLE SANTÉ

### Paramètres campagne

| Paramètre | Valeur |
|---|---|
| Nom | `[RA] Senior - Mutuelle Santé - Call Only` |
| Type | Réseau de Recherche uniquement |
| Objectif | Leads → Appels téléphoniques |
| Budget quotidien | **25 €/jour** (750 €/mois ÷ 30) |
| Stratégie d'enchères | Maximiser les conversions → puis Target CPA 35 € après 30 conversions |
| Rotation annonces | Optimiser (favoriser les meilleures performances) |
| Langues | Français |
| Réseau partenaire | ❌ Désactivé (Search Google uniquement) |
| Display Expansion | ❌ Désactivé |

---

### Groupe S1 — Changement de Mutuelle

**Correspondance de mots-clés** : Expression exacte + Large modifié uniquement (éviter les requêtes hors-sujet)

#### Mots-clés à cibler

| Mot-clé | Type | Intention |
|---|---|---|
| `"mutuelle santé senior"` | Expression | Recherche générale forte |
| `"changer de mutuelle après 60 ans"` | Expression | Intention de changement |
| `"comparateur mutuelle retraité"` | Expression | Phase de comparaison |
| `"meilleure mutuelle pour retraité"` | Expression | Décision imminente |
| `"mutuelle senior pas cher"` | Expression | Sensibilité prix |
| `"mutuelle complémentaire santé senior"` | Expression | Terme précis |
| `+courtier +mutuelle +senior` | Large modifié | Recherche de conseiller |
| `+simulation +mutuelle +retraité` | Large modifié | Phase devis |

#### Mots-clés à exclure (négatifs — liste de départ)

```
-mutuelle animaux
-mutuelle étudiante
-mutuelle entreprise
-mutuelle collective
-mutuelle obligatoire salarié
-MAAF avis
-Axa tarif
-April contact
-Harmonie avis
-MGEN
-résiliation mutuelle modèle lettre
-formulaire résiliation
-lettre type
-gratuit
```

---

### Groupe S2 — Urgence Soins / Remboursements

#### Mots-clés à cibler

| Mot-clé | Type | Intention |
|---|---|---|
| `"mutuelle dentaire senior"` | Expression | Forte urgence remboursement |
| `"remboursement prothèse auditive mutuelle"` | Expression | Besoin spécifique |
| `"mutuelle optique senior"` | Expression | Besoin spécifique |
| `"reste à charge retraité mutuelle"` | Expression | Douleur principale |
| `"mutuelle 100% santé senior"` | Expression | Réforme RAC0 |
| `"prise en charge auditive mutuelle"` | Expression | Besoin audioprothèse |
| `+mutuelle +couronne +dentaire +remboursement` | Large modifié | Besoin immédiat |
| `+implant +dentaire +mutuelle +senior` | Large modifié | Ticket élevé urgent |

---

### Groupe S3 — Hausse Cotisation / Résiliation Loi Châtel

#### Mots-clés à cibler

| Mot-clé | Type | Intention |
|---|---|---|
| `"résiliation mutuelle hausse tarif"` | Expression | Intent très fort |
| `"mutuelle moins chère +60 ans"` | Expression | Comparaison prix |
| `"loi Châtel résiliation mutuelle"` | Expression | Droits à la résiliation |
| `"résilier mutuelle santé"` | Expression | Action de résiliation |
| `"mutuelle trop chère retraite"` | Expression | Douleur tarifaire |
| `+résilier +mutuelle +sans +pénalité` | Large modifié | Cherche à changer |

---

### Annonces Call-Only — Segment A (Seniors)

> **Règles Google pour Call-Only Ads** :
> - Titre 1 : 30 caractères max
> - Titre 2 : 30 caractères max
> - Description : 90 caractères max
> - URL affichée : doit correspondre au domaine (rollandassurances.com)
> - Numéro de téléphone : obligatoire

---

#### Annonce A1 — Axe "Conseil Expert"

```
┌────────────────────────────────────────────────────────────────┐
│ Titre 1    : Mutuelle Senior — Devis Gratuit                   │
│ Titre 2    : Courtier Indépendant — Conseils 55+               │
│ Description: Comparez les meilleures mutuelles adaptées à      │
│              votre retraite. Appelez un conseiller maintenant. │
│ URL affich.: rollandassurances.com/mutuelle-senior             │
│ CTA        : Appeler Maintenant                                │
└────────────────────────────────────────────────────────────────┘
```

---

#### Annonce A2 — Axe "Économies"

```
┌────────────────────────────────────────────────────────────────┐
│ Titre 1    : Votre Mutuelle Coûte Trop Cher ?                  │
│ Titre 2    : Économisez — Courtier Retraités                   │
│ Description: Hausse de tarif ? Remboursements insuffisants ?   │
│              Notre courtier vous trouve une meilleure offre.   │
│ URL affich.: rollandassurances.com/mutuelle-senior             │
│ CTA        : Appeler Maintenant                                │
└────────────────────────────────────────────────────────────────┘
```

---

#### Annonce A3 — Axe "Reste à Charge / Dentaire"

```
┌────────────────────────────────────────────────────────────────┐
│ Titre 1    : Mutuelle Dentaire Senior Abordable                │
│ Titre 2    : Remboursements Optique & Audio                    │
│ Description: Réduisez votre reste à charge. Un courtier        │
│              indépendant compare pour vous — sans engagement.  │
│ URL affich.: rollandassurances.com/mutuelle-senior             │
│ CTA        : Appeler Gratuitement                              │
└────────────────────────────────────────────────────────────────┘
```

---

#### Annonce A4 — Axe "Résiliation / Changement"

```
┌────────────────────────────────────────────────────────────────┐
│ Titre 1    : Résilier Votre Mutuelle — Conseils Gratuits       │
│ Titre 2    : Loi Châtel — Changez Sans Frais                   │
│ Description: Vous pouvez changer de mutuelle à tout moment.   │
│              Appelez notre conseiller pour une analyse rapide. │
│ URL affich.: rollandassurances.com/mutuelle-senior             │
│ CTA        : Appeler Maintenant                                │
└────────────────────────────────────────────────────────────────┘
```

---

### Projections Budgétaires — Segment A (750 €/mois)

| Métrique | Estimation Phase Test | Estimation Phase Croissance |
|---|---|---|
| Budget mensuel | 750 € | 1 500 € |
| Budget quotidien | 25 € | 50 € |
| CPC moyen estimé | 2,50 – 4,00 € | 2,00 – 3,50 € |
| Clics estimés/mois | 190 – 300 | 430 – 750 |
| Taux d'appel depuis clic | 35 – 50% | 40 – 55% |
| Appels estimés/mois | 67 – 150 | 172 – 413 |
| Durée qualifiante | ≥ 60 secondes | ≥ 60 secondes |
| Appels qualifiés estimés | 25 – 55 | 65 – 155 |
| CPL cible (appel qualifié) | < 35 € | < 22 € |
| Taux de clôture estimé | 15 – 20% | 18 – 25% |
| Contrats estimés/mois | 4 – 11 | 12 – 39 |
| Commission moyenne | 180 – 220 €/an | 180 – 220 €/an |
| LTV (3 ans) | 540 – 660 € | 540 – 660 € |
| ROI estimé (mois 1) | 2,9x – 9,7x | 5,2x – 17x |

---

## CAMPAGNE 2 — SEGMENT B : PROFESSIONNELS BTP / ASSURANCE DÉCENNALE

### Paramètres campagne

| Paramètre | Valeur |
|---|---|
| Nom | `[RA] BTP - Décennale - Call Only` |
| Type | Réseau de Recherche uniquement |
| Objectif | Leads → Appels téléphoniques |
| Budget quotidien | **25 €/jour** (750 €/mois ÷ 30) |
| Stratégie d'enchères | Maximiser les conversions → puis Target CPA 55 € après 30 conversions |
| Rotation annonces | Optimiser |
| Langues | Français |
| Réseau partenaire | ❌ Désactivé |
| Display Expansion | ❌ Désactivé |

---

### Groupe D1 — Urgence Attestation (Intention maximale)

#### Mots-clés à cibler

| Mot-clé | Type | Intention |
|---|---|---|
| `"assurance décennale urgent"` | Expression | Urgence absolue |
| `"assurance décennale immédiate"` | Expression | Urgence absolue |
| `"attestation décennale rapide"` | Expression | Délai critique |
| `"décennale en 24h"` | Expression | Urgence délai |
| `"assurance décennale express"` | Expression | Urgence délai |
| `+obtenir +attestation +décennale +vite` | Large modifié | Urgence chantier |

---

### Groupe D2 — Création / Première Décennale

#### Mots-clés à cibler

| Mot-clé | Type | Intention |
|---|---|---|
| `"assurance décennale artisan"` | Expression | Cœur de cible |
| `"décennale auto entrepreneur bâtiment"` | Expression | Micro-entreprise BTP |
| `"assurance décennale maçon"` | Expression | Corps de métier |
| `"décennale électricien"` | Expression | Corps de métier |
| `"décennale plombier"` | Expression | Corps de métier |
| `"décennale couvreur"` | Expression | Corps de métier |
| `"décennale carreleur"` | Expression | Corps de métier |
| `"assurance décennale peintre"` | Expression | Corps de métier |
| `"assurance décennale devis"` | Expression | Demande de prix |
| `+souscrire +décennale +artisan` | Large modifié | Intention souscription |
| `+assurance +décennale +nouveau +artisan` | Large modifié | Création d'activité |

---

### Groupe D3 — Changement Assureur / Prix

#### Mots-clés à cibler

| Mot-clé | Type | Intention |
|---|---|---|
| `"changer assurance décennale"` | Expression | Changement en cours d'année |
| `"assurance décennale moins chère"` | Expression | Sensibilité prix |
| `"résiliation décennale"` | Expression | Changement assureur |
| `"comparateur décennale professionnel"` | Expression | Phase comparaison |
| `"assurance décennale pas cher artisan"` | Expression | Prix + profil |
| `+décennale +meilleur +prix +courtier` | Large modifié | Courtier = meilleur prix |

---

### Groupe D4 — Profils Complexes / Refusés

#### Mots-clés à cibler

| Mot-clé | Type | Intention |
|---|---|---|
| `"assurance décennale refusée"` | Expression | Profil difficile — très qualifié |
| `"décennale sinistre antérieur"` | Expression | Profil sinistré |
| `"assurance décennale artisan étranger"` | Expression | Profil hors-norme |
| `"décennale sans expérience"` | Expression | Jeune artisan |
| `"assurance décennale tous risques"` | Expression | Couverture étendue |
| `+décennale +refus +assureur +solution` | Large modifié | Cherche alternative |

#### Mots-clés à exclure — Segment B (négatifs)

```
-assurance décennale définition
-c'est quoi la décennale
-loi spinetta explication
-durée décennale
-décennale promoteur
-décennale maître d'ouvrage
-code des assurances
-jurisprudence décennale
-modèle contrat
-gratuit
-formation
-cours
-certification
-étude
```

---

### Annonces Call-Only — Segment B (Décennale BTP)

#### Annonce B1 — Axe "Urgence Attestation"

```
┌────────────────────────────────────────────────────────────────┐
│ Titre 1    : Décennale — Attestation en 24h                    │
│ Titre 2    : Courtier BTP Expert — Appelez                     │
│ Description: Besoin urgent d'une attestation décennale ?       │
│              Courtier indépendant — devis rapide tous métiers. │
│ URL affich.: rollandassurances.com/assurance-decennale         │
│ CTA        : Appeler Maintenant                                │
└────────────────────────────────────────────────────────────────┘
```

---

#### Annonce B2 — Axe "Obligation Légale / Sécurité"

```
┌────────────────────────────────────────────────────────────────┐
│ Titre 1    : Décennale Obligatoire — Devis Gratuit             │
│ Titre 2    : 10+ Assureurs Comparés En 1 Appel                 │
│ Description: Loi Spinetta — obligation légale pour tous les    │
│              artisans BTP. Notre courtier vous protège vite.   │
│ URL affich.: rollandassurances.com/assurance-decennale         │
│ CTA        : Appeler Maintenant                                │
└────────────────────────────────────────────────────────────────┘
```

---

#### Annonce B3 — Axe "Profils Difficiles"

```
┌────────────────────────────────────────────────────────────────┐
│ Titre 1    : Décennale Refusée Ailleurs ?                      │
│ Titre 2    : Tous Profils BTP Acceptés                         │
│ Description: Sinistre, jeune artisan, auto-entrepreneur —      │
│              nous trouvons une solution. Appelez maintenant.   │
│ URL affich.: rollandassurances.com/assurance-decennale         │
│ CTA        : Appeler Gratuitement                              │
└────────────────────────────────────────────────────────────────┘
```

---

#### Annonce B4 — Axe "Prix / Économies"

```
┌────────────────────────────────────────────────────────────────┐
│ Titre 1    : Décennale Moins Chère — Courtier Indép.           │
│ Titre 2    : Comparez Sans Engagement — Appelez                │
│ Description: Payez-vous trop cher votre assurance décennale ?  │
│              Un appel suffit pour savoir. Sans engagement.     │
│ URL affich.: rollandassurances.com/assurance-decennale         │
│ CTA        : Appeler Maintenant                                │
└────────────────────────────────────────────────────────────────┘
```

---

### Projections Budgétaires — Segment B (750 €/mois)

| Métrique | Estimation Phase Test | Estimation Phase Croissance |
|---|---|---|
| Budget mensuel | 750 € | 1 500 € |
| Budget quotidien | 25 € | 50 € |
| CPC moyen estimé | 4,00 – 7,00 € | 3,50 – 6,00 € |
| Clics estimés/mois | 107 – 188 | 250 – 430 |
| Taux d'appel depuis clic | 35 – 50% | 40 – 55% |
| Appels estimés/mois | 37 – 94 | 100 – 237 |
| Appels qualifiés (≥ 60s) | 18 – 42 | 50 – 120 |
| CPL cible (appel qualifié) | < 55 € | < 35 € |
| Taux de clôture estimé | 20 – 30% | 22 – 32% |
| Contrats estimés/mois | 4 – 13 | 11 – 38 |
| Commission moyenne | 250 – 350 €/an | 250 – 350 €/an |
| LTV (3 ans) | 750 – 1 050 € | 750 – 1 050 € |
| ROI estimé (mois 1) | 4x – 18x | 5,5x – 26x |

---

## 💰 RÉPARTITION BUDGÉTAIRE — 1 500 €/MOIS

### Allocation Phase Test (Mois 1–2)

```
Budget total mensuel : 1 500 €
│
├── Campagne Senior Mutuelle Santé .......... 750 € (50%)
│   ├── Groupe S1 - Changement mutuelle ...... 250 €
│   ├── Groupe S2 - Urgence soins ............ 300 €
│   └── Groupe S3 - Hausse cotisation ........ 200 €
│
└── Campagne BTP Assurance Décennale ........ 750 € (50%)
    ├── Groupe D1 - Urgence attestation ...... 300 €
    ├── Groupe D2 - Création décennale ....... 200 €
    ├── Groupe D3 - Changement assureur ...... 150 €
    └── Groupe D4 - Profils complexes ........ 100 €
```

### Budget quotidien par campagne

| Campagne | Budget/mois | Budget/jour | Jours actifs/mois |
|---|---|---|---|
| Senior Mutuelle | 750 € | 34,10 € | 22 jours (lun–ven) |
| BTP Décennale | 750 € | 34,10 € | 22 jours (lun–ven) |
| **TOTAL** | **1 500 €** | **68,20 €** | — |

> **Note** : Google Ads peut dépasser le budget quotidien jusqu'à 2× certains jours mais ne dépassera pas le budget mensuel. Le budget mensuel de 750 € par campagne est respecté sur 30 jours.

### Réallocation recommandée après 30 jours

Après analyse des données réelles (impressions, CTR, appels, durée) :

| Scénario | Action |
|---|---|
| Segment A CPA < 30 € | Augmenter budget Senior de 20–30% |
| Segment B CPA < 45 € | Augmenter budget Décennale de 20–30% |
| Groupe D1 (urgence) fonctionne bien | Doubler le budget de ce groupe |
| Groupe avec CPA > objectif × 1,5 | Réduire ou pauser, investiguer les requêtes |

---

## 📊 EXTENSIONS D'ANNONCES RECOMMANDÉES

> Les extensions s'appliquent aux campagnes Search standard qui accompagnent les Call-Only Ads. Pour les Call-Only Ads purs, seul le numéro de téléphone est affiché.

### Extensions d'Appel (Call Extensions) — Obligatoires

```
Numéro principal : [numéro Rolland Assurances]
Planification    : Lundi–Vendredi 09:00–18:30 uniquement
Rapport d'appel  : Activé (suivi des conversions)
```

### Extensions de Lieu (Location Extensions)

- Lier le compte Google Business Profile
- Affiche l'adresse de l'agence + distance pour les recherches locales
- Augmente la confiance (signal de présence physique)

### Extensions d'Accroche (Callout Extensions)

```
Pour Segment A (Senior) :
• "Courtier Indépendant"
• "Conseil Gratuit et Sans Engagement"
• "Spécialiste Retraités 55+"
• "Comparez 10+ Mutuelles"
• "Réponse en 24h"

Pour Segment B (BTP) :
• "Expert Assurance BTP"
• "Tous Corps de Métiers"
• "Attestation Rapide"
• "Profils Difficiles Acceptés"
• "Courtier Indépendant"
```

### Extensions de Liens Annexes (Sitelink Extensions)

```
Pour Segment A :
→ "Devis Mutuelle Senior"      | rollandassurances.com/mutuelle-senior
→ "Comparer les Mutuelles"     | rollandassurances.com/comparateur
→ "Nos Engagements"            | rollandassurances.com/a-propos
→ "Contactez-Nous"             | rollandassurances.com/contact

Pour Segment B :
→ "Devis Décennale Gratuit"    | rollandassurances.com/decennale
→ "Métiers Couverts"           | rollandassurances.com/metiers-btp
→ "Attestation Express"        | rollandassurances.com/attestation-rapide
→ "Contactez-Nous"             | rollandassurances.com/contact
```

---

## 📅 CALENDRIER DE LANCEMENT

### Semaine 0 — Technique (avant toute dépense)

| Tâche | Responsable | Priorité |
|---|---|---|
| Vérifier SSL https://rollandassurances.com | ✅ Fait | — |
| Créer compte Google Ads (si inexistant) | Rolland Assurances | Critique |
| Activer Numéro de Transfert Google | Google Ads Admin | Critique |
| Créer conversion "Appel ≥ 60 secondes" | Google Ads Admin | Critique |
| Lier Google Analytics 4 à Google Ads | Google Ads Admin | Haute |
| Créer/optimiser Google Business Profile | Rolland Assurances | Haute |
| Installer Google Tag Manager sur le site | Dev / Admin | Haute |

### Semaine 1 — Lancement Phase Test

| Tâche | Détail |
|---|---|
| Créer campagne Senior Call-Only | 750 €/mois, 3 groupes, 4 annonces |
| Créer campagne BTP Décennale Call-Only | 750 €/mois, 4 groupes, 4 annonces |
| Configurer Ad Schedule | Lun–Ven 09:00–18:30 uniquement |
| Configurer ajustements appareils | Mobile +40%, Tablette -30% |
| Ajouter toutes les extensions | Appel, Lieu, Accroche, Liens annexes |
| Ajouter listes de mots-clés négatifs | Voir listes ci-dessus |

### Semaine 2–4 — Optimisation Continue

| Tâche | Fréquence |
|---|---|
| Analyser le Rapport sur les termes de recherche | Chaque semaine |
| Ajouter nouveaux mots-clés négatifs | Chaque semaine |
| Vérifier durée moyenne des appels | Chaque semaine |
| Comparer CTR entre annonces | Fin semaine 2 |
| Pauser annonces CTR < 2% | Fin semaine 3 |

### Mois 2 — Optimisation Enchères

| Condition | Action |
|---|---|
| ≥ 30 conversions sur une campagne | Basculer en Target CPA |
| CPA réel < objectif × 0,8 | Augmenter le budget de 20% |
| CPA réel > objectif × 1,5 | Investiguer les requêtes, ajuster les enchères |
| Groupe avec 0 conversion en 30 jours | Pauser et réviser les mots-clés |

---

## 📈 INDICATEURS DE PERFORMANCE (KPIs)

### KPIs hebdomadaires à suivre

| KPI | Objectif Segment A | Objectif Segment B |
|---|---|---|
| Impressions | > 500/semaine | > 300/semaine |
| CTR (taux de clic) | > 8% | > 10% |
| Taux d'appel depuis clic | > 35% | > 40% |
| Durée moyenne appel | > 90 secondes | > 120 secondes |
| CPL (coût par appel qualifié) | < 35 € | < 55 € |
| Taux de clôture | > 15% | > 20% |

### Signaux d'alarme (à investiguer immédiatement)

| Signal | Interprétation | Action |
|---|---|---|
| CTR < 3% | Annonces non pertinentes ou enchères trop faibles | Réviser les titres, augmenter enchère |
| Appels < 60 secondes > 60% | Mauvaise qualité des prospects ou mauvais numéro | Vérifier le numéro, revoir les mots-clés |
| CPC > 8 € (Senior) | Concurrence intense sur ce mot-clé | Ajouter mots-clés longue traîne |
| CPC > 12 € (Décennale) | Enchère trop agressive | Ajuster enchère max ou passer en Target CPA |
| Aucune impression | Enchères trop basses ou erreur de configuration | Vérifier statut, augmenter enchère |

---

## 🔒 CONFORMITÉ RÉGLEMENTAIRE

### Mentions obligatoires ORIAS / ACPR

Toutes les annonces pour des produits d'assurance doivent respecter :

- **Catégorie sensible Google Ads** : "Crédit, logement et assurance" → certification requise
- **Mention ORIAS** : Le numéro ORIAS de Rolland Assurances doit apparaître sur la landing page de destination
- **Interdiction** : Promettre un "meilleur prix garanti" sans justification
- **RGPD** : Toute collecte de données via formulaire (même sur la landing) nécessite une politique de confidentialité à jour

### Certification Google Ads — Catégories Financières

> Avant de lancer les campagnes, vérifier que le compte Google Ads a complété la vérification pour les annonces de services financiers (assurances). Cela peut prendre 2–7 jours ouvrés.

**Étapes** :
1. Google Ads → Paramètres compte → Vérification de l'annonceur
2. Soumettre les documents requis (KBIS, numéro ORIAS, justificatifs)
3. Attendre validation avant la mise en ligne des campagnes

---

## 🎯 RÉSUMÉ ACTIONNABLE — PRIORITÉS

### Top 5 actions immédiates

| Priorité | Action | Impact |
|---|---|---|
| 🔴 1 | Créer compte Google Ads + vérification annonceur assurance | Bloquant |
| 🔴 2 | Activer Numéro de Transfert Google + conversion ≥ 60s | Bloquant |
| 🟠 3 | Créer les 2 campagnes Call-Only avec Ad Schedule Lun–Ven 09h–18h30 | Lancement |
| 🟠 4 | Ajouter toutes les extensions (appel, accroche, liens) | Performance +30% |
| 🟡 5 | Créer/optimiser Google Business Profile | Local + LSA |

### Horizon de résultats attendus

| Période | Attendu |
|---|---|
| Semaine 1 | Premières impressions, premiers appels |
| Semaine 2–3 | Données suffisantes pour optimiser les annonces |
| Mois 1 | 30–80 appels qualifiés, premiers contrats signés |
| Mois 2 | Optimisation enchères Target CPA, réduction CPL |
| Mois 3 | ROI stabilisé, identification du segment le plus rentable |
| Mois 4–6 | Scaling du segment gagnant, réduction budget segment faible |

---

## ANNEXE — GLOSSAIRE

| Terme | Définition |
|---|---|
| Call-Only Ad | Format d'annonce Google qui affiche uniquement un bouton d'appel — pas de lien vers un site |
| CPL | Coût par Lead — ici, coût par appel qualifié (≥ 60 secondes) |
| CPC | Coût par Clic |
| CTR | Click-Through Rate — taux de clic (clics ÷ impressions) |
| Target CPA | Stratégie d'enchères automatique de Google visant un coût par acquisition défini |
| Ad Schedule | Planification horaire des annonces — contrôle quand les annonces sont diffusées |
| RLSA | Remarketing Lists for Search Ads — retargeting sur le Search (phase suivante) |
| ORIAS | Organisme pour le registre unique des intermédiaires en assurance |
| Loi Spinetta | Loi du 4 janvier 1978 rendant l'assurance décennale obligatoire pour les constructeurs |
| Loi Châtel | Loi permettant aux assurés de résilier leur contrat lors du renouvellement annuel |

---

*Rapport généré le 11 Avril 2026 — Rolland Assurances | https://rollandassurances.com*
*Budget : 1 500 €/mois | Plateforme : Google Ads uniquement | Format : Click-to-Call*
