import random


def try_list():
    some_list = ['Python', 'Java', 'C#', [1, 2, 3], 1 + 3j, 5 - 2j]
    print("A list => ", some_list)

    if isinstance(some_list, list):
        print('This is a list.')

    # type of list
    print(type(some_list))

    # Concatenation and multiplication
    integers: list[int] = [1, 2, 3]
    real_numbers: list[float] = [4.0, 5.0, 6.0]

    numbers: list[float] = list(map(lambda number: float(number), integers)) + real_numbers
    print(numbers, type(numbers))


def register_player() -> dict:
    name: str = input('Enter your name: ')
    player: dict[str, str] | dict[str, int] = {'name': name, 'score': 0}
    return player


def randomGuessNumber(min_value: int, max_value: int) -> int:
    return random.choice(range(0, 11))


def is_guessed(userNumber: int, numberToGuess: int) -> bool:
    return userNumber == numberToGuess


def guessNumber():
    INITIAL_NUMBER = 0
    LIMIT_NUMBER = 10

    player = register_player()
    guessedNumber = randomGuessNumber(INITIAL_NUMBER, LIMIT_NUMBER)

    game = {
        'essai': 0,
        'guessTimes': 10,
    }

    while game.get('guessTimes') > 0:
        game['essai'] += 1
        print("Guess Number is between 0 and 10")
        try:
            userNumber = int(input('Guess the number'))
            game['guessTimes'] -= 1
            if is_guessed(userNumber, guessedNumber):
                player['score'] += 10
                print('You won 1Opts!')
                guessedNumber = randomGuessNumber(INITIAL_NUMBER, LIMIT_NUMBER)
        except ValueError as error:
            print('The entered number is incorrect!')
            print('Please retry')

    print('player => ', player)
    print('game => ', game)


def main():
    try_list()
    guessNumber()


if __name__ == '__main__':
    main()
