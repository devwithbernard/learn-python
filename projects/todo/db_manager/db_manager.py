import logging
import sqlite3
from sqlite3 import Connection, Cursor


class DatabaseManager:
    def __init__(self, db_name: str) -> None:
        self.__db_name = db_name
        self.__conn: Connection | None = None
        self.__cursor: Cursor | None = None
        self.__logger = logging.getLogger(__name__)

    def connect(self):
        """Establish the connection to the database"""
        try:
            self.__conn = sqlite3.connect(self.__db_name, timeout=10)
            self.__cursor = self.__conn.cursor()
            self.__logger.info("Connection established successfully")
        except sqlite3.Connection.Error as e:
            self.__logger.error(f"Failed to connect to database: {e}")

    def close(self):
        """Close the connection"""
        try:
            if self.__conn:
                self.__conn.close()
                self.__logger.info("Database close successfully")
        except sqlite3.Error as e:
            self.__logger.error(f"Failed to close the database: {e}")

    def create_table(self, name: str, schema: str):
        """Create a table with given schema"""
        try:
            query = f"""
            CREATE TABLE IF NOT EXISTS {name}({schema})
            """
            self.__cursor.execute(query)
            self.__conn.commit()
            self.__logger.info(f"table '{name}' created successfully")
        except sqlite3.Error as e:
            self.__logger.error(f"Failed to create the table '{name}': {e}")

    def insert(self, table_name: str, columns: tuple, values: tuple):
        """Insert records into table"""
        try:
            placeholders = ", ".join("?" * len(values))
            cols = ", ".join(columns)
            query = f"""INSERT INTO {table_name}({cols}) VALUES ({placeholders})"""
            self.__cursor.execute(query, values)
            self.__conn.commit()
            self.__logger.info(f"[INFO] Record inserted into '{table_name}'")
        except sqlite3.Error as e:
            self.__logger.error(f"Failed to insert records into '{table_name}' table: {e}")

    def fetch_all(self, table_name: str):
        """Fetch all records of table"""
        try:
            query = f"""SELECT * FROM {table_name}"""
            self.__cursor.execute(query)
            rows = self.__cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            self.__logger.error(f"Failed to fetch data from '{table_name}' table: {e}")
            return []

    def get_one(self, table_name: str, query: str):
        try:
            self.__cursor.execute(query)
            row = self.__cursor.fetchone()
            return row
        except sqlite3.Error as e:
            self.__logger.error(f"Failed to fetch data from '{table_name}' table: {e}")
            return tuple()

    def drop_table(self, table_name: str):
        try:
            query = f"""DROP TABLE IF EXISTS {table_name}"""
            self.__cursor.execute(query)
            self.__conn.commit()
        except sqlite3.Error as e:
            self.__logger.error(f"Failed to drop '{table_name}' table: {e}")