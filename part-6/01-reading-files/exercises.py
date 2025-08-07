"""
Reading files exercises
"""


# TODO: Largest number

def largest_numbers(file: str) -> int:
    with open(file) as f:
        numbers = []

        for line in f:
            number: int = int(line.replace("\n", ""))
            numbers.append(number)

        return max(numbers)


print("The largest number in the file: ", largest_numbers("files/numbers.txt"))