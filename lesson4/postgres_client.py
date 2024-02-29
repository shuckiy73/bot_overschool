import psycopg2


DB_PASS = 'root'
DB_USER = 'root'
DB_HOST = '45.135.234.66'
DB_PORT = '5432'


def create_users_table():
    with psycopg2.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT) as connection:
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
    with psycopg2.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (tg_id, phone, name, username) VALUES (%s, %s, %s, %s) ON CONFLICT (tg_id) DO NOTHING', (tg_id, phone, name, username))
        connection.commit()


def get_all_clients():
    with psycopg2.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT tg_id, name FROM Users')
        users = cursor.fetchall()
        return users


# create_users_table()
# print(get_all_clients())
