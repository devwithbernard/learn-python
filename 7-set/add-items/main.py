"""
Add set items
"""

from typing import Iterable


def main() -> None:
    fruits: set[str] = {"Apple", "Pineapple", "Lemon"}
    other_fruits: set[str] = {"Banana", "Cherry"}

    def add_items(sequence: set[str], item: str) -> set[str]:
        if item and item is not None:
            sequence.add(item)
            return sequence
        raise ValueError("item is not valid")

    new_fruits: set[str] = add_items(fruits, 'Mango')
    print("New fruits: ", new_fruits)

    def update_set(set1: set[str], set2: set[str]) -> set[str]:
        if isinstance(set1, set) and isinstance(set2, set):
            set1.update(set2)
            return set1
        raise ValueError('args are not instances of set')

    updated_fruits: set[str] = update_set(fruits, other_fruits)
    print(updated_fruits)

    def add_iterable_to_set(original_set: set[str], iterable: Iterable) -> set:
        original_set.update(iterable)
        return original_set

    updated_fruits: set[str] = add_iterable_to_set(fruits, ['Orange', 'Strawberry'])
    print(updated_fruits)


if __name__ == '__main__':
    main()
