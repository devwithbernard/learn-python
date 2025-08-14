"""
Writing files in python
"""

def create_new_file(filename: str) -> None:
    with open(filename, mode='w') as file:
        file.write("I love to code in python")


def multi_lines(texts: list[str], filename: str) -> None:
    if texts:
        with open(filename, mode='w') as file:
            for text in texts:
                line = f"Name: {text}\n"
                file.write(line)
    print("File wrote successfully")


def main() -> None:
    # Create a new file
    create_new_file("files/new_file.txt")

    # Write multine lines
    multi_lines(['John', 'Emma', 'Jane', 'Luigi'], "files/multi_lines_file.txt")


if __name__ == '__main__':
    main()