from fastapi import APIRouter

from app.modules.portfolio.schemas import PortfolioItemResponse
from app.modules.portfolio.service import PortfolioService


router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)


service = PortfolioService()


@router.get(
    "",
    response_model=list[PortfolioItemResponse],
)
def get_portfolio():
    """Return current portfolio."""

    return service.get_portfolio()