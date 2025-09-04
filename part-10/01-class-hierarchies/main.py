"""
Class hierarchies
"""

class Person:

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def update_email_domain(self, new_domain: str) -> None:
        old_domain = self.email.split("@")[1]
        self.email = self.email.replace(old_domain, new_domain)

# Inheritance
class Student(Person):

    def __init__(self, name: str, student_id: str, email: str, credit: int = 0) -> None:
        super().__init__(name, email)
        self.student_id = student_id
        self.credits = credit


class Teacher(Person):

    def __init__(self, name: str, email: str, room: str, teaching_years: int) -> None:
        super().__init__(name, email)
        self.room = room
        self.teaching_years = teaching_years



saul = Student("Saul Student", "1234", "saul@example.com", 0)
saul.update_email_domain("example.edu")
print(saul.email)

tara = Teacher("Tara Teacher", "tara@example.fi", "A123", 2)
tara.update_email_domain("example.ex")
print(tara.email)

# Second inheritance

class Book:
    """
    This class models a simple book
    """
    def __init__(self, name: str, author: str) -> None:
        self.name = name
        self.author = author

    def __str__(self) -> str:
        return f"{self.name} ({self.author})"


class BookContainer:
    """This class models a container for books"""
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def list_books(self) -> None:
        for book in self.books:
            print(book)

class Bookshelf(BookContainer):
    """This class models a shelf for books"""
    def __init__(self) -> None:
        super().__init__()

    def add_book(self, book: Book, location: int) -> None:
        self.books.insert(location, book)


# Create some books for testing
b1 = Book("Old Man and the Sea", "Ernest Hemingway")
b2 = Book("Silent Spring", "Rachel Carson")
b3 = Book("Pride and Prejudice", "Jane Austen")

# Create a BookContainer and add the books
container = BookContainer()
container.add_book(b1)
container.add_book(b2)
container.add_book(b3)

# Create a Bookshelf and add the books (always to the beginning)
shelf = Bookshelf()
shelf.add_book(b1, 0)
shelf.add_book(b2, 0)
shelf.add_book(b3, 0)


# Tulostetaan
print("Container:")
container.list_books()

print()

print("Shelf:")
shelf.list_books()