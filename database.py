
import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_connection() as connection:
      
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            country TEXT NOT NULL,
            id_number INTEGER NOT NULL
        )''')
        
     
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            country TEXT NOT NULL,
            id_number INTEGER NOT NULL
        )''')

       
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            title TEXT NOT NULL,
            credits INTEGER NOT NULL,
            semester TEXT NOT NULL,
            teacher_id INTEGER NOT NULL
        )''')


def add_student(name, age, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students (name, age, email, country, id_number) VALUES(?,?,?,?,?)',
            (name, age, email, country, id_number)
        )

def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()

def update_student(id, name, age, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            'UPDATE students SET name=?, age=?, email=?, country=?, id_number=? WHERE id=?',
            (name, age, email, country, id_number, id)
        )

def delete_student(id):
    with get_connection() as connection:
        connection.execute('DELETE FROM students WHERE id = ?', (id,))



def add_teacher(name, age, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name, age, email, country, id_number) VALUES(?,?,?,?,?)',
            (name, age, email, country, id_number)
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def update_teacher(id, name, age, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            'UPDATE teachers SET name=?, age=?, email=?, country=?, id_number=? WHERE id=?',
            (name, age, email, country, id_number, id)
        )

def delete_teacher(id):
    with get_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id = ?', (id,))



def add_course(code, title, credits, semester, teacher_id):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses (code, title, credits, semester, teacher_id) VALUES(?,?,?,?,?)',
            (code, title, credits, semester, teacher_id)
        )

def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def update_course(id, code, title, credits, semester, teacher_id):
    with get_connection() as connection:
        connection.execute(
            'UPDATE courses SET code=?, title=?, credits=?, semester=?, teacher_id=? WHERE id=?',
            (code, title, credits, semester, teacher_id, id)
        )

def delete_course(id):
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE id = ?', (id,))
