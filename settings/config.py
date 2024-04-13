import os
from typing import Union
import certifi
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent

CERTIFICATE = os.path.join(os.path.dirname(certifi.__file__), "cacert.pem")

# Path to .env file
DOTENV = os.path.join(BASE_DIR, ".env")



class Settings(BaseSettings):

    DEV: bool

    BASE_DIR: Union[str, Path] = str(BASE_DIR)

    SECRET_KEY: str

    JWT_ALGORITHM: str

    APPLICATION_CERTIFICATE: str = CERTIFICATE

    DEV_MONGO_URL : str

    PROD_MONGO_URL: str

    model_config = SettingsConfigDict(env_file=DOTENV)
