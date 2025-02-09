import json
import os


def save(players: list[dict]) -> None:
    with open("players.json", 'w') as file:
        json.dump(players, file, indent=4)


def load(filename="players.json") -> list[dict]:
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump([], file)

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            return data
    except (json.JSONDecodeError, ValueError):
        with open(filename, 'w') as file:
            json.dump([], file)
        return []
