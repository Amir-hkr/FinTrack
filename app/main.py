from fastapi import FastAPI

from app.core.config import settings
from app.modules.assets.api import router as assets_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)


@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    """Health check endpoint."""
    return {
        "message": f"Welcome to {settings.app_name}",
    }


app.include_router(assets_router)