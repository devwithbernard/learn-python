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

    def add(self, book: Book) -> None:
        self.books.append(book.__dict__)

    def update(self, title: str, author: str = None, published_date: str = None):
        if not title:
            return "book infos can't be updated! "

        book_titles: List[str] = [book['title'].capitalize() for book in self.books]

        if title.capitalize() not in book_titles:
            return "Book not in database!"

        book_infos = dict(filter(lambda book: book['title'].capitalize() == title.capitalize(), self.books))

        book_infos['title'] = title

        if author:
            book_infos['author'] = author
        if published_date:
            book_infos['published_date'] = '2025'


if __name__ == "__main__":
    b: Book = Book('Hey', 'Hi', '1809/03/14')
