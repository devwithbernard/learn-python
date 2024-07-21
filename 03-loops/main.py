"""
For loop --> Iterate over iterables
"""

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# Break statement

for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

# Search in list
names = ['Jane', 'Jack', 'John', 'Marc']

target_name = 'Job'

for name in names:
    if name.lower() == target_name.lower():
        print(f"Found at index {names.index(target_name)}")
        break
else:
    print('Not found')

# Search 5 modulo numbers between 0 and 100
five_times = []
for i in range(101):
    if i % 5 == 0:
        five_times.append(i)

# While Loop
import requests

posts = []
x = 0

while x < 10:
    resp = requests.get(f"https://jsonplaceholder.typicode.com/posts/{x + 1}")
    posts.append(resp.json())
    x += 1

from prettytable import PrettyTable

table = PrettyTable(list(posts[0].keys()))
for post in posts:
    table.add_row(list(post.values()))
print(table)
