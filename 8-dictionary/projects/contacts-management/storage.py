import json


def store_data(filename: str, data: dict) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_data(filename) -> dict:
    with open(filename, 'r') as file:
        existing_data: dict = json.load(file)
        return existing_data

