# Source Advantages Mapped Into This Template

本文件记录本模板从参考资料中吸收的优势，避免“为什么这样设计”只停留在个人记忆中。

## Agentic Engineering 规范建设指南

吸收点：

- `AGENTS.md` 只做入口索引，详细规则下沉。
- `context/` 作为人和 AI 共读的公共记忆。
- 需求过程中的 `notes.md` 是知识复利的种子。
- Command、Skill、Agent 按上下文影响分层。
- 工具设计应封装知识，不微观管理每一步。
- 需求完成后必须执行知识沉淀。
- 定期规范瘦身，避免规则膨胀。

落地位置：

- `AGENTS.md`
- `context/`
- `requirements/`
- `skills/`
- `commands/`
- `context/team/tooling-governance.md`

## Chromium AI Coding 实践

吸收点：

- AI Policy 明确人类最终责任。
- Prompt 分层组合，不维护巨型单体提示词。
- Knowledge Base 告诉 AI 去哪里找权威资料。
- Skills 按需激活专业能力。
- Eval 防止提示词和规则迭代造成行为退化。
- 项目级大型任务应保留可追溯设计和验证记录。

落地位置：

- `context/team/ai-policy.md`
- `prompts/`
- `eval/`
- `skills/verification-loop/`
- `prompts/task-prompts/`

## Everything Claude Code

吸收点：

- 跨 harness 适配，把 durable workflow 留在仓库中。
- rules 按 common 和语言/框架分层。
- hooks 用于机械化执行和会话记忆。
- 安装和适配必须避免重复加载。
- 持续学习和 skill stocktake 可用于防止工具腐化。
- 安全扫描和 prompt defense 应成为基础规则。

落地位置：

- `rules/`
- `hooks/`
- `mcp-configs/`
- `skills/tool-governance/`
- `skills/security-review/`
- `adapters/`

