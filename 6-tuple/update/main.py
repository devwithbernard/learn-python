"""
Update tuples
"""


def main() -> None:
    fruits: tuple[str, ...] = ('Mango', 'Apple', 'Banana')

    def change_tuple_value(sequence: tuple[str, ...], old_item: str, new_item: str) -> tuple[str, ...]:
        """
        Returns a tuple of items in which an old item is replaced with new item if it exists
        or add if it doesn't
        :param sequence: sequence of items
        :param old_item: item that must be changed
        :param new_item: item that replace the old item
        :return:A sequence of items after replacement or adding new item
        """
        if old_item in sequence:
            sequence_into_list: list[str] = list(sequence)
            old_item_index: int = sequence_into_list.index(old_item)
            new_sequence_list: list[str] = sequence_into_list[:old_item_index] + [new_item] + sequence_into_list[old_item_index + 1:]
            return tuple(new_sequence_list)

        sequence_list: list[str] = list(sequence)
        sequence_list.append(old_item)
        return tuple(sequence_list)

    print(f"""{change_tuple_value(fruits, 'Ananas', 'Lemon')}""")


if __name__ == '__main__':
    main()
