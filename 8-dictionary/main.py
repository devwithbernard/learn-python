"""
Introduction to python dictionary datatype
"""
from typing import Dict, List
from pprint import pprint
import requests


def main() -> None:
    def create_dictionary(key: str, value: str) -> Dict:
        return {key: value}

    print(create_dictionary('fruit', 'Orange'))

    def dictionary_items(dictionary: dict) -> set:
        values = set()
        for key in dictionary:
            values.add(dictionary[key])
        return values

    print(dictionary_items({'brand': "Ford", 'model': "Mustang", 'year': 1964}))

    def get_user(index: int) -> List[tuple]:
        user = requests.get(f"https://jsonplaceholder.typicode.com/users/{index}").json()

        def extract_key_value(user_dict: dict, parent_key='') -> List[tuple]:
            key_value: List[tuple] = []

            for key, value in user_dict.items():
                combined_key = f"{parent_key}.{key}" if parent_key else key

                if isinstance(value, dict):
                    key_value.extend(extract_key_value(value, combined_key))
                else:
                    key_value.append((combined_key, value))

            return key_value

        return extract_key_value(user)

    pprint(get_user(2))

    def number_of_items(data: dict) -> tuple:
        return 'Dict', f"Items: {len(data)}", f"type: {type(data).__name__}"

    print(number_of_items({'brand': "Ford", 'model': "Mustang", 'year': 1964}))


if __name__ == '__main__':
    main()
