from fastapi import APIRouter

from app.core.response import success_response
from app.modules.analytics.service import AnalyticsService


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


service = AnalyticsService()


@router.get("/summary")
async def get_summary():
    """Return portfolio analytics summary."""

    return success_response(
        data=await service.get_summary(),
        message="Analytics summary retrieved successfully",
    )