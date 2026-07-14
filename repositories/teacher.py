

from database import get_connection


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
def delete_teacher(teacher_id: int):
    """Deletes a teacher record from the database by ID."""
    from database import get_connection
    
    query = "DELETE FROM teachers WHERE id = ?"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (teacher_id,))
