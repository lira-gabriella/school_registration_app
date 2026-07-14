

from database import get_connection


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

