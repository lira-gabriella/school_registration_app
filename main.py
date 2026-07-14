from fastapi import FastAPI
from models import create_tables
from routers import teacher, course, student

app = FastAPI()

create_tables()

app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(course.router)
