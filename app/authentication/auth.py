import jwt

from ..models.user import BaseUser
from ..settings import settings
from datetime import datetime, timedelta
from pydantic import ValidationError
from ..utils.exceptions import UnauthorizedException, ForbiddenException
from .hashing import checkPassword
from ..schemas import LoginSchema, TokenData
from ..repository.user import UsersRepository
from ..utils.exceptions import BadRequestException
from fastapi import Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer = HTTPBearer()

from ..enums.user_roles import UserRoles



SECRET_KEY = settings.JWT_SECRET
ALGORITHM = 'H256'
ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(days=30)


class AuthToken:
    def __init__(self):
        self.secret_key = SECRET_KEY
        self.algorithm = ALGORITHM
        self.access_token_expire = ACCESS_TOKEN_EXPIRE_MINUTES


    @staticmethod
    def create_access_token(self, data: TokenData) -> str:

        data.exp = datetime.now() + self.access_token_expire

        token = jwt.encode(data.model_dump(), SECRET_KEY)

        return token

    @staticmethod
    def verify_access_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

            instance = TokenData(**payload)

            if instance.get_expiry_time < datetime.now():
                raise CredentialsException("access token has expired")

            return instance

        except jwt.PyJWTError as e:
            raise CredentialsException(str(e))

        except ValidationError as e:
            raise CredentialsException("invalid access token")


class Auth:
    def __init__(self):
        self.auth_token = AuthToken()

    async def authenticate_user(self, login_input: LoginSchema):
        user = await UsersRepository.get_user_by_email(email=login_input.email)

        if user is None or not checkPassword(login_input.password, user.password):
            raise BadRequestException("incorrect email or password")

        access_token = self.auth_token.create_access_token(TokenData(user_id=str(user.id)))

        return access_token

    async def get_current_user(
        self, request: Request, data: HTTPAuthorizationCredentials = Depends(bearer)
    ) -> BaseUser:
        credentials = data.credentials

        access_token_data = self.auth_token.verify_access_token(credentials)

        user = await UsersRepository.get_user_by_id(access_token_data.user_id)

        return user



async def auth(role:UserRoles):

    async def get_current_user(request: Request, data: HTTPAuthorizationCredentials = Depends(bearer)) -> BaseUser:
        credentials = data.credentials

        if not credentials:
            pass

        access_token_data = AuthToken.verify_access_token(credentials)

        user = await UsersRepository.get_user_by_id(access_token_data.user_id)

        return user
    

    return get_current_user




auth = Auth()
