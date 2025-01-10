"""
Add set items
"""


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


if __name__ == '__main__':
    main()
