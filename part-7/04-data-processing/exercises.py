"""
Data process: Exercise
"""

# TODO: Handling JSON files
import json


def print_persons(filename: str) -> None:
    with open(filename) as file:
        data = file.read()

    students = json.loads(data)

    for std in students:
        print(f"{std['name']} {std['age']} years({','.join(std['hobbies'])})")


print_persons("files/students.json")