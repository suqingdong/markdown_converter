import re
from pathlib import Path

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

from md2html import utils, PYGMENTS_CSS, STYLES_CSS, MATHJAX_JS, MERMAID_JS


class MD2HTML(object):
    def __init__(self, text_or_file):
        self.content = utils.get_content(text_or_file)
        self.md = self.init_md()
        self.template = utils.get_template()
        
    def init_md(self):
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
        return md
    

    def convert(
            self,
            output=None,
            styles_css=STYLES_CSS,
            pygments_css=PYGMENTS_CSS,
            mathjax_js=MATHJAX_JS,
            mermaid_js=MERMAID_JS,
        ):
        body = self.md.convert(self.content)
        body = utils.replace_mermaid(body)
        styles_css = utils.get_content(styles_css)
        pygments_css = utils.get_content(pygments_css)
        context = {
            'body': body,
            'styles_css': styles_css,
            'pygments_css': pygments_css,
            'mathjax_js': mathjax_js,
            'mermaid_js': mermaid_js,
        }
        html = self.template.render(context)

        if output:
            Path(output).write_text(html, encoding='utf-8')
        else:
            print(html)


if __name__ == '__main__':
    md2html = MD2HTML('tests/demo.md')
    md2html.convert('output.html')