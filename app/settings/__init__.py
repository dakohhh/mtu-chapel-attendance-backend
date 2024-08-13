import os
import certifi
from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

DEPLOYMENT_ENV = os.getenv("PYTHON_ENV")

BASE_DIR = Path(__file__).resolve().parent.parent

CERTIFICATE = os.path.join(os.path.dirname(certifi.__file__), "cacert.pem")

# Path to .env file
DOTENV = os.path.join(BASE_DIR, ".env")


class MailConfig(BaseModel):
    """
    Email configurations
    """
    SUPPORT_EMAIL: str = "support@fastapi-boilertemplate.com"
    DEFAULT_EMAIL_FROM: str = "fastapi-boilertemplate <no-reply@fastapi-boilertemplate.com>"


    # SMTP Configs
    SMTP_HOST: str = Field("", env="MAIL_HOST")
    SMTP_PORT: int = Field(587, env="MAIL_PORT")
    SMTP_USER: str = Field("", env="MAIL_USERNAME")
    SMTP_PASSWORD: str = Field("", env="MAIL_PASSWORD")
    MAIL_SECURE: bool = Field(False, env="MAIL_SECURE")


class GlobalConfig(BaseSettings):
    """
    Global configurations that are the same across all environments
    """
    APP_NAME: str = Field("application-name", env="APP_NAME")
    APP_VERSION: str = Field("application-version", env="APP_VERSION")
    APPLICATION_CERTIFICATE:str = Field(default=CERTIFICATE)
    PORT: int = Field(8000, env="PORT")

    # Security / Auth Configs
    BCRYPT_SALT: int = 10
    ACCESS_TOKEN_JWT_EXPIRES_IN: str = Field("1h", env="ACCESS_TOKEN_JWT_EXPIRES_IN")
    REFRESH_TOKEN_JWT_EXPIRES_IN: str = Field("30d", env="REFRESH_TOKEN_JWT_EXPIRES_IN")
    DEFAULT_DB_TOKEN_EXPIRY_DURATION: str = Field("5m", env="DEFAULT_DB_TOKEN_EXPIRY_DURATION")

    # Email / Auth Configs
    SUPPORT_EMAIL: str = "support@fastapi-boilertemplate.com"
    DEFAULT_EMAIL_FROM: str = "fastapi-boilertemplate <no-reply@fastapi-boilertemplate.com>"
    USE_AWS_SES: bool = False

    MAILER: MailConfig = Field(default_factory=MailConfig)



class DevelopmentConfig(GlobalConfig):
    """
    Development configurations
    """
    DEBUG: bool = True
    JWT_SECRET: str = "19d56917f78c581c15056ae050a6f2b790db82c5"
    MONGODB_URI: str = "mongodb://localhost:27017/"
    BASE_URL: str = "http://localhost:3000"


class ProductionConfig(GlobalConfig):
    """
    Production configurations
    """
    DEBUG: bool = False
    JWT_SECRET: str
    MONGODB_URI: str
    BASE_URL : str



def getenv():

    if DEPLOYMENT_ENV is None or DEPLOYMENT_ENV not in ["development", "production"]:
        raise ValueError("Invalid deployment environment")

    if DEPLOYMENT_ENV == "development":
        return DevelopmentConfig()
    
    return ProductionConfig()

# class GLOBAL_SETTINGS(BaseModel):
#     pass




settings = getenv()






# class Settings(BaseSettings):

#     DEV: bool

#     BASE_DIR: Union[str, Path] = str(BASE_DIR)

#     SECRET_KEY: str

#     JWT_ALGORITHM: str

#     APPLICATION_CERTIFICATE: str = CERTIFICATE

#     DEV_MONGO_URL : str

#     PROD_MONGO_URL: str

#     model_config = SettingsConfigDict(env_file=DOTENV)
