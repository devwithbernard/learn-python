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

# TODO: Lists within lists

my_list = [[1, 2, 3], [4, 1], [2, 2, 5, 1]]

print(my_list)
print(my_list[1])
print(my_list[0][2])

# Database of persons

persons: list[list[str | int | float]] = [["Betty", 10, 1.37], ["Peter", 7, 1.25], ["Emily", 32, 1.64],
                                          ["Alan", 39, 1.78]]

for person in persons:
    name: str = person[0]
    age: int = person[1]
    height: float = person[2]

    print(f"{name}: age {age} years old, height {height} meters.")

"""
Exercises
"""

# TODO: The longest string


def longest_string(strings: list[str]) -> str:
    """
     Find and return the longest string from a list of strings.

     Args:
         strings (list[str]): A list of strings to search through.

     Returns:
         str: The longest string in the list. If multiple strings have the same
              maximum length, returns the first one encountered. Returns an empty
              string if the input list is empty.

     Examples:
         >>> longest_string(["hello", "world", "python"])
         'python'
         >>> longest_string(["a", "bb", "ccc"])
         'ccc'
         >>> longest_string([])
         ''
         >>> longest_string(["same", "size"])
         'same'
     """

    if len(strings) == 0:
        return ""

    long_str = strings[0]

    for i in range(1, len(strings)):
        if len(strings[i]) > len(long_str):
            long_str = strings[i]

    return long_str


my_strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
print(longest_string(my_strings))