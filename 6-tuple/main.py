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


if __name__ == '__main__':
    main()
