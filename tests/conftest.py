import pytest
import json

@pytest.fixture()
def data():
    return {'default': {'hostname': 'DEFAULT_HOSTNAME',
                        'project': 'DEFAULT_PROJECT',
                        'column_names': ['COL_ONE', 'COL_TWO'],
                        'token1': 'TOKEN1',
                        'token2': 'TOKEN2',
                        'namespace': 'NAMESPACE',
                        'column_mapping_names': ['COL_ONE', 'COL_TWO'],
                        'column_mapping_trello': ['FFF000', 'AAA999'],
                        'polarion_url': 'POLARION',
                        'polarion_project': 'POLARION_PROJECT',
                        'username': 'USERNAME',
                        'password': 'PASSWORD',
                        'test_cycle': 'TESTCYCLE',
                        'ignore_titles': ['IGNORE']},
            'devel': {'project': 'PROJECT',
                      'hostname': 'HOSTNAME'}
            }


@pytest.fixture()
def data_json(data):
    return json.dumps(data)


@pytest.fixture()
def default_url_new_project():
    return "DEFAULT_HOSTNAME/v1/project/PROJECT/create"


@pytest.fixture()
def default_params_new_project():
    return {"columnNames": ['COL_ONE', 'COL_TWO']}


@pytest.fixture()
def devel_url_trello():
    return 'HOSTNAME/v1/service/trello/project/PROJECT/connect/namespace/NAMESPACE'


@pytest.fixture()
def devel_params_trello(data):
    return {'firstLoginCredential': "TOKEN1", "secondLoginCredential": "TOKEN2",
            'columnNames': data['default']['column_mapping_names'],
            'columnMapping': data['default']['column_mapping_trello']}


@pytest.fixture()
def devel_url_polarion(data):
    return f"{data['devel']['hostname']}/v1/project/PROJECT/polarion/"\
           f"{data['default']['polarion_project']}"


@pytest.fixture()
def devel_params_polarion(data):
    return {'url': 'OVERRIDDEN_URL',
            'username': data['default']['username'],
            'password': data['default']['password'],
            'testCycle': 'OVERRIDDEN_TC',
            # TODO in TASKSYNCER: Why the snake_case???
            'ignore_titles': data['default']['ignore_titles']}
