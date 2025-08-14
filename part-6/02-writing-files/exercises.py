"""
Exercises: Writing Files
"""

# TODO: Inscription

def inscription() -> None:
    name: str = input("What's your name? ")

    if name:
        text = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"

        with open("exercises-files/exo1.txt", mode='w') as file:
            file.write(text)
            print(f"'{text}'\nadded successfully.")


# TODO: Diary

def option() -> int:
    print("1- Add an entry, 2- Read entries, 0- Quit")
    choice = input("Function: ")
    return int(choice)

def save_entry(entry: str, filename: str) -> None:
    with open(filename, mode='a') as file:
        line = f"{entry}\n"
        file.write(line)
        print("Dairy saved!")


def read_entries(filename: str) -> None:
    print("Entries: ")
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            print(line)


def entry_point(filename: str) -> None:
    while True:
        user_option = option()

        if user_option == 0:
            print("Bye!")
            break
        elif user_option == 1:
            entry = input("Dairy entry: ")
            save_entry(entry, filename)
        elif user_option == 2:
            read_entries(filename)



def main() -> None:
    inscription()
    entry_point("exercises-files/dairy.txt")

if __name__ == '__main__':
    main()