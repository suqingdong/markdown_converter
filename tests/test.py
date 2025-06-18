import re

import markdown
from markdown.extensions.extra import ExtraExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension

from pymdownx.arithmatex import ArithmatexExtension
from pymdownx.highlight import HighlightExtension
from pymdownx.tasklist import TasklistExtension
from pymdownx.superfences import SuperFencesCodeExtension, fence_div_format
from pymdownx.b64 import B64Extension
from pymdownx.emoji import EmojiExtension
from pymdownx.saneheaders import SaneHeadersExtension

from pymdownx.blocks.definition import DefinitionExtension
from pymdownx.blocks.details import DetailsExtension
from pymdownx.blocks.tab import TabExtension


content = open('tests/demo.md', encoding='utf-8').read()

# 插件说明
# https://facelessuser.github.io/pymdown-extensions/

md = markdown.Markdown(extensions=[
    ExtraExtension(),
    TableExtension(),
    TocExtension(permalink=False),
    TasklistExtension(),
    ArithmatexExtension(preview=False, generic=True),
    SuperFencesCodeExtension(
        custom_fences=[
        {
            'name': 'mermaid',
            'class': 'mermaid',
            'format': fence_div_format,
        }
    ]),
    HighlightExtension(use_pygments=True, linenums=True),
    B64Extension(),
    DefinitionExtension(),
    DetailsExtension(),
    EmojiExtension(),
    SaneHeadersExtension(),
    TabExtension(),
])


# md.convertFile('tests/demo.md', 'output.html')
html = md.convert(content)
html = re.sub(r'<pre><code class="language-mermaid">(.+?)</code></pre>',
              r'<div class="mermaid">\1</div>', html, flags=re.DOTALL)

html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="monokai.css">
<style>
    body {{
        # font-family: Arial, sans-serif;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        padding: 0 10%;
        line-height: 2;
    }}
     table {{
        border-collapse: collapse;
        width: 100%;
    }}
        
        table th, table td {{
        border: 1px solid #ddd;
        padding: 6px 13px;
        text-align: left;
    }}
        
        table th {{
        background-color: #f5f5f5;
        font-weight: bold;
    }}
        
    table tr:nth-child(2n) {{
        background-color: #f8f8f8;
    }}

    blockquote {{
        border-left: 4px solid #ddd;
        padding: 0 15px;
        color: #777;
        margin: 1em 0;
    }}
        
    blockquote > :first-child {{ margin-top: 0; }}
    blockquote > :last-child {{ margin-bottom: 0; }}

    code:not(pre code):not(.codehilite code) {{
        background-color: #f5f5f5;
        color: #c7254e;
        padding: 2px 4px;
        font-size: 90%;
        border-radius: 4px;
        font-family: monospace;
    }}
    
    pre {{
        padding: 10px;
        overflow: auto;
        line-height: 1.45;
    }}

    .highlighttable .linenos {{
        width: 5px;
        padding: 0;
        margin: 0;
    }}

    .highlighttable td {{
        border: none !important;
        color: #ccc;
    }}

    .highlighttable .code {{
        padding: 0;
    }}
    
    img {{
        max-width: 100%;
    }}

    .task-list-item {{
        list-style-type: none !important;
    }}

    .task-list-item input[type="checkbox"] {{
        margin: 0 4px 0.25em -20px;
        vertical-align: middle;
    }}
</style>
</head>
<body>
{html}
</body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
<script type="module">
  import mermaid from 'https://cdnjs.cloudflare.com/ajax/libs/mermaid/11.6.0/mermaid.esm.min.mjs';
  mermaid.initialize({{ startOnLoad: true }});
</script>
'''
with open('output.html', 'w', encoding='utf-8') as out:
    out.write(html)
