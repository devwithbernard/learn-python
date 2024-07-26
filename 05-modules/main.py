from search import BASE_LANGUAGE as BL, find_index
import sys
import random

courses = ['History', 'Math', 'Physics', 'Computer Science']

print(sys.path)
index = find_index(courses, 'math')
print(index)
print(random.choice(courses))