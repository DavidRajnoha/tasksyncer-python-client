import click

from source.storage import data_dir

from source.cli.set_data import set_data
from source.cli.get_data import get_data
from source.cli.sync import sync


@click.group()
def cli():
    pass


cli.add_command(set_data)
cli.add_command(get_data)
cli.add_command(sync)


if __name__ == '__main__':
    data_dir()
    cli()
