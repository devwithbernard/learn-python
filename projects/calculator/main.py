from calculus.calculus import Calculus
from utils.utils import get_numbers, get_operator, infos_operator


def process_calculus():
    """Run an interactive calculator session.

        The user can perform up to 3 operations before being asked
        if they want
    """
    print("-----------------Make some calculus--------------")
    infos_operator()
    print()

    number_of_operations = 3

    while number_of_operations > 0:
        a, b = get_numbers()
        operator_num = get_operator()

        operation_map = {
            '1': ('+', Calculus.add),
            '2': ('-', Calculus.subtract),
            '3': ('x', Calculus.multiply),
            '4': ("/", Calculus.divide)
        }

        operator, func = operation_map[operator_num]
        result = func(a, b)

        if result is not None:
            print(f"{a} {operator} {b} == {result}")
        else:
            print("Operation could not be completed!")

        number_of_operations -= 1

        if number_of_operations == 0:
            yes_no = input("Would you want to terminate? (yes/no or y/n)? ").lower().strip()
            if yes_no in ('y', 'yes'):
                print("End of calculus")
            else:
                number_of_operations = 3
                print("The calculus continue...")


def main() -> None:
    """Entry point of the program."""
    process_calculus()


if __name__ == '__main__':
    main()
