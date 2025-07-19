# Changing the value of a variable

word: str = input("Type a word: ")
print(word)

word = input("Type another word: ")
print(word)

word = "Third"
print(word)

# Integers
age: int = 28

print(age)
print(f"Type of '{age}' =>", type(age))

number1 = 100
number2 = "100"

print(number1 + number1)  # 200
print(number2 + number2)  # 100100

# Combining values when printing
result = 25 * 10
print("The result is " + str(result))

product = input("Product name: ")
price = float(input("Product price: "))
quantity = int(input("Product quantity: "))

print(f"Product: {product}")
print(f"Price:   ${price}")
print(f"Quantity: {quantity}")
print(f"Total price: ${price * quantity}")


# Floating Numbers
PI: float = 3.1415
circle_radius: float = 2.5

circle_area: float = round(PI * circle_radius * circle_radius, 2)

print(f"The area of circle which radius is {circle_area}cm is: {circle_radius}cm2.")
