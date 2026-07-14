
from pydantic import BaseModel

class Teacher(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int