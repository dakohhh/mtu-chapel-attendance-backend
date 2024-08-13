from fastapi import FastAPI, Request
import random
from bson import ObjectId
from contextlib import asynccontextmanager
from .libraries.mongo import connect_to_mongo, disconnect_from_mongo
from .middleware.processes import configure_processes_middleware
from .middleware.exception import handle_custom_exceptions, add_exception_handlers
from .router.academic_session import router as academic_session
from .router.auth import router as auth
from .router.user import router as user
from .router.students import router as student
from .router.attendance import router as attendance



@asynccontextmanager
async def lifespan(application: FastAPI):
    try:
        await connect_to_mongo()
        yield
    finally:
        await disconnect_from_mongo()

app = FastAPI(title="MTU CHAPEL ATTENDANCE SYSTEM", lifespan=lifespan)


configure_processes_middleware(app)
add_exception_handlers(app)
handle_custom_exceptions(app)




app.include_router(auth)
app.include_router(user)
app.include_router(student)
app.include_router(academic_session)
app.include_router(attendance)


# addExceptionHandlers(app)


# import pandas as pd
# from database.schema import Student, AcademicSession


@app.post("/test")
async def creat_test_students(request: Request):

    data = pd.read_csv("./data/MTU Student Database.csv")

    for index, row in data.iterrows():

        split_names = row["OtherNames"].split(
            maxsplit=1
        )  # Split the full name into a list of names with at most one split
        if len(split_names) == 1:
            split_names.append(None)

        student = Student(
            firstname=split_names[0],
            othername=split_names[1],
            lastname=row["LastName"],
            matric_no=row["MatricNumber"],
            level=row["Level"],
            department=random.randint(1, 11),
            chapel_seat_number=random.randint(1, 35),
            chapel_group_number=random.randint(1, 8),
        )

        student.save()

    return True


@app.post("/apply")
async def apply_acdemic_session_students(request: Request):

    academic_session_ = AcademicSession.objects(
        id=ObjectId("661bf99480564d2bf479ccac")
    ).first()

    students = Student.objects()

    for student in students:
        student.academic_session = academic_session_

        student.save()

    return True


# import pandas as pd
# from database.choices import *
# from utils.resolve import resolve_dept, resolve_level, resolve_gender
# from bson import ObjectId
# from database.schema import AcademicSession


@app.post("/create-mtu-script")
async def create_script(request: Request):

    data = pd.read_excel(
        "./data/COMPREHENSIVE_LIST_OF_REGISTERED_STUDENTS_WITH_ALLOCATED_HOSTEL.xlsx"
    )

    data.drop(data.columns[-1], axis=1, inplace=True)

    data.dropna(subset=["LEVEL", "MATRICULATION"], inplace=True)

    data = data.drop_duplicates(subset=["MATRICULATION"], keep="first")

    dept = {val: key for key, val in dict(DEPARTMENT_CHOICES).items()}

    data["DEPT"] = data["DEPT"].apply(resolve_dept)

    data["LEVEL"] = data["LEVEL"].apply(resolve_level)

    data["GENDER"] = data["GENDER"].apply(resolve_gender)

    # data.to_excel("./data/preprocessed.xlsx", index=False)

    current_academic_session = AcademicSession.objects().first()

    print(current_academic_session)

    for index, row in data.iterrows():

        names = str(row["OTHER NAMES"]).split(" ")

        first_name = names[0]
        other_name = names[1] if len(names) > 1 else None

        print(row["S/N"])

        student = Student(
            firstname=first_name,
            othername=other_name,
            lastname=row["SURNAME"],
            matric_no=row["MATRICULATION"],
            level=row["LEVEL"],
            department=row["DEPT"],
            gender=row["GENDER"],
            chapel_seat_number=random.randint(1, 35),
            chapel_group_number=random.randint(1, 8),
            academic_session=current_academic_session,
        )

        student.save()
