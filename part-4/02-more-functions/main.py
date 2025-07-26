"""
More about functions
"""


# TODO: The parameters and arguments of a function
def greet(name: str) -> None:
    print("Hello", name)


def sum_numbers(a: float, b: float) -> None:
    print(f"{a} + {b} = {a + b}")


greet("Konan bernard")
sum_numbers(1.55, 3.66)


# TODO: Function cals within function calls

def greet_many_times(name: str, times: int) -> None:
    if times == 0 or not name:
        print("nobody has been greet yet!")
    else:
        while times > 0:
            greet(name)
            times -= 1


greet_many_times("Konan Bernard", 3)


# TODO: The return value of a function
def ask_name() -> str:
    name = input("What's your name? ")
    if not name:
        raise ValueError('name not valid.')
    return name


my_name = ask_name()
print(f"My name is {my_name}.")


def smallest(numbers: list[float]) -> float | None:
    """
    Returns the smallest number in a list of floats.
    If the input is empty, return None.

    Args:
        numbers (list[float]): a list of floats

    Returns:
        float or None: the smallest float in the input list, or None if the list is empty

    Examples:
        >>> smallest([3.5, 2.1, 5.0])
        2.1

        >>> smallest([])
        None
    """
    if numbers is None:
        return None

    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num

    return minimum


print(f"The smallest numbers in '{[8, 5, -1, 6, 2]}' is {smallest([8, 5, -1, 6, 2])}")


def my_diff(a: float, b: float) -> float:
    """
    Returns the subtraction between a and b
    :param a: the first float
    :rtype: float
    :param b: the second float
    :rtype: float
    :return: the subtraction of a and b

    Examples:
        >>> my_diff(5, 2)
        3.0
    """
    return a - b


"""
Exercises
"""


# TODO: The line function
def line(length: int, string: str) -> None:
    if not string.strip():
        print("*" * length)
    else:
        print(string[0] * length)


line(5, "%")
line(7, "")
line(8, "Line")


# TODO: A box of hashes
def box_of_hashes(height: int) -> None:
    if height == 0:
        print("")
    else:
        width: int = 10
        while height > 0:
            print("#" * width)
            height -= 1


box_of_hashes(5)
print()
box_of_hashes(2)


# TODO: A square of hashes
def square_of_hashes(width: int) -> None:
    if width == 0:
        print("")
    else:
        side: int = width
        while width > 0:
            print("#" * side)
            width -= 1


square_of_hashes(10)
print()
square_of_hashes(3)


# TODO: A square
def square(width: int, char: str) -> None:
    if width <= 0:
        return

    if not isinstance(char, str) or len(char) != 1:
        raise ValueError(f"'{char}' must be a single character")

    line_str = char * width

    for _ in range(width):
        print(line_str)


square(3, "*")
print()
square(5, "o")


# TODO: A triangle
def triangle(wide: int) -> None:
    if wide == 0:
        return

    i = 1
    while i <= wide:
        line(i, "*")
        i += 1


triangle(5)


# TODO: A spruce
def spruce(height: int, char: str) -> None:
    if height <= 0:
        return

    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("The char must a single character.")

    end_line = 0
    first_line = ""

    for i in range(1, height + 1):
        end_line += 1

        space = " " * (height - i)
        block = char * (2 * i - 1)
        lines = space + block + space

        print(lines)

        if end_line == 1:
            first_line = lines

        if end_line == height:
            print(first_line)


spruce(5, "*")
print()
spruce(3, "o")


# TODO: The greatest numbers

def greatest_number(*args) -> float:
    """
    Returns the greatest number among given arguments.

    Args:
        *args: One or more float or int to compare.

    Returns:
        float: The greatest numbers among the inputs.

    Raises:
        ValueError: If no arguments are provided.

    Examples:
        >>> greatest_number(4, 5, 8, 2)
        8
    """
    if not args:
        raise ValueError("A least one number must be provided.")
    return max(args)


print("The greatest numbers between 5, -2, 15, 18, 3 is ", greatest_number(5, -2, 15, 18, 3))
