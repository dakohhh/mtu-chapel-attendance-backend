from fastapi import Form, UploadFile, File
from beanie import PydanticObjectId


class GenerateAbsentees:
    def __init__(
        self,
        level: int = Form(...),
        title: str = Form(...),
        academic_session: PydanticObjectId = Form(...),
        log_file: UploadFile = File(...),
    ):
        self.level = level
        self.title = title
        self.academic_session = academic_session
        self.log_file = log_file
