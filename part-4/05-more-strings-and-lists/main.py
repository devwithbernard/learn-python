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

# TODO: More slices
my_string: str = "exemplary"
print(my_string[0:7:2])

my_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
print(my_list[6:2:-1])

# Reverse string
string: str = input("Please type in a string: ")
reversed_string: str = string[::-1]
print(reversed_string)