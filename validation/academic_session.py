from pydantic import BaseModel




class CreateAcademicSession(BaseModel):
    session: str
    semester: str
