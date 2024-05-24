"""The entrypoint for the FastAPI app

It creates an APIRouter and adds each of the individual versioned routers to it
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

import sentry_sdk
from fastapi import FastAPI

from src.api.v1.api import api_router_v1
from src.core.config import settings
from src.core.logging import logger

if settings.ENVIRONMENT != "local":
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN, environment=settings.ENVIRONMENT, enable_tracing=True
    )


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("Starting Up")
    logger.info(f"Collected ENV: {settings}")
    yield
    logger.info("Shutting Down")


app = FastAPI(
    lifespan=lifespan,
    title=settings.SERVICE_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
)

app.include_router(api_router_v1, prefix=settings.API_V1_PREFIX)
