"""
More comprehensions
"""

# Comprehensions with strings

name = "Peter Python"

uppercased = [character.upper() for character in name]
print(uppercased)

# Replace vowels with *
test_string = "Hello there, this is a test!"

test_string_after_replacing = ['*' if character.lower() in 'aeiouy' else character for character in test_string]
new_string = "".join(test_string_after_replacing)

print(new_string)

# Text with no initials
sentence = "Sheila keeps on selling seashells on the seashore"
text_with_no_initials = " ".join( word[1:] for word in sentence.split(" "))
print(text_with_no_initials)

# Own classes and comprehensions
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __str__(self):
        return f"Country: {self.name}, {self.population:,d}"

finland = Country("Finland", 6000000)
malta = Country("Malta", 500000)
sweden = Country("Sweden", 10000000)
iceland = Country("Iceland", 350000)

countries = [finland, malta, sweden, iceland]

populated_countries = [country.name for country in countries if country.population >= 5_000_000]
print("Populated countries: ")
for country in populated_countries:
    print("- ",country)

# Running Event
class RunningEvent:
    def __init__(self, length: int, name: str = "No name"):
        self.length = length
        self.name = name

    def __repr__(self):
        return f"RunningEvent(length={self.length}, name={self.name})"


lengths = [100, 200, 1500, 3000, 42195]
events = [RunningEvent(length) for length in lengths]

marathon = events[-1]
marathon.name = "Marathon"

print(events)

# Book shelf
class Book:
    def __init__(self, name: str, author: str, page_count: int):
        self.name = name
        self.author = author
        self.page_count = page_count

    def __str__(self):
        return f"Book: {self.name} by {self.author}, {self.page_count} pages"

class Bookshelf:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.books):
            book = self.books[self.n]
            self.n += 1
            return book
        else:
            raise StopIteration

b1 = Book("The Life of Python", "Montague Python", 123)
b2 = Book("The Old Man and the C", "Ernest Hemingjavay", 204)
b3 = Book("A Good Cup of Java", "Caffee Coder", 997)

shelf = Bookshelf()
shelf.add_book(b1)
shelf.add_book(b2)
shelf.add_book(b3)

# Create a list containing the names of all books
for book in shelf:
    print(book)


# Comprehensions and dictionaries
sentence = "hello there"

char_counts = {character: sentence.count(character) for character in sentence}

for character, char_count in char_counts.items():
    print(f"{character}: {char_count}")


def factorial(n: int):
    k = 1
    while n >= 2:
        k *= n
        n -= 1

    return k

numbers = [-2, 3, 2, 1, 4, -10, 5, 1, 6]
factorials = {number : factorial(number) for number in numbers if number > 0}
print(factorials)