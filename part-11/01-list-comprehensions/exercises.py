"""
List comprehensions: Exercises
"""
import math

# TODO: Square roots

def square_roots(numbers: list[float]) -> list[float]:
    if not numbers:
        raise ValueError(f'{numbers} is not in correct format')
    return [math.sqrt(x) for x in numbers]


lines = square_roots([1,2,3,4])
for line in lines:
    print(line)

# TODO: Rows of stars
def rows_of_stars(numbers: list[int]) -> list[str]:
    if not numbers:
        raise ValueError(f'{numbers} is not in correct format')
    return [ '*' * x for x in numbers]

rows = rows_of_stars([1,2,3,4])
for row in rows:
    print(row)

print()

rows = rows_of_stars([4, 3, 2, 1, 10])
for row in rows:
    print(row)
