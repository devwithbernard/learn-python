"""
Reading data from a file
"""

# Read the contents of a file

with open("files/example.txt") as file:
    contents = file.read()
    print(contents)

# Going through the contents of a file

with open("files/example.txt") as f:
    count_line = 0

    for line in f:
        count_line += 1
        print(f"Line {count_line}:", line.replace("\n",""))