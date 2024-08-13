from jwt.exceptions import PyJWTError
from pymongo.errors import PyMongoError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import FastAPI, Request, status,HTTPException
from fastapi.responses import JSONResponse
from app.utils.response import CustomResponse
from ..utils.exceptions import (
    BadRequestException,
    NotFoundException,
    UnauthorizedException,
    ForbiddenException,
    unauthorized_exception_handler,
    not_found,
    bad_request_exception_handler,
    forbidden_exception_handler,
)




def handle_custom_exceptions(app: FastAPI):

    app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
    app.add_exception_handler(NotFoundException, not_found)
    app.add_exception_handler(BadRequestException, bad_request_exception_handler)
    app.add_exception_handler(ForbiddenException, forbidden_exception_handler)



def add_exception_handlers(app:FastAPI):

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request:Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail, "success": False, "data":None},
        )
    

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return CustomResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message ="Internal Server Error", success = False)
    

    @app.exception_handler(PyJWTError)
    async def jwt_exception_handler(request: Request, exc: PyJWTError):
        return CustomResponse(status=status.HTTP_401_UNAUTHORIZED, message="invalid-token", success=False)


    # @app.exception_handler(requests.HTTPError)
    # async def http_exception_handler(request, exc: requests.HTTPError):
    #     return JSONResponse(
    #         status_code=exc.response.status_code,
    #         content={
    #             "status": exc.response.status_code,
    #             "message": exc.response.json()["message"],
    #             "success": False,
    #         },
    #     )


    # @app.exception_handler(PyMongoError)
    # async def http_exception_handler(request, exc: PyMongoError):
    #     return JSONResponse(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         content={
    #             "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
    #             "message": exc._message,
    #             "success": False,
    #         },
    #     )


