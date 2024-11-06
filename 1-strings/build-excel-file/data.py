"""
Module that represents our Type Data that we will fetch
"""
import requests


class Comment:
    """
        Class that represents Comment that we will fetch from
        https://jsonplaceholder.typicode.com/comments
    """
    comment_id: int
    name: str
    email: str
    body: str

    def build(self, comment_id: int, name: str, email: str, body: str):
        """
        Build an object that represents a Comment
        :param comment_id: unique id of comment
        :param name: name of the person who makes the comment
        :param email: email of the person who makes the comment
        :param body: Body of the comment
        """
        self.comment_id = comment_id
        self.name = name
        self.email = email
        self.body = body.capitalize()
        return Comment()


def fetch() -> list:
    """
    Fetch all comments from https://jsonplaceholder.typicode.com/comments
    :return: List of comments
    """
    ENDPOINT: str = "https://jsonplaceholder.typicode.com/comments"

    response: requests.Response = requests.get(ENDPOINT)
    comment = Comment()
    if response.status_code == 200:
        comments: list[Comment] = [
            comment.build(c['id'], c['name'], c['email'], c['body'])
            for c in response.json()]
        return comments
    else:
        raise requests.exceptions.HTTPError("Some errors occured!")


