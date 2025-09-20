def infos_operator() -> None:
    """Display the list of available arithmetic operations.

    This function prints the possible operations the user can choose from:
    1- Addition (+)
    2- Subtraction (-)
    3- Multiplication (x)
    4- Division (/)
    """
    print("""
    Choose an operation:
    1- Addition (+)
    2- Subtraction (-)
    3- Multiplication (x)
    4- Division (/)
    """)


def get_operator() -> str:
    """Prompt the user to select a valid arithmetic operation.

    Continuously asks the user to choose an operator until a valid choice is entered.
    Valid operators are represented by numbers: 1, 2, 3, or 4.

    Returns:
        str: A string representing the chosen operator ('1', '2', '3', or '4').
    """
    valid_operators = ('1', '2', '3', '4')
    while True:
        operator = input("Enter your operator: ").strip()
        if operator not in valid_operators:
            print("Invalid choice! Please select one of the following:")
            infos_operator()
        else:
            return operator


def get_numbers() -> tuple[float, float]:
    """Prompt the user to input two valid numbers.

    Continuously asks the user for input until two valid floating-point numbers
    are entered.

    Returns:
        tuple[float, float]: A tuple containing the first and second number.
    """
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
            return first_number, second_number
        except ValueError:
            print("Both inputs must be valid numbers. Please try again.")
