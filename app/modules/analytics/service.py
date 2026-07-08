from app.modules.portfolio.service import PortfolioService


class AnalyticsService:
    """Business logic for analytics."""

    def __init__(self) -> None:
        self._portfolio_service = PortfolioService()

    def get_summary(self) -> dict:
        """Return portfolio summary."""

        portfolio = self._portfolio_service.get_portfolio()

        total_invested = sum(
            item["total_invested"]
            for item in portfolio
        )

        current_value = sum(
            item["current_value"]
            for item in portfolio
        )

        total_profit_loss = (
            current_value - total_invested
        )

        profit_percentage = (
            (total_profit_loss / total_invested) * 100
            if total_invested > 0
            else 0
        )

        return {
            "total_invested": total_invested,
            "current_value": current_value,
            "total_profit_loss": total_profit_loss,
            "profit_percentage": profit_percentage,
            "assets_count": len(portfolio),
        }