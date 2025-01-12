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

    def union_multiple_sets(**kwargs) -> set:
        """
        Join multiple sets provided as keyword arguments

        :param kwargs: Keyword arguments where each value is a set
        :return: A single set containing all elements from the provided
        """

        combined_set = set()

        for key, value in kwargs.items():
            if isinstance(value, set):
                combined_set.update(value)
            else:
                raise ValueError(f"Value for '{key}' is not a set. All arguments must be sets.")

        return combined_set

    print(union_multiple_sets(set1=set_fruits_1, set2=set_fruits_2, set3={'Passion fruit', 'Cranberry'}))

    def intersection_sets(set_1: set[str], set_2: set[str]) -> set[str]:
        """
        Join two sets where the return value contains the items that are present in both parameters

        :param set_1: first set
        :param set_2: second set
        :return: A single set containing only values present in both sets
        """

        intersection_set: set[str] = set_1.intersection(set_2)
        return intersection_set

    print(f"intersection set: {intersection_sets(set_fruits_1, set_fruits_2)}")


if __name__ == '__main__':
    main()
