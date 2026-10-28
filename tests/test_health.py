from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient
from pydantic import SecretStr

from app.core.config import Settings
from app.main import create_app


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    settings = Settings(postgres_user="u", postgres_password=SecretStr("p"), postgres_db="db")
    transport = ASGITransport(app=create_app(settings))
    async with AsyncClient(transport=transport, base_url="http://test") as test_client:
        yield test_client


async def test_healthz_returns_ok(client: AsyncClient) -> None:
    response = await client.get("/api/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


async def test_healthz_rejects_post(client: AsyncClient) -> None:
    response = await client.post("/api/healthz")

    assert response.status_code == 405
