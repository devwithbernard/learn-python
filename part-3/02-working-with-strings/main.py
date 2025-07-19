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

# String index
my_string = input("Enter a fruit: ")
index = 0

print(f"'{my_string}' characters: ")
while index < len(my_string):
    print(my_string[index])
    index += 1

name = "Konan"

first_char = name[0]
second_char = name[1]
last_char = name[len(name) -1]

print(f"""
In '{name}':
first character: {first_char}
second character: {second_char}
last character: {last_char}
""")

# TODO: Substrings and slices
string = "presumptious"
print(string[0:3])
print(string[4:10])
print(string[:3])
print(string[4:])

# TODO: Searching for substrings
input_string = "test"

print(f"'t' is in '{input_string}'") if 't' in input_string else print("Not in")
print(f"'x' is in '{input_string}'") if 'x' in input_string else print("Not in")
print(f"'es' is in '{input_string}'") if 'es' in input_string else print("Not in")
print(f"'ets' is in '{input_string}'") if 'ets' in input_string else print("Not in")

# Searching for a substring
word = "perpendicular"
print(f"Word: {word}")

while True:
    substring = input("What are you looking for in word? ('Q' ou 'Quit' to exit): ")
    if substring.lower() in ('q', 'quit'):
        break

    if substring in word:
        print("Found it")
    else:
        print("Not found")

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

# TODO: End the beginning
name = input("What is your name: ")
index = 1
print("Reversed name characters:")
while len(name) - index >= 0:
    print(name[-index], end=" ")
    index += 1

# TODO: Second and second to last characters
word = input("Type in a word, please: ")

if word and len(word) > 3:
    second_char = word[1]
    second_last_char = word[-2]

    if second_char == second_last_char:
        print("The second and the second to last characters are the same.")
        print("Second character: ", second_char)
    else:
        print("The second and the second to last characters are different.")
        print("Second character: ", second_char)
        print("Second to last character: ", second_last_char)
else:
    print("Word not valid")

# TODO: Underlining
string = input("Please, enter a text: ")
underlining = "-" * len(string)

print(string)
print(underlining)

# TODO: Right-aligned
string = input("Type in a string: ")

if len(string) > 20:
    print(string)
else:
    star = "*" * (20 - len(string))
    print(star + string)

# TODO: A framed word
limit = None
left_space = None
right_space = None

word = input("Word: ")

if len(word) > limit:
    limit = len(word) + 10
else:
    limit = 30

row = "*" * limit

if len(word) % 2 == 0:
    left_space = right_space = (30 - len(word) - 2) // 2
else:
    left_space = (30 - len(word) - 2) // 2
    right_space = (30 - len(word) - 2) // 2 + 1

left_white_space = " " * left_space
right_white_space = " " * right_space

print(row)
print("*" + left_white_space + word + right_white_space + "*")
print(row)

# TODO: Substrings, part 1
text = input("Please type in a string: ")

if text:
    for i in range(len(text)):
        print(text[:i + 1])

# TODO: Substrings, part 2
"""
We use the same entry as part 1
"""
if text:
    for i in range(1, len(text) + 1):
        print(text[len(text) - i:])

# TODO: Does it contain vowels
word = input("Please type in a string: ")
vowels = ("a", "e", "i", "o", "u", "y")

if word:
    for vowel in vowels:
        if vowel in word:
            print(f"{vowel} found")
        else:
            print(f"{vowel} not found")

# TODO: Find the first substring
word = None
char = None

while True:
    word = input("Please type in a word: ")
    char = input("Please type in a character: ")

    if len(word) >= 3 and len(char) == 1:
        break
    else:
        print("The word is to short")
        print("The char must be a single character")

found_index = word.find(char)
if found_index >= 0:
    if len(word[found_index:]) >= 3:
        substring = word[found_index: found_index + 3]
        print(substring)
    else:
        print("The returned substring is not valid")
else:
    print(f"'{char}' not in '{word}'")

# TODO: The second occurrence
word = None
substring = None

while True:
    word = input("Please type in a string: ")
    substring = input("Please type in a substring: ")

    if (word and substring) and (len(word) > len(substring)):
        break
    else:
        print("word or substring must be incorrect.")

first_occurrence_index = word.find(substring)

if first_occurrence_index >= 0:
    sliced_substring = word[first_occurrence_index + 1:]
    second_occurrence_index = sliced_substring.find(substring)

    if second_occurrence_index >= 0:
        print(f"The second occurrence of the substring is at index "
              f"{first_occurrence_index + second_occurrence_index + 1}")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring is not in string.")