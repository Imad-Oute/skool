# Framework Development Workflow

## Objective

Define, scaffold, and integrate new Agents, Workflows, or Skills into the CAI ecosystem with strict adherence to BMAD-METHOD operational standards.

## Trigger

New operational requirement identified by the User.

## Operational Steps

1. **Visioning:** Define the objective and map the asset to one of the 4 Core Ecosystems.
2. **Scaffolding:** Generate directory structure (`src/cai-skills/` or `src/cai-workflows/`).
3. **Definition:** Draft official documentation (`SKILL.md` or `workflow.md`) + `manifest.yaml`.
4. **Integration:** Update the `Master Blueprint` and verify dependencies.
5. **Validation:** Execute `cai-validator` quality gate.

## Validation

- Asset matches BMAD-METHOD structural patterns.
- Pass architectural validation check.
- Documentation reflected in the Master Blueprint.

## Feedback

Validation fail -> Correct schema -> Re-run validator.
