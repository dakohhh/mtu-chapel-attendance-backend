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

    students = await StudentRepository.get_all_student_by_level_and_session(
        generate_absentees.level, generate_absentees.academic_session
    )

    log_data = pd.read_csv(generate_absentees.log_file.file)

    log_matric_no_list = log_data["ImageName"].to_list()

    for student in students:
        if student.matric_no not in log_matric_no_list:

            student_dict = student.to_dict()

            student_dict["title_of_service"] = generate_absentees.title
            absentees.append(student_dict)

    context = {"absentees": absentees, "title": generate_absentees.title}

    return CustomResponse(f"get absentees for {generate_absentees.title}", data=context)


@router.get("/warning_letter")
async def get_warning_letters(
    request: Request,
    student_id: PydanticObjectId,
    title: str,
    user: Users = Depends(auth.get_current_user),
):

    student = await StudentRepository.get_student_by_id(student_id)

    if student is None:
        return CustomResponse("student not found", status_code=status.HTTP_404_NOT_FOUND)

    warning_letter = WarningLetter(
        student.fullname, str(student.matric_no), "ABSENCE FROM CHAPEL", title
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
