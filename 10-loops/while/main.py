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

    # Continue Statement
    names: list[str] = ['John', 'Jane', 'Annabella', 'Chris']

    all_names_without_annabella: list = []

    counter: int = len(names)

    while counter > 0:
        counter -= 1
        if names[counter] == 'Annabella':
            continue
        else:
            all_names_without_annabella.append(tuple([counter, names[counter]]))

    print(all_names_without_annabella)


if __name__ == '__main__':
    main()
