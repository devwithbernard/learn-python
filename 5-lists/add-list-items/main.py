"""
Add List Items
"""
import copy

fruits: list[str] = ['Apple', 'Cherry']


def append_item(iterable: list[str]) -> None:
    # Append item at the end of the list
    fruit: str = input("Enter a name of fruit: ")
    if fruit and fruit.capitalize() not in iterable:
        iterable.append(fruit)
        print(f"'{fruit}' has been added to list.")
    else:
        print("not allowed or fruit is in fruit's list")


def insert_items(iterable: list[str]) -> None:
    #Insert item to the specified index
    item: str = input("Enter the name of fruit: ")
    if item and item.capitalize() not in iterable:
        iterable.insert(0, item)
        print("new iterable: ", iterable)
    else:
        print(f"'{item}' not allowed")


def extend_list(iterable1: list, iterable2: list) -> None:
    duplicated_iterable1: list = copy.copy(iterable1)
    duplicated_iterable1.extend(iterable2)

    print(f"""
        first iterable: {iterable1}
        second iterable: {iterable2}
        merged iterables: {duplicated_iterable1}
    """)


def main() -> None:
    append_item(fruits)
    insert_items(fruits)
    extend_list(fruits, ['Avoca'])


if __name__ == '__main__':
    main()
