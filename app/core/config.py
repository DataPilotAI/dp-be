from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

ENV_PREFIX = "DP_BE_"
DB_DRIVER = "postgresql+asyncpg"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix=ENV_PREFIX, env_file=".env", extra="ignore", populate_by_name=True
    )

    # Aliased to the unprefixed names so the Postgres container shares the same .env values.
    # Required, no default: credentials must come from the environment.
    postgres_user: str = Field(validation_alias="POSTGRES_USER")
    postgres_password: SecretStr = Field(validation_alias="POSTGRES_PASSWORD")
    postgres_db: str = Field(validation_alias="POSTGRES_DB")
    db_host: str = "localhost"
    db_port: int = 5432
    db_echo: bool = False
    cors_allowed_origins: list[str] = []

    @property
    def database_url(self) -> URL:
        # URL.create escapes special characters in the password.
        return URL.create(
            DB_DRIVER,
            username=self.postgres_user,
            password=self.postgres_password.get_secret_value(),
            host=self.db_host,
            port=self.db_port,
            database=self.postgres_db,
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
