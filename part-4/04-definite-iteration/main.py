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


# TODO: Anagrams
def anagrams(string1: str, string2: str) -> bool:
    """
        Checks whether two strings are anagrams of each other.

        An anagram is formed by rearranging the letters of a word or phrase 
        to produce a new word or phrase, using all the original letters exactly once.

        Args:
            string1 (str): The first string to compare.
            string2 (str): The second string to compare.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(string1) == sorted(string2)


print(anagrams("tame", "meta"))  # True
print(anagrams("tame", "mate"))  # True
print(anagrams("tame", "team"))  # True
print(anagrams("tabby", "batty"))  # False
print(anagrams("python", "java"))  # False


# TODO: Palindromes
def palindromes(string: str) -> bool:
    """
    Checks whether a given string is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same
    backward as forward.

    Args:
        string (str): The string to check.

    Raises:
        ValueError: If the input string is empty.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if string == "":
        raise ValueError("string is empty.")

    return string == string[::-1]


def main() -> None:
    string = input("Please type in a palindrome: ")

    if palindromes(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")


main()


# TODO: Sum of positive numbers
def sum_of_positives(numbers: list[float]) -> float:
    sum_of_numbers = 0

    for number in numbers:
        if number > 0:
            sum_of_numbers += number

    return sum_of_numbers


result = sum_of_positives([1, -2, 3, -4, 5])
print(f"The result is {result}")


# TODO:

def even_numbers(numbers: list[int]) -> list[int]:
    even_numbers: list[int] = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)


# TODO: The sum of lists

def list_sum(list1: list[int], list2: list[int]) -> list[int]:
    new_lists: list[int] = []

    if len(list1) == len(list2):
        for i in range(len(list1)):
            sum_of_items: int = list1[i] + list2[i]
            new_lists.append(sum_of_items)
    return new_lists


a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))
