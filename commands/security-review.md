# Command: security-review

## 目的

针对认证、授权、输入、上传、敏感数据、支付、外部 API 等场景执行安全审查。

## 输入

- 关联需求目录。
- 设计或 diff。

## 执行步骤

1. 读取 `context/team/ai-policy.md`。
2. 读取 `rules/common/security.md`。
3. 读取 `skills/security-review/SKILL.md`。
4. 输出风险、已验证防护和未验证风险。

## 完成标准

- 不跳过敏感场景。
- 风险有证据或明确待确认。
- 输出修复建议。

