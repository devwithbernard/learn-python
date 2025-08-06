"""
Learn more list features
"""

# TODO: Reversed list

def reversed_list(names: list[str]) -> list[str] | None:
    if not names:
        return None

    if len(names) == 0:
        return []

    index = len(names) - 1
    new_list: list[str] = []

    while index >= 0:
        new_list.append(names[index])
        index -= 1

    return new_list


name_list = ["Steve", "Jean", "Katherine", "Paul"]
reversed_lst = reversed_list(name_list)
print(reversed_lst)


# TODO: Unique numbers

def unique_numbers(numbers: list[int]) -> list[int]:
    """
        Return a new list containing only the unique numbers from the input list,
        preserving their original order of appearance.

        Args:
            numbers (list[int]): The list of integers which may contain duplicates.

        Returns:
            list[int]: A list containing the unique integers from `numbers`,
                       in the same order they first appeared.

        Example:
            >>> unique_numbers([1, 2, 2, 3, 4, 4, 5])
            [1, 2, 3, 4, 5]
    """

    new_list: list[int] = []

    for number in numbers:
        if number not in new_list:
            new_list.append(number)

    return new_list


numbers = [1, 2, 2, 3, 9, 9, 8, 10]
print(unique_numbers(numbers))