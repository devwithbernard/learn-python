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


# TODO: Climbing Route

class ClimbingRoute:
    def __init__(self, name: str, length: float, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


def sort_by_length(routes: list[ClimbingRoute]):
    def by_length(route: ClimbingRoute):
        return route.length

    return sorted(routes, key=by_length, reverse=True)

r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]

for route in sort_by_length(routes):
    print(route)