# Implementation Plan: Agentic Engineering 模板 MVP

## 目标

创建一个可 fork 的 Agentic Engineering 模板仓库，包含计划书定义的第一版工程骨架。

## 任务拆分

| 步骤 | 内容 | 产物 | 状态 |
| --- | --- | --- | --- |
| 1 | 创建目录结构 | 根目录和子目录 | done |
| 2 | 编写 README 与 AGENTS | `README.md`、`AGENTS.md` | done |
| 3 | 编写 context 知识结构 | `context/` | done |
| 4 | 编写需求模板和示例需求 | `requirements/` | done |
| 5 | 编写模板、Skill、Agent、command | `templates/`、`skills/`、`agents/`、`commands/` | done |
| 6 | 编写工具适配和 eval 用例 | `adapters/`、`eval/` | done |
| 7 | 验证文件完整性 | 文件清单检查 | done |

## 变更范围

- 新增模板仓库文件。
- 不修改原始资料文件。

## 不做事项

- 不实现自动化插件。
- 不绑定某个 AI 工具。
- 不引入数据库、向量索引或 CI 框架。

## 验证方式

- 检查计划中列出的文件均存在。
- 检查示例需求包含 7 个生命周期文件。
- 检查 `AGENTS.md` 保持轻量入口。

## 追溯关系

| 需求点 | 设计点 | 实现任务 | 测试项 |
| --- | --- | --- | --- |
| 可 fork 模板 | 单仓库 Markdown 结构 | 创建完整目录和文件 | eval 需求生命周期用例 |
| 工具中立 | 核心规范与适配层分离 | `adapters/` | eval 知识沉淀用例 |
| 质量门禁 | 5 类门禁 | `commands/requirement-next.md` | eval 代码审查用例 |

