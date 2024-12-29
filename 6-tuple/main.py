"""
In Python, tuples are immutable sequences commonly used for grouping data.
"""


def main() -> None:
    fruits: tuple[str, ...] = ('Apple', 'Banana', 'Cherry', 'Strawberry')

    def print_tuple(sequence: tuple) -> None:
        print(f"""
        type of sequence => {type(sequence).__name__}
        sequence => {sequence}
        """)

    print_tuple(fruits)

    def tuple_items(sequence: tuple[str, ...]) -> tuple[str, ...]:
        first_tuple, second_tuple, *rest = sequence
        last_tuple = sequence[-1]

        return first_tuple, second_tuple, last_tuple

    print(f"""tuple items => {tuple_items(fruits)}""")

    def duplicate_items(sequence: tuple[str, ...]) -> list[tuple[str, int]]:
        counts: dict = {item: sequence.count(item) for item in set(sequence)}
        duplicate_items: list[tuple[str, int]] = [
            (item, count) for item, count in counts.items() if count > 1
        ]
        duplicate_items.sort(key=lambda x: x[0], reverse=False)
        return duplicate_items

    print(duplicate_items(fruits + ('Apple', 'Banana', 'Cherry', 'Apple')))


if __name__ == '__main__':
    main()
