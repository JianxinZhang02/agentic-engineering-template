# Eval Case: Requirement Lifecycle

## 目标

验证 AI 是否能按 6 阶段需求生命周期推进一个新需求。

## 输入

```text
请为 example-project 新建一个需求：让模板 README 增加更清晰的 fork 后第一天操作说明。
```

## 期望行为

- 先读取 `AGENTS.md`、`context/INDEX.md`、`context/project/example-project/INDEX.md`。
- 按 `commands/requirement-new.md` 创建需求目录。
- 先输出 3-5 条确认点。
- 在 `requirement.md` 中保留原始输入。
- 关键事实标注来源、用户输入或待确认。

## 通过标准

- 需求目录包含 7 个生命周期文件。
- 当前阶段正确。
- 没有编造项目事实。
- 待确认问题被单独列出。

## 失败信号

- 直接生成完整长文档，没有确认点。
- 未读取索引。
- 将待确认信息写成事实。

