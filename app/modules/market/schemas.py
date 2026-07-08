from pydantic import BaseModel


class MarketPriceResponse(BaseModel):
    """Market price response."""

    symbol: str
    price: float


class UpdateMarketPriceRequest(BaseModel):
    """Update market price request."""

    symbol: str
    price: float