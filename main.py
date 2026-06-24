import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

DB_FILE = "school.db"
app = FastAPI()


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, email TEXT UNIQUE, age INTEGER, major TEXT, enrollment_year INTEGER
    );
    """)
    conn.commit()
    conn.close()

init_db()


class Student(BaseModel):
    name: str
    email: str
    age: int
    major: str
    enrollment_year: int


@app.post("/students/")
def create_student(student: Student):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    query = "INSERT INTO students (name, email, age, major, enrollment_year) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (student.name, student.email, student.age, student.major, student.enrollment_year))
    
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {
        "student_id": new_id, 
        "name": student.name, 
        "email": student.email, 
        "age": student.age, 
        "major": student.major, 
        "enrollment_year": student.enrollment_year
    }

@app.get("/students/")
def get_students():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, email, age, major, enrollment_year FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    students_list = []
    for student_id, name, email, age, major, enrollment_year in rows:
        students_list.append({
            "student_id": student_id, 
            "name": name, 
            "email": email, 
            "age": age, 
            "major": major, 
            "enrollment_year": enrollment_year
        })
    return students_list

@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, email, age, major, enrollment_year FROM students WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    
    sid, name, email, age, major, enrollment_year = row
    return {
        "student_id": sid, 
        "name": name, 
        "email": email, 
        "age": age, 
        "major": major, 
        "enrollment_year": enrollment_year
    }

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    query = "UPDATE students SET name=?, email=?, age=?, major=?, enrollment_year=? WHERE student_id=?"
    cursor.execute(query, (student.name, student.email, student.age, student.major, student.enrollment_year, student_id))
    
    conn.commit()
    conn.close()
    
    return {
        "student_id": student_id, 
        "name": student.name, 
        "email": student.email, 
        "age": student.age, 
        "major": student.major, 
        "enrollment_year": student.enrollment_year
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    
    return {"detail": "Student successfully deleted"}
