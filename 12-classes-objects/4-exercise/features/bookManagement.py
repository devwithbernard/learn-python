from typing import List


class Book:
    def __init__(self, title: str, author: str, published_date: str, category: str = None) -> None:
        self.title = title
        self.author = author
        self.published_date = published_date
        self.category = category

    def __str__(self) -> str:
        return self.title


class BookLibrary:
    books: List[dict] = []
    categories: dict = {}

    @classmethod
    def add(cls, book: Book) -> None:
        cls.books.append(book.__dict__)

    @classmethod
    def update(cls, title: str, author: str = None, published_date: str = None):
        if not title:
            print("book infos can't be updated! ")
            return None

        book_titles: List[str] = [book['title'].upper() for book in cls.books]

        if title.upper() not in book_titles:
            print(f"Book titled '{title}' is not in library!")
            return None

        book_infos = list(filter(lambda book: book['title'].capitalize() == title.capitalize(), cls.books))[0]

        book_infos['title'] = title

        if author:
            book_infos['author'] = author
        if published_date:
            book_infos['published_date'] = published_date

    @classmethod
    def delete(cls, title: str) -> None:
        if not title:
            print("Provide valid title for deleting book")
            return None

        book_titles: List[str] = [book['title'].upper() for book in cls.books]

        if title.upper() not in book_titles:
            print(f"No book titled '{title}'\nIt can't be deleted!")
            return None

        cls.books = [book for book in cls.books if book['title'].upper() != title.upper()]

    @classmethod
    def categorize_books(cls):
        for book in cls.books:
            category: str = book['category']

            if category not in cls.categories:
                cls.categories[category] = []

            cls.categories[category].append(book)

    @classmethod
    def search(cls, title: str, author: str = None):
        if not title or not author:
            print("No book found!")

        found_books: List[dict] = [book for book in cls.books if book['title'].upper() == title.upper()]
        number_of_books_found: int = len(found_books)

        if number_of_books_found > 0:
            print(f"{number_of_books_found} found!")
            for found_book in found_books:
                print(f"{found_book['author']} => {found_book['title']}")
        else:
            print("No book found!")

        if author and title:
            found_books_by_author: List[dict] = [book for book in cls.books if book['author'].upper() == author.upper()]
            if found_books_by_author:
                print(found_books_by_author)


if __name__ == "__main__":
    b0: Book = Book('Hey', 'Hi', '2010/09/15', 'Fiction')
    b1: Book = Book('Les fleurs du mal', 'Hi', '1809/03/14', 'Tragedy')
    b2: Book = Book('AI Agent', 'Daniel Altman', '2009/03/14', 'AI')

    BookLibrary.add(b0)
    BookLibrary.add(b1)
    BookLibrary.add(b2)

    BookLibrary.categorize_books()

    print(BookLibrary.categories)
