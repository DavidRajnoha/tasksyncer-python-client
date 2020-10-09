"""
File for storing the data to be used later when conducting the sync
The argument(s) are stored using the store data function to the ~.tasksyncer/data directory
TODO: Unify the functions and pass what to save in argument
"""
import click

from source.storage import load_data, store_data

ALLOWED_KEYS = ['hostname', 'project', 'polarion_url', 'column_names',
                'token1', 'token2', 'namespace', 'column_mapping_names',
                'column_mapping_trello', 'polarion_project', 'username',
                'password', 'test_cycle', 'ignore_titles']


@click.command('set')
@click.option('--version', default='default')
@click.argument('key')
@click.argument('value', nargs=-1)
def set_data(version, key, value):
    """
    Click group for this file
    """
    if key not in ALLOWED_KEYS:
        raise Exception('The key is not allowed')
    if len(value) == 1:
        value = value[0]
    save_data(load_data(), version, key, value)
    

def save_data(data, version, key, value):
    try:
        data[version][key] = value
    except KeyError:
        data[version] = {key: value}
    store_data(data)
