"""
 Datatypes in python
"""


if __name__ == '__main__':
    # String
    welcome: str = 'Welcome to Japan'

    if isinstance(welcome, str):
        print(f"'{welcome}' is a string.")

    # Slicing a string
    five_first_characters = welcome[:5]
    print(f"five first characters of '{welcome}' => '{five_first_characters}'")

    # Numeric
    import time
    from random import randint
    import matplotlib.pyplot as plt
    seconds: int = 10
    while seconds > 0:
        print(f"Seconds left: {seconds}")
        time.sleep(1)
        seconds -= 1

    LIMIT: int = 1000
    random_numbers: list[int] = [randint(0, LIMIT) for number in range(LIMIT)]
    matrix = []
    initial_index, final_index = 0, 10

    for item in range(100):
        matrix.append(random_numbers[initial_index: final_index])
        initial_index += 10
        final_index += 20

    duplicate_max_values = [max(vector) for vector in matrix]
    distinct_max_values = list(set(duplicate_max_values))
    print("Distinct maximum values ==> ", distinct_max_values)

    x_axis = [x for x in range(len(duplicate_max_values))]

    # plt.plot(x_axis, distinct_max_values, marker='o', label='Distinct random max values', color='orange')
    plt.plot(x_axis, duplicate_max_values, marker='o', label='Duplicate random max values', color='blue')
    plt.xlabel='Valeur unitaire'
    plt.ylabel='Maximum de valeur aléatoire'
    plt.show()
