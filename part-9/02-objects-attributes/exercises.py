"""
Objects as attributes: Exercises
"""

from present import Present
from box import Box


# TODO: Pets

class Pet:
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed


class Person:
    def __init__(self, name: str, pet: Pet) -> None:
        self.name = name
        self.pet = pet

    def __str__(self) -> str:
        return f"{self.name}, whose pal is {self.pet.name}, a {self.pet.breed}"


hulda = Pet("Hulda", "mixed-breed dog")
levi = Person("Levi", hulda)

print(levi)

# TODO: A box of presents
book = Present("ABC Book", 2)
cd = Present("Pink Floyd: Dark Side of the Moon", 1)

box = Box()

box.add_present(book)
box.add_present(cd)

print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)
print(f"Box weight: {box.total_weight()}kg")
