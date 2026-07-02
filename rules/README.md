# Rules

`rules/` 是可安装、可裁剪的规则切片。`context/team/` 是团队规范的权威来源，`rules/` 面向具体工具或技术栈安装。

## 结构

```text
rules/
├── common/              # 所有项目通用
└── _language-template/  # 新技术栈规则模板
```

后续可按技术栈增加：

```text
rules/typescript/
rules/python/
rules/golang/
rules/java/
```

## 安装原则

- 始终安装 `common/`。
- 只安装当前项目实际使用的语言或框架规则。
- 复制目录时保留目录结构，不要把多个目录拍平成一个目录。
- 工具私有安装路径可以不同，但规则源头仍在本仓库。

## 维护原则

- `common/` 不放语言特定代码示例。
- 语言目录只扩展 common，不重复 common。
- 新增规则必须说明来源、适用场景和不适用场景。
- 低频、一次性、未验证规则不进入 rules。

