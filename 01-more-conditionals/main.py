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