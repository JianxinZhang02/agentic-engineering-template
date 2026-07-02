# Command: tool-stocktake

## 目的

盘点 Skill、Agent、Command、Rule、Hook、Prompt 和 MCP 配置的质量与价值。

## 输入

- 目标范围：全仓库或指定目录。

## 执行步骤

1. 读取 `skills/tool-governance/SKILL.md`。
2. 盘点相关工具文件。
3. 检查触发场景、输出格式、索引更新、eval 覆盖。
4. 输出保留、合并、降级、删除、需要验证清单。

## 完成标准

- 不只看数量，要判断实际价值。
- 低频或重复工具应建议合并或删除。
- 每个保留项应有明确适用场景。

