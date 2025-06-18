# A user-friendly tool to convert markdown to html

## Installation

```bash
pip install md2html-python
```

## Usage

### Use in CMD

```bash
md2html --help

md2html --version

md2html input.md -o output.html

md2html input.md -o output.html --styles-css your_styles.css
```

### Use in Python

```python
from md2html.core import MD2HTML

content = '''
# Hello World

This is a test.
'''

md2html = MD2HTML(content)

md2html.convert('output.html')

html = md2html.convert()
print(html)
```

### Generate Pygments CSS

```bash
# List all available styles
pygmentize -L styles

# Generate css for given style
pygmentize -S default -f html -a .highlight > pygments.css
```

## Support Features
- [x] TOC
- [x] Code block
- [x] Inline code
- [x] Latex
- [x] Table
- [x] Image as B64
- [x] Mermaid
- [x] Checkbox
- [x] Details
- [x] Definition
- [x] Emoji
- [x] Tabbed

---

### Thanks
- [markdown](https://github.com/Python-Markdown/markdown)
- [pymdown-extensions](https://github.com/facelessuser/pymdown-extensions)
