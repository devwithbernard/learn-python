# Conditional Statement

age: int = int(input("How old are you? "))

if age > 16:
    print("You are of age!")
    print("Here is a copy of GTA6 for you.")
else:
    print("Denied Access...")
    print("Next costumer, please!")

# Comparison operators
number = int(input("Please type a number: "))

if number < 0:
    print("The number is negative.")
elif number > 0:
    print("The number is positive.")
elif number == 0:
    print(print("The number is zero."))

# Exercise
"""
Write a program and check if a student can pass to next class
"""

name: str = input("Enter your name: ")
mean: float = float(input("Enter your class mean/20: "))

if mean < 0:
    print("You entered a negative value!")
elif mean < 10:
    print(f"😥😥 Sorry {name}!")
    print("Your mean is too low for next class.")
elif mean <= 20:
    print(f"✨✨ Congratulations {name}!")
    print("You pass to next class.")
else:
    print("⛔ Mean must be lower or equal to 20.")

"""
Write a program which asks the user for an integer number.
The program should print out "Orwell" if the number is exactly 1984, and otherwise dot nothing.
"""

entry_number = int(input("Please type the number: "))

if entry_number == 1984:
    print("Orwell")

"""
The Absolute Value
"""
print("---- THE ABSOLUTE VALUE ----")
user_entry = int(input("Please type in a number: "))

if user_entry < 0:
    print(f"Absolute value: {-1 * user_entry}")
else:
    print(f"Absolute value: {user_entry}")

"""
Soup or no soup
"""

username = input("Please tell me your name: ")
portion_price = 5.90

if username.lower() != "jerry":
    portion_quantity = int(input("How many portions of soup? "))
    total = portion_price * portion_quantity

    print(f"The total cost is {total:,.2f}")

print("Next please!")

number = int(input("Please a number: "))
quotient = number // 10
message = ""

if number >= 0:
    if quotient >= 10:
        message = "This number is smaller than 1000"
    elif quotient >= 1:
        message = """
This number is smaller than 1000
This number is smaller than 100"""
    elif quotient == 0:
        message = """
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10"""
    print(message)
    print("Thank you!")
else:
    print("Negative number not allowed!")



