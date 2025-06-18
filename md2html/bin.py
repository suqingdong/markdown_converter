import time
import click
import loguru

from md2html import version_info, STYLES_CSS, PYGMENTS_CSS, MATHJAX_JS, MERMAID_JS
from md2html.core import MD2HTML


CONTEXT_SETTINGS = dict(
    help_option_names=['-?', '-h', '--help'],
    max_content_width=200,
)

epilog = click.style('''
\n\b
examples:
    {prog} input.md -o output.html
                   
contact:
    {author} <{author_email}>
''', fg='yellow').format(**version_info)

@click.command(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    epilog=epilog,
)
@click.argument('infile')
@click.option('-o', '--output', help='the output filename, default is stdout')
@click.option('--styles-css', help='the styles css file', default=STYLES_CSS, show_default=True)
@click.option('--pygments-css', help='the pygments css file', default=PYGMENTS_CSS, show_default=True)
@click.option('--mathjax-js', help='the mathjax js file', default=MATHJAX_JS, show_default=True)
@click.option('--mermaid-js', help='the mermaid js file', default=MERMAID_JS, show_default=True)
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
def cli(infile, output, styles_css, pygments_css, mathjax_js, mermaid_js):
    start_time = time.time()
    loguru.logger.debug(f'''Arguments:
        INPUT:\t\t{infile}
        OUTPUT:\t\t{output}
        STYLES_CSS:\t{styles_css}
        PYGMENTS_CSS:\t{pygments_css}
        MATHJAX_JS:\t{mathjax_js}
        MERMAID_JS:\t{mermaid_js}
    ''')
    md2html = MD2HTML(infile)
    html = md2html.convert(output, styles_css, pygments_css, mathjax_js, mermaid_js)
    if html:
        print(html)
    if output:
        loguru.logger.info(f'saved html to: {output}')
    loguru.logger.info(f'elapsed time: {time.time() - start_time:.2f} seconds')


def main():
    cli()


if __name__ == '__main__':
    main()
