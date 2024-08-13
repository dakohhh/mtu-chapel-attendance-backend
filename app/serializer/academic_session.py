from pydantic import BaseModel
from beanie import PydanticObjectId
import json
from typing import List, Optional
from bson import ObjectId


# class AcademicSessionSerializer(BaseModel):
#     id: PydanticObjectId
#     session: str
#     semester: str

#     class Config:
#         json_encoders = {ObjectId: lambda v: str(v)}




class AcademicSessionSerializer(BaseModel):
    id: str
    session: str
    semester: str

    class Config:
        json_encoders = {ObjectId: lambda v: str(v)}


class AllAcademicSessionSerializer(BaseModel):
    academic_session: List[AcademicSessionSerializer]

    @property
    def model_serialize(self):
        return json.loads(super().model_dump_json())
