from fastapi import APIRouter

from app.api.api_v1.endpoints import fibonacci

api_router = APIRouter()
api_router.include_router(fibonacci.router, tags=["fibonacci"])
