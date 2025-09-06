from db_manager import DatabaseManager


def main() -> None:
    db_manager = DatabaseManager("../database.db")

    # Create table todo
    table_name = "todo"
    todo_schema = f"""
    todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    completed BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at INTEGER,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
    """
    db_manager.connect()
    db_manager.create_table(table_name, todo_schema)

    # Create table user
    table_name = "user"
    user_schema = """
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    """
    db_manager.create_table(table_name, user_schema)

    db_manager.close()

def drop_table():
    db_manager = DatabaseManager("../database.db")
    db_manager.connect()
    db_manager.drop_table('todo')


if __name__ == '__main__':
    main()
