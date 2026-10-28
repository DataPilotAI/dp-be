from pydantic import SecretStr

from app.core.config import Settings
from app.main import APP_TITLE, create_app


def test_create_app_uses_configured_title() -> None:
    settings = Settings(postgres_user="u", postgres_password=SecretStr("p"), postgres_db="db")

    app = create_app(settings)

    assert app.title == APP_TITLE
