# Sort a list based on default criteria: first item of tuple

products: list[tuple[str, float]] = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

sorted_products = sorted(products)

for product in sorted_products:
    print(f"{product[0]}: ${product[1]}")

print()


# Functions as arguments: Sort list based on custom criteria

def order_by_price(product: tuple[str, float]) -> float:
    return product[1]


products_order_by_price = sorted(products, key=order_by_price)

for product in products_order_by_price:
    print(f"{product[0]}: ${product[1]}")

print()

# A function definition within a function definition

persons: list[tuple[str, int]] = [('Bryan', 28), ('Jane', 15), ('Merlin', 17), ('Mark', 23)]


def sort_by_age(items: list[tuple[str, int]]) -> list[tuple[str, int]]:
    def order_by_age(item: tuple[str, int]) -> int:
        return item[1]

    return sorted(items, key=order_by_age)


persons_order_by_age = sort_by_age(persons)

for person in persons_order_by_age:
    print(f"{person[0]}: {person[1]} years old.")

print()
