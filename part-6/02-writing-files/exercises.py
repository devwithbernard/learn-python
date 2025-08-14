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


def main() -> None:
    inscription()


if __name__ == '__main__':
    main()