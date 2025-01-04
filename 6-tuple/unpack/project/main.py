"""
REQUEST PROJECT
"""
from typing import Any
import requests
import sqlite3
import os


class Comment:
    def __init__(self, name: str, body: str) -> None:
        self.name = name
        self.body = body

    def __repr__(self) -> str:
        return f"<Comment ({self.name}, {self.body})>"

    def __str__(self) -> str:
        return self.name

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "body": self.body
        }


def get_data(url: str) -> list[dict[str, Any]]:
    try:
        response: requests.Response = requests.get(url)
        return response.json()
    except requests.HTTPError as http_error:
        print(f"Error occurs while fetching data: {http_error.__str__()}")
    except requests.ConnectionError as conn_error:
        print(f"Error occurs during connection to server: {conn_error.__str__()}")
    except requests.RequestException as e:
        print(f"Exception throws : {e.__str__()}")


def connect_to_db() -> sqlite3.Connection:
    return sqlite3.connect(os.path.join(os.path.curdir, 'data.db'))


def create_table(table_name: str) -> None:
    statement: str = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        name VARCHAR(255) NOT NULL,
        body TEXT
    )
    """

    try:
        conn: sqlite3.Connection = connect_to_db()
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(statement)
        conn.commit()
        conn.close()
        print(f"Table ({table_name}) created")
    except sqlite3.Connection.Error as error:
        print(f"Connection failed: {error}")


def insert_data_to_db(data: list[Any]) -> None:
    conn: sqlite3.Connection = connect_to_db()
    cursor: sqlite3.Cursor = conn.cursor()
    try:
        cursor.executemany("""INSERT INTO comment VALUES (?, ?)""", data)
        conn.commit()
        conn.close()
        print("Data inserted")
    except conn.OperationalError as op_error:
        print(f"Error occurs during transaction: {op_error.__str__()}")
    except conn.ProgrammingError as p_error:
        print(f"Execution error occurs: {p_error.__str__()}")


def get_comments() -> list[Comment]:
    conn: sqlite3.Connection = connect_to_db()
    try:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("""SELECT name, body FROM comment""")
        values: list[tuple | Any] = cursor.fetchall()
        comments: list[Comment] = [Comment(value[0], value[1]) for value in values]
        return comments
    except conn.OperationalError as op_error:
        print(f"Error occurs during connection to db: {op_error.__str__()}")
    except Exception as e:
        print(f"Error occurs during execution: {e.__str__()}")


def get_comment(name: str) -> Comment:
    conn: sqlite3.Connection = connect_to_db()
    try:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(f'''SELECT name, body FROM comment WHERE name LIKE "%{name}%"''')
        value: tuple | None = cursor.fetchone()
        comment: Comment = Comment(value[0], value[1])
        return comment
    except conn.OperationalError as op_error:
        print(f"Error occurs during transaction: {op_error.__str__()}")
    except Exception as e:
        print(f"Error occurs during execution: {e.__str__()}")


def insert_comment(comment: Comment) -> Comment:
    conn: sqlite3.Connection = connect_to_db()
    try:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO comment (name, body) VALUES(:name, :body)""", comment.to_dict())
        conn.commit()
        conn.close()
        print(f"{comment.__str__()} has been inserted")
        return comment
    except conn.OperationalError as op_error:
        print(f"Error occurs during transaction: {op_error.__str__()}")
    except Exception as e:
        print(f"Error occurs during execution: {e.__str__()}")


def main() -> None:

    create_table('comment')

    comments: list[dict[str, Any]] = get_data("https://jsonplaceholder.typicode.com/comments")
    new_comments: list[tuple[str, str]] = [(c['name'], c['body']) for c in comments]

    # Insert fetched data in to database
    insert_data_to_db(new_comments)

    # Get data
    comments: list[Comment] = get_comments()
    for index, comment in enumerate(comments):
        if index == 2:
            print(comment.__repr__())
            break
    comment: Comment = get_comment('id')
    print(f"Comment => {comment.__repr__()}")

    # Insert a comment
    comment: Comment = Comment("Hello world", "Hello world")
    insert_comment(comment)


if __name__ == '__main__':
    main()
