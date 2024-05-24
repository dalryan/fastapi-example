from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """All the necessary settings to run/configure the app"""

    SERVICE_NAME: str = "example-service"
    DESCRIPTION: str = "This is indeed an example service."
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "local"

    API_V1_PREFIX: str = "/api/v1"
    API_V2_PREFIX: str = "/api/v2"

    ORIGINS: List[str] = ["*"]

    SENTRY_DSN: str = ""


settings = Settings()
