import requests
import sqlite3


def get_posts() -> list:
    """
    Get a list of post from jsonplaceholder site
    :return: list of post
    """
    URL = "https://jsonplaceholder.typicode.com/posts"

    try:
        resp = requests.get(URL)
        data = resp.json()
    except requests.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except Exception as error:
        print(f"Some errors occurred! --> {error}")
    else:
        return data


def connect_db() -> sqlite3.Connection:
    con = sqlite3.connect('posts.db')
    return con


def create_post_table():
    query = """CREATE TABLE post(id, title, body)"""
    con = connect_db()
    # execute query
    con.cursor().execute(query)
    con.close()


# create_post_table()

def insert_records():
    posts = get_posts()
    data = [(post.get('id'), post.get('title'), post.get('body')) for post in posts]
    con = connect_db()
    con.cursor().executemany("INSERT INTO post VALUES(?, ?, ?)", data)
    con.commit()
    con.close()


# Insert records
# insert_records()

def select_post(id: int):
    query = f"""SELECT id, title, body FROM post WHERE id = {id}"""
    con = connect_db()
    res = con.execute(query)
    record = res.fetchone()
    con.close()
    return record


print(select_post(1))