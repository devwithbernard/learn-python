from typing import List


class Book:
    def __init__(self, title: str, author: str, published_date: str) -> None:
        self.title = title
        self.author = author
        self.published_date: str = published_date

    def __str__(self) -> str:
        return self.title


class BookLibrary:
    books: List[Book] = []

    def add(self, book: Book) -> None:
        self.books.append(book)

    def update(self, title: str, author: str = None, published_date: str = None):
        if not title:
            return "book infos can't be updated! "

        book_titles: List[str] = [book.title.capitalize() for book in self.books]
