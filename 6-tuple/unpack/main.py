"""
Unpack Tuples
"""


def main() -> None:
    fruits: tuple[str, ...] = ('Banana', 'Cherry', 'Apple', 'Pineapple')

    def unpacking_tuple(sequence: tuple[str, ...]) -> dict[str, str]:
        (first_item, second_item, *rest) = sequence
        items: dict[str, str] = {
            "first item": first_item,
            "second item": second_item
        }
        return items

    print(unpacking_tuple(sequence=fruits))


if __name__ == '__main__':
    main()
