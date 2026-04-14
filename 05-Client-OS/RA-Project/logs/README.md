# LOGS
## Agent Execution Logs — Auto-Generated, Do Not Edit

---

## PURPOSE

This folder contains execution logs generated automatically by CAI and MGI agents during their skill runs. Logs record what each agent did, what decisions were made, and what outputs were produced during each session.

**These files are auto-generated.** Do not manually edit them. Do not delete them unless explicitly cleaning up old sessions. They are the audit trail of agent activity.

---

## WHAT IS LOGGED HERE

Each agent that produces a log file creates an entry in the format:
```
[agent-name].log
```

Currently present:
- `mgi-adversarial-designer.log` — stress-test sessions run by the Inversionist
- `mgi-first-principles-deconstructor.log` — first-principles deconstruction sessions by the Thinker
- `mgi-system-auditor.log` — system entropy audits run by the Architect

---

## HOW TO USE LOGS

Logs are useful for:
- Reviewing what an agent produced in a previous session without re-running it
- Debugging unexpected agent outputs
- Building a historical record of strategic decisions made through agent sessions
- Cross-referencing when a specific analysis was done

---

## WHAT DOES NOT BELONG HERE

- Agent output documents (→ `output/knowledge/`)
- Performance reports (→ `01-intelligence/SS2-performance/`)
- Weekly directives (→ `01-intelligence/SS2-performance/directives/`)
- Any manually created document

Logs are system artifacts. If you want the output of an agent session in a usable format, look in `output/` — that's where the produced documents land.
