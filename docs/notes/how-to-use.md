---
title: 如何使用本博客
date: 2025-02-19
tags:
  - mkdocs
---

# 如何使用本博客

!!! info "文章信息"
    **发布时间**: 2025-02-19
    **标签**: mkdocs

本博客使用 MkDocs 和 Material for MkDocs 主题构建，已实现完全自动化的文章管理。你只需要创建符合格式的 Markdown 文件，所有的列表、索引和导航都会自动更新。

## 添加新笔记的步骤

### 1. 创建 Markdown 文件

在 `docs/notes/` 目录下创建一个新的 `.md` 文件，例如 `my-article.md`

建议使用小写字母和连字符作为文件名。

### 2. 添加 YAML 元数据

在文件顶部添加 YAML frontmatter（必需）：

```yaml
---
title: 你的文章标题
date: 2025-02-19
tags:
  - 标签1
  - 标签2
---
```

!!! warning "必需字段"
    - `title`: 文章标题（必需）
    - `date`: 发布日期，格式为 `YYYY-MM-DD`（必需）
    - `tags`: 标签列表（可选）

### 3. 编写内容

推荐使用以下结构：

```markdown
# 文章标题

!!! info "文章信息"
    **发布时间**: 2025-02-19
    **标签**: 标签1, 标签2

## 章节标题

你的内容...

### 子章节

更多内容...
```

### 4. 预览和构建

```bash
# 本地预览（带实时刷新）
mkdocs serve

# 构建生产版本
mkdocs build
```

就这样！所有索引会自动更新。

## 自动化功能

本博客的以下功能都是全自动的，无需手动维护：

### 🗂️ 左侧导航栏
- 自动扫描所有笔记文件
- 按标题的拼音/字母序自动排序
- 中文标题按拼音排序，英文标题按字母排序

### 📅 首页"最近更新"
- 自动显示最新的 10 篇文章
- 按发布日期倒序排列

### 🗓️ 时间归档
- 按年份和月份自动分组
- 在笔记列表页面显示

### 🏷️ 标签系统
- 自动收集所有文章的标签
- 标签可点击，跳转到该标签的所有文章
- 标签索引页自动生成

### 🔍 搜索功能
- 支持中英文全文搜索
- 自动索引所有文章内容

## 支持的 Markdown 扩展

### 代码高亮

```python
def greet(name: str) -> str:
    """问候函数"""
    return f"Hello, {name}!"

print(greet("World"))
```

### 提示框

!!! note "提示"
    这是一个提示框

!!! tip "技巧"
    这是一个技巧提示

!!! warning "警告"
    这是一个警告

!!! danger "危险"
    这是一个危险警告

### 任务列表

- [x] 已完成的任务
- [ ] 未完成的任务
- [ ] 另一个任务

### 表格

| 功能 | 说明 | 状态 |
|------|------|------|
| 自动导航 | 按拼音/字母序排序 | ✅ |
| 标签系统 | 自动收集和索引 | ✅ |
| 搜索功能 | 中英文全文搜索 | ✅ |

### 插入图片

将图片放在 `docs/images/` 目录下，然后在 Markdown 中引用：

```markdown
![图片描述](../images/example.svg)
```

效果如下：

![MkDocs 博客示例](../images/example.svg)

你也可以指定图片大小和对齐方式：

```markdown
<figure markdown>
  ![示例图片](../images/example.svg){ width="300" }
  <figcaption>图片说明文字</figcaption>
</figure>
```

!!! tip "图片建议"
    - 将图片统一放在 `docs/images/` 目录
    - 使用有意义的文件名，如 `architecture-diagram.png`
    - 支持的格式：PNG、JPG、SVG、GIF
    - SVG 格式适合图表和图标，体积小且清晰

## 文章模板

将以下内容复制到新文件中作为起点：

```markdown
---
title: 文章标题
date: 2025-02-19
tags:
  - 标签1
  - 标签2
---

# 文章标题

!!! info "文章信息"
    **发布时间**: 2025-02-19
    **标签**: 标签1, 标签2

## 引言

简要介绍文章主题...

## 主要内容

### 第一部分

内容...

### 第二部分

内容...

## 代码示例

\`\`\`python
# 示例代码
def example():
    pass
\`\`\`

## 总结

总结要点...
```

## 部署到 GitHub Pages

### 方法 1: 使用 mkdocs 命令

```bash
mkdocs gh-deploy
```

这会自动构建并推送到 `gh-pages` 分支。

### 方法 2: 手动构建

```bash
mkdocs build
# 然后将 site/ 目录的内容部署到服务器
```

## 技术栈

- **生成器**: [MkDocs](https://www.mkdocs.org/)
- **主题**: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **插件**:
  - `search`: 搜索功能
  - `tags`: 标签系统
  - `macros`: 动态内容生成
- **自定义钩子**: `auto_nav_sort.py` - 自动导航排序

## 注意事项

1. **日期格式**: 必须是 `YYYY-MM-DD`，如 `2025-02-19`
2. **文件编码**: 使用 UTF-8 编码
3. **图片路径**: 建议将图片放在 `docs/images/` 目录
4. **构建输出**: `site/` 目录已加入 `.gitignore`，不会被提交

## 常见问题

### Q: 文章没有出现在导航中？
A: 检查 YAML frontmatter 是否包含必需的 `title` 和 `date` 字段。

### Q: 标签没有显示？
A: 确保 `tags` 字段格式正确，使用 YAML 列表格式。

### Q: 中文排序不正确？
A: 自动导航排序使用 pypinyin 库，已正确处理中文拼音排序。

## 开始写作

现在你可以开始创建自己的笔记了！记住，只需要：

1. 在 `docs/notes/` 创建 `.md` 文件
2. 添加 YAML frontmatter（title 和 date）
3. 编写内容
4. 运行 `mkdocs serve` 预览

一切都会自动处理！✨
