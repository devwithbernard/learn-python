"""
    Get started with python dictionary data type
"""
student = {
    'name': 'Jack Doe',
    'age': 25,
    'courses': ["Math", 'Computer science', 'Biology']
}

# print(student)
#
# # Access value
# print('Name of student: ', student['name'])
#
# if student.get('phone') is None:
#     student['phone'] = '+01-185-128-855-326'
#
# student['name'] = 'John'
#
# # update key values
# student.update({"name": 'Jack Doe', 'phone': '+225-07-694-543-35'})
#
# print(student)
#
# # delete key
# del student['age']
#
# print("New student infos: ", student)

# Number of keys
print('number of keys: ', len(student))

# print student keys, values
print(student.keys())
print(student.values())

# keys and values
print(student.items())

# Loop through dictionary
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
