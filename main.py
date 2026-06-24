import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

DB_FILE = "school.db"
app = FastAPI(title="School Registration App")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, email TEXT UNIQUE, age INTEGER, major TEXT, enrollment_year INTEGER
    );
    """)
   
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, email TEXT UNIQUE, department TEXT, office_number TEXT, years_experience INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_code TEXT UNIQUE, title TEXT, credits INTEGER, semester TEXT, teacher_id INTEGER
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

class Teacher(BaseModel):
    name: str
    email: str
    department: str
    office_number: str
    years_experience: int

class Course(BaseModel):
    course_code: str
    title: str
    credits: int
    semester: str
    teacher_id: int




@app.post("/students/")
def create_student(student: Student):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "INSERT INTO students (name, email, age, major, enrollment_year) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (student.name, student.email, student.age, student.major, student.enrollment_year))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"student_id": new_id, "name": student.name, "email": student.email, "age": student.age, "major": student.major, "enrollment_year": student.enrollment_year}

@app.get("/students/")
def get_students():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, email, age, major, enrollment_year FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    students_list = []
    for student_id, name, email, age, major, enrollment_year in rows:
        students_list.append({"student_id": student_id, "name": name, "email": email, "age": age, "major": major, "enrollment_year": enrollment_year})
    return students_list

@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, email, age, major, enrollment_year FROM students WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    
    sid, name, email, age, major, enrollment_year = row
    return {"student_id": sid, "name": name, "email": email, "age": age, "major": major, "enrollment_year": enrollment_year}

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "UPDATE students SET name=?, email=?, age=?, major=?, enrollment_year=? WHERE student_id=?"
    cursor.execute(query, (student.name, student.email, student.age, student.major, student.enrollment_year, student_id))
    conn.commit()
    conn.close()
    return {"student_id": student_id, "name": student.name, "email": student.email, "age": student.age, "major": student.major, "enrollment_year": student.enrollment_year}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    return {"detail": "Student successfully deleted"}


@app.post("/teachers/")
def create_teacher(teacher: Teacher):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "INSERT INTO teachers (name, email, department, office_number, years_experience) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (teacher.name, teacher.email, teacher.department, teacher.office_number, teacher.years_experience))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"teacher_id": new_id, "name": teacher.name, "email": teacher.email, "department": teacher.department, "office_number": teacher.office_number, "years_experience": teacher.years_experience}

@app.get("/teachers/")
def get_teachers():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT teacher_id, name, email, department, office_number, years_experience FROM teachers")
    rows = cursor.fetchall()
    conn.close()
    
    teachers_list = []
    for t_id, name, email, dept, office, exp in rows:
        teachers_list.append({"teacher_id": t_id, "name": name, "email": email, "department": dept, "office_number": office, "years_experience": exp})
    return teachers_list

@app.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT teacher_id, name, email, department, office_number, years_experience FROM teachers WHERE teacher_id = ?", (teacher_id,))
    row = cursor.fetchone()
    conn.close()
    
    t_id, name, email, dept, office, exp = row
    return {"teacher_id": t_id, "name": name, "email": email, "department": dept, "office_number": office, "years_experience": exp}

@app.put("/teachers/{teacher_id}")
def update_teacher(teacher_id: int, teacher: Teacher):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "UPDATE teachers SET name=?, email=?, department=?, office_number=?, years_experience=? WHERE teacher_id=?"
    cursor.execute(query, (teacher.name, teacher.email, teacher.department, teacher.office_number, teacher.years_experience, teacher_id))
    conn.commit()
    conn.close()
    return {"teacher_id": teacher_id, "name": teacher.name, "email": teacher.email, "department": teacher.department, "office_number": teacher.office_number, "years_experience": teacher.years_experience}

@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teachers WHERE teacher_id = ?", (teacher_id,))
    conn.commit()
    conn.close()
    return {"detail": "Teacher successfully deleted"}



@app.post("/courses/")
def create_course(course: Course):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "INSERT INTO courses (course_code, title, credits, semester, teacher_id) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (course.course_code, course.title, course.credits, course.semester, course.teacher_id))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"course_id": new_id, "course_code": course.course_code, "title": course.title, "credits": course.credits, "semester": course.semester, "teacher_id": course.teacher_id}

@app.get("/courses/")
def get_courses():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_code, title, credits, semester, teacher_id FROM courses")
    rows = cursor.fetchall()
    conn.close()
    
    courses_list = []
    for c_id, code, title, credits, semester, t_id in rows:
        courses_list.append({"course_id": c_id, "course_code": code, "title": title, "credits": credits, "semester": semester, "teacher_id": t_id})
    return courses_list

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_code, title, credits, semester, teacher_id FROM courses WHERE course_id = ?", (course_id,))
    row = cursor.fetchone()
    conn.close()
    
    c_id, code, title, credits, semester, t_id = row
    return {"course_id": c_id, "course_code": code, "title": title, "credits": credits, "semester": semester, "teacher_id": t_id}

@app.put("/courses/{course_id}")
def update_course(course_id: int, course: Course):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "UPDATE courses SET course_code=?, title=?, credits=?, semester=?, teacher_id=? WHERE course_id=?"
    cursor.execute(query, (course.course_code, course.title, course.credits, course.semester, course.teacher_id, course_id))
    conn.commit()
    conn.close()
    return {"course_id": course_id, "course_code": course.course_code, "title": course.title, "credits": course.credits, "semester": course.semester, "teacher_id": course.teacher_id}

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE course_id = ?", (course_id,))
    conn.commit()
    conn.close()
    return {"detail": "Course successfully deleted"}
