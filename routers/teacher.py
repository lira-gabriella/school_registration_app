from fastapi import APIRouter
from schemas.teacher import Teacher

from repositories.teacher import add_teacher, get_teachers, update_teacher, delete_teacher 

router = APIRouter(prefix="/teachers", tags=["teachers"])


@router.post("") 
def register_teacher(t: Teacher):
    add_teacher(t.name, t.age, t.email, t.country, t.id_number)
    return {"message": "teacher registered"}


@router.get("")
def list_teachers():
    return get_teachers()


@router.put("/{id}")
def modify_teacher(id: int, t: Teacher):
    update_teacher(id, t.name, t.age, t.email, t.country, t.id_number)
    return {"message": "teacher updated"}


@router.delete("/{id}")
def remove_teacher(id: int):
    delete_teacher(id)
    return {"message": "teacher deleted"}
