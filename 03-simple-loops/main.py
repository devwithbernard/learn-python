# While Loops

while True:
    number = int(input("Please, type in a number, -1 to quit: "))

    if number == -1:
        break

    print(f"n² = {number**2}")

print(f"Thanks and bye!")

# While loop: PIN Code
while True:
    code = input("Enter your PIN: ")
    if code == "1234":
        break
    print("Incorrect...Try again")
print("Correct PIN entered!")

# Exercises
"""
Shall we continue?
"""
while True:
    print("hi")
    yesno = input("Shall we continue? ")
    if yesno.lower() == "no":
        break
print("Okay then")

"""
Input validation
"""
while True:
    number = int(input("Please type in a number: "))

    if number < 0:
        print("Invalid number")
    elif number == 0:
        break
    else:
        print(number**2)

print("Exiting...")

"""
Repeat password
"""
password = input("Password: ")

while True:
    repeated_password = input("Repeat password: ")

    if password == repeated_password:
        print("User account created!")
        break
    else:
        print("They do not match!")

"""
Story
"""
story = ""

previous_word = ""
while True:
    word = input("Please type in a word: ")
    if word == previous_word or word == "end":
        break
    else:
        story += word + " "
        previous_word = word

print(story.strip())

"""
Working with numbers
"""
print("Please type in integer numbers. Type in 0 to finish.")

number_typed = 0
count_positive_numbers = 0
count_negative_numbers = 0
sum_of_numbers = 0

while True:
    number = int(input("Number: "))
    number_typed += 1
    sum_of_numbers += number

    if number == 0:
        break

    if number > 0:
        count_positive_numbers += 1
    else:
        count_negative_numbers += 1

if number_typed > 0:
    # Part: Count, Sum, Mean
    print("... The program asks for numbers")
    print(f"Numbers typed in {number_typed}")
    print(f"The sum of the numbers is {sum_of_numbers}")
    print(f"The mean of the number is {sum_of_numbers/number_typed:,.1f}")
    print(f"Positive numbers {count_positive_numbers}")
    print(f"Negative numbers {count_negative_numbers}")
