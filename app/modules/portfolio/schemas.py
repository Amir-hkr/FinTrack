from pydantic import BaseModel


class PortfolioItemResponse(BaseModel):
    """Single portfolio item response."""

    asset_symbol: str
    quantity: float