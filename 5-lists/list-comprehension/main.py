from typing import List
import pprint
import requests


def main() -> None:
    fruits: List[str] = ['apple', 'banana', 'cherry', 'kiwi', 'strawberry', 'mango']

    def a_list(sequence: List[str]) -> List[str]:
        """
        List of fruits that each fruit contains 'a' in its name
        :return: List[str]
        """
        return [item for item in sequence if 'a' in item.lower()]

    print(a_list(fruits))

    def get_users(url) -> List[dict]:
        try:
            response = requests.get(url)
            users: List[dict] = response.json()
            return users
        except requests.exceptions.ConnectionError:
            print('Connection error')
        except requests.exceptions.HTTPError:
            print('HTTP error')

    def a_user_names(users: List[dict]) -> List[dict]:
        a_usernames: List[dict] = [{'name': user['name'], 'address': user['address']}
                                   for user in users if 'a' in user['name'].lower()]
        return a_usernames

    user_list: List[dict] = get_users("https://jsonplaceholder.typicode.com/users")
    pprint.pprint(a_user_names(user_list))

    def get_even_numbers(numbers: List[int]) -> List[int]:
        range_number: range = range(20)
        even_numbers: List[int] = [number for number in range_number if number%2 == 0]
        return even_numbers

    even_numbers: List[int] = get_even_numbers(list(range(20)))
    pprint.pprint(even_numbers)


if __name__ == '__main__':
    main()
