# Commands

本目录定义工具中立的标准动作。它们不是某个工具的 slash command 实现，而是所有工具都应能映射的动作契约。

## 第一版动作

- `requirement-new.md`：创建需求目录和初始文档。
- `requirement-next.md`：进入下一阶段前执行门禁检查。
- `requirement-status.md`：查看当前需求状态。
- `code-review.md`：执行代码审查。
- `note.md`：记录过程笔记。
- `verify.md`：执行验证循环。
- `security-review.md`：执行安全审查。
- `context-garden.md`：整理和修复过时上下文。
- `tool-stocktake.md`：盘点 Skill、Agent、Command、Rule、Hook。
- `doctor.md`：检查模板仓库是否可用。

## 适配方式

- Claude Code 可映射为 slash command。
- Codex 可映射为提示词或任务说明。
- WorkBuddy 可映射为按钮、表单或自然语言入口。

## 设计约束

- Command 只做预检和委托，不复制 Skill 的完整逻辑。
- Command 应控制在短小范围内，方便不同工具映射。
- 如果命令开始承载复杂知识，应下沉到 Skill。
