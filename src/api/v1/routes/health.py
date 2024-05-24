"""Endpoints for base checks"""

from fastapi import APIRouter

from src.api.v1 import models

router = APIRouter()


@router.get(
    path="/health",
    response_model=models.Health,
    description="Request a health check against the API",
)
async def read_health() -> models.Health:
    """Get the health status of the API"""

    return models.Health()
