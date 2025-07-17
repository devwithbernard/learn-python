# TODO: Initialisation, condition and update

number = int(input("Please type in a number: "))  # Initialisation

while number < 10:  # Condition
    print(number)
    number += 1

print("Execution finished.")

# TODO: Writing conditions

number = int(input("Please, type in a number: "))

while number < 100 and number % 5 != 0:  # Condition
    print(number)
    number += 3


"""
Exercises
"""

# TODO: Print numbers
number = 2

while number <= 30:
    print(number)
    number += 1

# TODO: Fix the code: Countdown
print("Are you ready?")
number = int(input("Please type in a number"))

while number > 0:
    print(number)
    number -= 1

print("Now!")
