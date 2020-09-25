import click

from storage import data_dir

from set_data import set_data
from get_data import get_data
from sync import sync


@click.group()
def cli():
    pass


cli.add_command(set_data)
cli.add_command(get_data)
cli.add_command(sync)


if __name__ == '__main__':
    data_dir()
    cli()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
