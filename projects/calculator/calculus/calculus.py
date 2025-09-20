"""
This module provides a simple `Calculus` class that implements basic arithmetic
operations such as addition, subtraction, multiplication, and division.

Classes:
    Calculus: A utility class that provides class methods for arithmetic operations.
"""


class Calculus:
    """A utility class for performing basic arithmetic operations.

    This class provides class methods to perform fundamental mathematical
    calculations, including addition, subtraction, multiplication, and division.
    """

    @classmethod
    def add(cls, a: float, b: float) -> float:
        """Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return a + b

    @classmethod
    def subtract(cls, a: float, b: float) -> float:
        """Subtract one number from another.

        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.

        Returns:
            float: The result of the subtraction.
        """
        return a - b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return a * b

    @classmethod
    def divide(cls, a: float, b: float) -> float | None:
        """Divide one number by another.

        Args:
            a (float): The dividend.
            b (float): The divisor.

        Returns:
            float | None: The quotient rounded to 5 decimal places if division is
            possible; otherwise, None.

        Raises:
            ZeroDivisionError: Prints an error message and returns None if
            division by zero is attempted.
        """
        try:
            result = a / b
            return round(result, 5)
        except ZeroDivisionError:
            print("Impossible to divide by 0")
