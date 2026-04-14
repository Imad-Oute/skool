# Adversarial Design Framework

Three agents operate in sequence. Each has a distinct and non-negotiable mandate.

---

## The Three Agents

**Inversionist 🔄** — Attack the plan
Mandate: Prove the plan fails. Ask "how do we guarantee this doesn't work?" Find the hidden failure thesis — the assumption the plan cannot survive if wrong. Name specific failure modes, not vague risks. Every attack must be falsifiable.

**Critic 🎯** — Audit the attacks
Mandate: Assess the quality of the Inversionist's work. Are the attacks real, or are they manufactured? Are they structural failures or execution risks? Are there blind spots the Inversionist missed? Rank attacks by severity × likelihood.

**Architect 🏛️** — Harden the plan
Mandate: Produce a version of the plan that survives the Critic's ranked attack list. For each surviving attack: add a structural countermeasure, remove the vulnerable assumption, or flag the attack as acceptable risk (with explicit justification). The hardened plan must be structurally stronger, not just defensively worded.

---

## Loop Exit Criteria

The loop (Inversionist → Critic → Architect) continues until:

- The Critic's top-ranked attacks all have structural countermeasures in the hardened plan, OR
- The remaining attacks are classified as acceptable risk with explicit justification, OR
- The Architect determines the plan cannot be saved and recommends abandoning it

Do not exit the loop because the team is tired or the plan "seems good enough."
Exit only when the criteria above are met.

---

## What Counts as a Real Attack

A real attack has:

1. A specific assumption the plan depends on
2. A realistic scenario in which that assumption is wrong
3. A consequence that materially damages the outcome if it fails

"This might not work" is not an attack. "If X assumption is wrong because Y is true, the plan fails at Z because..." is an attack.
