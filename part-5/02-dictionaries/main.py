"""
Learn python dictionary
"""

# Dictionary

student: dict = {'name': 'John', 'age': 23, 'studies': ['Computer Science', 'Math', 'Physic', 'Politics']}

print("Name: ", student['name'])
print("Age:", student['age'], 'years old')
print("Studies:")
for index, study in enumerate(student['studies']):
    print(f"  {index}. {study}")
