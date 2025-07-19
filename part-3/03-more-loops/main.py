# TODO: The break command

# 1st version using the break command
sum_of_numbers = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))

    if number == -1:
        break

    sum_of_numbers += number

print(f"The sum is{sum_of_numbers}")

# 2nd version with the break command
sum_of_numbers = 0
number = 0

while number != -1:
    number = int(input("Please type in a number, -1 to exit: "))

    if number != -1:
        sum_of_numbers += number

print(f"The sum is {sum_of_numbers}")
