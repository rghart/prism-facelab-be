import json


def load_test_json(file_path):
    f = open(f"{file_path}.json")
    return json.load(f)
