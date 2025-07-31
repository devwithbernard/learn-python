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


# TODO: List of stars

def list_of_stars(star_counts: list[int], star: str) -> None:
    """
    Prints lines of stars based on the values in the star_counts list.

    Each line printed corresponds to one integer in star_counts, and contains
    that many repetitions of the given star character.

    Args:
        star_counts (list[int]): A list of integers representing the number of stars to print per line.
        star (str): A single character string used as the star symbol.

    Raises:
        ValueError: If the 'star' argument is not a single character.

    Returns:
        None
    """
    if len(star) > 1:
        raise ValueError("'star' must be a single character.")

    for star_count in star_counts:
        print(star * star_count)


num_stars: list[int] = [3, 7, 1, 1, 2]
list_of_stars(num_stars, "*")
