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


# TODO: Fruits market

def read_fruits(file):
    contents = []

    with open(file) as f:
        titles = f.readline().replace("\n", "").replace("ï»¿","").strip().split(";")

        for line in f:
            rows = line.replace("\n", "").strip().split(";")
            new_dict = {}

            for i in range(len(titles)):
                new_dict[titles[i]] = rows[i]

            contents.append(new_dict)

    return contents

print(read_fruits("files/fruits.csv"))