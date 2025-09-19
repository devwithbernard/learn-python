"""
Exercises: Generators
"""

# TODO: Even numbers

def even_numbers(beginning: int, maximum: int):
    number = beginning
    while number <= maximum:
        if number % 2 == 0:
            yield number

        number += 1

numbers = even_numbers(11, 21)

for number in numbers:
    print(number)
