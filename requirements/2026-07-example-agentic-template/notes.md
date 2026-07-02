# Notes: Agentic Engineering 模板 MVP

## 原始记录

- 用户要求按照计划书直接实现模板仓库。
- 模板来源于团队对 Agentic Engineering 研发规范的整理和实践计划。
- 模板应以 Git 仓库文本资产为核心，不绑定单一工具。

## 上下文收集记录

| 时间 | 读取内容 | 结论 |
| --- | --- | --- |
| 2026-07-02 | 原始计划书 | 需要创建完整模板仓库 |
| 2026-07-02 | 对话和 PDF 摘要 | 目标是工具中立、可 fork 的研发规范仓库 |

## 待确认问题

- 是否将该目录初始化为独立 Git 仓库。
- 是否发布为 GitHub Template Repository。
- 是否补充自动化初始化脚本。

## 待沉淀知识

| 知识 | 建议位置 | 原因 |
| --- | --- | --- |
| 示例需求应保留完整生命周期产物 | `context/project/example-project/experience.md` | 方便新人照着跑 |
| AGENTS.md 不应膨胀 | `context/experience/common-pitfalls.md` | 避免上下文过载 |

## AI 错误和纠偏

| 场景 | 错误 | 缺失知识 | 修正方式 | 建议沉淀 |
| --- | --- | --- | --- | --- |
| 模板发布前检查 | 示例 notes 曾引用本地原始资料文件 | 模板分发时不能依赖本地资料 | 改为通用来源描述 | `context/experience/common-pitfalls.md` |

## 不沉淀信息

| 信息 | 原因 |
| --- | --- |
| 本次命令行创建目录的细节 | 一次性执行信息 |
