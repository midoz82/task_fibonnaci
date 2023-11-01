import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import (AnyHttpUrl, AnyUrl, BaseSettings, EmailStr, HttpUrl,
                      PostgresDsn, validator)


class Settings(BaseSettings):
    # Reviewed:
    PROJECT_NAME: str = "task-demo"
    API_V1_STR: str = "/api/v1"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "fast-api-celery"
    POSTGRES_PASSWORD: str = "123"
    POSTGRES_DB: str = "fast-api-celery"
    POSTGRES_PORT: str = "5432"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
