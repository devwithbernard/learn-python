"""
Exercises using Tuples
"""


# TODO: Create a tuple

def create_tuple(x: int, y: int, z: int) -> tuple[int, ...]:
    items: list[int] = [x, y, z]
    items.sort()

    return_tuple: tuple[int, ...] = (items[0], items[2], sum(items))

    return return_tuple

print(create_tuple(5, 3, -1))