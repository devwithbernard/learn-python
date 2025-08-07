"""
Exercises using Tuples
"""


# TODO: Create a tuple

def create_tuple(x: int, y: int, z: int) -> tuple[int, ...]:
    items: list[int] = [x, y, z]
    items.sort()

    return_tuple: tuple[int, ...] = (items[0], items[2], sum(items))

    return return_tuple


print(create_tuple(5, 3, -1))


# TODO: The oldest person

def oldest_person(people: list[tuple[str, int]]) -> dict[str, int]:
    min_birth_year = people[0][1]
    search_person: dict[str, int] = None

    for person in people:
        if person[1] < min_birth_year:
            min_birth_year = person[1]
            search_person = person

    return search_person


p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

older = oldest_person(people)

print(f"The oldest person is {older[0]}.")


# TODO: Older people

def older_people(people: list[tuple[str, int]], year: int) -> list[str]:
    names: list[str] = []

    for person in people:
        if person[1] < year:
            names.append(person[0])

    return names


names = older_people(people, 1979)
print("Older persons: ")
for name in names:
    print(name)

# TODO: Student database
students: dict[str, list[tuple[str, int]]] = {}


def add_student(database: dict, name: str) -> dict:
    if name and name.lower() not in database:
        database[name.lower()] = []
    else:
        print("Name not valid or is already in database.")
    return database


def print_student(database: dict[str, list[tuple[str, int]]], name: str) -> None:
    if name.lower() not in database:
        print(f"{name.title()}: no such person in the database.")
    else:
        print(f"{name.title()}:")
        completed_courses: list = database[name.lower()]
        if not completed_courses:
            print("no completed courses")
        else:
            n_courses = len(completed_courses)
            total_grades = 0

            print(f"{n_courses} completed course{'s' if n_courses > 1 else None}:")

            for course, grade in completed_courses:
                total_grades += grade
                print(f"  {course} {grade}")
            print(f"Average grade: {(total_grades / n_courses):,2f}")


def add_course(
    database: dict[str, list[tuple[str, int]]],
    name: str,
    course: tuple[str, int]
) -> dict[str, list[tuple[str, int]]]:
    lower_name: str = name.lower()

    if lower_name in database:
        database[lower_name].append(course)
    else:
        database = add_student(name)
        database[lower_name].append(course)

    return database


students = add_student(students, "Peter")
students = add_student(students, "Eliza")

print_student(students, "Eliza")
print_student(students, "Jack")

add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
print_student(students, "Peter")

