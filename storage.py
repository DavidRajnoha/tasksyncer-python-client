from json import JSONDecodeError
import json
from pathlib import Path


def store_data(data):
    file = open(f"{str(Path.home())}/.tasksyncer-client/data", 'w')
    json.dump(data, file)


def load_data():
    data = {}
    with open(f"{str(Path.home())}/.tasksyncer-client/data", 'r') as data_file:
        try:
            data = json.load(data_file)
        except JSONDecodeError:
            pass
    return data


def data_dir():
    path = f"{str(Path.home())}/.tasksyncer-client"
    Path(path).mkdir(parents=True, exist_ok=True)
    filepath = f"{path}/data"
    if not Path(filepath).is_file():
        open(filepath, 'w')
