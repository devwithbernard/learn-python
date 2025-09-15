"""
Recursion
"""

# A function calls itself
def hello(name: str) -> None:
    print("Hello", name)

def hello_many_times(name: str, times: int) -> None:
    for i in range(times):
        hello(name)


hello_many_times("Bernard", 5)

# Recursion
def fill_list(numbers: list):
    """ if the length of the list is less than 10, add items to the list """
    if len(numbers) < 10:
        numbers.append(0)
        fill_list(numbers)

test_list = [1, 2, 3, 4]
fill_list(test_list)
print(test_list)


def fact(number: int) -> int:
    if number < 0:
        raise ValueError("the number must be a positive number")

    if number == 0 or number == 1:
        return 1

    return number * fact(number -1)


number = int(input("Enter a number: "))
print(f"{number}! = {fact(number)}")

# Recursion and return value

def fibonacci(number: int) -> int:
    if number < 0:
        raise ValueError("The number must be greater than or equal to 0")
    if number < 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


for i in range(1, 7):
    print(fibonacci(i), end=" ")