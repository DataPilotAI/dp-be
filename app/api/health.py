from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: str


@router.get("/healthz")
async def healthz() -> HealthResponse:
    return HealthResponse(status="ok")
