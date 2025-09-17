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
