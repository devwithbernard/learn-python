from random_number import random_number
from player.player import Player
from save_data import save_data
from guess.guess import guess_number, get_player


def main() -> None:
    players = save_data.load()
    player_data: dict = get_player(players)
    player: Player = Player(player_data['name'], player_data['score'], player_data['attempts'])
    start_game: bool = False
    guessed_number: int = random_number.generate_random_number()

    print("......Game starts........")

    while not start_game:
        player.attempts += 1

        player_guessed_number: int = int(
            input(f"Guess the number between {random_number.MIN_NUMBER} and {random_number.MAX_NUMBER}: ")
        )

        if guess_number(player_guessed_number, guessed_number):
            print("You win 10 pts")
            player.win()
            guessed_number = random_number.generate_random_number()
        else:
            print("You lost 5 pts")
            player.lost()

        if player.attempts % 5 == 0:
            continue_or_not: str = input("End of game: (y/yes or n/not)")
            if continue_or_not.lower() in ['y', 'yes']:
                start_game = True
            else:
                print("Game continue!!")

    print("...... End of Game .......")
    print(f"""
    Player:
      Name     => {player.name}
      Score    => {player.score}
      Attempts => {player.attempts}
    """)

    player_names: list[str] = [p.get('name') for p in players]

    if player.name in player_names:
        index_player: int = player_names.index(player.name)
        print(index_player)
        players[index_player] = player.__dict__()
    else:
        players.insert(0, player.__dict__())

    save_data.save(players)


if __name__ == '__main__':
    main()
