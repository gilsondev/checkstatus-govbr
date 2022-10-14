from functools import lru_cache
from typing import Any, Dict, List, Union

from pydantic import BaseSettings, PostgresDsn, SecretStr
from src import __version__


class Settings(BaseSettings):
    DEBUG: bool = False
    SECRET_KEY: SecretStr = SecretStr("s3cret")
    ALLOWED_HOSTS: List[str] = ["*"]
    ALLOWED_METHODS: List[str] = ["*"]
    ALLOWED_HEADERS: List[str] = ["*"]

    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    TITLE: str = "Checkstatus GovBR API"
    VERSION: str = __version__

    DATABASE_URL: Union[PostgresDsn, str] = "sqlite:///database.sqlite3"
    TEST_DATABASE_URL: Union[
        PostgresDsn, str
    ] = "postgresql://postgres:postgres@localhost:5435/checkstatusgovbr_test"

    class Config:
        env_file = ".env"

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.DEBUG,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "title": self.TITLE,
            "version": self.VERSION,
            "description": "API REST of project Checkstatus .gov.br",
            "contact": {
                "name": "Gilson Filho",
                "url": "https://gilsondev.in",
                "email": "me@gilsondev.in",
            },
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
