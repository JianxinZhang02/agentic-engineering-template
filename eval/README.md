# Eval

第一版 eval 是人工可执行的规范回归用例，用于验证模板仓库是否仍然可用。

## 执行频率

- 初始化模板后执行一次。
- 修改 `AGENTS.md`、`context/`、`skills/`、`commands/` 后执行相关用例。
- 每月规范瘦身后执行一次。

## 用例

- `requirement-lifecycle-case.md`
- `code-review-case.md`
- `knowledge-curation-case.md`

## 通过标准

- AI 能先读索引再工作。
- 关键事实能标注来源。
- 门禁能发现缺口。
- 输出格式稳定。
- 不把工具适配写死到核心规范。

