class Player:
    def __init__(self, name: str, goals: int) -> None:
        self.name = name
        self.goals = goals

    def __str__(self) -> str:
        return f"Player: {self.name}, {self.goals} goals"
