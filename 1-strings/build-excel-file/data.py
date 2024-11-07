"""
Module that represents our Type Data that we will fetch
"""
import requests


def fetch() -> list[dict]:
    """
    Fetch all comments from https://jsonplaceholder.typicode.com/comments
    :return: List of comments
    """
    ENDPOINT: str = "https://jsonplaceholder.typicode.com/comments"

    response: requests.Response = requests.get(ENDPOINT)
    if response.status_code == 200:
        comments: list[dict] = [{
            'id': d['id'], 'name': d['name'],
            'email': d['email'], 'body': d['body'].capitalize()
        } for d in response.json()]
        return comments
    else:
        raise requests.exceptions.HTTPError("Some errors occured!")
