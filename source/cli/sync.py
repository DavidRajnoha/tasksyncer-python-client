"""
File containing the logic of the polarion sync
"""
import click
import requests

from source.storage import load_data


@click.group("sync")
@click.pass_context
@click.option('--version', default='default')
def sync(ctx, version):
    """
    cli group
    the --version option defines which version of saved parameters
    will be used
    """
    ctx.ensure_object(dict)
    ctx.obj['version'] = version


def get_data(data, key, version='default'):
    """
    :returns the data[version][key] value or data['default'][key] if the
        former is not present
    """
    try:
        return data[version][key]
    except KeyError:
        return data['default'][key]


def new_project(data, version, project):
    """
    calls the endpoint for creating new projects in the tasksyncer
    """
    hostname = get_data(data, 'hostname', version)
    column_names = get_data(data, 'column_names', version)

    url = f"{hostname}/v1/project/{project}/create"
    params = {"columnNames": column_names}

    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(response)
        raise Exception


def trello_sync(data, version, project):
    """
    calls the endpoint for syncing issues from trello of tasksyncer
    """
    hostname = get_data(data, 'hostname', version)
    token1 = get_data(data, 'token1', version)
    token2 = get_data(data, 'token2', version)
    namespace = get_data(data, 'namespace', version)
    column_mapping_names = get_data(data, 'column_mapping_names', version)
    column_mapping_trello = get_data(data, 'column_mapping_trello', version)

    if len(column_mapping_names) != len(column_mapping_trello):
        print("Mapping must be a bijection")
        raise Exception

    url_trello = f"{hostname}/v1/service/trello/project/{project}/connect/namespace/{namespace}"
    params_trello = {"firstLoginCredential": token1, "secondLoginCredential": token2,
                     "columnNames": column_mapping_names, "columnMapping": column_mapping_trello}

    response = requests.post(url_trello, params=params_trello)
    if response.status_code != 200:
        print(response)
        raise Exception


def polarion_push(data, version, project, polarion_url, test_cycle):
    """
    calls the endpoint for pushing issues to polarion
    """
    hostname = get_data(data, 'hostname', version)
    polarion_url = polarion_url or get_data(data, 'polarion_url', version)
    polarion_project = get_data(data, 'polarion_project', version)
    username = get_data(data, 'username', version)
    password = get_data(data, 'password', version)
    test_cycle = test_cycle or get_data(data, 'test_cycle', version)
    ignore_titles = get_data(data, 'ignore_titles', version)

    url_polarion = f"{hostname}/v1/project/{project}/polarion/{polarion_project}"
    params_polarion = {"url": polarion_url, "username": username, "password": password, "testCycle": test_cycle,
                       "ignore_titles": ignore_titles}

    response = requests.post(url_polarion, params=params_polarion)
    if response.status_code != 200:
        print(response)
        raise Exception


@sync.command('polarion')
@click.option('--project')
@click.option('--polarion_url')
@click.option('--test_cycle')
@click.pass_context
def polarion(ctx, project, polarion_url, test_cycle):
    """
    Conducts the polarion sync - calls the tasksyncer endpoints for the
    new project, trello sync and the push to polarion
    """
    version = ctx.obj['version']
    data = load_data()
    try:
        project = project or get_data(data, 'project', version)
    except KeyError:
        print("The project name is not inputted and can not be found in the stored data")
        return

    try:
        new_project(data, version, project)
        trello_sync(data, version, project)
        polarion_push(data, version, project, polarion_url, test_cycle)
    except KeyError as ke:
        print(f"The {ke} was not found in the stored data")
        return
