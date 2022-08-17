
import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.executemany("INSERT INTO `users` (user_id, first_name, username) VALUES (?, ?, ?)", (user_id,))
        return self.conn.commit()

    def get_all_id(self,) -> list:
        """Достаем id всех юзеров в базе """
        result =  self.cursor.execute("SELECT user_id FROM users")
        return result.fetchall()


    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()















def add_users(user_id: int, user_log: str, user_name: str):

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user
                          (user_id INTEGER, user_log TEXT, user_name TEXT)
               """)
    conn.commit()

    m = [(user_id, user_log, user_name)]

    cursor.executemany("INSERT INTO user VALUES (?,?,?)", m)
    conn.commit()


