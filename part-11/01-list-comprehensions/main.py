"""
List comprehensions
"""

# Using regular loop
numbers = [1, 2, 3, 4, 5]

strings = []
for number in numbers:
    strings.append(str(number))

print(strings)

# Using list comprehensions
strings = [str(number) for number in numbers]
print("Using list comprehensions:", strings)


def factorials(n):
    k = 1
    while n >= 2:
        k *= n
        n -= 1

    return k

factorial_numbers = [factorials(number) for number in numbers]
print(f"Factorial {numbers}: {factorial_numbers}")

# Filtering the items
numbers = [1, 1, 2, 3, 4, 6, 4, 5, 7, 10, 12, 3]

even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

numbers = [-2, 3, -1, 4, -10, 5, 1]
factorial_numbers = [(number, factorials(number)) for number in numbers if number >= 0]
print(factorial_numbers)

# Alternative execution with list comprehensions

numbers = [1, -3, 45, -110, 2, 9, -11]
abs_values = [number if number >= 0 else -number for number in numbers]
print("Abs values:", abs_values)

def string_lengths(my_list: list) -> list[int]:
    return [len(item) if isinstance(item , str) else -1 for item in my_list]

test_list = ["hi", 3, True, "there", -123.344, "toodlepip", 2, False]
lengths = string_lengths(test_list)
print(lengths)
