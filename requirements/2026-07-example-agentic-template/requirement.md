# Requirement: Agentic Engineering 模板 MVP

## 元信息

- 需求 ID：`2026-07-example-agentic-template`
- 相关项目：`example-project`
- 当前阶段：验收与知识沉淀
- 负责人：示例负责人
- 创建日期：2026-07-02

## 原始输入

> 建设一个工具中立、基于 Git 仓库、可被新项目直接 fork 使用的 Agentic Engineering 研发规范模板。

## 业务目标

- 让新项目 fork 后即可获得 AI 协同研发骨架。
- 将团队规范、上下文管理、需求生命周期、质量门禁、知识沉淀机制放入仓库。
- 保持工具中立，通过适配层支持 Claude Code、Codex、WorkBuddy 等工具。

## 范围

### In Scope

- 轻量 `AGENTS.md`。
- `context/` 三层知识结构。
- `requirements/` 需求生命周期模板。
- 基础 Skill、Agent、command 说明。
- 工具适配说明。
- 人工 eval 用例。

### Out of Scope

- 自动化插件市场。
- 数据库或向量检索。
- 完整 CI 执行框架。
- 真实业务项目知识。

## 关键事实

| 事实 | 标注 | 来源 |
| --- | --- | --- |
| 模板必须工具中立 | 用户输入 | 原始计划 |
| AGENTS.md 应保持轻量入口 | 来源 | `AGENTS.md`、`context/experience/common-pitfalls.md` |
| 需求生命周期采用 6 阶段 | 用户输入 | 原始计划 |

## 待确认问题

- fork 后是否需要发布为 GitHub Template Repository：待确认。
- 是否需要后续补充自动化初始化脚本：待确认。

## 验收标准

- 仓库结构完整。
- 新项目能通过 README 启动。
- AI 能通过 AGENTS.md 找到上下文入口。
- 示例需求完整覆盖需求、设计、计划、测试、评审、验收、笔记。

## AI 使用说明

- 是否计划使用 AI 辅助：是。
- AI 负责：根据参考资料整理模板骨架、补充规范草稿、执行结构检查。
- 人类确认点：模板定位、是否合入、是否发布为 GitHub Template Repository。

## 阶段门禁

- [x] 需求标题明确。
- [x] 业务目标明确。
- [x] 相关项目明确或标记待确认。
- [x] 关键事实均有来源、用户输入或待确认标注。
- [x] AI 参与边界明确。
