"""
Exercises using Tuples
"""
import datetime


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