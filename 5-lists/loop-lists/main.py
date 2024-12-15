"""
Loop through list
"""
from typing import List
import requests


def get_todos(url: str) -> List[dict]:
    try:
        response: requests.Response = requests.request('GET', url)
        if response.status_code == 200:
            todos: List[dict] = response.json()
            return todos
    except requests.HTTPError as e:
        print(e.__str__())


def loop_through_list(sequence: List[dict]) -> None:
    for item in sequence:
        if item["id"] == 5:
            break

        print(f"""
            UserId: {item["userId"]}
                id: {item["id"]}
             title: {item["title"]}
             completed: {item["completed"]}
        """)
        print("-" * 100)


def loop_through_index_numbers(sequence: List[dict]) -> None:
    for index in range((len(sequence))):
        if index % 2 == 0 and index <= 10:
            item: dict = sequence[index]
            print(f"""
            Todo(id={item['id']}):
              title: {item["title"]}
              completed: {item["completed"]}  
            """)
            print("-" * 50)


def main() -> None:
    todos: List[dict] = get_todos("https://jsonplaceholder.typicode.com/todos")
    # loop_through_list(todos)
    loop_through_index_numbers(todos)


if __name__ == '__main__':
    main()
