class Player:
    name: str = ""
    score: int = 0
    attempts: int = 0

    def __init__(self, name: str, score: int, attempts: int) -> None:
        self.name = name
        self.score = score
        self.attempts = attempts

    def __str__(self) -> str:
        return self.name

    def __dict__(self) -> dict:
        return {
            "name": self.name,
            "score": self.score,
            "attempts": self.attempts
        }

    def win(self) -> None:
        self.score += 10

    def lost(self) -> None:
        self.score -= 5
