"""
Randomness in python
"""

# Generate a random number

import random

print("The result of the throw:", random.randint(1, 6))

# More randomizing functions

fruits: list[str] = ["Apple", "Banana", "Mango", "Orange", "Pineapple"]
random.shuffle(fruits)
print(fruits)