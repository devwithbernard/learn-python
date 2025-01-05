"""
Tuple methods
"""

from typing import Any


def main() -> None:
    fruits: tuple[Any, ...] = ('Banana', 'Cherry', 'Pineapple', 'Banana')

    def count(sequence: tuple[Any, ...], item: Any) -> dict:
        return {
            "item": item,
            "count": sequence.count(item)
        }

    print(count(fruits, 'Banana'))  # {'item': 'Banana', 'count': 2}

    def index(sequence: tuple[Any, ...], item: Any) -> dict:
        if item in sequence:
            return {
                "item": item,
                "found_index": sequence.index(item)
            }
        raise Exception(f"Item not in tuple")

    print(index(fruits, 'Pineapple'))


if __name__ == '__main__':
    main()
