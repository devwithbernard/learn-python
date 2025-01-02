"""
Access to tuple items
"""


def main() -> None:
    fruits: tuple[str, ...] = ('Cherry', 'Banana', 'Pineapple', 'Apple', 'Mango')

    def access_tuple_items(sequence: tuple[str, ...]) -> str:
        first_item: str = sequence[0]
        second_item: str = sequence[1]
        last_item: str = sequence[len(sequence) - 1]

        return f"""
        first item => {first_item}
        second item => {second_item}
        last item => {last_item}
        """

    print(access_tuple_items(fruits))


if __name__ == '__main__':
    main()
