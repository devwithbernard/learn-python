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

    def sort_by_numerically(sequence: List[float]) -> List[float]:
        copy_sequence: List[float] = sequence[:]
        copy_sequence.sort()
        return copy_sequence

    print(sort_by_numerically([100, 50, 65, 82, 23]))

    def descending_sort(sequence: List[Any]) -> List[Any]:
        copy_sequence: List[Any] = sequence[:]
        copy_sequence.sort(reverse=True)
        return copy_sequence

    print(descending_sort([200, 50, 25, 82, 23]))

    def custom_sort(sequence: List[Any], key) -> List[Any]:
        copy_sequence: List[Any] = sequence[:]
        copy_sequence.sort(key=key, reverse=False)
        return copy_sequence

    print(custom_sort([200, 500, 65, 42, 230], key=lambda number: number - 50))
    print(custom_sort(fruits, key=lambda word: len(word)))
    print(custom_sort([100, -400, -22, 17, 234_000], key=abs))


if __name__ == '__main__':
    main()
