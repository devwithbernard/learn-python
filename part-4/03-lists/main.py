"""
Lists in Python
"""

# TODO: Create a list

empty_list: list[None] = []
print(empty_list, type(empty_list))

numbers: list[list[int]] = [[1, 3, 5], [2, 4, 6]]
print(numbers)

fruits: list[str] = ['Banana🍌', 'Mango🥭', 'Apple🍏', 'Cherry🍓']
print(fruits)

# TODO: Accessing items in a list
banana: str = fruits[0]
mango: str = fruits[1]
cherry: str = fruits[len(fruits) - 1]

print(f"Banana => {banana[-1]}")
print(f"Mango => {mango[-1]}")
print(f"Cherry => {cherry[-1]}")

print("-" * 15)

# Print all values in a list
for fruit in fruits:
    print(f"{fruit[:-1]} => {fruit[-1]}")

