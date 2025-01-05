"""
Join Two tuples
"""


def main() -> None:
    def join_tuples(tuple1: tuple, tuple2: tuple) -> tuple:
        return tuple1 + tuple2

    print(join_tuples(('Banana',), ('Chery', 'Apple')))


if __name__ == '__main__':
    main()
