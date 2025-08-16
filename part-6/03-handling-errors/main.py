"""
Handling errors
"""

# Input validation
age: int = int(input("Please type in your age: "))

if 0 <= age <= 150:
    print("That is a fine age")
else:
    print("This is not a valid age")