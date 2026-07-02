# Eval Case: Knowledge Curation

## 目标

验证 AI 是否能将需求 `notes.md` 整理为可复用知识，并过滤一次性信息。

## 输入

```text
请整理 requirements/2026-07-example-agentic-template/notes.md，给出需要沉淀到 context/ 的知识。
```

## 期望行为

- 读取 `skills/knowledge-curation/SKILL.md`。
- 读取 `context/team/knowledge-management.md`。
- 区分建议沉淀和不建议沉淀。
- 为每条建议沉淀内容选择目标位置。
- 标注需要人类确认的事项。

## 通过标准

- 不把一次性执行细节沉淀为长期知识。
- 能提出目标位置。
- 能提醒负责人 review。

## 失败信号

- 把所有 notes 内容无差别写入 `context/`。
- 未标注待确认信息。
- 忘记更新相关索引。

