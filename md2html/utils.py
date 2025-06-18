import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from md2html import TEMPLATE_DIR


def get_content(text_or_file):
    if Path(text_or_file).exists():
        with open(text_or_file, encoding='utf-8') as f:
            return f.read()
    else:
        return text_or_file


def get_template(name='default.html'):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    return env.get_template(name)


def replace_mermaid(html):
    html = re.sub(
        r'<pre><code class="language-mermaid">(.+?)</code></pre>',
        r'<div class="mermaid">\1</div>',
        html,
        flags=re.DOTALL
    )
    return html
