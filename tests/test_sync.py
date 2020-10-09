from source.cli.sync import new_project, get_data, trello_sync, polarion_push


class Response:
    def __init__(self, status_code):
        self.status_code = status_code


def test_get_data(data):
    """
    gets data returns the correct value and defaults to the 'default' value
    when no version is passed
    """
    assert get_data(data, 'project') == 'DEFAULT_PROJECT'
    assert get_data(data, 'project', 'devel') == 'PROJECT'


def test_new_project(mocker, data, default_url_new_project,
                     default_params_new_project):
    """
    creating the new project calls the correct url with correct params
    """
    mocked_request = mocker.patch(
        'source.cli.sync.requests.post',
        return_value=Response(200)
    )
    new_project(data, 'default', 'PROJECT')
    mocked_request.assert_called_once_with(default_url_new_project,
                                           params=default_params_new_project)


def test_trello_sync(mocker, data, devel_url_trello,
                     devel_params_trello):
    """
    conducting the trello sync calls the correct url with correct params
    """
    mocked_request = mocker.patch(
        'source.cli.sync.requests.post',
        return_value=Response(200)
    )
    trello_sync(data, 'devel', 'PROJECT')
    mocked_request.assert_called_once_with(devel_url_trello, params=devel_params_trello)


def test_polarion_push(mocker, data, devel_url_polarion,
                       devel_params_polarion):
    """
    pushing to polarion calls the correct url with correct params
    """
    mocked_request = mocker.patch(
        'source.cli.sync.requests.post',
        return_value=Response(200)
    )
    polarion_push(data, 'devel', 'PROJECT', 'OVERRIDDEN_URL', 'OVERRIDDEN_TC')
    mocked_request.assert_called_once_with(devel_url_polarion, params=devel_params_polarion)
