# Conditional Statement

age: int = int(input("How old are you? "))

if age > 16:
    print("You are of age!")
    print("Here is a copy of GTA6 for you.")
else:
    print("Denied Access...")
    print("Next costumer, please!")

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