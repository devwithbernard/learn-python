"""
Introduction to set datatype
"""


def main() -> None:
    def create_set() -> set[str]:
        fruits: set[str] = {'Banana', 'Apple', 'Cherry'}
        return fruits

    print(f"fruits: {create_set()}")

    def len_set(sequence: set) -> int:
        return len(sequence)

    fruits: set[str] = {'Banana', 'Apple', 'Cherry'}
    print(f"Nombre de fruits: {len_set(fruits)}")


if __name__ == '__main__':
    main()
