# Command: context-garden

## 目的

定期整理 `context/`，修复过时知识、重复规则和缺失索引，防止文档腐化。

## 输入

- 目标目录：`context/team/`、`context/project/{project}/` 或 `context/experience/`。

## 执行步骤

1. 读取目标目录 `INDEX.md`。
2. 检查链接、更新时间、来源和待确认项。
3. 找出重复、过时、低价值、缺少来源的知识。
4. 给出保留、合并、删除、待确认清单。
5. 必要时更新索引。

## 输出

```text
保留：
合并：
删除：
待确认：
索引更新：
需要负责人 review：
```

