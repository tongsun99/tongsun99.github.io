"""
MkDocs Macros 插件的自定义宏函数
用于动态生成博客内容
"""

import os
import re
from datetime import datetime
from pathlib import Path
from pypinyin import lazy_pinyin


def define_env(env):
    """
    定义可以在 Markdown 中使用的宏和变量
    """

    @env.macro
    def recent_posts(limit=10):
        """
        获取最近更新的文章列表

        Args:
            limit: 返回的文章数量，默认 10 篇

        Returns:
            str: 格式化的 Markdown 列表
        """
        docs_dir = Path(env.conf['docs_dir'])
        notes_dir = docs_dir / 'notes'

        if not notes_dir.exists():
            return "暂无文章"

        posts = []

        # 遍历所有 markdown 文件
        for md_file in notes_dir.glob('*.md'):
            if md_file.name == 'index.md':
                continue

            # 读取文件内容
            try:
                content = md_file.read_text(encoding='utf-8')

                # 提取 YAML frontmatter
                frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)

                if frontmatter_match:
                    frontmatter = frontmatter_match.group(1)

                    # 提取标题
                    title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
                    title = title_match.group(1).strip() if title_match else md_file.stem

                    # 提取日期
                    date_match = re.search(r'^date:\s*(.+)$', frontmatter, re.MULTILINE)
                    if date_match:
                        date_str = date_match.group(1).strip()
                        try:
                            date = datetime.strptime(date_str, '%Y-%m-%d')
                        except ValueError:
                            continue
                    else:
                        continue

                    # 添加到列表
                    posts.append({
                        'title': title,
                        'date': date,
                        'date_str': date_str,
                        'path': f'notes/{md_file.name}'
                    })
            except Exception as e:
                print(f"警告: 无法解析文件 {md_file}: {e}")
                continue

        # 按日期排序（从新到旧）
        posts.sort(key=lambda x: x['date'], reverse=True)

        # 限制数量
        posts = posts[:limit]

        # 生成 Markdown 列表
        if not posts:
            return "暂无文章"

        result = []
        for post in posts:
            result.append(f"- [{post['title']}]({post['path']}) - {post['date_str']}")

        return '\n'.join(result)


    @env.macro
    def posts_by_year():
        """
        按年份和月份分组的文章列表

        Returns:
            str: 格式化的 Markdown 列表
        """
        docs_dir = Path(env.conf['docs_dir'])
        notes_dir = docs_dir / 'notes'

        if not notes_dir.exists():
            return "暂无文章"

        posts = []

        # 遍历所有 markdown 文件
        for md_file in notes_dir.glob('*.md'):
            if md_file.name == 'index.md':
                continue

            try:
                content = md_file.read_text(encoding='utf-8')
                frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)

                if frontmatter_match:
                    frontmatter = frontmatter_match.group(1)

                    title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
                    title = title_match.group(1).strip() if title_match else md_file.stem

                    date_match = re.search(r'^date:\s*(.+)$', frontmatter, re.MULTILINE)
                    if date_match:
                        date_str = date_match.group(1).strip()
                        try:
                            date = datetime.strptime(date_str, '%Y-%m-%d')
                        except ValueError:
                            continue
                    else:
                        continue

                    posts.append({
                        'title': title,
                        'date': date,
                        'year': date.year,
                        'month': date.month,
                        'date_str': date_str,
                        'path': md_file.name
                    })
            except Exception as e:
                print(f"警告: 无法解析文件 {md_file}: {e}")
                continue

        # 按日期排序（从新到旧）
        posts.sort(key=lambda x: x['date'], reverse=True)

        if not posts:
            return "暂无文章"

        # 按年份和月份分组
        result = []
        current_year = None
        current_month = None

        for post in posts:
            # 新的年份
            if post['year'] != current_year:
                current_year = post['year']
                current_month = None
                result.append(f"\n### {current_year}年")

            # 新的月份
            if post['month'] != current_month:
                current_month = post['month']
                result.append(f"\n#### {current_year}年{current_month}月")

            # 添加文章
            result.append(f"- [{post['title']}]({post['path']}) - {post['date_str']}")

        return '\n'.join(result)


def on_config(config):
    """
    MkDocs 钩子函数，在配置加载后自动修改导航
    自动读取所有笔记并按拼音/字母序排序
    """
    docs_dir = Path(config['docs_dir'])
    notes_dir = docs_dir / 'notes'

    if not notes_dir.exists():
        return config

    # 收集所有笔记文件
    notes = []

    for md_file in notes_dir.glob('*.md'):
        if md_file.name == 'index.md':
            continue

        try:
            content = md_file.read_text(encoding='utf-8')
            frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)

            if frontmatter_match:
                frontmatter = frontmatter_match.group(1)
                title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)

                if title_match:
                    title = title_match.group(1).strip()
                    notes.append({
                        'title': title,
                        'path': f'notes/{md_file.name}'
                    })
        except Exception as e:
            print(f"警告: 无法解析文件 {md_file}: {e}")
            continue

    # 按拼音/字母序排序
    # 对于中文标题，使用 pypinyin 转换为拼音进行排序
    def sort_key(note):
        title = note['title']
        # 将中文转换为拼音，英文保持不变
        pinyin = ''.join(lazy_pinyin(title)).lower()
        return pinyin

    notes.sort(key=sort_key)

    # 构建新的导航结构
    notes_nav = [{'notes/index.md': 'notes/index.md'}]
    for note in notes:
        notes_nav.append({note['title']: note['path']})

    # 更新配置中的导航
    config['nav'] = [
        {'首页': 'index.md'},
        {'笔记': notes_nav},
        {'标签': 'tags.md'}
    ]

    return config

