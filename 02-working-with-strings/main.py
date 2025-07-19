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

# TODO: The length and index of a string

input_string = input("Please type in a string: ")
print(input_string)
print("length:", len(input_string))
print("-" * len(input_string))

"""
Exercise
"""

# TODO: String multiplied
string = input("Please type in a string: ")
amount = int(input("Please type i an amount: "))

print(string * amount)

# TODO: The longest string
strings = ""
stop = False

while not stop:
    string = input("Type in a string ('Q' or 'Quit' to exit): ")

    if string.lower() in ('q', 'quit'):
        stop = True

    if not stop:
        strings += f"{string}, "

if len(strings):
    words = strings.strip(", ").split(", ")
    longest_word = max(words, key=len)
    print("The longest word of strings: ")
    print(f"word: {longest_word}\nlength: {len(longest_word)}")

