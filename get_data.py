import click

from storage import load_data, store_data


@click.group("get")
def get_data():
    pass


@get_data.command('data')
def show_data():
    data = load_data()
    print(data)
