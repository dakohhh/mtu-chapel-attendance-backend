import jwt
import jwt

from datetime import datetime
from pydantic import ValidationError
from ..schemas import TokenData
from fastapi.security import HTTPBearer

bearer = HTTPBearer()





class TokenService:
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
