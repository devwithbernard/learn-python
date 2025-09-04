from .item import Item
from .suitcase import Suitcase

class CargoHold:

    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__suitcases: list[Suitcase] = []

    def weight(self) -> float:
        return sum([suitcase.weight() for suitcase in self.__suitcases])

    def add_suitcase(self, suitcase: Suitcase) -> None:
        if self.weight() + suitcase.weight() < self.__max_weight:
            self.__suitcases.append(suitcase)
        else:
            print("The maximum number has been reached")

    def print_items(self) -> None:
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self) -> str:
        text = "suitcases"
        if len(self.__suitcases) == 1:
            text = 'suitcase'

        return f"{len(self.__suitcases)} {text} ({self.weight()} kg)"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()