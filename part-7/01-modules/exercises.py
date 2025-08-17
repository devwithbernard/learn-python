"""
Modules Exercises
"""

import string


def separate_characters(my_string: str) -> tuple[str, ...]:
    """
    returns a list of string in which we separate ascii letters, punctuation and other characters

    Args:
        my_string (str): the input string

    Returns:
        tuple[str]: the separated tuple of strings

    Raises:
        ValueError: if the input string is None or Empty
    """

    if not my_string:
        raise ValueError("Invalid input string or empty input string.")

    ascii_characters: str = ""
    punctuation_characters: str = ""
    other_characters: str = ""

    for char in my_string:
        if char in string.ascii_letters and char not in ascii_characters:
            ascii_characters += char
        elif char in string.punctuation and char not in punctuation_characters:
            punctuation_characters += char
        elif char not in other_characters:
            other_characters += char

    return ascii_characters, punctuation_characters, other_characters


separate_chars = separate_characters("Olé!!! Hey, are ümläüts wörking?")

for item in separate_chars:
    print(item)