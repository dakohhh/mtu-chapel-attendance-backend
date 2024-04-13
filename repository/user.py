from database.schema import Users
from validation import CreateUser
from beanie import PydanticObjectId
from authentication.hashing import hashPassword


class UsersRepository:
    @staticmethod
    async def create_user(user: CreateUser) -> Users:
        query = Users(
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.email,
            password=hashPassword(user.password),
        )

        query.save()

        return query

    @staticmethod
    async def get_user_by_email(email: str) -> Users:

        query = Users.objects(email=email).first()
        return query

    @staticmethod
    async def get_user_by_id(user_id: PydanticObjectId) -> Users:

        query = Users.objects(id=user_id).first()

        return query
