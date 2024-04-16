from fastapi import Form, UploadFile, File


class GenerateAbsentees:
    def __init__(self, level: int = Form(...), log_file: UploadFile = File(...)):
        self.level = level
        self.log_file = log_file
