"""
Introduction to set datatype
"""


def main() -> None:
    def create_set() -> set[str]:
        fruits: set[str] = {'Banana', 'Apple', 'Cherry'}
        return fruits

    print(f"fruits: {create_set()}")


if __name__ == '__main__':
    main()
