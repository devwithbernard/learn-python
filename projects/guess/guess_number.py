from random import choice

MAX_INTERVAL: int = 10


def generate_random_number(max_interval=None) -> int:
    if max_interval is None:
        max_interval = MAX_INTERVAL
    return choice(range(1, max_interval + 1))


def is_correct(input_number: int, random_number: int) -> bool:
    return input_number == random_number
