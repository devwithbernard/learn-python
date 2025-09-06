from db_manager.db_manager import DatabaseManager


class User:
    def __init__(self, name: str, email: str, db_manager: DatabaseManager):
        self.name = name
        self.email = email
        self.__db_manager = db_manager

    def __str__(self):
        return f"User: {self.name}, {self.email}"

    def save(self):
        # check if there is a user with the same email
        query = f"""SELECT user_id, name, email FROM user WHERE email = '{self.email}'"""
        self.__db_manager.connect()
        user = self.__db_manager.get_one('user', query)

        if user:
            print(f"a user with email={self.email} already exists")
        else:
            cols = ('name', 'email')
            values = (self.name, self.email)
            self.__db_manager.insert('user', cols, values)


if __name__ == "__main__":
    pass
