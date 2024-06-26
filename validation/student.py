from pydantic import BaseModel, field_validator
from exceptions import BadRequestException
from beanie import PydanticObjectId
from typing import Optional


class CreateStudent(BaseModel):
    firstname: str
    othername: Optional[str]
    lastname: str
    matric_no: int
    level: int
    department: int
    gender:int
    academic_session: PydanticObjectId
    chapel_seat_number: int
    chapel_group_number: int


class UpdateStudent(BaseModel):
    firstname: Optional[str] = None
    othername: Optional[str] = None
    lastname: Optional[str] = None
    matric_no: Optional[int] = None
    level: Optional[int] = None
    department: Optional[int] = None
    academic_session: Optional[PydanticObjectId] = None
    chapel_seat_number: Optional[int] = None
    chapel_group_number: Optional[int] = None

    @field_validator("department")
    def validate_department(cls, department):
        if department is not None and (department < 1 or department > 18):
            raise BadRequestException("Department must be between 1 and 18, representing the types of department.")
        return department


    @field_validator("level")
    def validate_level(cls, level):
        if level is not None and level not in [100, 200, 300, 400, 500]:
            raise BadRequestException("Level must either 100, 200, 300, 400 or 500 level")
        return level