# Adapter: Codex

## 推荐用法

Codex 可直接读取仓库文件并按 `AGENTS.md` 工作。使用时，在任务开始要求 Codex：

```text
请先阅读 AGENTS.md、context/INDEX.md 和相关项目索引，再推进当前需求。
```

## 标准动作映射

| 标准动作 | Codex 使用方式 |
| --- | --- |
| `requirement-new` | 要求 Codex 按 `commands/requirement-new.md` 创建需求 |
| `requirement-next` | 要求 Codex 按 `commands/requirement-next.md` 执行门禁 |
| `requirement-status` | 要求 Codex 汇总需求目录状态 |
| `code-review` | 要求 Codex 按 `skills/code-review/SKILL.md` 审查 |
| `note` | 要求 Codex 将发现追加到 `notes.md` |

## 工作约束

- Codex 执行代码改动前，应先读相关源码和项目上下文。
- 需求类文档应先输出确认点，再写正式内容。
- 验证结果必须记录已执行和未执行项。
- Codex 没有通用 Hook parity 时，应把 `hooks/README.md` 当作人工/指令式门禁。
- 涉及工具化变更时，先读 `skills/tool-governance/SKILL.md`。

## 注意事项

- Codex 可以直接编辑仓库，因此更要遵守“最小改动”和“不得覆盖无关变更”。
- 如果当前工作区不是 Git 仓库，应在交付说明中明确。
