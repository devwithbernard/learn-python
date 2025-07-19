# Prompt a question and print a message

name: str = input("What is your name? ")
print("Hi there, " + name)

age: str = input("How old are You? ")
print("You are " + age + " years old.")

# More than one input
firstname: str = input("What is your firstname? ")
lastname: str = input("What is your lastname? ")
email: str = input("What is your email address? ")

print("Information about you: ")
print("Your name: " + firstname + " " + lastname)
print("Your email address: " + email)

# Exercises
"""
Write a program which asks for the user's name and then prints it twice, on two consecutive lines.
"""
username: str = input("What is your name? ")
print(username)
print(username)

"""
Write a program which asks for the user's name and address
"""
first_name: str = input("What is your first name? ")
last_name: str = input("What is your last name? ")
street: str = input("What's is your street's address? ")
city_postal: str = input("Your City and postal code? ")

print(first_name)
print(last_name)
print(street)
print(city_postal)

"""
Story programming exercise:

Write a program which prints out the following story. The user gives a name and a year, 
which should be inserted into the printout.
"""

name: str = input("Please, Enter the name: ")
year: str = input("Please, Enter the year: ")

story = f"""
{name} is a valiant knight, born in the year {year}. One morning Mary woke up to an 
awful racket: a dragon was approaching the village. Only Mary could save the
village's residents.
"""

print(story)
