"""
Recursion is a fundamental concept in programming where a function calls itself to solve smaller instances of a problem.
It is particularly useful for problems that can be broken down into subproblems of the same type.


A recursive function has two main parts:
    Base Case –> The condition that stops recursion.
    Recursive Case –> The function calls itself with a smaller input.
"""


def countdown(number: int) -> None:
    if number <= 0:
        print("Done 👌")
        return None

    print(number)
    countdown(number - 1)


def factorial(number: int) -> int:
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


def fibonacci(number: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1

    return factorial(number - 1) + factorial(number - 2)


def sum_of_numbers(numbers: list[int]) -> int:
    if not numbers:
        return 0  # Empty list
    return numbers[0] + sum_of_numbers(numbers[1:])


def main() -> None:
    # Count down with recursion
    countdown(10)

    # Factorial using recursion
    print(factorial(5))  # 120

    # Fibonacci number
    print(fibonacci(6))

    # Finding sum of numbers recursively
    print("Sum:", sum_of_numbers([i for i in range(10)]))


if __name__ == '__main__':
    main()
