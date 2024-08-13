from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def configure_processes_middleware(app: FastAPI):

    handle_CORS(app)


def handle_CORS(app: FastAPI):

    origins = [
        "http://localhost:3000",

    ]


    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
