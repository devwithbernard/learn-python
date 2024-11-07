from operation import calculation


def calculate() -> None:
    operation: dict = get_operation()
    first_number, second_number = get_numbers()
    result: float = 0

    if operation['sign'] == '+':
        result = calculation.addition(first_number, second_number)
    elif operation['sign'] == '-':
        result = calculation.minus(first_number, second_number)
    elif operation['sign'] == 'x':
        result = calculation.multiplication(first_number, second_number)
    elif operation['sign'] == '/':
        result = calculation.division(first_number, second_number)

    print(f"{first_number}{operation['sign']}{second_number}={result}")


def get_numbers() -> list:
    numbers: list = []
    while not len(numbers) == 2:
        try:
            first_number: float = float(input('Enter first number:'))
            second_number: float = float(input('Enter second number:'))
            numbers.append(first_number)
            numbers.append(second_number)
        except ValueError as error:
            print("Enter correct numbers")
    return numbers


def get_operation() -> dict:
    option: str = """
    Choose your operation (enter operation number):
        1- Addition
        2- Subtraction
        3- Multiplication
        4- Division
    """
    operation_number: int
    operation: dict

    print(option)
    while True:
        try:
            operation_number = int(input("Choose your operation: "))
            if operation_number in [1, 2, 3, 4]:
                correct_choice = True
                break
            else:
                print("Choose correct operation number")
        except ValueError as error:
            print("Choose correct number\nPlease Retry")

    if correct_choice:
        default: dict = {'name': 'Addition', 'sign': '+'}

        match operation_number:
            case 1:
                operation = {'name': 'Addition', 'sign': '+'}
            case 2:
                operation = {'name': 'Subtraction', 'sign': '-'}
            case 3:
                operation = {'name': 'Multiplication', 'sign': 'x'}
            case 4:
                operation = {'name': 'Division', 'sign': '/'}
            case _:
                operation = default

        return operation


def main() -> None:
    calculate()


if __name__ == '__main__':
    main()
