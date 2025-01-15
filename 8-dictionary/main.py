"""
Introduction to python dictionary datatype
"""
from typing import Dict


def main() -> None:
    def create_dictionary(key: str, value: str) -> Dict:
        return {key: value}

    print(create_dictionary('fruit', 'Orange'))


if __name__ == '__main__':
    main()
