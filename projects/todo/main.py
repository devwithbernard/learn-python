from models.todo import Todo
from db_manager.db_manager import DatabaseManager
from models.user import User
def main() -> None:
    db_manager = DatabaseManager('database.db')

    # Create user
    david = User(name= 'David martins', email= 'david.martins@gmail.com', db_manager=db_manager)
    david.save()


if __name__ == '__main__':
    main()