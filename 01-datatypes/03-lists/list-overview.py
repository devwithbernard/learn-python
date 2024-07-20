# courses = ['History', 'Geography', 'Math', 'Physics']
#
# print(f"Number of courses : {len(courses)}")
# print(courses)
#
# # Accesing items
# print("First course: ", courses[0])
# print("Last course: ", courses[3])
# print("Last course with negative index: ", courses[-1])
#
# """
# If you try to access item out of index, we got IndexError
# """
# print("We got index error:\n")
# # print(courses[4])
#
# # Slicing
# print("First two courses: ", courses[0:2])
# print("First tree courses: ", courses[:3])
# print("Copy courses: ", courses[::])
# print("Copy courses and reverse: ", courses[::-1])
#
# # List methods
# import requests
# from requests.exceptions import HTTPError
#
# BASE_URL = "https://jsonplaceholder.typicode.com/users/"
# urls = [BASE_URL + str(i) for i in range(1, 11)]
# users = []
#
# for index, url in enumerate(urls):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         users.append(response.json())
#     except HTTPError as http_error:
#         print(f"Http Error occurred: {http_error}")
#     except Exception as err:
#         print(f"Other Error occurred: {err}")
#     else:
#         print(f"User n°{index + 1} fetched!")
#
# names = [user['name'] for user in users]
#
# print("List of users: ")
#
# for index, name in enumerate(names):
#     print(f"{index + 1} --> {name}")
#
# emails = []
#
# for user in users:
#     emails.insert(0, user['email'])
#
# print("User emails: ", emails)
#
#
# def get_data(url: str) -> list:
#     """
#     Get data
#     :param url: str
#     :return:
#     """
#     try:
#         resp = requests.get(url)
#         data = resp.json()
#     except HTTPError as http_error:
#         print(f'HTTP error occurred: {http_error}')
#     except Exception as error:
#         print(f"An error occured! --> {error}")
#     else:
#         return data
#
#
# def format_data():
#     users = get_data("https://jsonplaceholder.typicode.com/users")
#     posts = get_data("https://jsonplaceholder.typicode.com/posts?_limit=10")
#     formated_data = [{'username': user['name'], 'post': posts[user['id'] - 1]['title']} for user in
#                      users]
#     return formated_data
#
#
# print(format_data())

# Sorting
alphabet = ['A', 'D', 'B', 'E']
nums = [10, 15, 2, 9, 22]

sorted_alphabet = sorted(alphabet)
sorted_nums = sorted(nums)
print("Nums: ", nums, "Sorted nums: ", sorted_nums)
print("Alphabet: ", alphabet, "Sorted alphabet: ", sorted_alphabet)

# function
print("Max value of nums: ", max(nums))
print("Min value of nums: ", min(nums))
print("Sum of values in nums: ", sum(nums))

# Finding values

print(alphabet.index('D'))

if "A" in alphabet:
    print("It is in")
else:
    print("Not")

# Looping through list

for item in alphabet:
    print(item)

for index, item in enumerate(alphabet, start=1):
    print(index, item)

alphabet_str = ', '.join(alphabet)
print(alphabet_str)

new_alphabet = alphabet_str.split(', ')
print(new_alphabet)