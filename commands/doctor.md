# Command: doctor

## 目的

检查模板仓库是否处于可使用状态。

## 推荐执行

```bash
python scripts/doctor.py
```

## 检查项

- 根目录是否存在 `README.md`、`AGENTS.md`。
- `context/INDEX.md` 和 `context/team/INDEX.md` 是否存在。
- `requirements/_template/` 是否包含 7 个生命周期文件。
- `skills/`、`commands/`、`eval/` 是否有 README。
- 是否存在明显本地路径、密钥、私有资料残留。
- 示例需求是否仍能作为 onboarding 材料。
- `core_skills.json` 中的核心 Skill 是否存在。
- `prompts/*.tmpl.md` 与对应 `.md` 是否同步。

## 输出

```text
通过项：
警告项：
阻塞项：
建议修复：
```
