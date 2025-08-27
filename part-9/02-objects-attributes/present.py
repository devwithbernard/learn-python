class Present:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return f"Present: {self.name} ({self.weight} kg)"

