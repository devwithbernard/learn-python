"""
Get started with python tuple concepts
"""

courses = ('Physic', 'Math', 'Computer Science', 'Art', 'Physic')

print("Occurrence of 'Physic': ", courses.count('Physic'))

for index, course in enumerate(courses):
    print(index, course)


"""
    Get started with python set concepts
"""
names = {"Jack", "Joe", "Jack", "Marc", "Alice"}
surnames = {"Joe", "Jean", "Aline", "Marc", "Jane"}

print(names.intersection(surnames)) # {'Marc', 'Joe'}
print(names.difference(surnames)) # 'Alice', 'Jack'}
print(names.union(surnames))
print(names.add('Jeannett'))
print(names)