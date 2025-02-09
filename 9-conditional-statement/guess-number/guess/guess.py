def get_player(players: list[dict]) -> dict:
    name: str = input("Your name: ")
    names: list[str] = [player['name'].lower() for player in players]

    if name.lower() in names:
        player: dict = [p for p in players if p['name'].lower() == name.lower()][0]
        return player

    return {
        'name': name,
        'score': 0,
        'attempts': 0
    }


def guess_number(player_number: int, guessed_number: int) -> bool:
    return player_number == guessed_number
