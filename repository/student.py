from database.schema import Student
from validation import CreateStudent
from beanie import PydanticObjectId
from typing import List

class StudentRepository:
    @staticmethod
    async def create_student(student: CreateStudent) -> Student:
        query = Student(
            firstname=student.firstname,
            lastname=student.lastname,
            othername=student.othername,
            matric_no=student.matric_no,
            level=student.level,
            department=student.department,
            chapel_seat_number=student.chapel_seat_number,
            chapel_group_number=student.chapel_group_number,
        )

        query.save()

        return query

    @staticmethod
    async def get_student_by_matric_no(matric_no: int) -> Student:

        query = Student.objects(matric_no=matric_no).first()
        return query

    @staticmethod
    async def get_user_by_id(user_id: PydanticObjectId) -> Student:

        query = Student.objects(id=user_id).first()

        return query
    


    @staticmethod
    async def get_all_students() -> List[Student]:

        query = Student.objects()

        return query