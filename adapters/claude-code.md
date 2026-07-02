# Adapter: Claude Code

## 推荐映射

- 将 `AGENTS.md` 作为 Claude Code 的主入口说明。
- 将 `commands/` 中的动作映射为 slash command。
- 将 `skills/` 中的 `SKILL.md` 作为 Claude Code Skill 的来源。
- 将 `agents/` 中的角色定义映射为 Subagent 或审查提示。
- 将 `rules/` 按 common + 技术栈复制或安装。
- 将 `hooks/` 映射为 Claude Code 原生 hooks 时，避免重复加载。

## 配置建议

1. 保持核心规范在仓库中，不复制到用户目录形成第二份真相。
2. slash command 只做预检和委托，不重复 Skill 全部内容。
3. Skill 只在触发时加载，避免上下文膨胀。
4. Subagent 只用于输出较多或需要独立审查的任务。

## 示例映射

| 标准动作 | Claude Code 入口 |
| --- | --- |
| `requirement-new` | `/requirement:new` |
| `requirement-next` | `/requirement:next` |
| `requirement-status` | `/requirement:status` |
| `code-review` | `/code-review` |
| `note` | `/note` |

## 注意事项

- 不要让 `AGENTS.md` 变成巨型 CLAUDE 配置。
- 工具配置变化时，优先更新适配文档，而不是改核心流程。
- 如果通过插件加载了 Skills/Commands/Hooks，不要再手工完整复制同一批能力，避免重复触发。
