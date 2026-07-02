# Project Context

每个项目应在本目录下拥有一个独立知识库，例如：

```text
context/project/payment-service/
├── INDEX.md
├── architecture.md
├── business-context.md
├── api-contracts.md
├── domain-glossary.md
└── experience.md
```

创建新项目知识库时，复制 `_template/` 并改名。

## 维护要求

- 每个项目目录必须有 `INDEX.md`。
- 业务规则、接口契约、架构约束必须标注来源或负责人。
- 需求中产生的新知识先进入 `requirements/{id}/notes.md`，验收后再沉淀到项目知识库。

