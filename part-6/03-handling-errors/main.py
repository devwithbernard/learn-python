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

# Until the humber is small
def read_small_number():
    while True:
        try:
            input_str = input("Please type in a small integer: ")
            number = int(input_str)

            if number <= 100:
                return number
        except ValueError as e:
            print(f"An error occurs: {e}")

        print("This input is invalid!")


number = read_small_number()
print(number, "to the power of three is", number ** 3)