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


if __name__ == '__main__':
    main()
