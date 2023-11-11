import sqlite3


class StorageSQLite:
    def __init__(self, database_name: str):
        self.database_name = database_name
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS story (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    username TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )"""
            cursor.execute(query)
            connection.commit()

    def get_stories(self, limit: int = 5):

        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = """
                SELECT *
                FROM story
                ORDER BY id DESC
                LIMIT :Limit
            """
            result = cursor.execute(query, {'Limit': limit})
            return result.fetchall()

    def search_story(self, query_str: str):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM story
                WHERE 
                    title LIKE '%{query_str}%'
                OR 
                    username LIKE '%{query_str}%'
                OR
                    content LIKE '%{query_str}%'
                ORDER BY id DESC
            """
            result = cursor.execute(query)
            return result.fetchall()

    def add_story(self, *, title: str, username: str, content: str):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO story (title, username, content)
                VALUES (?,?,?)
            """
            cursor.execute(query, (title, username, content))
            connection.commit()


database = StorageSQLite('database.sqlite3')
