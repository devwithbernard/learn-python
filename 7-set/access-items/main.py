"""
Access items in a set
"""


def main() -> None:
    fruits: set[str] = {'Banana', 'Apple', 'Cherry'}

    def access_items(sequence: set[str]) -> None:
        (first_item, second_item,*rest, last_item) = tuple(sequence)
        print(first_item, second_item, last_item)

    access_items(fruits)


if __name__ == '__main__':
    main()
