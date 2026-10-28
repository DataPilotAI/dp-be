from fastapi import APIRouter

from app.api import health

# The BFF forwards /api/ unchanged, so every route lives under this prefix.
API_PREFIX = "/api"

api_router = APIRouter(prefix=API_PREFIX)
api_router.include_router(health.router)
