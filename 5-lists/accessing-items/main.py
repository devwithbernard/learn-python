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
            second_item: str = iterable[1-len(iterable)]
            last_item: str = iterable[-1]
            print(f"""
            Negative indexing:
              First item => {first_item}
              Second item => {second_item}
              last_item => {last_item}
            """)

    negative_indexing(fruits)


if __name__ == '__main__':
    main()
