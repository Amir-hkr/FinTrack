from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)


@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    """Health check endpoint."""
    return {"message": f"Welcome to {settings.app_name}"}