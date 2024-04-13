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

router = APIRouter(tags=["User"], prefix="/api/user")


@router.post("/create")
async def create_user(
    request: Request,
    user: CreateUser,
):
    if await UsersRepository.get_user_by_email(email=user.email):
        raise BadRequestException("email already exist")

    new_user = await UsersRepository.create_user(user)

    return CustomResponse(
        "created user successfully",
        status=status.HTTP_201_CREATED,
        data=new_user.to_dict(),
    )


@router.get("/")
async def get_user(request: Request, user: Users = Depends(auth.get_current_user)):

    return CustomResponse(
        "get user successfully",
        status=status.HTTP_200_OK,
        data=user.to_dict(),
    )
