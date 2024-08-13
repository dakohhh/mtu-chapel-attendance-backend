from mongoengine import Document, StringField

class AcademicSession(Document):
    session = StringField(default="2023/2024")
    semester = StringField(default="First")

    def to_dict(self):

        return {"id": str(self.id), "session": self.session, "semester": self.semester}
    
    @property
    def format_session(self):
        return f"{self.session} {self.semester} Semester"