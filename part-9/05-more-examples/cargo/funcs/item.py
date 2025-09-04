class Item:
    def __init__(self, name: str, weight: float = 0):
        self.name = name
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name != "":
            self.__name = name
        else:
            raise ValueError('The name should not be an empty string')

    @property
    def weight(self) -> float:
        return self.__weight

    def __str__(self) -> str:
        return f"{self.name} ({self.weight} kg)"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name)
    print("Weight of the book:", book.weight)

    print("Book:", book)
    print("Phone:", phone)
