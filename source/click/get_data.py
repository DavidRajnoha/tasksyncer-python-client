from source import click

from source.storage import load_data


@click.group("get")
def get_data():
    pass


@get_data.command('data')
def show_data():
    """
    prints the stored data
    """
    data = load_data()
    print(data)
