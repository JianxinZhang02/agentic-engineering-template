# Git Workflow

## 分支策略

- `main` 或 `master` 保持可发布状态。
- 每个需求使用独立分支，建议命名为 `feature/{requirement-id}-{short-name}`。
- 修复线上问题使用 `fix/{issue-id}-{short-name}`。
- 规范和知识库改动使用 `docs/{topic}`。

## 提交流程

1. 开始需求前确认当前工作区状态。
2. 创建或切换到需求分支。
3. 将需求产物放入 `requirements/{id}/`。
4. 代码、测试、文档分批提交，避免巨大混合提交。
5. PR 描述必须说明需求目标、主要改动、测试结果和知识沉淀情况。

## 提交信息建议

```text
type(scope): summary
```

常用 type：

- `feat`：功能。
- `fix`：缺陷修复。
- `docs`：文档或知识库。
- `test`：测试。
- `refactor`：不改变行为的重构。
- `chore`：工程维护。

## Agent 约束

- 不得主动重写历史。
- 不得修改与当前需求无关的文件。
- 遇到脏工作区时，必须先说明已存在变更并避免覆盖。
- 提交前必须记录已执行和未执行的验证。

