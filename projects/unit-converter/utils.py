"""Unit conversion utilities with user interface.

This module provides functions for common unit conversions and a simple
command-line interface for user interaction.
"""

from typing import Literal


def celsius_to_fahrenheit(temperature: float) -> float:
    """Convert temperature from Celsius to Fahrenheit.

    Uses the formula: F = (C × 9/5) + 32

    Args:
        temperature: Temperature value in Celsius.

    Returns:
        Temperature converted to Fahrenheit, rounded to 2 decimal places.

    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(25.5)
        77.9
    """
    return round(32 + (9 / 5 * temperature), 2)


def kilometer_to_meter(distance: float) -> float:
    """Convert distance from kilometers to meters.

    Args:
        distance: Distance value in kilometers.

    Returns:
        Distance converted to meters.

    Example:
        >>> kilometer_to_meter(1)
        1000.0
        >>> kilometer_to_meter(2.5)
        2500.0
        >>> kilometer_to_meter(0.001)
        1.0
    """
    return distance * 1000


def get_user_choice() -> Literal['1', '2']:
    """Prompt user to select a conversion option.

    Displays available conversion options and validates user input.
    Continues prompting until a valid choice is made.

    Returns:
        User's choice as a string: '1' for Celsius to Fahrenheit,
        '2' for kilometer to meter conversion.

    Example:
        >>> choice = get_user_choice()  # User enters '1'
        >>> choice
        '1'
    """
    menu_text = """
Make a choice:
1 - Celsius to Fahrenheit
2 - Kilometer to meter
"""

    print(menu_text)

    while True:
        user_input = input("Your choice: ").strip()

        if user_input in ('1', '2'):
            return user_input

        print("Invalid choice! Please enter 1 or 2.")
