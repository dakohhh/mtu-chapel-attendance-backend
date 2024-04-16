import pandas as pd
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, Request, status
from utils.warning_letter import WarningLetter
from fastapi.responses import StreamingResponse
from io import BytesIO
from authentication.auth import auth
from client.response import CustomResponse
from validation import GenerateAbsentees
from database.schema import Users
from repository.student import StudentRepository


router = APIRouter(tags=["Atttendance"], prefix="/api/attendance")


@router.post("/absentees")
async def get_absentees(
    request: Request,
    generate_absentees: GenerateAbsentees = Depends(),
    user: Users = Depends(auth.get_current_user),
):

    absentees = []

    students = await StudentRepository.get_all_student_by_level_only(
        generate_absentees.level
    )

    log_data = pd.read_csv(generate_absentees.log_file.file)

    log_matric_no_list = log_data["ImageName"].to_list()

    for student in students:
        if student.matric_no not in log_matric_no_list:
            absentees.append(student.to_dict())

    context = {"absentees": absentees}

    return CustomResponse("get absentees for", data=context)


@router.get("/warning_letter")
async def get_warning_letters(
    request: Request,
    student_id: PydanticObjectId,
    user: Users = Depends(auth.get_current_user),
):

    student = await StudentRepository.get_student_by_id(student_id)

    warning_letter = WarningLetter(
        student.fullname, str(student.matric_no), "ABSENCE FROM CHAPEL"
    ).create_warning_letter()

    buffer = BytesIO()

    warning_letter.save(buffer)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": f"attachment; filename={student.fullname}_warning_letter.docx"
        },
    )
