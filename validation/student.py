from pydantic import BaseModel
from typing import Optional


class CreateStudent(BaseModel):
    firstname: str
    othername: Optional[str]
    lastname: str
    matric_no: int
    level: int 
    department: int
    chapel_seat_number:int
    chapel_group_number:int
