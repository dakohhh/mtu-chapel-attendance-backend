from fastapi import Request, status
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from mongoengine.errors import MongoEngineException


class UnauthorizedException(Exception):
    def __init__(self, message: str):
        self.message = message


async def unauthorized_exception_handler(
    request: Request, exception: UnauthorizedException
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "status": status.HTTP_401_UNAUTHORIZED,
            "message": exception.message,
            "success": False,
        },
        headers={"WWW-Authenticate": "Bearer"}
    )


class NotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message


async def not_found(request: Request, exception: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "status": status.HTTP_404_NOT_FOUND,
            "message": exception.message,
            "success": False,
        },
    )




class ForbiddenException(Exception):
    def __init__(self, message: str):
        self.message = message


async def forbidden_exception_handler(request: Request, exception: ForbiddenException):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "status": status.HTTP_403_FORBIDDEN,
            "message": exception.message,
            "success": False,
        },
    )


class BadRequestException(Exception):
    def __init__(self, message: str):
        self.message = message


async def bad_request_exception_handler(
    request: Request, exception: BadRequestException
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status": status.HTTP_400_BAD_REQUEST,
            "message": exception.message,
            "success": False,
        },
    )
