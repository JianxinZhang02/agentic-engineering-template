# Agentic Engineering Template

这是一个工具中立的 Agentic Engineering Git 仓库模板。它把 AI 协作研发需要的上下文、规范、需求生命周期、质量门禁、知识沉淀和工具适配方式沉淀为可版本化的 Markdown 文件。

本模板不绑定 Claude Code、Codex、WorkBuddy 或其他单一工具。核心资产是仓库中的文本规范；不同工具只需要在 `adapters/` 中做轻量映射。

## 适用场景

- 新项目希望从第一天就具备 AI Agent 协同研发的规范。
- 团队希望把隐性研发经验沉淀为 AI 和人都能读取的公共知识。
- 现有项目希望逐步引入需求生命周期、代码审查、测试验收和知识复利机制。
- 多个 AI 工具并存，但团队希望使用同一套研发规则。

## 最小启动路径

1. fork 本仓库。
2. 修改 `README.md` 和 `AGENTS.md` 中的项目描述。
3. 在 `context/project/` 下复制 `_template/`，创建你的项目目录。
4. 复制 `requirements/_template/` 创建第一个需求目录。
5. 让 AI 按 `AGENTS.md` 推进需求生命周期。
6. 需求完成后，将 `notes.md` 中的经验沉淀到 `context/`。

## 仓库结构

```text
.
├── AGENTS.md              # AI Agent 的入口索引和硬规则
├── context/               # 团队和项目公共记忆
├── requirements/          # 需求生命周期工作区
├── templates/             # 需求、设计、测试、知识条目的模板
├── prompts/               # 分层 Prompt：核心、工作流、技术栈、任务提示
├── rules/                 # 可安装规则切片：common + 技术栈扩展
├── skills/                # 工具中立的专业能力包说明
├── agents/                # 角色化审查者和辅助者定义
├── agent-projects/        # 长期 AI 辅助工程计划
├── commands/              # 标准动作说明
├── hooks/                 # Hook 设计和跨工具自动化约束
├── mcp-configs/           # MCP 集成样例和风险边界
├── adapters/              # Claude Code、Codex、WorkBuddy 等工具适配
├── eval/                  # 人工可执行的规范回归用例和指标
├── docs/                  # onboarding、运行模型、维护说明
├── schemas/               # 后续机械化校验的轻量 schema
├── scripts/               # 轻量健康检查脚本
└── core_skills.json       # 核心 Skill 清单
```

## 第一天要改什么

- `AGENTS.md`：把项目身份、默认项目名、工具约束改成你的团队语境。
- `context/team/`：确认 Git、评审、测试和知识管理规范是否符合团队现状。
- `context/team/ai-policy.md`：确认 AI 使用、责任边界和安全边界。
- `context/project/_template/`：复制为真实项目目录，例如 `context/project/payment-service/`。
- `requirements/_template/`：复制为第一个真实需求目录，例如 `requirements/2026-07-login-audit/`。
- `adapters/`：选择你实际使用的工具，按文档配置入口。
- `prompts/templates/` 和 `rules/`：按你的项目技术栈补充或裁剪。
- 运行 `python scripts/doctor.py`：确认模板复制后没有缺文件、坏 JSON 或本地资料残留。

## 如何启动第一个需求

1. 复制 `requirements/_template/` 到一个新目录。
2. 在 `requirement.md` 写入原始需求和业务目标。
3. 要求 AI 先读取 `AGENTS.md`、`context/INDEX.md` 和相关项目的 `INDEX.md`。
4. 让 AI 输出 3-5 条关键确认点，不要直接生成长文档。
5. 人类确认后，再让 AI 填写需求、设计、实现计划和测试计划。
6. 阶段切换前使用 `commands/requirement-next.md` 的门禁清单检查。

## 如何沉淀项目知识

- 需求推进中，所有临时发现先记入该需求的 `notes.md`。
- 需求验收时，使用 `skills/knowledge-curation/SKILL.md` 进行整理。
- 重复出现、AI 易错、跨会话需要保留的信息，沉淀到 `context/project/{project}/` 或 `context/experience/`。
- 偶发信息、一次性讨论、没有复用价值的细节，不进入长期知识库。

## 如何适配工具

- Claude Code：参考 `adapters/claude-code.md`。
- Codex：参考 `adapters/codex.md`。
- WorkBuddy：参考 `adapters/workbuddy.md`。

适配层可以变化，但所有工具都必须遵守同一套 `AGENTS.md`、`context/` 和 `requirements/` 规则。

## 如何让模板持续变强

- 新增规则前，先阅读 `context/team/tooling-governance.md`，判断是否真的应该工具化。
- 修改 Prompt、Skill、Command、Hook 后，补充或复跑 `eval/`。
- 每月按 `docs/template-maintenance.md` 做一次规范瘦身。
- 用 `context/team/metrics.md` 记录门禁拦截、知识沉淀和工具使用情况。
- 涉及安全、权限、敏感数据时，按 `skills/security-review/SKILL.md` 执行安全审查。
- 长期迁移、清理、现代化、质量治理类工作，放入 `agent-projects/`，不要塞进单个需求目录。
- 修改通用 Prompt 或核心 Skill 后，使用 `eval/tasks/` 增加可复现任务，并运行 `python scripts/doctor.py`。

## 第一版完成定义

- fork 后能在 30 分钟内启动第一个需求。
- AI 能通过 `AGENTS.md` 找到上下文入口。
- 需求、设计、实现、测试、验收有可追溯产物。
- 代码审查和测试记录有统一格式。
- 需求结束后能产生至少一条可复用知识或明确说明无沉淀项。
- `eval/` 中的人工用例能够验证模板可用。
- 核心责任边界、提示词分层、规则切片、Hook/MCP 边界和评估指标有明确入口。
