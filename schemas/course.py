from pydantic import BaseModel

class Course(BaseModel):
    code: str
    title: str
    credits: int
    semester: str
    teacher_id: int
