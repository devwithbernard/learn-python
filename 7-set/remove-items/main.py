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


if __name__ == '__main__':
    main()
