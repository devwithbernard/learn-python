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

    def negative_indexing(sequence: tuple[str, ...]) -> str:
        first_item: str = sequence[-len(sequence)]
        second_item: str = sequence[1 - len(sequence)]
        last_item: str = sequence[-1]

        return f"""
        Access items through Negative Indexing:
        first item => {first_item}
        second item => {second_item}
        last item => {last_item}
        """

    print(negative_indexing(fruits))

    def check_if_item_exists(sequence: tuple[str, ...], item: str) -> bool:
        return item in sequence

    fruit: str = 'Mango'
    if check_if_item_exists(fruits, fruit):
        print(f"You got a {fruit} 🥭")
    else:
        print("😒😒")

    def range_of_items(sequence: tuple[str, ...], min_index: int, max_index: int) -> tuple[str, ...]:
        if min_index > max_index:
            raise ValueError("min_index should be less or equal to max_index")
        return sequence[min_index:max_index]

    print(f"""Range of items: {range_of_items(fruits, 1, 4)}""")


if __name__ == '__main__':
    main()
