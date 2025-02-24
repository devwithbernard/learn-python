"""
Class and Static Method
"""

import requests


class HTTP:
    url: str = ''

    @staticmethod
    def get(cls):
        try:
            response: requests.Response = requests.get(cls.url)
            data = response.json()
            return data
        except requests.ConnectionError as con_error:
            print(f"Connection error occurs: {con_error}")
        except requests.HTTPError as http_error:
            print(f"Request Error occurs: {http_error}")


def main() -> None:
    HTTP.url = 'https://jsonplaceholder.typicode.com/posts/1'
    post: dict = HTTP.get(HTTP)

    if post:
        for key, value in post.items():
            print(f"{key} => {value}") if key != 'userId' else None


if __name__ == '__main__':
    main()
