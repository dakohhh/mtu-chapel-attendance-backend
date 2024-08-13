from pydantic import BaseModel



class CreateUser(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
