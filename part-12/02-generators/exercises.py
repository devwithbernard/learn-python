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

# TODO: Prime numbers

def prime_numbers():
    def is_prime(number: int):
        if number < 2:
            return False

        for i in range(2, number):
            if number % i == 0:
                return False

        return True

    number = 2

    while True:
        if is_prime(number):
            yield number
        number += 1

numbers = prime_numbers()
for i in range(10):
    print(next(numbers))


