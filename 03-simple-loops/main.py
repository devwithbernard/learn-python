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

while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    else:
        story += word + " "
print(story.strip())
