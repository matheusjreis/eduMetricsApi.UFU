from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables or .env files."""

    model_config = SettingsConfigDict(
        env_file=(".env", ".env.local"),
        env_file_encoding="utf-8",
        extra="ignore",
        env_prefix="",
    )

    app_name: str = Field(default="EduMetrics API", env="APP_NAME")
    api_prefix: str = Field(default="/api")
    database_url: str = Field(default="sqlite:///./data/edumetrics.db", env="DATABASE_URL")
    sqlalchemy_echo: bool = Field(default=False, env="SQLALCHEMY_ECHO")

    @property
    def is_sqlite(self) -> bool:
        return self.database_url.startswith("sqlite")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
