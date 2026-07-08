from pydantic import BaseModel


class PortfolioItemResponse(BaseModel):
    """Portfolio item response."""

    asset_symbol: str
    quantity: float

    total_invested: float
    average_buy_price: float

    current_price: float
    current_value: float

    profit_loss: float
    profit_percentage: float