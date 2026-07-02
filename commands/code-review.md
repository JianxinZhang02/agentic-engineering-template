# Command: code-review

## 目的

按团队标准执行代码审查。

## 输入

- 当前 diff 或 PR。
- 关联需求目录。

## 执行步骤

1. 读取 `context/team/code-review-standard.md`。
2. 读取关联需求的 `requirement.md`、`design.md`、`implementation-plan.md`、`test-plan.md`。
3. 审查 diff。
4. 如果涉及敏感场景，联动 `skills/security-review/SKILL.md`。
5. 输出阻塞问题、主要问题、建议优化、已验证和未验证事项。
6. 将结论写入或建议写入 `review-report.md`。

## 完成标准

- 问题有证据。
- 未验证事项明确。
- 不包含无关重构要求。
- AI 参与和未验证风险已记录。
