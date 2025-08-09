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
        titles = f.readline().replace("\n", "").replace("ï»¿", "").strip().split(";")

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
            line = line.replace("\n", "").strip()
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

# TODO: Course grading

def get_names(file):
    names: dict = {}

    with open(file) as f:
        for line in f:
            line = line.strip().replace("\n","")
            parts = line.split(";")

            if parts[0] == "id":
                continue

            names[parts[0]] = " ".join(parts[1:])

    return names


def get_exercise_pts(file):
    points = {}

    with open(file) as f:
        for line in f:
            line = line.strip().replace("\n","")
            parts = line.split(";")

            if parts[0] == "id":
                continue

            format_parts = [int(part) for part in parts[1:]]

            points[parts[0]] = sum(format_parts)

    return points

def get_grade(note: int) -> int:
    if note:
        match note:
            case note if 0<= note <= 14:
                return 0
            case note if note <= 17:
                return 1
            case note if note <= 20:
                return 2
            case note if note <= 23:
                return 3
            case note if note <= 27:
                return 4
            case note if note >= 28:
                return 5
            case _:
                return 0
    else:
        raise ValueError("Note is not correct.")

names = get_names("files/courses/students.csv")
points = get_exercise_pts("files/courses/exercises.csv")
exams = get_exercise_pts("files/courses/exams.csv")
grades = {pk: get_grade(note) for pk, note in exams.items()}
