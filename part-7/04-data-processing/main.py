"""
Data processing
"""

# Reading csv files

import csv


def format_salary(values: list[str]) -> dict:
    keys = ['rank', 'discipline', 'phd', 'service', 'sex', 'salary']
    new_salary = {}

    for key, value in zip(keys, values):
        if key == "salary":
            value = int(value)

        new_salary[key] = value

    return new_salary


def get_salaries(filename: str) -> list[dict]:
    if not filename:
        raise FileExistsError("File not found")

    salaries = []

    try:
        with open(filename) as file:
            csv_reader = csv.reader(file)

            for index, values in enumerate(csv_reader):
                if index == 0:
                    continue

                salaries.append(format_salary(values))

    except FileNotFoundError as e:
        print(e)

    return salaries

def categorize(category: str, data: list[dict]):
    categories = None

    if data:
        categories = list(data[0].keys())

    if category.lower() not in categories:
        print("Category not exists.")
        return None

    categorized_data = {}

    for item in data:
        lower_category = category.lower()

        if item[lower_category] in categorized_data:
            categorized_data[item[lower_category]].append(item)
        else:
            categorized_data[item[lower_category]] = []

    return categorized_data


salaries = get_salaries("files/salaries.csv")
categories = categorize("Discipline", salaries)

for category, values in categories.items():
    print(category, len(values))

# Reading JSON files
import json

def load_json(filename: str):
    with open(filename) as file:
        data = file.read()

    courses = json.loads(data)
    return courses

courses = load_json("files/courses.json")

for course in courses:
    print(f"{course['abbreviation']} => {course['name']}")


# Retrieving a file from the internet
import urllib.request


def get_data(url: str):
    with urllib.request.urlopen(url) as request:
        data = json.loads(request.read())
        print(data)


get_data("https://jsonplaceholder.typicode.com/users")
