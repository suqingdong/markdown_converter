import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
version_info = json.load(BASE_DIR.joinpath('version.json').open())

__version__ = version_info['version']

TEMPLATE_DIR = BASE_DIR.joinpath('template')

PYGMENTS_CSS = TEMPLATE_DIR.joinpath('pygments.css')
STYLES_CSS = TEMPLATE_DIR.joinpath('styles.css')

MATHJAX_JS = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js'
MERMAID_JS ='https://cdnjs.cloudflare.com/ajax/libs/mermaid/11.6.0/mermaid.min.js'
