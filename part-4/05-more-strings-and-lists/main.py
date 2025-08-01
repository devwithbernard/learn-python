"""
Learn more about strings and lists
"""

# TODO: Slices
message: str = "Hello world!"

print(message[3:8])
print(message[:6])

numbers: list[int] = [3, 4, 2, 4, 6, 1, 2, 4, 2]
part: list[int] = numbers[3:7]
print(part)
