# Agent Projects

`agent-projects/` stores long-running AI-assisted engineering initiatives. This is different from `context/project/`:

- `context/project/` stores knowledge about business or software projects.
- `agent-projects/` stores repeatable AI work programs, such as modernization, code health, migration, cleanup, or quality campaigns.

This mirrors the useful Chromium pattern of keeping project-specific agent work separate from general prompts and skills.

## When To Create An Agent Project

Create an agent project when work is:

- larger than one requirement,
- likely to produce reusable prompts, evals, or skills,
- owned by a person or team,
- expected to run repeatedly or across multiple repositories.

Do not create one for a one-off task that fits in a single `requirements/{id}/`.

## Required Files

```text
agent-projects/{name}/
├── README.md
├── skills.json
├── evals/
└── notes.md
```

## Ownership

Each agent project must declare:

- owner,
- scope,
- success criteria,
- related skills,
- related evals,
- exit condition.

