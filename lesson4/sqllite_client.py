import sqlite3

DB_NAME = 'clients.db'


def create_users_table():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        tg_id INTEGER PRIMARY KEY,
        phone TEXT,
        name TEXT,
        username TEXT
        )
        ''')
        connection.commit()


def save_phone_to_db(tg_id, phone, name, username):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT OR REPLACE INTO users (tg_id, phone, name, username) VALUES (?, ?, ?, ?) ', (tg_id, phone, name, username))
        connection.commit()


def get_all_clients():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT tg_id, name FROM Users')
        users = cursor.fetchall()
        return users


# create_users_table()
# print(get_all_clients())
