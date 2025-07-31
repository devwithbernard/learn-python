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

# TODO: From range to list
nums: range = range(2, 10)
print(nums)

nums_list: list[int] = list(nums)
print(nums_list)

"""
Exercises
"""


# TODO: Star-studded
def star_studded(text: str) -> None:
    if text:
        for char in text:
            print(char)
            print("*")


string: str = input("Please, Enter a string: ")
star_studded(string)

# TODO: Prime number


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


prime_numbers: list[int] = []

for i in range(2, 100):
    if is_prime(i):
        prime_numbers.append(i)

print("Prime numbers between 0 and 100 are: ")
for prime_number in prime_numbers:
    print(prime_number, end=" ")

# TODO: From negative to positive
number: int = abs(int(input("Please enter a number: ")))

if number == 0:
    print("Not authorized")
else:
    for i in range(-number, number + 1):
        if i == 0:
            continue
        else:
            print(i)
