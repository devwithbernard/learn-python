# Sort a list based on default criteria: first item of tuple

products: list[tuple[str, float]] = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

sorted_products = sorted(products)

for product in sorted_products:
    print(f"{product[0]}: ${product[1]}")

print()