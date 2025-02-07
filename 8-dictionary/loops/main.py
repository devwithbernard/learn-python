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


if __name__ == '__main__':
    main()
