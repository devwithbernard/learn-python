"""
Objects and Methods
"""

# Group Data

name = "In Search of lost Typing"
author = "Marcel Pythons"
year = 1992

# Combine these in tuple
book = (name, author, year)

print("Name of book:", book[0])

# combine these in dictionary
new_book = {'name': name, 'author': author, 'year': year}

for key, item in new_book.items():
    print(f"{key}: {item}")