# Adapters

`adapters/` 存放工具适配说明。核心规范必须保持工具中立；适配层只负责把这些规范映射到具体工具。

## 已提供适配

- `claude-code.md`
- `codex.md`
- `workbuddy.md`

## 适配原则

- 不复制核心规范到工具私有配置中。
- 工具入口必须指向 `AGENTS.md`。
- 工具命令必须映射到 `commands/` 中的标准动作。
- 成熟工作流可以封装为工具能力，但源规范仍保留在仓库。
- Hook 不可用的工具，应使用 `hooks/README.md` 中的指令式门禁替代。
- MCP 配置必须从 `mcp-configs/` 样例派生，不提交真实密钥。

## 可移植资产

- `SKILL.md` 是最可移植的能力单元。
- `AGENTS.md` 和 `prompts/` 是行为入口。
- `rules/` 是可安装规则。
- `hooks/` 是可选机械化层。
- `mcp-configs/` 是连接模板。
