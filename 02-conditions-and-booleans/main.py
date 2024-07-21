
# If statement
language = 'Javascript'

if True:
    print("Conditional was True")
base = "You are a"
if language == 'Python':
    print(base + " python developer")
elif language == 'Java':
    print(base + ' java developer')
elif language == 'Javascript':
    print(base + ' javascript developer')
else:
    print('No match')

"""
Another example
"""
is_admin = True
logged_in = True

if is_admin or logged_in:
    print('Admin Page')
    import requests

    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/users/1")
        data = resp.json()
        admin_infos = {'name': data.get('name') if data['name'] is not None else 'Unknown',
                       'email': data.get('email') if data['email'] is not None else 'Unknown email'}
        print(admin_infos)
    except requests.HTTPError as http_error:
        print(http_error)
    except Exception as ex:
        print(ex)
else:
    print('Bad credentials')

"""
Exercise
"""
num1 = [1, 2, 3]
num2 = [1, 2, 3]

print('id num1 ', id(num1))
print('id num2 ', id(num2))