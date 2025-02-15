"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""


# Define a block of function

def greet() -> None:
    print("Hello, World!")


# Function with parameters

def say_hello(name: str) -> None:
    print(f"Hello, {name}")


def main() -> None:
    greet()

    names: list[str] = ['Carlos', 'Jessie', 'Tania']

    for name in names:
        say_hello(name)


if __name__ == '__main__':
    main()
