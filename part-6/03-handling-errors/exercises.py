"""
Handling errors: Exercise
"""


# TODO: Reading input

def read_input(message: str, left_bound: int, right_bound: int) -> float:
    if left_bound > right_bound:
        right_bound, left_bound = left_bound, right_bound

    if left_bound == right_bound:
        raise ValueError(f"'{left_bound}' must be less than '{right_bound}'")

    while True:
        try:
            input_str = input(message)
            number = int(input_str)

            if left_bound <= number <= right_bound:
                return number
        except ValueError as e:
            print(f"An error occurs:{e}")

        print(f"You must type in a integer between {left_bound} and {right_bound}.")


number = read_input("Please type in a number:", 5, 10)
print("You typed in:", number)