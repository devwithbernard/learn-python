from enum import Enum
from typing import List


def user_exists_in_database(name: str, users_db: List[dict[str, ...]] = None) -> bool:
    if users_db is not None:
        usernames: List[str] = [user.get('name').capitalize() for user in users_db]
        if name.capitalize() in usernames:
            return True
    return False


class Role(Enum):
    ADMIN: str = "Admin"
    LIBRARIAN: str = "Librarian"
    MEMBER: str = "Member"


class User:
    phone: str = ''
    city: str = ''
    address: str = ''

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.role = Role.MEMBER,
        self.is_auth = False

    def __str__(self) -> str:
        return self.name

    def update(self,
               email: str = None,
               phone: str = None,
               city: str = None,
               address: str = None,
               users_db: List[dict[str, ...]] = None):

        if not self.is_auth:
            return "Authentication before update profile!"

        if not user_exists_in_database(self.name, users_db):
            return "User not found!"

        if email:
            self.email = email

        if phone:
            self.phone = phone

        if city:
            self.city = city

        if address:
            self.address = address

        current_user = self.__dict__
        users = list(
            filter(lambda user: user.get('name').capitalize() != self.name.capitalize(),
                   users_db))
        users.append(current_user)

        return users
