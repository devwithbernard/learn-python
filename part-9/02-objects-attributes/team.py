from player import Player

class Team:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: list[Player] = []

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def summary(self) -> None:
        goals: list[int] = []

        for player in self.players:
            goals.append(player.goals)

        print("Team:", self.name)
        print(f"The team has {len(self.players)} players")
        print(f"Total goals: {sum(goals)}")