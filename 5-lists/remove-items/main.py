"""
Remove items from list
"""
from typing import List, Any


class RemoveItems:
    entry_sequences: List[Any] = []

    def __init__(self, entry_sequences: list[Any]) -> None:
        self.entry_sequences = entry_sequences

    def remove_specified_item(self, item: Any) -> Any:
        if item not in self.entry_sequences:
            raise ValueError(f"{item} cannot be remove from {self.entry_sequences}")
        self.entry_sequences.remove(item)
        return item

    def remove_item_at_specified_index(self, index: Any) -> Any:
        if index not in range(-len(self.entry_sequences), len(self.entry_sequences)):
            raise IndexError("Specified index is out of range")
        removed_item: Any = self.entry_sequences.pop(index)
        return removed_item

    def clear_list(self) -> None:
        self.entry_sequences.clear()


def main() -> None:
    fruits: List = ["Banana", "Cherry", "Apple", "Orange", "Pineapple"]
    RI: RemoveItems = RemoveItems(fruits)
    RI.remove_specified_item("Banana")
    print(f"New list: ", RI.entry_sequences)

    RI.remove_item_at_specified_index(-1)
    print(f"New list: ", RI.entry_sequences)

    RI.clear_list()
    print(f"New list: ", RI.entry_sequences)


if __name__ == '__main__':
    main()