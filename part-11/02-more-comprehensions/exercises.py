# TODO: Filter forbidden
def filter_forbidden(text: str, forbidden: str):
    def filter_character(word):
        return "".join([character for character in word if character.lower() not in forbidden.lower()])

    return " ".join([filter_character(word) for word in text.split(" ")])

sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)

# TODO: Products in shopping list

class Product:
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"Product: {self.name}, ${self.amount:,d.2}"


class ShoppingList:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product_name: str, amount: int):
        product = Product(product_name, amount)
        self.products.append(product)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration


def products_in_shopping_list(shopping_list: ShoppingList, amount: int):
    return [product.name for product in shopping_list if product.amount >= amount]


my_list = ShoppingList()
my_list.add("bananas", 10)
my_list.add("apples", 5)
my_list.add("alcohol free beer", 24)
my_list.add("pineapple", 1)

print("the shopping list contains at least 8 of the following items:")
for product in products_in_shopping_list(my_list, 8):
    print(product)


# TODO: Price difference of cheaper properties

class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int, description: str):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
        self.description = description


def cheaper_properties(properties: list[RealProperty], property: RealProperty):
    return [p for p in properties if p.price_per_sqm > property.price_per_sqm]

a1 = RealProperty(1, 16, 5500, "Central studio")
a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
a5 = RealProperty(4, 105, 1700, "Loft in a small town")
a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

properties = [a1, a2, a3, a4, a5, a6]

print(f"cheaper options when compared to {a3.description}:")
for item in cheaper_properties(properties, a3):
    print(f"{item.description:35} price difference {item.price_per_sqm - a3.price_per_sqm} euros")

# TODO: Lengths of strings

def lengths(strings: list[str]) -> dict[str, int]:
    return {string: len(string) for string in strings}

word_list = ["once", "upon" , "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)

# TODO: Most common words
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        lines = [line.replace("\n","").replace(".", "").replace(',', "") for line in f]
        split_words = " ".join(lines).lower().split(" ")

        words = {word: split_words.count(word) for word in split_words if split_words.count(word) >=
                 lower_limit}
        return words


print(most_common_words("text.txt", 3))