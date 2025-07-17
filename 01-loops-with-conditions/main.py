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

# TODO: Numbers
number = int(input("Upper limit: "))
limit = 1

while number > limit:
    print(number - 1)
    number -= 1

# TODO: Powers of two
upper_limit = int(input("Upper limit: "))
number = 1

while number < upper_limit:
    print(number)
    number *= 2

# TODO: Powers of base n
upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))

start = 1
while start <= upper_limit:
    print(start)
    start *= base

# TODO: The sum of consecutive numbers, version 1
limit = int(input("Limit: "))
sum_of_numbers = 0

start = 1

while start <= limit:
    if sum_of_numbers >= limit:
        break

    sum_of_numbers += start
    start += 1

print("sum: ", sum_of_numbers)
