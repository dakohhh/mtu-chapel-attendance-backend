from datetime import datetime
from mongoengine import Document, StringField, IntField, ReferenceField, CASCADE, DateTimeField
from ..enums.department_choices import Department
from .academic_session import AcademicSession

class Student(Document):

    firstname = StringField(required=True)
    othername = StringField(null=True, required=False, default=None)
    lastname = StringField(required=True)
    matric_no = IntField(required=False, unique=True)
    level = IntField()
    department = IntField(choices=Department)

    academic_session: AcademicSession = ReferenceField(
        AcademicSession, default=None, reverse_delete_rule=CASCADE, required=True
    )
    
    gender = IntField(required=False)

    chapel_seat_number = IntField(required=True)

    chapel_group_number = IntField(required=True)

    created_at = DateTimeField(default=datetime.now)

    updated_at = DateTimeField(default=datetime.now)

    meta = {"strict": False}


    @property
    def resolve_gender(self):
        if self.gender == 1:
            return "F"
        return "M"

    def to_dict(self):
        return {
            "id": str(self.id),
            "firstname": self.firstname,
            "lastname": self.lastname,
            "gender": self.resolve_gender,
            "matric_no": self.matric_no,
            "level": self.level,
            "academic_session": {
                "academic_session_id": str(self.academic_session.id),
                "session": self.academic_session.session,
                "semester": self.academic_session.semester,
                "format": self.academic_session.format_session if self.academic_session else None
            },
            "department": self.department,
            "chapel_group_number": self.chapel_group_number,
            "chapel_seat_number": self.chapel_seat_number,
        }
    

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"