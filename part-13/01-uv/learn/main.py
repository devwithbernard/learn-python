import logging
import requests


def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        logging.info(f"Send request at {url}")
        request = requests.get(url)

        if request.status_code == 200:
            data = request.json()
            return data
    except requests.exceptions.HTTPError as e:
        logging.error(e)


def main():
    users = get_users()
    print(users)


if __name__ == "__main__":
    main()
