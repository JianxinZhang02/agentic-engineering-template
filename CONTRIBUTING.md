# Contributing

本仓库的贡献目标是让 Agentic Engineering 模板更可靠、更轻、更容易 fork，而不是堆叠更多规则。

## 贡献类型

- 修订团队规范：更新 `context/team/`。
- 补充项目知识：更新 `context/project/{project}/`。
- 沉淀通用经验：更新 `context/experience/`。
- 调整需求模板：更新 `requirements/_template/` 或 `templates/`。
- 改进能力包：更新 `skills/`、`agents/`、`commands/`。
- 补充工具适配：更新 `adapters/`。
- 增加回归用例：更新 `eval/`。

## Review 规则

- `context/team/` 改动至少需要 1 名团队成员 review。
- `context/project/` 改动需要对应项目负责人 review。
- `AGENTS.md` 改动必须说明为什么不能下沉到其他目录。
- 新增 Skill、Agent、command 必须说明触发场景和复用频率。
- AI 生成的规范可以作为草稿，但合入前必须有人类确认。

## 不建议合入的内容

- 偶发问题的永久规则。
- 没有来源的项目事实。
- 重复已有规范的长篇说明。
- 绑定单一工具且没有适配说明的核心流程。
- 无真实使用场景的 Agent 或 Skill。

## 每月维护

每月进行一次规范瘦身：

- 删除过时知识。
- 合并重复规则。
- 检查 `context/INDEX.md` 是否仍准确。
- 检查 `AGENTS.md` 是否保持轻量。
- 复跑 `eval/` 中的人工用例。

