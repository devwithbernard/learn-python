"""
Learn python dictionary
"""

# Dictionary

student: dict[str, str | int | list[str]] = {
    'name': 'John',
    'age': 23,
    'studies': ['Computer Science', 'Math', 'Physic', 'Politics']
}

print("Name: ", student['name'])
print("Age:", student['age'], 'years old')
print("Studies:")
for index, study in enumerate(student['studies']):
    print(f"  {index}. {study}")

# Set key: value
student['phone'] = "+1 899 200 315"
student['studies'].append("Sociology")
student['studies'].append("Biology")

print(student)

# Traversing a dictionary
employee: dict[str, ...] = {
    'name': "Jane Smith",
    'age': 52,
    'employee_code': "1553B",
    'email': "janesmith@gmail.com",
    'role': "Manager",
    'salary': 1_200_000,
}

for key in employee:
    print("key:", key)
    print("value:", employee[key])

print()

# key:value Pair

for key, value in employee.items():
    print(f"{key}: {value}")

# Advanced ways to use dictionaries

fruits: list[str] = [
    "Apple", "Banana", "Orange", "Mango", "Strawberry",
    "Pineapple", "Grapes", "Watermelon", "Kiwi", "Peach",
    "Apple", "Blueberry", "Cherry", "Lemon", "Lime",
    "Papaya", "Coconut", "Avocado", "Pomegranate", "Raspberry",
    "Blackberry", "Plum", "Apricot", "Fig", "Banana",
    "Dragon fruit", "Passion fruit", "Lychee", "Rambutan", "Durian",
    "Orange", "Grapefruit", "Tangerine", "Mandarin", "Apple",
    "Pear", "Cantaloupe", "Honeydew", "Cranberry", "Gooseberry",
    "Elderberry", "Mulberry", "Boysenberry", "Strawberry", "Kiwi",
    "Persimmon", "Pomelo", "Star fruit", "Jackfruit", "Breadfruit",
    "Mango", "Guava", "Papaya", "Banana", "Plantain",
    "Date", "Grape", "Raisin", "Currant", "Cherry",
    "Peach", "Nectarine", "Plum", "Apricot", "Apple",
    "Pineapple", "Coconut", "Lime", "Lemon", "Orange",
    "Watermelon", "Cantaloupe", "Honeydew", "Strawberry", "Blueberry",
    "Raspberry", "Blackberry", "Kiwi", "Mango", "Papaya",
    "Acai berry", "Goji berry", "Cloudberry", "Lingonberry", "Huckleberry",
    "Jabuticaba", "Miracle fruit", "Horned melon", "Finger lime", "Buddha's hand",
    "Ugli fruit", "Cherimoya", "Soursop", "Custard apple", "Tamarind",
    "Carambola", "Longan", "Mangosteen", "Salak", "Feijoa"
]


# Count each fruit in fruits list
def counts(words: list[str]) -> dict[str, int]:
    word_counts: dict[str, int] = {}

    for word in words:
        if word not in word_counts:
            word_counts[word] = 0

        word_counts[word] += 1

    return word_counts


fruit_counts: dict[str, int] = counts(fruits)

for fruit, number in fruit_counts.items():
    print(f"{fruit} => {number} items.")


# Categorize word base of first initial
def categorize_initial(words: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}

    for word in words:
        initial = word[0].upper()

        if initial not in groups:
            groups[initial] = []

        groups[initial].append(word)

    return groups


categories: dict[str, list[str]] = categorize_initial(fruits)

for category, fruits in categories.items():
    print(f"{category}: ")
    for index, fruit in enumerate(fruits):
        print(f" {index + 1}. {fruit}")