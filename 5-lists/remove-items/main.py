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


def main() -> None:
    fruits: List = ["Banana", "Cherry"]
    RI: RemoveItems = RemoveItems(fruits)
    RI.remove_specified_item("Banana")
    print(f"New list: ", RI.entry_sequences)


if __name__ == '__main__':
    main()