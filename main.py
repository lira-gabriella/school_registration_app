from fastapi import FastAPI
from pydantic import BaseModel
from database import (
    create_table,
    add_student, get_students, update_student, delete_student,
    add_teacher, get_teachers, update_teacher, delete_teacher,
    add_course, get_courses, update_course, delete_course
)

app = FastAPI()
create_table()


class Student(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int

class Teacher(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int

class Course(BaseModel):
    code: str
    title: str
    credits: int
    semester: str
    teacher_id: int


@app.get("/")
def home():
    return {"message": "welcome to my API server"}




@app.post("/students") 
def register_student(s: Student):
    add_student(s.name, s.age, s.email, s.country, s.id_number)
    return {"message": "student registered"}

@app.get("/students")
def list_students():
    return get_students()

@app.put("/students/{id}")
def modify_student(id: int, s: Student):
    update_student(id, s.name, s.age, s.email, s.country, s.id_number)
    return {"message": "student updated"}

@app.delete("/students/{id}")
def remove_student(id: int):
    delete_student(id)
    return {"message": "student deleted"}




@app.post("/teachers") 
def register_teacher(t: Teacher):
    add_teacher(t.name, t.age, t.email, t.country, t.id_number)
    return {"message": "teacher registered"}

@app.get("/teachers")
def list_teachers():
    return get_teachers()

@app.put("/teachers/{id}")
def modify_teacher(id: int, t: Teacher):
    update_teacher(id, t.name, t.age, t.email, t.country, t.id_number)
    return {"message": "teacher updated"}

@app.delete("/teachers/{id}")
def remove_teacher(id: int):
    delete_teacher(id)
    return {"message": "teacher deleted"}



@app.post("/courses") 
def register_course(c: Course):
    add_course(c.code, c.title, c.credits, c.semester, c.teacher_id)
    return {"message": "course registered"}

@app.get("/courses")
def list_courses():
    return get_courses()

@app.put("/courses/{id}")
def modify_course(id: int, c: Course):
    update_course(id, c.code, c.title, c.credits, c.semester, c.teacher_id)
    return {"message": "course updated"}

@app.delete("/courses/{id}")
def remove_course(id: int):
    delete_course(id)
    return {"message": "course deleted"}
