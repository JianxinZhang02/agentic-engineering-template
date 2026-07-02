# Skills

Skill 是可复用专业能力包。第一版只保留最小集合，避免过早工具化。

## 第一版 Skill

- `requirement-lifecycle/`：需求从创建到验收的流程编排。
- `context-collection/`：按索引收集上下文，避免盲读和幻觉。
- `code-review/`：按团队标准做代码审查。
- `knowledge-curation/`：把需求笔记整理成可复用知识。
- `verification-loop/`：功能完成或 PR 前执行质量验证循环。
- `security-review/`：敏感场景下执行安全审查。
- `tool-governance/`：判断是否新增/修改工具并执行 stocktake。

## 设计原则

- `SKILL.md` 只写触发条件、输入、输出、流程边界。
- 详细模板放 `templates/`。
- 不把所有规则塞进一个 Skill。
- 不为偶发任务创建 Skill。
- 新增或修改 Skill 后，必须更新 `eval/` 或说明无需更新。
- Skill 的详细资源应一跳可达，避免深层嵌套。
