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