# Command: verify

## 目的

在功能完成、文档规范变更或创建 PR 前执行验证循环。

## 输入

- 当前 diff。
- 关联需求目录。
- 项目构建、测试、lint 命令。

## 执行步骤

1. 读取 `skills/verification-loop/SKILL.md`。
2. 确认项目命令，不猜测。
3. 依次执行或记录构建、类型检查、lint、测试、安全快速检查、diff 自审。
4. 将结果写入或建议写入 `test-plan.md` 和 `review-report.md`。

## 输出

```text
验证结论：
已执行：
失败项：
未执行：
风险：
下一步：
```

