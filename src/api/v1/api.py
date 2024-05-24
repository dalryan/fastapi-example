"""V1 API router

Collects all the V1 endpoints and adds them to the APIRouter
"""

from fastapi import APIRouter

from src.api.v1.routes import health

api_router_v1 = APIRouter()

api_router_v1.include_router(health.router, prefix="", tags=["Health"])
