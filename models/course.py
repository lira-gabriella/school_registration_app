
from database import get_connection


def create_table():
    with get_connection() as connection:
         connection.execute('''CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            title TEXT NOT NULL,
            credits INTEGER NOT NULL,
            semester TEXT NOT NULL,
            teacher_id INTEGER NOT NULL
        )''')