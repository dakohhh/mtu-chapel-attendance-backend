from mongoengine import Document, StringField, IntField, ReferenceField, CASCADE
from .choices import DEPARTMENT_CHOICES


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
            "email": self.email
        }


class AcademicSession(Document):
    session = StringField(default="2023/2024")

    def to_dict(self):

        return {"session": self.session}


class Student(Document):

    firstname = StringField(required=True)
    othername = StringField(null=True, required=False)
    lastname = StringField(required=True)
    matric_no = IntField()
    level = IntField()
    departmant = IntField(choices=DEPARTMENT_CHOICES)

    academic_session: AcademicSession = ReferenceField(
        AcademicSession, default=None, reverse_delete_rule=CASCADE
    )

    chapel_seat_number = IntField(required=True)

    chapel_group_number = IntField(required=True)

    meta = {"strict": False}

    def to_dict(self):
        return {
            "id": str(self.id),
            "firstname": self.firstname,
            "matric_no": self.matric_no,
            "level": self.level,
            "academic_session": self.academic_session.session,
            "departmant": self.departmant,
            "chapel_group_number": self.chapel_group_number,
            "chapel_seat_number": self.chapel_seat_number,
        }
