from fastapi import APIRouter, status

from app.modules.market.schemas import (
    MarketPriceResponse,
    UpdateMarketPriceRequest,
)
from app.modules.market.service import MarketService


router = APIRouter(
    prefix="/market",
    tags=["Market"],
)


service = MarketService()


@router.get(
    "",
    response_model=list[MarketPriceResponse],
)
def get_prices():
    """Return market prices."""

    return service.get_prices()


@router.post(
    "",
    response_model=MarketPriceResponse,
    status_code=status.HTTP_201_CREATED,
)
def update_price(
    request: UpdateMarketPriceRequest,
):
    """Create or update market price."""

    return service.update_price(
        symbol=request.symbol,
        price=request.price,
    )