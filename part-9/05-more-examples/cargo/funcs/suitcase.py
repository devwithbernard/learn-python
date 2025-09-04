from .item import Item


class Suitcase:
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__bags: list[Item] = []

    def weight(self) -> float:
        return sum([item.weight for item in self.__bags])

    def add_item(self, item: Item):
        if self.weight() + item.weight < self.__max_weight:
            self.__bags.append(item)
        else:
            print("The maximum number has been reached")

    def print_items(self) -> None:
        for item in self.__bags:
            print(item)

    def heaviest_item(self) -> Item | None:
        if len(self.__bags) == 0:
            return None

        heavy_item = max(self.__bags, key = lambda x: x.weight)

        return heavy_item


    def __str__(self):
        text = "items"
        if len(self.__bags) == 1:
            text = "item"

        return f"{len(self.__bags)} {text} ({self.weight()} kg)"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

    print()

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")