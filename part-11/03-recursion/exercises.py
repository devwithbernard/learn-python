"""
Exercises: Recursion
"""


# TODO: Add numbers to a list

def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        max_number = max(numbers)
        numbers.append(max_number + 1)
        add_numbers_to_list(numbers)


numbers = [1, 3, 4, 5, 10, 11]
add_numbers_to_list(numbers)
print(numbers)


# TODO: Recursive sum
def recursive_sum(number: int):
    if number <= 1:
        return number
    return number + recursive_sum(number - 1)


print("sum from 1 to 20:", recursive_sum(20))
