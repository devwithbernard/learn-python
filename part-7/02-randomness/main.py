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

# Randomness Case Study: Lottery numbers
number_pool: list[int] = list(range(1, 41))
random.shuffle(number_pool)
weekly_draw: list[int] = number_pool[:7]
print(weekly_draw)