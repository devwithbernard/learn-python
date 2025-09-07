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