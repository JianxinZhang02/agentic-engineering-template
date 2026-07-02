# Command: requirement-new

## 目的

创建一个新需求目录，并初始化生命周期文件。

## 输入

- 需求标题。
- 相关项目。
- 原始需求描述。

## 执行步骤

1. 确认需求标题和相关项目。
2. 生成需求 ID，格式为 `YYYY-MM-short-name`。
3. 从 `requirements/_template/` 复制目录。
4. 将原始输入写入 `requirement.md` 和 `notes.md`。
5. 读取 `context/INDEX.md` 和相关项目索引。
6. 输出 3-5 条关键确认点。

## 完成标准

- 需求目录存在。
- 7 个生命周期文件存在。
- 原始输入已保留。
- 当前阶段为“需求启动”。

