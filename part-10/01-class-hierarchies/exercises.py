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

# TODO: Game Museum

class ComputerGame:
    def __init__(self, name: str, production_house: str, production_year: int):
        self.name = name
        self.studio = production_house
        self.year = production_year

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) by {self.studio}"


class GameWarehouse:
    def __init__(self):
        self.games = []

    def add_game(self, game: ComputerGame) -> None:
        self.games.append(game)

    def list_games(self) -> list[ComputerGame]:
        return self.games

class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self) -> list[ComputerGame]:
        games = [game for game in self.games if game.year < 1990]
        return games


museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))

for game in museum.list_games():
    print(game)


# TODO: Areas

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self) -> str:
        return f"Rectangle {self.width}x{self.height}"

class Square(Rectangle):
    def __init__(self, width: float):
        super().__init__(width, width)
        self.width = width

    def __str__(self) -> str:
        return f"Square {self.width}x{self.width}"


rectangle = Rectangle(2, 3)
print(rectangle)
print("area:", rectangle.area())

square = Square(4)
print(square)
print("area:", square.area())