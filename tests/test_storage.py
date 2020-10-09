from source.storage import store_data, load_data, data_dir
import pytest
from pathlib import Path


@pytest.fixture()
def filepath():
    return f"{str(Path.home())}/.tasksyncer-client/data"


def test_data_dir_not_exists(mocker, filepath):
    """
    When the file with data does not exist, a now one is
    created
    """
    mock_open = mocker.patch('source.storage.open')
    mock_mkdir = mocker.patch.object(Path, 'mkdir')
    mocker.patch.object(Path, 'is_file', return_value=False)

    data_dir()

    mock_mkdir.assert_called_once()
    mock_open.assert_called_once_with(filepath, 'w')


def test_data_dir_exists(mocker, filepath):
    """
    When the file with data exists, new one is not created
    """
    mock_open = mocker.patch('source.storage.open')
    mock_mkdir = mocker.patch.object(Path, 'mkdir')
    mocker.patch.object(Path, 'is_file', return_value=True)

    data_dir()

    mock_mkdir.assert_called_once()
    mock_open.assert_not_called()


def test_store_data(mocker, data, filepath):
    """
    Tests that the store data stores the data as expected
    """
    file = "this_is_indeed_file"
    mock_open = mocker.patch('source.storage.open', return_value=file)
    mock_json_dump = mocker.patch('source.storage.json.dump')

    store_data(data)

    mock_open.assert_called_once_with(filepath, 'w')
    mock_json_dump.assert_called_once_with(data, file)


def test_load_data_successfully(mocker, data, data_json, filepath):
    """
    Tests that the load_data function loads the data as expected, when valid
    data are in present in the file
    """
    mock_open = mocker.patch('source.storage.open', mocker.mock_open(read_data=data_json))

    loaded_data = load_data()

    assert loaded_data == data
    mock_open.assert_called_once_with(filepath, 'r')


def test_load_data_json_failed(mocker, filepath):
    """
    Tests that when the loaded string is not valid json, the empty dict is
    returned
    """
    mock_open = mocker.patch('source.storage.open', mocker.mock_open(read_data=""))

    loaded_data = load_data()

    assert loaded_data == {}
    mock_open.assert_called_once_with(filepath, 'r')
