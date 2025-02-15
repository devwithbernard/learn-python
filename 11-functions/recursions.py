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


def main() -> None:
    # Count down with recursion
    countdown(10)


if __name__ == '__main__':
    main()
