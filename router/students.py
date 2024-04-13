from fastapi import (
    Depends,
    Request,
    APIRouter,
    status,
)
from exceptions import BadRequestException
from database.schema import Users
from repository.user import UsersRepository

from authentication.auth import auth

from validation import CreateStudent
from client.response import CustomResponse
from repository.student import StudentRepository

router = APIRouter(tags=["Student"], prefix="/student")


@router.get("/")
async def get_all_students(
    request: Request,
    user: Users = Depends(auth.get_current_user),
):
    

    students = [student.to_dict() for student in await StudentRepository.get_all_students()]

    context = {"students": students}
    
    return CustomResponse("get students successfully", data=context)



@router.post("/create")
async def create_student(
    request: Request,
    student: CreateStudent,
    user: Users = Depends(auth.get_current_user),
):

    new_student = await StudentRepository.create_student(student)

    context = {"student": new_student.to_dict()}

    return CustomResponse("created student successfully", data=context)
