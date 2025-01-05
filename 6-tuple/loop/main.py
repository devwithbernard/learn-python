"""
Loop through tuple
"""

from typing import Generator


def main() -> None:
    fruits: tuple[str, ...] = ('Mango', 'Banana', 'Cherry', 'Pineapple')

    def loop_through_tuple(sequence: tuple[str, ...]) -> Generator[int, str, str]:
        for index, item in enumerate(sequence):
            yield index, item, item.upper()

    for value in loop_through_tuple(fruits):
        (index, item, upper_item) = value
        print(f"""
        index => {index}
        item => {item}
        upper format => {upper_item}
        """)

    def loop_using_index(sequence: tuple[str, ...]) -> None:
        for index in range(len(sequence)):
            print(f"({index},{sequence[index]})")

    loop_using_index(fruits)


if __name__ == '__main__':
    main()
