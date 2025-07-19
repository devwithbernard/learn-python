"""
Working with strings
"""

# TODO: String concatenation

begin = "Exam"
end = "ple"
word = begin + end

print("Final word: " + word)

# TODO: String Repetition
fruit = "Banana"

print(f"Repeat '{fruit}' 3 times: {fruit * 3}")

# Build pyramid with string repetition
base = 10
row = "*"

while base > 0:
    print(" " * base + row)
    row += "**"
    base -= 1

# Build rectangle with string repetition
length = 5
width = 2 * length + 10
row = " * "
while length > 0:
    print(row * width)
    length -= 1

# Build isosceles triangle
base = 5
row = 0
while row < 5:
    space = " " * (base - row + 1)
    stars = "*" * (2 * row + 1)
    print(space + stars)
    row += 1
