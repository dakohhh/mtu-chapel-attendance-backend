import asyncio
from fastapi import APIRouter, Request, Depends
from exceptions import BadRequestException



router = APIRouter(prefix="/api/academic_session", tags=["Academic Session"])


@router.get("/")
async def get_all_academic_sessions():

    return None


@router.post("/")
async def add_academic_session():

    
    pass