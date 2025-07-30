"""
Iterate Sequence using loop
"""

# TODO: Iterate using while loop

numbers: list[int] = [3, 2, 1, 4, 5]
index: int = 0

while index < len(numbers):
    print(numbers[index])
    index += 1

# TODO: for loop
names: tuple[str, ...] = ("Jack", "Luigi", "Marc")

for name in names:
    print(name)
