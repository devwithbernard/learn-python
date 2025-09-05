class PhoneBook:

    def __init__(self) -> None:
        self.__persons: dict[str, list[str]] = {}

    def add_number(self, name: str, number: str) -> None:
        if not name in self.__persons:
            self.__persons[name] = []
        else:
            self.__persons[name].append(number)

    def get_numbers(self, name: str) -> list[str] | None:
        if not name in self.__persons:
            return None

        return self.__persons[name]

    def all_entries(self):
        return self.__persons


def help() -> None:
    print("Commands:")
    print("0 exit")
    print("1 add entry")
    print("2 search entry")


class PhoneBookApplication:
    def __init__(self) -> None:
        self.__phone_book = PhoneBook()

    def add_entry(self):
        name = input("Name: ")
        number = input("Number: ")
        self.__phone_book.add_number(name, number)

    def search(self) -> None:
        name = input("Name: ")
        numbers = self.__phone_book.get_numbers(name)

        if numbers is None:
            print("Number unknow")
            return None

        for number in numbers:
            print(number)

        return None

    def execute(self):
        help()

        while True:
            print("")
            command = input("Command: ")

            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                help()
