# Knowledge Base Routing

This file defines Agentic RAG guidance for this template. It tells agents where to look before answering or changing files.

## Core Principle: Consult, Then Answer

Do not answer from general model knowledge alone when project facts are involved. Consult the relevant repository documents first.

## Routing

### Requirements

If the task involves a feature, bug, design, or delivery workflow:

1. Read `requirements/README.md`.
2. Read the target `requirements/{id}/` files.
3. Read `commands/requirement-next.md` before phase transitions.

### Project Facts

If the task involves business behavior, architecture, APIs, terminology, or domain rules:

1. Read `context/project/{project}/INDEX.md`.
2. Follow the index to architecture, business context, API contracts, glossary, and experience.
3. Mark missing facts as待确认.

### Team Rules

If the task involves Git, review, testing, security, tool creation, or knowledge management:

- Git: `context/team/git-workflow.md`
- Review: `context/team/code-review-standard.md`
- Testing: `context/team/testing-standard.md`
- Security and responsibility: `context/team/ai-policy.md`
- Tool changes: `context/team/tooling-governance.md`
- Knowledge: `context/team/knowledge-management.md`

### Coding

If editing code:

1. Read `prompts/common.minimal.md`.
2. Read `prompts/common.md` if the task is non-trivial.
3. Read the relevant technology template in `prompts/templates/`.
4. Read existing source and at least one call site before editing.

### External Tools

If using MCP or extensions:

1. Read `mcp-configs/README.md`.
2. Use `mcp-configs/mcp-servers.example.json` only as a template.
3. Do not commit real credentials.

