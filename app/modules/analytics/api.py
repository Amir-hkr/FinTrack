from fastapi import APIRouter

from app.core.response import success_response
from app.modules.analytics.service import AnalyticsService


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


service = AnalyticsService()


@router.get("/summary")
def get_summary():
    """Return portfolio analytics summary."""

    return success_response(
        data=service.get_summary(),
        message="Analytics summary retrieved successfully",
    )