"""
Change List Items
"""
from copy import copy
from typing import Sequence, List, Any


def main() -> None:
    fruits: Sequence[str] = ['Mango', 'Apple', 'Lemon', 'Banana']

    def change_item_value(
            iterable: Sequence[Any],
            old_value: Any, new_value: Any) -> None:
        if old_value in iterable:
            found_index: int = iterable.index(old_value)
            iterable[found_index] = new_value
            print(f"""
                Insert {new_value} at the index : {found_index}
                new iterable: {iterable}
            """)
        else:
            print(f"{old_value} isn't ")

    def change_range_of_item_values(
            iterable: Sequence, start_index: int,
            end_index: int, range_of_items) -> None:
        """
        Change a range of items
        :param iterable: An iterable
        :param start_index: started index of replaced range
        :param end_index: ended index of replaced range
        :param range_of_items: range of items to replace
        """
        duplicated_iterable: Sequence = copy(iterable)
        if start_index <= end_index <= len(iterable):
            duplicated_iterable[start_index:end_index] = range_of_items

            print(f"""
                Last Sequence => {iterable}
                New Sequence => {duplicated_iterable}
            """)
        else:
            print("Error of indexes")
            raise IndexError("Started Index or Ended index must be ordered!")

    def insert_items(iterable: Sequence | List, insert_index: int, item: Any) -> None:
        """
        Insert items in an iterable
        :param iterable: an iterable
        :param insert_index: index of item that will be inserted
        :param item: item that will be inserted
        """
        duplicated_iterable: Sequence | List = copy(iterable)
        duplicated_iterable.insert(insert_index, item)
        print(f"""
                Last Sequence => {iterable}
                New Sequence => {duplicated_iterable}
        """)

    change_item_value(fruits, 'Mango', 'Cherry')
    change_range_of_item_values(fruits, 1, 3, ['Melon', 'Orange'])
    insert_items(fruits, 2, "Pineapple")


if __name__ == '__main__':
    main()
