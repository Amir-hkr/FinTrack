from collections import defaultdict

from app.modules.transactions.models import Transaction, TransactionType


class PortfolioCalculator:
    """Calculate portfolio from transactions."""

    def calculate(
        self,
        transactions: list[Transaction],
    ) -> list[dict]:
        """Calculate current holdings."""

        holdings = defaultdict(float)

        for transaction in transactions:
            if transaction.type == TransactionType.BUY:
                holdings[transaction.asset_symbol] += (
                    transaction.quantity
                )

            elif transaction.type == TransactionType.SELL:
                holdings[transaction.asset_symbol] -= (
                    transaction.quantity
                )

        return [
            {
                "asset_symbol": symbol,
                "quantity": quantity,
            }
            for symbol, quantity in holdings.items()
            if quantity > 0
        ]