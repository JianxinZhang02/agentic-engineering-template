# Agents

Agent 文件定义角色化审查者或辅助者。第一版只提供轻量角色说明，不依赖特定工具。

## 第一版 Agent

- `requirement-reviewer.md`
- `design-reviewer.md`
- `code-reviewer.md`
- `test-reviewer.md`
- `documentation-curator.md`

## 使用原则

- 适合独立审查、输出较多、需要隔离上下文的任务。
- 主 Agent 负责协调，不把所有工作都拆成多 Agent。
- Agent 输出应摘要返回，避免污染主对话。

