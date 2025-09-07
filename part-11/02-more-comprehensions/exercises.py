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
