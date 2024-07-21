"""
    Get started with python dictionary data type
"""
student = {
    'name': 'Jack Doe',
    'age': 25,
    'courses': ["Math", 'Computer science', 'Biology']
}

print(student)

# Access value
print('Name of student: ', student['name'])

if student.get('phone') is None:
    student['phone'] = '+01-185-128-855-326'
print(student)