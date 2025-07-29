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

"""
Exercises
"""
# TODO: Change the value of an item
numbers: list[float] = [1, 2, 3, 4, 5]

while True:
    index: int = int(input("Index (length of list: 5): "))

    if index == -1:
        print("🥲 End of exercise!")
        break

    if 0 <= index < len(numbers):
        new_value: float = float(input("New value: "))
        numbers[index] = new_value
    else:
        print("Index out of list indexes")

    print(numbers)

# TODO: Add items to a list
adding_times: int = int(input("How many times: "))

items: list[int] = []
current: int = 1

while adding_times > 0:
    item = int(input(f"Item {current}: "))
    items.append(item)

    adding_times -= 1
    current += 1

    if adding_times == 0:
        print("Items:", items)
