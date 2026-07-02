# Skill: tool-governance

## 触发条件

- 准备新增或修改 Skill、Agent、Command、Rule、Hook、Prompt、MCP 配置。
- AI 行为反复出错，需要判断改哪一层。
- 每月工具 stocktake 和规范瘦身。

## 输入

- 变更诉求或错误案例。
- `context/team/tooling-governance.md`
- 相关 `skills/`、`agents/`、`commands/`、`rules/`、`hooks/` 文件。
- 相关 eval 用例。

## 输出

```text
问题分类：
建议改动层级：
是否工具化：
影响文件：
需要新增/更新的 eval：
不建议做的事：
```

## 决策流程

1. 判断问题是原则、能力、场景规范还是工具产物问题。
2. 判断是否满足工具化条件。
3. 选择 Command、Skill、Agent、Rule、Hook、Prompt 或 MCP。
4. 检查是否有现有能力可复用。
5. 更新索引和 eval。
6. 记录设计原因。

## Stocktake 输出

```text
保留：
合并：
降级：
删除：
需要验证：
```

