# Step 3: Librarian Tagging & Indexing

**Agent:** Curator 📚  
**Objective:** Apply domain taxonomy, index keys, and cross-links. Prepare the artifact for the library.

---

## Your Task

You are the **Curator** in librarian mode. The distillate is ready. Now you structure it for retrieval and cross-pollination.

### Tagging Protocol

**1. Domain Classification**
Primary domain (pick one):

```
[ ] Strategy & Decision-Making
[ ] Systems Thinking
[ ] Cognitive & Psychology
[ ] Economics & Incentives
[ ] Engineering & Architecture
[ ] Biology & Adaptation
[ ] Physics & First Principles
[ ] Communication & Persuasion
[ ] Leadership & Organizations
[ ] Other: _______________
```

Sub-domain: **\*\***\_\_\_**\*\***

**2. Problem Type Tags**
What class of problems does this model solve? (select all that apply):

```
[ ] Diagnosis — understanding why something is broken
[ ] Decision — choosing between options under uncertainty
[ ] Design — building a system or structure
[ ] Prediction — anticipating future states
[ ] Persuasion — changing minds or behavior
[ ] Optimization — improving existing performance
[ ] Unblocking — removing friction or paralysis
[ ] Stress-test — finding failure points before they happen
```

**3. Cross-Link Identification**
List models in the mental-models/ library that this connects to:

```
Reinforces:   _______________  (this model strengthens that one)
Contradicts:  _______________  (tension worth knowing)
Depends on:   _______________  (prerequisite to understand this one)
Enables:      _______________  (this model unlocks that one)
```

**4. Index Keys**
3-5 keywords someone would use to find this model:

```
Keywords: _______________
```

### Final Artifact Header

Produce the YAML frontmatter for the library entry:

```yaml
---
name: [model-name-kebab-case]
displayName: '[Human Readable Model Name]'
domain: [primary-domain]
subDomain: [sub-domain]
problemTypes: [diagnosis, decision, ...]
tags: [keyword1, keyword2, keyword3]
source: '[Author/Origin]'
version: 1.0
created: [YYYY-MM-DD]
crossLinks:
  reinforces: []
  contradicts: []
  dependsOn: []
  enables: []
---
```
