import bson
from database.schema import Student
from validation import CreateStudent, UpdateStudent
from beanie import PydanticObjectId
from typing import List, Union

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
    async def get_student_by_id(user_id: PydanticObjectId) -> Union[Student, None]:

        query = Student.objects(id=user_id).first()

        return query
    


    @staticmethod
    async def get_all_students(offset, per_page, level:int=None) -> List[Student]:

        if level:
            query = Student.objects(level=level).order_by("-created_at").skip(offset).limit(per_page)

        else:

            query = Student.objects().order_by("-created_at").skip(offset).limit(per_page)

        return query
    

    @staticmethod
    async def get_all_student_by_level_only(level:int) -> List[Student]:

        query =  Student.objects(level=level)

        return query
    

    @staticmethod
    async def get_all_student_by_level_and_session(level:int, academic_session:PydanticObjectId) -> List[Student]:

        query =  Student.objects(level=level, academic_session=academic_session)

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
    async def remove_student(student:Student) -> Student:

        student.delete()

        return student
    
    @staticmethod
    async def remove_all_students():

        query = Student.objects().delete()

        return query
    


    @staticmethod
    async def update_student(student:Student, param: UpdateStudent) -> Student:

        if param.firstname:
            student.firstname = param.firstname
        
        if param.othername:
            student.othername = param.othername

        if param.lastname:
            student.lastname = param.lastname

        if param.matric_no:
            student.matric_no = param.matric_no

        if  param.level:
            student.level = param.level

        if param.department:
            student.department = param.department

        if param.academic_session: 
            student.academic_session = param.academic_session

        if param.chapel_group_number:
            student.chapel_group_number = param.chapel_group_number

        if param.chapel_seat_number:
            student.chapel_seat_number = param.chapel_seat_number


        student.save()

        return student