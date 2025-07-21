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

# TODO: Another version
sum_of_numbers = 0
while True:
    number = int(input("Please type in a number, -1 to exit: "))

    if number == -1:
        break
    sum_of_numbers += number
    if sum_of_numbers >= 100:
        break
print(f"The sum is {sum_of_numbers}")

# TODO: The continue command
positive_sum = 0

while True:
    number = int(input("Enter a positive number, -1 to exit: "))

    if number == -1:
        break

    if number < 0 and number != -1:
        print("Number not authorized!")
        continue

    positive_sum += number

print(f"The sum of positive numbers is {positive_sum}")

# TODO: Nested loops
number = int(input("Enter a number: "))
while number > 0:
    i = 0
    while i < number:
        print(f"{i}", end=" ")
        i += 1
    print()
    number -= 1

# Exercises

# TODO: multiplication
number = int(input("Please type in a number: "))
i = 1
while i <= number:
    j = 1
    while j <= number:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1

# TODO: First letters of words
sentence = input("Please type in a sentence: ").strip()
index = 1

print(sentence[0])
while index < len(sentence):
    if sentence[index].strip() == "":
        print(sentence[index + 1])

    index += 1
