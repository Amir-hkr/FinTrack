from fastapi import APIRouter

from app.core.response import success_response
from app.modules.portfolio.service import PortfolioService


router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)


service = PortfolioService()


@router.get("")
def get_portfolio():
    """Return current portfolio."""

    return success_response(
        data=service.get_portfolio(),
        message="Portfolio retrieved successfully",
    )