"""
A collection of functions for storing data in the fail
the location of the saved data is ~/.tasksyncer-client/data
"""

from json import JSONDecodeError
import json
from pathlib import Path


def store_data(data):
    """
    Stores the data (dict) in the json format
    """
    file = open(f"{str(Path.home())}/.tasksyncer-client/data", 'w')
    json.dump(data, file)


def load_data():
    """
    The data are stored in the json format. This function extracts the data from
    the json and returns them as a dict
    """
    data = {}
    with open(f"{str(Path.home())}/.tasksyncer-client/data", 'r') as data_file:
        try:
            data = json.load(data_file)
        except JSONDecodeError:
            pass
    return data


def data_dir():
    """
    The data are stored in the ~/.tasksyncer-client/file
    If the file or directory does not exist, creates the new one
    """
    path = f"{str(Path.home())}/.tasksyncer-client"
    Path(path).mkdir(parents=True, exist_ok=True)
    filepath = f"{path}/data"
    if not Path(filepath).is_file():
        open(filepath, 'w')
