import requests
from pymongo.errors import PyMongoError
from fastapi import FastAPI, status,HTTPException
from fastapi.responses import JSONResponse
from exceptions import (
    BadRequestException,
    NotFoundException,
    UnauthorizedException,
    CredentialsException,
    ServerErrorException,
    UserExistException,
    user_exist_exception_handler,
    unauthorized_exception_handler,
    server_exception_handler,
    not_found,
    credentail_exception_handler,
    bad_request_exception_handler
)



def handleCustomExceptions(app: FastAPI):

    app.add_exception_handler(UserExistException, user_exist_exception_handler)
    app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
    app.add_exception_handler(ServerErrorException, server_exception_handler)
    app.add_exception_handler(NotFoundException, not_found)
    app.add_exception_handler(CredentialsException, credentail_exception_handler)
    app.add_exception_handler(BadRequestException, bad_request_exception_handler)




def addExceptionHandlers(app:FastAPI):

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"status": exc.status_code, "message": exc.detail, "success": False},
        )


    @app.exception_handler(requests.HTTPError)
    async def http_exception_handler(request, exc: requests.HTTPError):
        return JSONResponse(
            status_code=exc.response.status_code,
            content={
                "status": exc.response.status_code,
                "message": exc.response.json()["message"],
                "success": False,
            },
        )


    @app.exception_handler(PyMongoError)
    async def http_exception_handler(request, exc: PyMongoError):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": exc._message,
                "success": False,
            },
        )


