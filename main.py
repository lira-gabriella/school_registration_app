
import sqlite3
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

DB_FILE = "school.db"

def init_db():
  
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        
       
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            major TEXT,
            enrollment_year INTEGER
        );
        """)
        
     
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            department TEXT,
            office_number TEXT,
            years_experience INTEGER
        );
        """)
        
       
       
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            credits INTEGER,
            semester TEXT,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE SET NULL
        );
        """)
        conn.commit()



class StudentCreate(BaseModel):
    name: str
    email: str
    age: int
    major: str
    enrollment_year: int

class StudentResponse(StudentCreate):
    student_id: int

class TeacherCreate(BaseModel):
    name: str
    email: str
    department: str
    office_number: str
    years_experience: int

class TeacherResponse(TeacherCreate):
    teacher_id: int

class CourseCreate(BaseModel):
    course_code: str
    title: str
    credits: int
    semester: str
    teacher_id: Optional[int] = None

class CourseResponse(CourseCreate):
    course_id: int


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
  
  
    init_db()
    yield

app = FastAPI(title="School Registration App", lifespan=lifespan)


@app.post("/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            query = "INSERT INTO students (name, email, age, major, enrollment_year) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (student.name, student.email, student.age, student.major, student.enrollment_year))
            conn.commit()
            new_id = cursor.lastrowid
            
        return {**student.model_dump(), "student_id": new_id}
    except Exception:
        raise HTTPException(status_code=400, detail="Email already exists.")

@app.get("/students/", response_model=List[StudentResponse])
def get_students():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        
  
    return [dict(row) for row in rows]

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        row = cursor.fetchone()
        
    if not row:
        raise HTTPException(status_code=404, detail="Student not found")
    return dict(row)

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate):
  
    get_student(student_id)
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        query = "UPDATE students SET name=?, email=?, age=?, major=?, enrollment_year=? WHERE student_id=?"
        cursor.execute(query, (student.name, student.email, student.age, student.major, student.enrollment_year, student_id))
        conn.commit()
        
    return {**student.model_dump(), "student_id": student_id}

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):

    get_student(student_id)
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        conn.commit()

@app.post("/teachers/", response_model=TeacherResponse, status_code=status.HTTP_201_CREATED)
def create_teacher(teacher: TeacherCreate):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            query = "INSERT INTO teachers (name, email, department, office_number, years_experience) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (teacher.name, teacher.email, teacher.department, teacher.office_number, teacher.years_experience))
            conn.commit()
            new_id = cursor.lastrowid
            
        return {**teacher.model_dump(), "teacher_id": new_id}
    except Exception:
        raise HTTPException(status_code=400, detail="Email already exists.")

@app.get("/teachers/", response_model=List[TeacherResponse])
def get_teachers():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers")
        rows = cursor.fetchall()
        
    return [dict(row) for row in rows]

@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int):
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers WHERE teacher_id = ?", (teacher_id,))
        row = cursor.fetchone()
        
    if not row:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return dict(row)

@app.put("/teachers/{teacher_id}", response_model=TeacherResponse)
def update_teacher(teacher_id: int, teacher: TeacherCreate):
    get_teacher(teacher_id)
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        query = "UPDATE teachers SET name=?, email=?, department=?, office_number=?, years_experience=? WHERE teacher_id=?"
        cursor.execute(query, (teacher.name, teacher.email, teacher.department, teacher.office_number, teacher.years_experience, teacher_id))
        conn.commit()
        
    return {**teacher.model_dump(), "teacher_id": teacher_id}

@app.delete("/teachers/{teacher_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_teacher(teacher_id: int):
    get_teacher(teacher_id)
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM teachers WHERE teacher_id = ?", (teacher_id,))
        conn.commit()


@app.post("/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            conn.execute("PRAGMA foreign_keys = ON;")
            query = "INSERT INTO courses (course_code, title, credits, semester, teacher_id) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (course.course_code, course.title, course.credits, course.semester, course.teacher_id))
            conn.commit()
            new_id = cursor.lastrowid
            
        return {**course.model_dump(), "course_id": new_id}
    except Exception:
        raise HTTPException(status_code=400, detail="Course code must be unique / valid teacher_id needed.")

@app.get("/courses/", response_model=List[CourseResponse])
def get_courses():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()
        
    return [dict(row) for row in rows]

@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE course_id = ?", (course_id,))
        row = cursor.fetchone()
        
    if not row:
        raise HTTPException(status_code=404, detail="Course not found")
    return dict(row)

@app.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseCreate):
    get_course(course_id)
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = ON;")
