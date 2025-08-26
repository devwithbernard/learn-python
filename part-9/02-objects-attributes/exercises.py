"""
Objects as attributes: Exercises
"""


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
