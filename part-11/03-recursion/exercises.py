"""
Exercises: Recursion
"""


# TODO: Add numbers to a list

def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        max_number = max(numbers)
        numbers.append(max_number + 1)
        add_numbers_to_list(numbers)


numbers = [1, 3, 4, 5, 10, 11]
add_numbers_to_list(numbers)
print(numbers)


# TODO: Recursive sum
def recursive_sum(number: int):
    if number <= 1:
        return number
    return number + recursive_sum(number - 1)


print("sum from 1 to 20:", recursive_sum(20))

# TODO: Balance all the brackets

def balanced_brackets(my_string: str) -> bool:
    filtered = "".join([ch for ch in my_string if ch in "()[]"])

    # Base case: empty string
    if not filtered:
        return True

    # If the length has odd length, it can't be balanced
    if len(filtered) % 2 != 0:
        return False

    # If we find "()" or "[]", remove it and recurse
    if "()" in filtered:
        return balanced_brackets(filtered.replace("()", "", 1))

    if "[]" in filtered:
        return balanced_brackets(filtered.replace("[]", "", 1))

    # Not valid pairs found -> not balanced
    return False

# Tests
print(balanced_brackets("(((())))"))        # True
print(balanced_brackets("()())"))           # False
print(balanced_brackets(")()"))             # False
print(balanced_brackets("()(())"))          # True
print(balanced_brackets("[()]"))            # True
print(balanced_brackets("[(])"))            # False
print(balanced_brackets("([][])"))          # True
print(balanced_brackets("(hello [world])")) # True
