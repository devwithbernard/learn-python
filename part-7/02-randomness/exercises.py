"""
Randomness Exercises
"""
import random


# TODO: Lottery numbers
def lottery_numbers(amount: int, lower: int, upper: int) -> list[int]:
    """
        Generate a list of unique random lottery numbers.

        The function creates a list of integers within the inclusive range [lower, upper],
        shuffles them, and returns a sorted selection of `amount` numbers.

        Args:
            amount (int): The number of lottery numbers to generate.
            lower (int): The minimum possible number in the lottery draw.
            upper (int): The maximum possible number in the lottery draw.

        Returns:
            list[int]: A sorted list of `amount` unique random numbers.

        Raises:
            ValueError: If any parameter is negative.
            ValueError: If `amount` is greater than the size of the interval [lower, upper].
    """

    if lower < 0 or upper < 0 or amount < 0:
        raise ValueError("Parameters must be positive number")

    if amount > abs(upper - lower):
        raise ValueError("amount > upper - lower")

    if lower > upper:
        lower, upper = upper, lower

    numbers = list(range(lower, upper + 1))
    random.shuffle(numbers)

    return sorted(numbers[:amount])


for number in lottery_numbers(7, 1, 40):
    print(number)