from fastapi import FastAPI

from app.core.config import settings
from app.core.response import success_response

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)


@app.get("/", tags=["Root"])
def root():
    """Health check endpoint."""
    return success_response(
        message=f"Welcome to {settings.app_name}",
        data=None,
    )