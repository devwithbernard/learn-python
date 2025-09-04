"""
Class hierarchies: Exercises
"""

# TODO: Laptop computer

class Computer:

    def __init__(self, model: str, speed: int) -> None:
        self.model = model
        self.speed = speed


class LaptopComputer(Computer):

    def __init__(self, model: str, speed: int, weight: float) -> str:
        super().__init__(model, speed)
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.model}, {self.speed} MHz, {self.weight} kg"


laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)