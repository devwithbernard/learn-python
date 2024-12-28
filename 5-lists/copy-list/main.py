"""
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes
 made in list1 will automatically also be made in list2.
"""

from typing import List, Any


def main() -> None:
    fruits: List[str] = ["Apple", "Banana", "Cherry"]

    def use_copy_method(sequence: List[Any]) -> List[Any]:
        copy_sequence: List[Any] = sequence.copy()
        return copy_sequence

    print(f"""copy_fruits = {use_copy_method(fruits)}""")


if __name__ == '__main__':
    main()
