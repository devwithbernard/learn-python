"""
Introduction to python dictionary datatype
"""
from typing import Dict


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


if __name__ == '__main__':
    main()
