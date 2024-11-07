"""
Working with numbers
"""
from typing import List


def add(numbers: List[int]) -> int:
    """
    Adds two numbers
    :param numbers: list of numbers
    :return: sum of numbers
    """
    cumulate_number: int = 0

    for number in numbers:
        cumulate_number += number

    return cumulate_number


def minus(x: int, y: int) -> int:
    """
    Subtracts two numbers
    :param x: first number
    :param y: second number
    :return: difference of numbers
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers
    :param x: first number
    :param y: second number
    :return: multiplication of two numbers
    """
    return x * y


def main() -> None:
    # Calculate sum
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(add(numbers))

    # Calculate minus
    print(minus(5, 9))

    # Multiply two number
    x: int = 7
    y: int = 9
    print(f" {x} x {y} = {multiply(x, y)}")


if __name__ == '__main__':
    main()
