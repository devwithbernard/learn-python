# Logical operators

number = int(input("Please type in a number: "))

if (number >= 5) and (number <= 8):
    print(f"The number is between 5 and 8.")

if (number < 5) or (number > 8):
    print("The number is not within the range of 5 to 8.")

# Combining and chaining conditions
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

greatest = None

if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
if n2 > n3 and n2 > n4:
    greatest = n2
if n3 > n4:
    greatest = n3
else:
    greatest = n4

print(f" {greatest} is the greatest of the numbers")

# Nested conditionals

number = int(input("Please type in the a number: "))

if number > 0:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
else:
    print("The number is negative or zero.")

# Exercises
"""
Age check
"""

age = int(input("What is your age? "))

if age <= 0:
    print("That must be a mistake.")
elif age < 10:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")

"""
Grades and points
"""
points = int(input("How many points [0-100]: "))
grade = None

if points < 0 or points > 100:
    grade = "impossible!"
elif 0 <= points <= 49:
    grade = "fail"
elif 50 <= points <= 59:
    grade = 1
elif 60 <= points <= 69:
    grade = 2
elif 70 <= points <= 79:
    grade = 3
elif 80 <= points <= 89:
    grade = 4
elif 90 <= points <= 100:
    grade = 5

print(f"Grade: {grade}")

"""
FizzBuzz
"""

number = int(input("Number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
