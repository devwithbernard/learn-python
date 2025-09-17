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


# TODO: BallPlayers

class BallPlayer:
    """ This class models a single ball player """

    def __init__(self, name: str, shirt_number: int, goals: int, assists: int, minutes: int):
        self.name = name
        self.number = shirt_number
        self.goals = goals
        self.assists = assists
        self.minutes = minutes

    def __str__(self):
        return (f"BallPlayer(name={self.name}, number={self.number}, goals={self.goals}, passes={self.assists}, "
                f"minutes={self.minutes})")


def most_goals(ball_players: list[BallPlayer]):
    player = max(ball_players, key=lambda ball_player: ball_player.goals)
    return player.name


def most_points(ball_players: list[BallPlayer]) -> tuple[str, int]:
    player = max(ball_players, key=lambda ball_player: ball_player.goals + ball_player.assists)
    return player.name, player.number


def least_minutes(ball_players: list[BallPlayer]):
    return min(ball_players, key=lambda ball_player: ball_player.minutes)


print()

player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)

team = [player1, player2, player3, player4, player5]
print(most_goals(team))
print(most_points(team))
print(least_minutes(team))
