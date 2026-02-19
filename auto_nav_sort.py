"""
MkDocs 钩子：自动排序导航
"""

import re
from pathlib import Path
from pypinyin import lazy_pinyin


def on_config(config, **kwargs):
    """
    在配置加载后自动修改导航
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
    def sort_key(note):
        title = note['title']
        # 将中文转换为拼音，英文保持不变
        pinyin = ''.join(lazy_pinyin(title)).lower()
        return pinyin

    notes.sort(key=sort_key)

    # 构建新的导航结构
    notes_nav = ['notes/index.md']  # 笔记首页
    for note in notes:
        notes_nav.append({note['title']: note['path']})

    # 更新配置中的导航
    config['nav'] = [
        {'首页': 'index.md'},
        {'笔记': notes_nav},
        {'标签': 'tags.md'}
    ]

    print(f"[Auto Nav Sort] 已自动排序 {len(notes)} 篇笔记")
    return config

