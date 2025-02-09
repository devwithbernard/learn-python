"""
While Loop
"""


def main() -> None:
    # print value
    index: int = 0
    while index < 10:
        index += 1
        print(index)

    # Break statement
    number: int = 10

    while number > 0:
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")

        number -= 1


if __name__ == '__main__':
    main()
