"""
Working with textual data in python
"""


def split_text(text: str, separator=' ') -> list[str]:
    """
    Split text by separator and return a list of strings
    :param text: entry text
    :param separator: sep
    """
    strings: list[str] = []

    if separator in text:
        separator_index = 0

        for i in range(0, len(text)):
            if text[i].strip() == separator.strip():
                strings.append(text[separator_index:i])
                separator_index = i + 1
        else:
            strings.append(text[separator_index:len(text)])

    return strings


def main() -> None:
    """
        Entry point
    """
    my_message: str = 'Hello world'
    print(my_message, type(my_message))

    phrase: str = "I love to program."

    concatenate_string: str = my_message + '.' + phrase
    print(concatenate_string)

    # Length of string
    message_length: int = len(my_message)
    print(my_message, f";Length: {message_length}")

    # Accessing to character
    first_character: str = my_message[0]
    second_character: str = my_message[1]
    last_character: str = my_message[message_length - 1]

    print(f"""
    First character => {first_character}
    Second character => {second_character}
    Last character => {last_character}
    """)

    print(split_text("Hello world. I love programming"))


if __name__ == '__main__':
    main()
