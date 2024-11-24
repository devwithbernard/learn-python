"""
Change List Items
"""
from typing import Sequence, Any


def main() -> None:
    fruits: Sequence[str] = ['Mango', 'Apple', 'Lemon', 'Banana']

    def change_item_value(
            iterable: Sequence[Any],
            old_value: Any, new_value: Any) -> None:
        if old_value in iterable:
            found_index: int = iterable.index(old_value)
            iterable[found_index] = new_value
            print(f"""
                Insert {new_value} at the index : {found_index}
                new iterable: {iterable}
            """)
        else:
            print(f"{old_value} isn't ")

    change_item_value(fruits, 'Mango', 'Cherry')


if __name__ == '__main__':
    main()
