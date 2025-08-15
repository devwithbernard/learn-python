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


def append_name(filename: str) -> None:
    new_name = input("Your name: ")
    if new_name:
        with open(filename, mode='a') as file:
            line = f"Name: {new_name}\n"
            file.write(line)
    else:
        print(f"'{new_name}' is not valid.")


def write_csv_file(filename: str, data: list[dict], delimiter=None) -> None:
    if not delimiter:
        delimiter = ","

    headers: list[str] = [key for key in data[0].keys()]
    header = f"{delimiter}".join(headers)

    with open(filename, mode='a') as file:
        file.write(header + "\n")
        for item in data:
            values = [str(val) for val in item.values()]
            line = f"{delimiter}".join(values)
            file.write(line + "\n")

    print("Data saved successfully!")


def main() -> None:
    # Create a new file
    create_new_file("files/new_file.txt")

    # Write multine lines
    multi_lines(['John', 'Emma', 'Jane', 'Luigi'], "files/multi_lines_file.txt")

    # Append name to existing file
    append_name("files/multi_lines_file.txt")

    # Writing CSV files
    coders: list[dict[str, str | int]] = [
        {"name": "Eric", "os": "Windows", "language": "Pascal", "experience": 10},
        {"name": "Matt", "os": "Linux", "language": "PHP", "experience": 2},
        {"name": "Alan", "os": "Linux", "language": "Java", "experience": 17},
        {"name": "Emily", "os": "Mac", "language": "Cobol", "experience": 9},
        {"name": "Sophia", "os": "Windows", "language": "Python", "experience": 5},
        {"name": "David", "os": "Linux", "language": "C++", "experience": 8},
        {"name": "Laura", "os": "Mac", "language": "Ruby", "experience": 4},
        {"name": "John", "os": "Windows", "language": "C#", "experience": 12},
        {"name": "Hannah", "os": "Linux", "language": "Go", "experience": 6},
        {"name": "Peter", "os": "Mac", "language": "Swift", "experience": 3}
    ]

    write_csv_file("files/coders.csv", coders, delimiter=";")



if __name__ == '__main__':
    main()