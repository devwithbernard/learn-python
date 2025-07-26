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
