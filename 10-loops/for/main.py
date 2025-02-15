"""
For loop is used to iterate over the sequence like List, String, Tuple, Dictionary and other iterable objects
"""
import typing
from typing import List


def iterate_over_list(iterable: List[str]) -> None:
    for item in iterable:
        print(item)


def print_even_number(number: int) -> None:
    if number % 2 == 0:
        print(f"\t{number}")


def even_numbers(min_number: int, max_number: int, callback: typing.Callable) -> None:
    if min_number < max_number:
        print("Even numbers: ")
        for i in range(min_number, max_number):
            callback(i)
        else:
            print("End of list")
    else:
        raise Exception(f"{min_number} must be less than {max_number}")


def iterate_over_string(text: str) -> None:
    print(f"{text}:")

    for character in text:
        print(f"\t{character}")


def capitalize(text: str) -> str:
    letter_dict: dict[str, str] = {
        chr(i): chr(i).upper() for i in range(ord('a'), ord('z') + 1)
    }

    upper_text: str = ''

    for letter in text.lower():
        if letter not in letter_dict.keys():
            upper_text += letter
            continue
        upper_text += letter_dict.get(letter)

    return upper_text


def range_function() -> None:
    numbers: range = range(10)

    print("Range of numbers: ")
    for number in numbers:
        print(number)


def decorate_func(fn):
    def wrapper(*args, **kwargs):
        print(f"---Start of {fn.__name__}---")
        result = fn(*args, **kwargs)
        print(f"---End of {fn.__name__}---")
        return result

    return wrapper


@decorate_func
def double():
    def is_even(number: int) -> bool:
        return number % 2 == 0

    double_numbers: List[int] = [number * 2 for number in range(20) if is_even(number)]

    print("Double even numbers: ")

    for double_number in double_numbers:
        print(f"\t{double_number}")


def matrix(number_of_rows: int = 1, number_of_cols: int = 1):
    if number_of_rows == 0 or number_of_cols == 0:
        raise ValueError(f"row or col must be superior to 0")

    if number_of_rows == 1 and number_of_cols == 1:
        return [number_of_rows, number_of_cols]

    nested_list: List[List[int]] = []

    for i in range(number_of_rows):
        row = []
        for j in range(number_of_cols):
            row.append(i+j)
        nested_list.append(row)

    return nested_list


@decorate_func
def iterate_matrix():
    tab = matrix(3, 3)

    print("MATRIX:")
    for row in tab:
        print(f"\t{row}")


def main() -> None:
    fruits: List[str] = ['Banana', 'Mango', 'Cherry', 'Pineapple']

    iterate_over_list(fruits)

    even_numbers(1, 30, print_even_number)

    text: str = "I love python"

    iterate_over_string(text)

    print(capitalize(text))

    range_function()

    double()

    iterate_matrix()


if __name__ == '__main__':
    main()
