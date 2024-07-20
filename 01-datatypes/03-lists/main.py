"""
A list of numbers
"""
numbers = [1, 2, 3, 4, 5]

print(type(numbers), '--> ', numbers)
if isinstance(numbers, list):
    index = 0
    for index, number in enumerate(numbers):
        print(f"{index} -> {number}")

"""
List indexing : ['a', 'b', 'c', 'd']
                  0    1    2    3   : positive indexation
                  -4   -3   -2   -1  : negative indexation
"""

products = ['Shoe', 'Trowser', 'Bag', 'Watch']
for idx in range(len(products)): # Positive indexation
    product = products[idx]
    print(f"Product N°{idx + 1} --> {product}")

for idx in range(1, len(products) + 1): # Negative indexation
    product = products[-idx]
    print(f"Product N°{len(products) + 1 - idx} --> {product}")

"""
Lists are mutable
"""
import time
numbers = []

for i in range(11):
    time.sleep(1)
    result = i * 3
    numbers.append(result)
    print(f"{result} has been added.")

print("Numbers[] = ", numbers)