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

from validation import CreateUser
from client.response import CustomResponse

router = APIRouter(tags=["Student"], prefix="/student")


@router.post("/create")
async def create_student(request: Request,user: CreateUser):


    pass