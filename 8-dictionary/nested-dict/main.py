"""
Nested Dictionary
"""
import requests
from requests import Response
from typing import Union


def get_users(endpoint: str) -> Union[Response, list[dict]]:
    try:
        response: Response = requests.get(endpoint).json()
        for user in response:
            yield user
    except requests.HTTPError as http_error:
        print(f"Some errors occur while fetching data: {http_error.__str__()}")


def print_nested_dict(d, parent_key=""):
    """Recursively prints keys and values from a nested dictionary in dotted notation."""
    for key, value in d.items():
        new_key = f"{parent_key}.{key}" if parent_key else key  # Append parent key if exists

        if isinstance(value, dict):
            print_nested_dict(value, new_key)  # Recursively process nested dict
        else:
            print(f"{new_key}: {value}")  # Print key in dotted format with value


def main() -> None:
    users: Union[Response | list[dict]] = get_users("https://jsonplaceholder.typicode.com/users")
    for user in users:
        print_nested_dict(user)
        print("-" * 50)


if __name__ == '__main__':
    main()
