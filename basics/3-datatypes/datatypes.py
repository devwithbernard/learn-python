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
