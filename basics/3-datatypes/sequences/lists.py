def try_list():
    some_list = ['Python', 'Java', 'C#', [1, 2, 3], 1 + 3j, 5 - 2j]
    print("A list => ", some_list)

    if isinstance(some_list, list):
        print('This is a list.')

    # type of list
    print(type(some_list))

    # Concatenation and multiplication
    integers: list[int] = [1, 2, 3]
    real_numbers: list[float] = [4.0, 5.0, 6.0]

    numbers: list[float] = list(map(lambda number: float(number), integers)) + real_numbers
    print(numbers, type(numbers))


def main():
    try_list()


if __name__ == '__main__':
    main()
