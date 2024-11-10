from random import randint


class Game:
	number_of_games: int = 0
	starting: bool = False

	def increment_number_of_games(self) -> None:
		self.number_of_games += 1

	def end_game(self) -> None:
		self.starting = False

	def __str__(self) -> str:
		return f"Game(number_of_games={self.number_of_games}, starting={self.starting})"


class Player:
	score: int = 0
	lives: int = 10

	def __init__(self, name: str) -> None:
		self.name = name

	def __str__(self) -> str:
		return f"Player(name={self.name}, lives={self.lives}, score={self.score})"

	def change_score(self, score: int) -> None:
		self.score += score

	def change_lives(self, lives: int) -> None:
		self.lives += lives


def get_player() -> Player:
	name: str = ''

	while len(name) < 4:
		name = input("Enter your name: ")
		if len(name) >= 4:
			break
		else:
			print("Player name is not valid.\nRetry please!")

	player: Player = Player(name)

	return player


def generate_random_number(min: int, max: int) -> int:
	"""
	Generate a random number between two numbers
	:return: Return the random number between min and max (include)
	"""
	return randint(min, max)


def continue_or_not() -> bool:
	yes_or_no: str = input("Would want to continue (yes/no)? ")
	if yes_or_no.lower() in ['y', 'yes']:
		return True
	return False


def play():
	instructions: str = """
	Welcome to the “guess the number” game.
	The principle of the game is simple. In each round, you must guess a random number between 0 and 10. 
	If you win, you get 10 points and an extra life; if you don't, you lose a life.
	The game ends when your life level reaches zero.
	Remember that you start with 10 lives.
	Ready??? Play!!!
	"""
	print(instructions + "\n")

	# Ask player name
	player: Player = get_player()

	# generate number to guess
	number_to_guess: int = generate_random_number(0, 10)

	# Start the game
	game: Game = Game()
	game.starting = True

	while game.starting:
		try:
			player_number: int = int(input("Guess the number: "))
			game.increment_number_of_games()

			if player_number == number_to_guess:
				print("Bingo!!\nYou guess the correct number")
				player.change_lives(1)
				player.change_score(10)
				number_to_guess = generate_random_number(0, 10)
			else:
				print("You're wrong!\nContinue...")
				player.change_lives(-1)

			if player.lives == 0:
				game.end_game()

			if game.number_of_games % 3 == 0 and player.lives > 0:
				continue_game: bool = continue_or_not()
				if not continue_game:
					game.end_game()
		except ValueError as error:
			print("Your entry isn't correct.\n")
			print("Enter a number please!")

	if not game.starting:
		print(f"""
		Game
		    Games play: {game.number_of_games}
		Player
		    Name: {player.name}
		    Lives left: {player.lives}
		    Score made: {player.score}
		""")


def main() -> None:
	play()


if __name__ == '__main__':
	main()
