from fastapi import (
    Depends,
    Request,
    APIRouter,
    status,
)
from ..utils.exceptions import BadRequestException
from ..models import BaseUser
from ..repository.user import UsersRepository

from ..authentication.auth import auth

from ..schemas import CreateUser
from ..utils.response import CustomResponse

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
async def get_user(request: Request, user: BaseUser = Depends(auth.get_current_user)):

    return CustomResponse(
        "get user successfully",
        status=status.HTTP_200_OK,
        data=user.to_dict(),
    )
