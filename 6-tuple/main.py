"""
In Python, tuples are immutable sequences commonly used for grouping data.
"""


def main() -> None:
    def print_tuple() -> None:
        fruits: tuple[str,...] = ('Apple', 'Banana', 'Cherry', 'Strawberry')
        print(f"""
        type of fruits => {type(fruits).__name__}
        fruits => {fruits}
        """)

    print_tuple()


if __name__ == '__main__':
    main()
