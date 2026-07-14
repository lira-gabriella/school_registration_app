from models.teacher import create_table as create_teacher_table
from models.course import create_table as create_course_table
from models.student import create_table as create_student_table

def create_tables():
    """Executes table creation functions for all models."""
    create_teacher_table()
    create_course_table()
    create_student_table()
