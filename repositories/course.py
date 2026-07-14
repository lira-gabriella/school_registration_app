
from database import get_connection


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
