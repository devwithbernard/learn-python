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

# TODO: Matrices
matrix: list[list[float]] = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


def sum_of_row(matrix: list[list[int]], row_no: int) -> int:
    """
    Calculate the sum of all elements in a specific row of a matrix.

    Args:
        matrix (list[list[int]]): A 2D list representing a matrix of integers.
        row_no (int): The index of the row to sum (0-based indexing).

    Returns:
        int: The sum of all integers in the specified row.

    Raises:
        IndexError: If row_no is greater than or equal to the number of rows
                   in the matrix.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> sum_of_row(matrix, 0)
        6
        >>> sum_of_row(matrix, 1)
        15
        >>> sum_of_row(matrix, 2)
        24
        >>> sum_of_row(matrix, 3)
        IndexError: '3' out of index
    """
    if row_no >= len(matrix):
        raise IndexError(f"'{row_no}' out of index")

    row = matrix[row_no]
    sum_row = 0

    for item in row:
        sum_row += item

    return sum_row


my_sum = sum_of_row(matrix, 1)
print(my_sum)


def sum_of_col(matrix: list[list[int]], col_no: int) -> int:
    sum_col = 0

    for row in matrix:
        sum_col += row[col_no]

    return sum_col


m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_col(m, 2)
print(my_sum)


def change_value(matrix: list[list[float]], row_no: int,
                 col_no: int, new_value: int) -> None:
    row = matrix[row_no]
    row[col_no] = new_value


m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

print(m)
change_value(m, 2, 3, 1000)
print(m)

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


# TODO: Number of matching elements

def count_matching_elements(my_matrix: list[list[int]], element: int) -> int:
    total_count = 0

    for row in my_matrix:
        total_count += row.count(element)

    return total_count


m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))

# TODO: Go
from random import choice


def generate_game_board(row: int, col: int) -> list[list[int]]:
    new_list = []

    for i in range(row):
        new_row = []
        for j in range(col):
            new_row.append(choice([0, 1, 2]))
        new_list.append(new_row)

    return new_list


def count_values(matrix: list[list[int]]) -> dict[str, int]:
    one_total = 0
    two_total = 0

    for row in matrix:
        one_total += row.count(1)
        two_total += row.count(2)

    return {
        "1": one_total,
        "2": two_total
    }


def who_won(game_board: list[list[int]]) -> int:
    count_val = count_values(game_board)

    if count_val.get("1") > count_val.get("2"):
        return 1
    elif count_val.get("1") < count_val.get("2"):
        return 2
    return 0


game_board = generate_game_board(8, 8)

winner = who_won(game_board)

if winner == 1:
    print("The player 1 won")
elif winner == 2:
    print("The player 2 won")
elif winner == 0:
    print("Both players have the same number of pieces")