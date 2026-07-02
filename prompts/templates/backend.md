# Backend Template Prompt

适用于后端、API、任务、数据库、消息队列和服务集成任务。

## 开始前读取

- 项目 `architecture.md`
- 项目 `api-contracts.md`
- 项目 `business-context.md`
- `context/team/testing-standard.md`
- 涉及安全时读取 `context/team/ai-policy.md` 和 `skills/security-review/SKILL.md`

## 工作规则

- 明确输入、输出、错误码、幂等性和兼容性。
- 不凭猜测修改数据契约。
- 数据迁移和兼容性改动必须说明回滚方式。
- 外部服务调用必须说明超时、重试、降级和观测。
- 涉及敏感数据必须执行安全审查。

## 输出

- 契约变更。
- 数据影响。
- 部署和回滚风险。
- 测试和监控建议。

