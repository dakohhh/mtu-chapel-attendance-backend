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
            academic_session=student.academic_session,
            chapel_group_number=student.chapel_group_number,
        )

        query.save()

        return query

    @staticmethod
    async def get_student_by_matric_no(matric_no: int) -> Student:

        query = Student.objects(matric_no=matric_no).first()
        return query

    @staticmethod
    async def get_student_by_id(user_id: PydanticObjectId) -> Student:

        query = Student.objects(id=user_id).first()

        return query
    


    @staticmethod
    async def get_all_students(offset, per_page, level:int=None) -> List[Student]:

        if level:
            query = Student.objects(level=level).order_by("+firstname").skip(offset).limit(per_page)

        else:

            query = Student.objects().order_by("+firstname").skip(offset).limit(per_page)

        return query
    

    @staticmethod
    async def get_all_student_by_level_only(level:int) -> List[Student]:

        query =  Student.objects(level=level)

        return query
    


    @staticmethod
    async def get_total_student_count() -> int:
        query = Student.objects().count()

        return query
    

    @staticmethod
    async def get_total_student_count_by_level(level) -> int:
        query = Student.objects(level=level).count()

        return query
    

    @staticmethod
    async def remove_student():
        return