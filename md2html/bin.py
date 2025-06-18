import click
from md2html import version_info


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])

epilog = click.style('''
\b
examples:
    {prog} input.md -o output.docx    
''')

@click.command(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
)
def cli(**kwargs):
    pass


def main():
    cli()


if __name__ == '__main__':
    main()
