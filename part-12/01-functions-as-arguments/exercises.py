# TODO: Sort by remaining stock

def sort_by_remaining_stock(items: list[tuple[str, float, int]]):
    def order_by_remaining_stock(item: tuple[str, float, int]):
        return item[-1]

    return sorted(items, key=order_by_remaining_stock)


products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

for product in sort_by_remaining_stock(products):
    print(f"{product[0]} {product[2]} pcs")


# TODO: Sort by number of seasons

def sort_by_seasons(items: list[dict]):
    return sorted(items, key=lambda item: item['seasons'])


shows = [{"name": "Dexter", "rating": 8.6, "seasons": 9}, {"name": "Friends", "rating": 8.9, "seasons": 10},
         {"name": "Simpsons", "rating": 8.7, "seasons": 32}]

for show in sort_by_seasons(shows):
    print(f"{show['name']} {show['seasons']} seasons")
