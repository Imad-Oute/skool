# Attack Vector Catalog

Use this catalog to ensure comprehensive coverage. Weak attack sessions miss entire categories.

---

## Structural Failures

- **Single point of failure**: One component's failure collapses the whole plan
- **Hidden dependency**: Plan depends on X, which depends on Y, which is uncontrolled
- **Circular assumption**: Plan succeeds IF condition A, but condition A requires the plan to already be succeeding
- **Threshold sensitivity**: Plan works at scale X but not at X-1 or X+1
- **Coupling failure**: Two components are more tightly coupled than the plan assumes

## Assumption Failures

- **Optimism bias**: Best-case assumptions treated as base-case
- **Static environment assumption**: Plan assumes competitors, market, or technology stays the same
- **Competence assumption**: Plan requires execution capability the team does not yet have
- **Resource assumption**: Plan requires resources that are not yet secured
- **Timeline assumption**: Plan requires events to happen in sequence; any delay cascades

## Human & Incentive Failures

- **Misaligned incentives**: Key stakeholders are rewarded for behaviors that contradict the plan
- **Commitment gap**: Plan requires sustained commitment; what happens when novelty fades?
- **Authority gap**: Plan requires decisions no one in the team has authority to make
- **Coordination failure**: Plan requires precise coordination between parties with no shared incentive

## External & Market Failures

- **Competitive response**: Plan assumes competitors don't react, adapt, or retaliate
- **Regulatory exposure**: Plan triggers a regulatory response that wasn't modeled
- **Demand assumption**: Plan assumes demand that hasn't been validated at the required scale
- **Timing risk**: Plan works in current conditions but not if executed 6 months later

## Second-Order Failures

- **Success creates new problem**: Plan succeeds, but success itself creates a crisis (scaling, culture, competition)
- **Metric gaming**: Optimizing for the metric destroys the outcome the metric was measuring
- **Survivorship selection**: Plan attracts only a specific type of customer/partner, poisoning future growth
