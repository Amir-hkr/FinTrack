from pydantic import BaseModel


class AnalyticsSummaryResponse(BaseModel):
    """Analytics summary response."""

    total_invested: float
    current_value: float
    total_profit_loss: float
    profit_percentage: float
    assets_count: int