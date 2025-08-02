from . import user, guess_number

username: str = user.get_username()

guessed_number: int = guess_number.generate_random_number(10)
GAME: dict[str, int] = {"win_tours": 0, "fail_tour": 0}
user: dict[str, int] = user.user_infos(username)


def win_or_lose(input_number: int) -> None:
    random_number: int = guess_number.generate_random_number(10)
    if guess_number.is_correct(input_number, random_number):
        GAME['win_tours'] += 1
        user['score'] += 10
        print("You guess the mystery number 😊!")
    else:
        GAME['fail_tour'] += 1
        print("You failed to guess mystery number!")


def play() -> None:
    while True:
        user_input: int = int(input("Guess the number (or 0 to exit): "))
        if user_input == 0:
            break
        win_or_lose(user_input)

    essay = GAME["win_tours"] + GAME["fail_tour"]

    print(f"""
    -------------- GUESS NUMBER GAME ----------------
    Player: {user["username"]}
    Total essay: {essay}
    Fail tour: {GAME["fail_tour"]}
    Win tour: {GAME["win_tour"]}
    Total Score: {user["score"]}
    """)


if __name__ == "__main__":
    play()