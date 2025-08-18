"""
Define classes: Exercises
"""

# TODO: Book

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int) -> None:
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    def describe(self) -> None:
        description = f"{self.author}: {self.name}({self.year})"
        return description

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(python.describe())
print(everest.describe())