"""
Guess Number Functionality
"""

from random import randint

MIN_NUMBER: int = 0
MAX_NUMBER: int = 10


def generate_random_number() -> int:
    """
    Generate a random between _MIN_NUMBER and _MAX_NUMBER
    :return: a random number
    """
    return randint(MIN_NUMBER, MAX_NUMBER)

