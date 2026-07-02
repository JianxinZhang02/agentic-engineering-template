# Eval: Template Smoke

- Owner: template maintainers
- Description: Verify that a fresh template copy can create a project context and requirement workspace.
- Git-Revision: current
- Result: The agent should identify required files, copy templates, and report missing project facts as待确认 rather than inventing them.
- Modified files:
  - `context/project/example-smoke/`
  - `requirements/2026-07-example-smoke/`
- Pass criteria:
  - Reads `AGENTS.md` and `context/INDEX.md`.
  - Creates or verifies 6 project context files.
  - Creates or verifies 7 requirement lifecycle files.
  - Does not invent domain facts.
- Tags:
  - template
  - lifecycle
  - smoke

