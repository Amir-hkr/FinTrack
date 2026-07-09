from fastapi import APIRouter

from app.modules.market.service import MarketService


router = APIRouter(
    prefix="/market",
    tags=["Market"]
)


@router.get("/{symbol}")
async def get_market_price(symbol: str):

    price = await MarketService.get_price(symbol)

    return {
        "success": True,
        "symbol": symbol.upper(),
        "price": price,
        "currency": "USD"
    }