# Requirements

`requirements/` 是需求生命周期工作区。每个需求使用一个独立目录保存需求、设计、实现计划、测试计划、评审、验收和过程笔记。

## 命名建议

```text
requirements/YYYY-MM-short-feature-name/
```

示例：

```text
requirements/2026-07-login-audit/
```

## 目录结构

```text
requirements/{id}/
├── requirement.md
├── design.md
├── implementation-plan.md
├── test-plan.md
├── review-report.md
├── acceptance.md
└── notes.md
```

## 生命周期

1. 需求启动
2. 上下文收集
3. 需求定义
4. 方案设计
5. 实现与测试
6. 验收与知识沉淀

进入下一阶段前，必须使用 `commands/requirement-next.md` 的门禁清单。

