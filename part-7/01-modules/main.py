"""
Modules in python
"""

# Using modules
import math

def hypotenuse(base: int, side: int) -> float:
    """
    Returns the hypotenuse of a triangle

    Args:
        base (int): The length of the base of the triangle
        side (int): the other side of the triangle

    Returns:
        int: the hypotenuse of the triangle
    """

    return round(math.sqrt(base ** 2 + side ** 2), 2)

base = int(input("Base of triangle: "))
side = int(input("Side of triangle: "))

print(f"The hypotenuse of triangle: {hypotenuse(base, side)}")
