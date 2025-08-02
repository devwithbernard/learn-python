
def get_username() -> str:
    username: str = input("Enter your username: ")
    return username


def user_infos(username: str) -> dict[str, int]:
    user_data = {"username": username, "score": 0}
    return user_data



