# Skill: knowledge-curation

## 触发条件

- 需求进入验收阶段。
- 用户要求整理经验、沉淀知识、更新 context。
- `notes.md` 中存在待沉淀条目。

## 输入

- 当前需求的 `notes.md`。
- 当前需求的 `requirement.md`、`design.md`、`review-report.md`、`acceptance.md`。
- `context/team/knowledge-management.md`。
- 目标项目的 `context/project/{project}/INDEX.md`。

## 输出

```text
建议沉淀：
不建议沉淀：
目标位置：
需要人类确认：
```

## 筛选标准

值得沉淀：

- 重复出现。
- AI 易错。
- 跨会话需要保留。
- 与接口、业务规则、架构约束有关。

不值得沉淀：

- 一次性信息。
- 临时日志。
- 未验证猜测。
- 无复用价值的讨论。

## 流程边界

1. 先分类 `notes.md`。
2. 为每条建议沉淀内容选择目标位置。
3. 生成知识条目草稿。
4. 标注来源需求和待确认项。
5. 提醒需要负责人 review。

## 不负责

- 不把未确认信息直接写成长期事实。
- 不替代项目负责人 review。

