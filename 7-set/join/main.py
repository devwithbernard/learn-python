"""
Join two sets
"""


def main() -> None:
    set_fruits_1: set[str] = {'Apple', 'Banana', 'Orange', }
    set_fruits_2: set[str] = {'Orange', 'Grape', 'Watermelon'}

    def union_sets(
            sequence_1: set[str], sequence_2: set[str]
    ) -> set[str]:
        union_sequence: set[str] = sequence_1.union(sequence_2)
        return union_sequence

    print(union_sets(set_fruits_1, set_fruits_2))


if __name__ == '__main__':
    main()
