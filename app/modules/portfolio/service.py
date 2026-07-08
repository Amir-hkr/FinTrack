from app.modules.market.repository import MarketRepository
from app.modules.portfolio.calculator import PortfolioCalculator
from app.modules.transactions.repository import TransactionRepository


class PortfolioService:
    """Business logic for portfolio."""

    def __init__(self) -> None:
        self._transaction_repository = TransactionRepository()
        self._market_repository = MarketRepository()
        self._calculator = PortfolioCalculator()

    def get_portfolio(self) -> list[dict]:
        """Return current portfolio."""

        transactions = self._transaction_repository.get_all()

        portfolio = self._calculator.calculate(
            transactions
        )

        result = []

        for item in portfolio:
            market_price = self._market_repository.get_by_symbol(
                item["asset_symbol"]
            )

            current_price = (
                market_price.price
                if market_price
                else 0
            )

            current_value = (
                item["quantity"]
                * current_price
            )

            profit_loss = (
                current_value
                - item["total_invested"]
            )

            profit_percentage = (
                (profit_loss / item["total_invested"]) * 100
                if item["total_invested"] > 0
                else 0
            )

            result.append(
                {
                    **item,
                    "current_price": current_price,
                    "current_value": current_value,
                    "profit_loss": profit_loss,
                    "profit_percentage": profit_percentage,
                }
            )

        return result