from fastapi import APIRouter

from app.modules.portfolio.service import PortfolioService


router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)


portfolio_service = PortfolioService()


@router.get("")
async def get_portfolio():
    """
    Get current portfolio with live market prices.
    """

    data = await portfolio_service.get_portfolio()

    return {
        "success": True,
        "message": "Portfolio retrieved successfully",
        "data": data,
    }