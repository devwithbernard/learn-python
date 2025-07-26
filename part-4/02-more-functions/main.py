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