# Eval Tasks

Each subdirectory is a reproducible task used as a regression test for prompts, skills, commands, or adapter behavior.

## Structure

```text
eval/tasks/{task-name}/
├── eval.md
└── prompt.md
```

## `eval.md` Format

- Owner:
- Description:
- Git-Revision:
- Result:
- Modified files:
- Pass criteria:
- Tags:

## Rules

- Add an eval task when changing common prompts, core skills, safety policy, or command behavior.
- Keep prompts self-contained enough that another maintainer can reproduce the behavior.
- Record the git revision that last reproduced the task.

