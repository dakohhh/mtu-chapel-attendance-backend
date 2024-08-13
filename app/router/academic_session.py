import asyncio
from fastapi import APIRouter, Request, Depends
from app.utils.response import CustomResponse
from ..schemas import CreateAcademicSession
from ..utils.exceptions import BadRequestException
from ..serializer import AllAcademicSessionSerializer
from ..repository.academic_session import AcademicSessionRepository


router = APIRouter(prefix="/api/academic_session", tags=["Academic Session"])


@router.get("/")
async def get_all_academic_sessions():

    academic_sessions = await AcademicSessionRepository.get_all_academic_session()

    serialize_academic_sessions = AllAcademicSessionSerializer(
        academic_session=list(academic_sessions)
    )

    context = {
        "academic_sessions": serialize_academic_sessions.model_dump()["academic_session"]
    }
    return CustomResponse(
        "get all academic sessions",
        data=context,
    )


@router.post("/")
async def add_academic_session(session: CreateAcademicSession):

    academic_session = await AcademicSessionRepository.add_academic_session(session)

    context = {"academic_session": academic_session.to_dict()}

    return CustomResponse("create academic session", data=context)
