# Schemas

`schemas/` 存放轻量 JSON Schema，用于后续把 Markdown 产物逐步机械化校验。第一版不强制自动化，但所有 schema 都可被 CI 或脚本使用。

## 文件

- `skill-metadata.schema.json`：Skill 元数据约束。
- `knowledge-entry.schema.json`：知识条目约束。
- `requirement-metadata.schema.json`：需求元信息约束。

## 使用原则

- Schema 只校验稳定结构。
- 不把开放性业务内容过度结构化。
- 自动化校验失败时应给出修复建议。

