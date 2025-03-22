from typing import List


class Book:
    def __init__(self, title: str, author: str, published_date: str) -> None:
        self.title = title
        self.author = author
        self.published_date: str = published_date

    def __str__(self) -> str:
        return self.title


class BookLibrary:
    books: List[dict] = []

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


if __name__ == "__main__":
    b0: Book = Book('Hey', 'Hi', '2010/09/15')
    b1: Book = Book('Les fleurs du mal', 'Hi', '1809/03/14')
    b2: Book = Book('AI Agent', 'Daniel Altman', '2009/03/14')

    BookLibrary.add(b0)
    BookLibrary.add(b1)
    BookLibrary.add(b2)

