"""
Handling errors
"""

# Input validation
age: int = int(input("Please type in your age: "))

if 0 <= age <= 150:
    print("That is a fine age")
else:
    print("This is not a valid age")

# Exceptions
try:
    my_age: int = int(input("Please type in your age: "))
except ValueError:
    my_age = -1

if 0 <= my_age <= 150:
    print(f"{my_age} is a fine age")
else:
    print(f"{my_age} is not a valid age")