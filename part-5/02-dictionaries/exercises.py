"""
Dictionaries: Exercises
"""


# TODO: Times ten

def times_ten(start_index: int, end_index: int) -> dict[int, int]:
    new_dict: dict[int, int] = {}

    for i in range(start_index, end_index + 1):
        new_dict[i] = i * 10

    return new_dict


print(times_ten(3, 6))


# TODO: Factorials

def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("'number' parameter must be a positive integer.")

    if number == 0:
        return 1

    return number * factorial(number - 1)


def factorials(n: int) -> dict[int, int]:
    if n < 0:
        raise ValueError("Negative value not authorized.")

    fact_dict: dict[int, int] = {}

    for i in reversed(range(1, n + 1)):
        fact_dict[i] = factorial(i)

    return fact_dict


k = factorials(5)

print(k[1])
print(k[3])
print(k[5])
