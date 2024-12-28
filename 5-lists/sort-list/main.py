"""
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
"""

from typing import List, Any


def main() -> None:
    fruits: List[str] = ["Orange", "Mango", "Kiwi", "Pineapple", "Banana"]

    def sort_by_alphanumerically(sequence: List[Any]) -> List[Any]:
        copy_sequence: List[Any] = sequence[:]
        copy_sequence.sort()
        return copy_sequence

    print(sort_by_alphanumerically(fruits))


if __name__ == '__main__':
    main()
