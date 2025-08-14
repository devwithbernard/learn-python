"""
Writing files in python
"""

def create_new_file(filename: str) -> None:
    with open(filename, mode='w') as file:
        file.write("I love to code in python")


def main() -> None:
    # Create a new file
    create_new_file("files/new_file.txt")


if __name__ == '__main__':
    main()