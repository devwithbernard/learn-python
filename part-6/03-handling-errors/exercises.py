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

# TODO: Parameter Validation

def new_person(name: str, age: int) -> tuple[str, int]:
    """
    Return a tuple containing the name and the age of a person

    Args:
        name (str): The name of a person.
        age (int): The age of a person

    Returns:
        tuple[str, int]: A tuple containing in first position the name and in second position the age

    Raises:
        ValueError: If either name or age is not valid.
    """

    if not name:
        raise ValueError('Name must not be an empty string.')

    if len(name) < 2:
        raise ValueError("Name contains less than 2 characters.")

    if len(name) > 40:
        raise ValueError("Name is too long. More than 40 characters.")

    if age < 0:
        raise ValueError("Age must a positive number.")

    if age > 150:
        raise ValueError("Age must be less than 150.")

    return name, age

print(new_person("Luigi", 23))
print(new_person("M", 12))
print(new_person("Jack", -12))