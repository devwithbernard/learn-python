from db_manager.db_manager import DatabaseManager

class Todo:
    @classmethod
    def save(cls, table_name: str, db_manager: DatabaseManager, values: tuple):
        cols = ('content', 'completed', 'user_id')
        db_manager.connect()
        db_manager.insert(table_name, cols, values)
        db_manager.close()

