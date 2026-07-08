from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Application configuration."""

    app_name: str = "FinTrack API"
    app_version: str = "1.0.0"
    app_description: str = "Portfolio Tracker API"
    debug: bool = True


settings = Settings()