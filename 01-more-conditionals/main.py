# Else statement

number = int(input("Please type in a number: "))

if number < 0:
    print("The number is negative")

if number >= 0:
    print("The number is positive or zero")

# Write previous program with else statement

new_number = int(input("Please type in a new number: "))

if new_number < 0:
    print(f"{new_number} is negative")
else:
    print(f"{new_number} is positive or zero")

# Alternative branches using elif statement
goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("The home team won!")
elif goals_away > goals_home:
    print("The way team won!")
else:
    print("It's a tie!")

# Exercises
"""
Age of maturity
"""

age = int(input("How old are you? "))

if age < 0:
    print("You are not born!")
elif age < 18:
    print("You are not of age!")
else:
    print("You are of age!")

"""
Greater than or equal to
"""

first_number = int(input("Please type in the first number: "))
second_number = int(input("Please type in another number: "))

if first_number > second_number:
    print(f"The greater number was: {first_number}")
elif second_number > first_number:
    print(f"The greater number was: {second_number}")
else:
    print(f"The numbers are equal!")

"""
The elder
"""

print("Person 1:")
person1_name = input("Name: ")
person1_age = int(input("Age: "))
print("Person 2:")
person2_name = input("Name: ")
person2_age = int(input("Age: "))

if person1_age > person2_age:
    print(f"The elder is {person1_name}")
elif person2_age > person1_age:
    print(f"The elder is {person2_name}")
else:
    print(f"{person1_name} and {person2_name} are the same age.")

"""
Alphabetically last
"""

first_word = input("Please type in the 1st word: ")
second_word = input("Please type in the 2nd word: ")

if first_word.lower() > second_word.lower():
    print(f"{first_word} comes alphabetically last.")
elif second_word.lower() > first_word.lower():
    print(f"{second_word} comes alphabetically last.")
else:
    print("You gave the same word twice.")
