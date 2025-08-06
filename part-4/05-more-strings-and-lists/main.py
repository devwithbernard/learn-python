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

# More methods for lists and strings
my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print(my_string.count('ch'))

my_list = [1, 2, 3, 1, 4, 5, 1, 6]
print(my_list.count(1))

message = "Hi there!"
print(message.replace("Hi", "Hello"))
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


# TODO: Most common character
def most_common_character(string: str) -> str:
    """
        Returns the character that appears most frequently in the given string.
        If multiple characters have the same highest frequency, the one that appears
        first in the string is returned.

        Args:
            string (str): The input string.

        Returns:
            str: The most common character.
    """

    char_counts = {}

    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    result_char = ''
    max_count = -1

    for char in string:
        if char_counts[char] > max_count:
            max_count = char_counts[char]
            result_char = char

    return result_char


first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))


# TODO: No vowels allowed


def no_vowels(string: str) -> str:
    """
    Remove all vowels from a string.

    This function removes all vowels (a, e, i, o, u, y) from the input string,
    treating both uppercase and lowercase letters as vowels. The original
    case of non-vowel characters is preserved in the output.

    Args:
        string (str): The input string from which to remove vowels.

    Returns:
        str: A new string with all vowels removed.

    Examples:
        >>> no_vowels("Hello World")
        'hll wrld'
        >>> no_vowels("Python Programming")
        'pthn prgrmmng'
        >>> no_vowels("AEIOU")
        ''
        >>> no_vowels("bcdfg")
        'bcdfg'
    """
    vowels: tuple[str, ...] = ('a', 'e', 'i', 'o', 'u', 'y')
    new_string: str = string.lower()

    for vowel in vowels:
        if vowel in new_string:
            new_string = new_string.replace(vowel, '')

    return new_string


my_string = "this is an example"
print(no_vowels(my_string))


# TODO: Grade statistics
def grade(note: float) -> float:
    match note:
        case note if note <= 14:
            return 0
        case note if note <= 17:
            return 1
        case note if note <= 20:
            return 2
        case note if note <= 23:
            return 3
        case note if note <= 27:
            return 4
        case note if note <= 30:
            return 5
        case _:
            return 0


def exercise_point(point: float):
    match point:
        case point if point < 10:
            return 0
        case point if point < 20:
            return 1
        case point if point < 30:
            return 2
        case point if point < 40:
            return 3
        case point if point < 50:
            return 4
        case point if point < 60:
            return 5
        case point if point < 70:
            return 6
        case point if point < 80:
            return 7
        case point if point < 90:
            return 8
        case point if point < 100:
            return 9
        case point if point == 100:
            return 10
        case _:
            return 0


def result(cumul_pts: list[float]) -> None:
    grades = [grade(pt) for pt in cumul_pts]

    print('Grade distribution: ')

    row = 5
    while row >= 0:
        print(f"{row}: {"*" * grades.count(row)}")
        row -= 1


def cumulate_points(points: list[tuple[int, ...]]) -> list[float] | None:
    cumulate_pts = []
    if not points:
        return

    for exam_pt, ex_pt in points:
        cumulate_pts.append(exam_pt + exercise_point(ex_pt))

    return cumulate_pts


def entry() -> None:
    exam_exercise_pts = []

    while True:
        user_input = input("Exam points and exercises completed: ").strip()

        if user_input == "":
            break

        exam_exercise_pt = tuple([int(item) for item in user_input.split(" ")])
        exam_exercise_pts.append(exam_exercise_pt)

    cuml_pts = cumulate_points(exam_exercise_pts)

    result(cuml_pts)


entry()
