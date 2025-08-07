"""
Dictionaries: Exercises
"""


# TODO: Times ten

def times_ten(start_index: int, end_index: int) -> dict[int, int]:
    new_dict: dict[int, int] = {}

    for i in range(start_index, end_index + 1):
        new_dict[i] = i * 10

    return new_dict


print(times_ten(3, 6))


# TODO: Factorials

def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("'number' parameter must be a positive integer.")

    if number == 0:
        return 1

    return number * factorial(number - 1)


def factorials(n: int) -> dict[int, int]:
    if n < 0:
        raise ValueError("Negative value not authorized.")

    fact_dict: dict[int, int] = {}

    for i in reversed(range(1, n + 1)):
        fact_dict[i] = factorial(i)

    return fact_dict


k = factorials(5)

print(k[1])
print(k[3])
print(k[5])


# TODO: Histogram
def histogram(string: str) -> None:
    def count(string: str) -> dict[str, int]:
        char_counts: dict[str, int] = {}

        for char in string:
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1

        return char_counts

    char_counts: dict[str, int] = count(string)

    for char, count in char_counts.items():
        print(char, "*" * count)


histogram("abba")
print()
histogram("statistically")

# TODO: Phone book

phone_books: list[dict[str, str]] = {}


def search(name: str, books: list[dict[str, str]]) -> dict[str, str] | None:
    name_lower = name.lower()

    for item in books:
        item_name = item.get('name', '').lower()
        if item_name == name_lower:
            return item

    return None


def add(name: str, phone: str, books: list[dict[str, str]]) -> list[dict[str, str]]:
    found_contact = search(name, books)

    if found_contact:
        # Contact exists - check if phone is different
        if found_contact['phone'].lower() != phone.lower():
            # Add new entry with same name but different phone
            new_contact = {"name": name.lower(), "phone": phone}
            books.append(new_contact)
        else:
            # Exact match already exists
            print(f"The contact with name: {name} and phone: {phone} already exists.")
    else:
        # Contact doesn't exist - add new contact
        new_contact = {"name": name.lower(), "phone": phone}
        books.append(new_contact)

    return books


def ask_name_phone() -> tuple[str, str]:
    name_phone = []

    while True:
        name = input("Name: ")
        if name:
            phone = input("Phone number: ")
            if phone:
                name_phone.append(name)
                name_phone.append(phone)
                break
        print("Name or Phone number not valid.")

    return tuple(name_phone)


def ask_name():
    name = None
    while True:
        input_name = input("Name: ")
        if input_name:
            name = input_name
            break
        print("Name is not valid.")
    return name


def print_contact_infos(contact: dict[str, str] | None) -> None:
    if not contact:
        print("Contact not found.")
        return
    print("Found Contact: ")
    for key, value in contact.items():
        print(f"{key}: {value}")


def main() -> None:
    books: list[dict[str, str]] = []

    while True:
        command = int(input("Command(1 search, 2 add, 3 quit): ").strip())

        if command == 3:
            print("quitting...")
            break

        if command == 1:
            name = ask_name()
            found_contact = search(name, books)
            print_contact_infos(found_contact)
        elif command == 2:
            name, phone = ask_name_phone()
            books = add(name, phone, books)
            print(f"(Contact: {name}, {phone}) has been added!")


main()


# TODO: Invert a dictionary

def invert(dictionary: dict) -> dict:
    new_dict: dict = {}

    for key, value in dictionary.items():
        new_dict[value] = key

    return new_dict


s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)


# TODO: Movie Database

def add_movie(database: list, name: str, director: str, year: int, runtime: int) -> list:
    if name and director and year and runtime:
        movie = {
            'name': name,
            'director': director,
            'year': year,
            'runtime': runtime
        }
        database.append(movie)
    return database


def find_movies(database: list, search_term: str) -> list | None:
    if not database:
        print("Empty database.")
        return None

    found_movies = []

    for movie in database:
        if search_term.lower() in movie['name'].lower():
            found_movies.append(movie)

    return found_movies


database = []

database = add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
database = add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)

found_movies = find_movies(database, 'Python')

if found_movies:
    print(found_movies)
