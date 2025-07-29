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

# TODO: Adding item to a list
shoe_sizes: list[int] = []

shoes_number: int = 3

while shoes_number > 0:
    shoe_size: int = int(input("Shoe size: "))

    if 20 <= shoe_size <= 50:
        shoe_sizes.append(shoe_size)
        shoes_number -= 1
    else:
        print("Shoe size must be between 20 and 50")
        print("Retry!")

    if shoes_number == 0:
        print("Shoe sizes: ", shoe_sizes)

# TODO: Adding to a specific index
points: list[tuple[float, float]] = [(0.0, 0.0), (3.2, 5.3), (1.5, 1.75)]

while True:
    index: int = int(input("Specific index (-1 to end): "))
    if index == -1:
        print("Points:", points)
        break

    if not (0 <= index < len(points)):
        print("Index out of range!")
        print(f"Retry!\nLength of coordinates: {len(points)}")
    else:
        x: float = float(input("X = "))
        y: float = float(input("Y = "))

        coord = (x, y)
        points.insert(index, coord)

# TODO: Removing items from a list
names: list[str] = ["Sophia", "Luigi", "Mark", "Simon"]
indexes: list[int] = [i for i in range(5)]

while len(indexes) > 0:
    index: int = int(input("Removing index (-1 to end): "))

    if not (0 <= index < len(indexes)):
        print(f"Index out of range (They are {len(indexes)}\nRetry!")
    else:
        removed_item: int = indexes.pop(index)
        print(f"{removed_item} at index {index}")

    if len(indexes) == 0:
        print("Empty list\nEnd!")

print("Following names: ", ", ".join(names))
while True:
    name: str = input("Remove a name (or 'end' to end): ").strip()

    if name.capitalize() not in names:
        print(f"'{name}' not in list of names")
    else:
        names.remove(name)
        print(f"'{name}' removed to names.")

    if len(names) == 0 or name.lower() == 'end':
        print("End")
        break

# TODO: Sorting lists
nums: list[int] = [1, 5, 3, 4, 2]

nums.sort()
print("Sorted list: ", nums)

sorted_list: list[int] = sorted(nums)
print("New sorted list: ", sorted_list)

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


# TODO: Addition and removal
def add(item: int, items: list[int]) -> list[int]:
    """
        Appends an item to the list and returns the updated list.

        Args:
            item (int): The integer to add to the list.
            items (list[int]): The list to which the item will be added.

        Returns:
            list[int]: The updated list containing the added item.
    """
    items.append(item)
    return items


def remove(items: list[int]) -> list[int]:
    """
        Removes the last item from the list if it is not empty.
        If the list is empty, a message is printed and the list remains unchanged.
        Finally, return the updated or unchanged list.

        Args:
            items (list[int]): The list from which the last item will be removed.

        Returns:
            list[int]: The updated list after attempting to remove the last item.
    """
    if not items:
        print("Empty list. Impossible to remove an item.")
    else:
        items.pop(len(items) - 1)

    return items


data: list[int] = []

while True:
    choice: str = input("A(d)d or (r)emove or e(x)it: ").strip().lower()

    if choice == 'x':
        print("Bye!")
        break
    elif choice == 'r':
        data = remove(data)
        print(data)
    elif choice == 'd':
        item = int(input("Added item: "))
        data = add(item, data)
        print(data)
    else:
        print("Bad choice!")

# TODO: Same word twice
words: list[str] = []
while True:
    word: str = input("Word: ")

    if not word.strip():
        print("Empty word not authorized!")
    if word in words:
        print(f"You typed in {len(words)} different words")
        break
    else:
        words.append(word)

# TODO: List twice
items: list[int] = []

while True:
    new_item: int = int(input("New item (O to end): "))

    if new_item == 0:
        break

    items.append(new_item)
    new_items = sorted(items)
    print("The list now:", new_items)
