"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""
import math


# Define a block of function

def greet() -> None:
    print("Hello, World!")


# Function with parameters

def say_hello(name: str) -> None:
    print(f"Hello, {name}")


# Function with return value
def uppercase(text: str) -> str:
    if text is None:
        raise ValueError("Parameter can't be a NoneType")

    return text.upper()


# Multiple positional arguments
def sum_numbers(*numbers) -> float:
    return sum(numbers)


# Keywords arguments
def print_info(**details):
    for key, value in details.items():
        print(f"{key} => {value}")


# Lambda (Anonymous) functions
def lambda_functions() -> None:
    numbers: list[int] = [1, 2, 3, 4]
    squares: list[int] = list(map(lambda number: number * 2, numbers))

    print(f"Square of {numbers} => {squares}")


def even_numbers(numbers: list[int]) -> list[int]:
    if not numbers:
        raise ValueError('Empty list')

    even_nums: list[int] = list(filter(lambda number: number % 2 == 0, numbers))

    return even_nums


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True


def prime_numbers(min_number: int, max_number: int) -> list[int]:
    nums: list[int] = list(filter(lambda number: is_prime(number), range(min_number, max_number)))
    return nums


def main() -> None:
    greet()

    names: list[str] = ['Carlos', 'Jessie', 'Tania']

    for name in names:
        say_hello(name)

    upper_names: list[str] = [uppercase(name) for name in names]
    for upper_name in upper_names:
        print(upper_name)

    print("Sum of 1, 2, 3, 4, 5 = ", sum_numbers(1, 2, 3, 4, 5))

    print_info(name="Konan Bernard", email="devwithbernard@gmail.com", city="Abidjan")

    lambda_functions()

    print(f"Even numbers: ")
    print(f"\t{even_numbers(list(range(20)))}")

    print("Prime numbers between 1 and 100")
    print(prime_numbers(1, 200))


if __name__ == '__main__':
    main()
