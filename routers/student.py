from fastapi import APIRouter
from schemas.student import Student

from repositories.student import add_student, get_students, update_student, delete_student

router = APIRouter(prefix="/students", tags=["students"])


@router.post("") 
def register_student(s: Student):
    add_student(s.name, s.age, s.email, s.country, s.id_number)
    return {"message": "student registered"}

@router.get("")
def list_students():
    return get_students()


@router.put("/{id}")
def modify_student(id: int, s: Student):
    update_student(id, s.name, s.age, s.email, s.country, s.id_number)
    return {"message": "student updated"}

@router.delete("/{id}")
def remove_student(id: int):
    delete_student(id)
    return {"message": "student deleted"}
