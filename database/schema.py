from mongoengine import (
    Document,
    StringField,
    IntField,
    ReferenceField,
    CASCADE,
    DateTimeField,
)
from .choices import DEPARTMENT_CHOICES
from utils.date import get_current_datetime
from datetime import datetime


class Users(Document):
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    email = StringField(required=True)
    password = StringField()

    def to_dict(self):
        return {
            "id": str(self.id),
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }


class AcademicSession(Document):
    session = StringField(default="2023/2024")
    semester = StringField(default="First")

    def to_dict(self):

        return {"id": str(self.id), "session": self.session, "semester": self.semester}
    
    @property
    def format_session(self):
        return f"{self.session} {self.semester} Semester"


class Student(Document):

    firstname = StringField(required=True)
    othername = StringField(null=True, required=False)
    lastname = StringField(required=True)
    matric_no = IntField()
    level = IntField()
    department = IntField(choices=DEPARTMENT_CHOICES)

    academic_session: AcademicSession = ReferenceField(
        AcademicSession, default=None, reverse_delete_rule=CASCADE
    )

    chapel_seat_number = IntField(required=True)

    chapel_group_number = IntField(required=True)

    created_at = DateTimeField(default=datetime.now)

    updated_at = DateTimeField(default=datetime.now)

    meta = {"strict": False}

    def to_dict(self):
        return {
            "id": str(self.id),
            "firstname": self.firstname,
            "lastname": self.lastname,
            "matric_no": self.matric_no,
            "level": self.level,
            "academic_session": (
                self.academic_session.format_session if self.academic_session else None
            ),
            "department": self.department,
            "chapel_group_number": self.chapel_group_number,
            "chapel_seat_number": self.chapel_seat_number,
        }
    

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
