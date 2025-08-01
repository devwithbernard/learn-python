"""
Learn more about strings and lists
"""

# TODO: Slices
message: str = "Hello world!"

print(message[3:8])
print(message[:6])

numbers: list[int] = [3, 4, 2, 4, 6, 1, 2, 4, 2]
part: list[int] = numbers[3:7]
print(part)

# TODO: More slices
my_string: str = "exemplary"
print(my_string[0:7:2])

my_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
print(my_list[6:2:-1])

# Reverse string
string: str = input("Please type in a string: ")
reversed_string: str = string[::-1]
print(reversed_string)

"""
Exercises
"""


# TODO: Everything reversed

def everything_reversed(strings: list[str]) -> list[str]:
    """
    Returns a new list with each string reversed and the list order reversed.

    This function takes a list of strings, reverses the characters in each string,
    and also reverses the order of the strings in the list.

    Args:
        strings (list[str]): A list of strings.

    Returns:
        list[str]: A new list containing the reversed strings in reversed order.

    Example:
        >>> everything_reversed(["hello", "world", "python"])
        ['nohtyp', 'dlrow', 'olleh']
    """
    new_strings: list[str] = []

    for string in strings:
        reversed_string = string[::-1]
        new_strings.append(reversed_string)

    return new_strings[::-1]


new_my_lists: list[str] = ["Hi", "there", "example", "one more"]
reversed_lists: list[str] = everything_reversed(new_my_lists)
print(reversed_lists)

