"""
File for storing the data to be used later when conducting the sync
The argument(s) are stored using the store data function to the ~.tasksyncer/data directory
"""
import click

from storage import load_data, store_data


@click.group('set')
@click.option('--version', default='default')
@click.pass_context
def set_data(ctx, version):
    """
    Click group for this file
    """
    ctx.ensure_object(dict)
    ctx.obj['version'] = version
    ctx.obj['data'] = load_data()
    

def save_data(ctx, key, value):
    data = ctx.obj['data']
    version = ctx.obj['version']
    try:
        data[version][key] = value
    except KeyError:
        data[version] = {key: value}
    store_data(data)


@set_data.command('hostname')
@click.argument('hostname')
@click.pass_context
def set_hostname(ctx, hostname):
    save_data(ctx, 'hostname', hostname)


@set_data.command('project')
@click.argument('project')
@click.pass_context
def set_project(ctx, project):
    save_data(ctx, 'project', project)
    
    
@set_data.command('polarion_url')
@click.argument('polarion_url')
@click.pass_context
def set_polarion_url(ctx, polarion_url):
    save_data(ctx, 'polarion_url', polarion_url)
    
    
@set_data.command('column_names')
@click.argument('column_names', nargs=-1)
@click.pass_context
def set_column_names(ctx, column_names):
    save_data(ctx, 'column_names', column_names)
    
    
@set_data.command('token1')
@click.argument('token1')
@click.pass_context
def set_token1(ctx, token1):
    save_data(ctx, 'token1', token1)
    
    
@set_data.command('token2')
@click.argument('token2')
@click.pass_context
def set_token2(ctx, token2):
    save_data(ctx, 'token2', token2)
    
    
@set_data.command('namespace')
@click.argument('namespace')
@click.pass_context
def set_namespace(ctx, namespace):
    save_data(ctx, 'namespace', namespace)
    
    
@set_data.command('column_mapping_names')
@click.argument('column_mapping_names', nargs=-1)
@click.pass_context
def set_column_mapping_names(ctx, column_mapping_names):
    save_data(ctx, 'column_mapping_names', column_mapping_names)
    
    
@set_data.command('column_mapping_trello')
@click.argument('column_mapping_trello', nargs=-1)
@click.pass_context
def set_column_mapping_trello(ctx, column_mapping_trello):
    save_data(ctx, 'column_mapping_trello', column_mapping_trello)    
    
    
@set_data.command('polarion_project')
@click.argument('polarion_project')
@click.pass_context
def set_polarion_project(ctx, polarion_project):
    save_data(ctx, 'polarion_project', polarion_project)    
    
    
@set_data.command('username')
@click.argument('username')
@click.pass_context
def set_username(ctx, username):
    save_data(ctx, 'username', username)    
    
    
@set_data.command('password')
@click.argument('password')
@click.pass_context
def set_password(ctx, password):
    save_data(ctx, 'password', password)    
    
    
@set_data.command('test_cycle')
@click.argument('test_cycle')
@click.pass_context
def set_test_cycle(ctx, test_cycle):
    save_data(ctx, 'test_cycle', test_cycle)    
    
    
@set_data.command('ignore_titles')
@click.argument('ignore_titles', nargs=-1)
@click.pass_context
def set_ignore_titles(ctx, ignore_titles):
    save_data(ctx, 'ignore_titles', ignore_titles)
