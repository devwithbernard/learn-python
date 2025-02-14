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


def main() -> None:
    fruits: List[str] = ['Banana', 'Mango', 'Cherry', 'Pineapple']

    iterate_over_list(fruits)

    even_numbers(1, 30, print_even_number)


if __name__ == '__main__':
    main()
