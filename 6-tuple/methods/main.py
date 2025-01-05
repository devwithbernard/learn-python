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

    print(count(fruits, 'Banana')) # {'item': 'Banana', 'count': 2}


if __name__ == '__main__':
    main()
