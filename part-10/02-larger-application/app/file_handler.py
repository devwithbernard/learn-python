class FileHandler:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def load_file(self):
        names = {}

        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(";")
                name, *numbers = parts
                names[name] = numbers

        return names

    def save_file(self, phone_book: dict):
        with open(self.__filename, 'w') as f:
            for name, numbers in phone_book.items():
                line = [name] + phone_book.items()
                f.write(";".join(line) + "\n")