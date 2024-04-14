import random
from bson import ObjectId
from settings import settings
from mongoengine import connect
from middleware.processes import handleMiddlewareProcesses
from middleware.exception import addExceptionHandlers, handleCustomExceptions
from fastapi import FastAPI, Request
from router.academic_session import router as academic_session
from router.auth import router as auth
from router.user import router as user
from router.students import router as student


connect(
    host=(settings.DEV_MONGO_URL if settings.DEV else settings.PROD_MONGO_URL),
    name="MTU_CHAPEL",
    tls=True if not settings.DEV else False,
    tlsCAFile=settings.APPLICATION_CERTIFICATE if not settings.DEV else None,
)


app = FastAPI(title="MTU CHAPEL ATTENDANCE SYSTEM")


handleMiddlewareProcesses(app)
handleCustomExceptions(app)

app.include_router(auth)
app.include_router(user)
app.include_router(student)
app.include_router(academic_session)


addExceptionHandlers(app)


import pandas as pd
from database.schema import Student,AcademicSession


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


    academic_session_ = AcademicSession.objects(id=ObjectId("661bf99480564d2bf479ccac")).first()

    students = Student.objects()

    for student in students:
        student.academic_session = academic_session_

        student.save()

    return True

