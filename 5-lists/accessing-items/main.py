"""
Accessing to list items
"""


def main() -> None:
    fruits: list[str] = ["Pineapple", "Cherry", "Mango", "Banana"]

    def negative_indexing(iterable: list[str]) -> None:
        """
        Negative indexing
        :param iterable: list of items
        """
        if len(iterable) > 2:
            first_item: str = iterable[-len(iterable)]
            second_item: str = iterable[1 - len(iterable)]
            last_item: str = iterable[-1]
            print(f"""
            Negative indexing:
              First item => {first_item}
              Second item => {second_item}
              last_item => {last_item}
            """)

    def range_of_indexes(iterable: list[str], max_range: int, min_range: int = 0) -> None:
        """
        Range of indexes
        :param iterable: list of items
        :param min_range: min of range while indexing
        :param max_range: max of range while indexing
        """
        range_of_iterable: list[str] = []
        if (0 <= min_range < max_range) and (max_range <= len(iterable) + 1):
            range_of_iterable = iterable[min_range: max_range]
        if max_range > len(iterable) + 1:
            range_of_iterable = iterable[min_range:]
        else:
            print("Verify arguments!\nmax_range must be greater than min_range")

        print(f"Range of indexes: {range_of_iterable}")

    negative_indexing(fruits)
    range_of_indexes(fruits, 10, 2)


if __name__ == '__main__':
    main()
