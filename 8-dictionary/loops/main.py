"""
Loop in dictionary
"""

from typing import Any


def main() -> None:
    person: dict[str, Any] = {
        "name": "Konan Bernard",
        "age": 28,
        "degree": "Civil Engineer",
        "sale": 15_000
    }

    def loop_through_keys(data: dict) -> None:
        for key in data:
            print(key)

    loop_through_keys(person)

    def print_key_value(data: dict) -> None:
        if data:
            for key in data:
                print(f"{key} => {data[key]}")

    print_key_value(person)

    def loop_through_values(data: dict) -> None:
        if data:
            print("Person:")
            for value in data.values():
                print(f"\t{value}")

    loop_through_values(person)

    def loop_through_items(data: dict) -> None:
        if data:
            print("Person")
            for key, value in data.items():
                print(f"\t{key.capitalize()}: {value}")

    loop_through_items(person)


if __name__ == '__main__':
    main()
