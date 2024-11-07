def addition(x: float, y: float) -> float:
    """
    Sum two numbers
    :param x: first number
    :param y: second number
    :return: sum of two numbers
    """
    return x + y


def minus(x: float, y: float) -> float:
    """
    Make the difference of two numbers
    :param x: first number
    :param y: second number
    :return: minus of two numbers
    """
    return x - y


def multiplication(x: float, y: float) -> float:
    """
    Multiply two numbers
    :param x: first number
    :param y: second number
    :return: multiplication of two numbers
    """
    return x * y


def division(x: float, y: float) -> float:
    """
    Divide two numbers
    :param x: number to divide
    :param y: divider
    :return: division result rounded to the nearest 3 digits
    """
    try:
        result: float = round(x/y, 3)
        return result
    except ZeroDivisionError as error:
        print("Division by Zero!\nPlease retry...")
        raise ZeroDivisionError()

