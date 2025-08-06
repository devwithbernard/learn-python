"""
Dictionaries: Exercises
"""

# TODO: Times ten

def times_ten(start_index: int, end_index: int) -> dict[int, int]:
    new_dict: dict[int, int] = {}

    for i in range(start_index, end_index + 1):
        new_dict[i] = i * 10

    return new_dict

print(times_ten(3, 6))