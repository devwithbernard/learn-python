"""
Access items in a set
"""


def main() -> None:
    fruits: set[str] = {'Banana', 'Apple', 'Cherry'}

    def access_items(sequence: set[str]) -> None:
        (first_item, second_item, *rest, last_item) = tuple(sequence)
        print(first_item, second_item, last_item)

    access_items(fruits)

    def loop_through_set(sequence: set[str]) -> None:
        if len(sequence) == 0:
            print("Empty sequence")
        else:
            for index, item in enumerate(sequence):
                print(f"Index n°{index} => {item}")

    loop_through_set(fruits)


if __name__ == '__main__':
    main()
