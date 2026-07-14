from fastapi import APIRouter
from schemas.course import Course 
from repositories.course import add_course, get_courses, update_course, delete_course  

router = APIRouter(prefix="/courses", tags=["courses"])

@router.post("") 
def register_course(c: Course):
    add_course(c.code, c.title, c.credits, c.semester, c.teacher_id)
    return {"message": "course registered"}

@router.get("")
def list_courses():
    return get_courses()


@router.put("/{id}")
def modify_course(id: int, c: Course):
    update_course(id, c.code, c.title, c.credits, c.semester, c.teacher_id)
    return {"message": "course updated"}

@router.delete("/{id}")
def remove_course(id: int):
    delete_course(id)
    return {"message": "course deleted"}
