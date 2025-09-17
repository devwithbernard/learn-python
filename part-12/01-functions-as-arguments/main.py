# Sort a list based on default criteria: first item of tuple

products: list[tuple[str, float]] = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

sorted_products = sorted(products)

for product in sorted_products:
    print(f"{product[0]}: ${product[1]}")

print()


# Functions as arguments: Sort list based on custom criteria

def order_by_price(product: tuple[str, float]) -> float:
    return product[1]


products_order_by_price = sorted(products, key=order_by_price)

for product in products_order_by_price:
    print(f"{product[0]}: ${product[1]}")

print()

# A function definition within a function definition

persons: list[tuple[str, int]] = [('Bryan', 28), ('Jane', 15), ('Merlin', 17), ('Mark', 23)]


def sort_by_age(items: list[tuple[str, int]]) -> list[tuple[str, int]]:
    def order_by_age(item: tuple[str, int]) -> int:
        return item[1]

    return sorted(items, key=order_by_age)


persons_order_by_age = sort_by_age(persons)

for person in persons_order_by_age:
    print(f"{person[0]}: {person[1]} years old.")

print()


# Sorting collections of your own objects

class Student:
    def __init__(self, name: str, student_id: str, credits: int):
        self.__student_id = student_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.student_id}), {self.credits} cr."

    @property
    def student_id(self):
        return self.__student_id


def sort_by_id(student: Student):
    return student.student_id


def sort_by_credits(student: Student):
    return student.credits


o1 = Student("Archie", "a123", 220)
o2 = Student("Marvin", "m321", 210)
o3 = Student("Anna", "a999", 131)

students = [o1, o2, o3]

print("Sort by id:")
for student in sorted(students, key=sort_by_id):
    print(student)

print()

print("Sort by credits:")
for student in sorted(students, key=sort_by_credits):
    print(student)
