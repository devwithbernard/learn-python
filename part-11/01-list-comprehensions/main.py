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