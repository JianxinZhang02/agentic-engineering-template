# Eval Metrics

Eval 是模板行为的回归测试。每次修改 `AGENTS.md`、`prompts/`、`skills/`、`commands/`、`rules/` 或 `hooks/` 后，都应复跑相关用例。

## Eval 类型

- Capability Eval：验证新增能力能否完成。
- Regression Eval：验证旧能力没有退化。
- Safety Eval：验证安全和责任边界。
- Knowledge Eval：验证是否基于上下文而非编造。

## Grader 类型

| 类型 | 适用 |
| --- | --- |
| Code-based | 文件是否存在、命令是否通过、格式是否匹配 |
| Model-based | 需求质量、设计质量、审查质量 |
| Human | 高风险业务判断、安全确认、最终验收 |

## 最小记录格式

```text
Eval：
日期：
模板版本：
输入：
预期：
结果：
失败原因：
后续动作：
```

## 通过率建议

- 核心生命周期用例必须 100% 通过。
- 安全和事实门禁不得降级。
- 新增工具必须至少有 1 个正向用例和 1 个失败用例。

