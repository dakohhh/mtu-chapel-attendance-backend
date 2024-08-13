from ..models import BaseUser
from ..schemas import CreateUser
from ..authentication.hashing import hashPassword
from beanie import PydanticObjectId


class UsersRepository:
    @staticmethod
    async def create_user(user: CreateUser) -> BaseUser:
        query = BaseUser(
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.email,
            password=hashPassword(user.password),
        )

        query.save()

        return query

    @staticmethod
    async def get_user_by_email(email: str) -> BaseUser:

        query = BaseUser.objects(email=email).first()
        return query

    @staticmethod
    async def get_user_by_id(user_id: PydanticObjectId) -> BaseUser:

        query = BaseUser.objects(id=user_id).first()

        return query
