from app.modules.portfolio.calculator import PortfolioCalculator
from app.modules.transactions.repository import TransactionRepository


class PortfolioService:
    """Business logic for portfolio."""

    def __init__(self) -> None:
        self._transaction_repository = TransactionRepository()
        self._calculator = PortfolioCalculator()

    def get_portfolio(self) -> list[dict]:
        """Return current portfolio."""

        transactions = self._transaction_repository.get_all()

        return self._calculator.calculate(
            transactions
        )