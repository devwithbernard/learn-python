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