from source import click

from source.storage import data_dir

from source.click.set_data import set_data
from source.click.get_data import get_data
from source.click import sync


@click.group()
def cli():
    pass


cli.add_command(set_data)
cli.add_command(get_data)
cli.add_command(sync)


if __name__ == '__main__':
    data_dir()
    cli()
