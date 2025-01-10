"""
Remove set items
"""


def main() -> None:
    fruits: [str] = {"Banana", "Mango", "Cherry"}

    def remove_set_item(sequence: set[str], item: str) -> set[str]:
        if item in sequence:
            sequence.remove(item)
            return sequence
        else:
            raise ValueError('Item not in sequence')

    new_fruits: set[str] = remove_set_item(fruits, 'Banana')
    print(new_fruits)

    def discard_set_item(sequence: set[str], item: str) -> set[str]:
        sequence.discard(item)
        return sequence

    new_fruits_after_discarded_item: set[str] = discard_set_item(fruits, 'Cherry')
    print(new_fruits_after_discarded_item)


if __name__ == '__main__':
    main()
