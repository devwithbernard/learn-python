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

# TODO: Matrix items

def matrix(file) -> list[list[int]]:
    matrix: list[list[int]] = []

    with open(file) as f:
        for line in f:
            line = line.replace("\n","").strip()
            row = [int(i) for i in line.split(",")]
            matrix.append(row)

    return matrix

def row_sums(m: list[list[int]]) -> list[int]:
    sums: list[int] = []

    for row in m:
        sums.append(sum(row))

    return sums

def max_matrix(m: list[list[int]]) -> int:
    max_list = [max(row) for row in m]
    return max(max_list)

m = matrix("files/matrix.txt")

print("Sum of row items:", row_sums(m))
print("Max of matrix items:", max_matrix(m))