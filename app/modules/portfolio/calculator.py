from collections import defaultdict

from app.modules.transactions.models import (
    Transaction,
    TransactionType,
)


class PortfolioCalculator:
    """Calculate portfolio from transactions."""

    def calculate(
        self,
        transactions: list[Transaction],
    ) -> list[dict]:
        """Calculate current holdings."""

        holdings = defaultdict(
            lambda: {
                "quantity": 0,
                "total_invested": 0,
            }
        )

        for transaction in transactions:

            symbol = transaction.asset_symbol

            if transaction.type == TransactionType.BUY:

                holdings[symbol]["quantity"] += (
                    transaction.quantity
                )

                holdings[symbol]["total_invested"] += (
                    transaction.quantity
                    * transaction.price
                    + transaction.fee
                )

            elif transaction.type == TransactionType.SELL:

                current_quantity = (
                    holdings[symbol]["quantity"]
                )

                if current_quantity <= 0:
                    continue

                average_price = (
                    holdings[symbol]["total_invested"]
                    / current_quantity
                )

                holdings[symbol]["quantity"] -= (
                    transaction.quantity
                )

                holdings[symbol]["total_invested"] -= (
                    average_price
                    * transaction.quantity
                )

        result = []

        for symbol, data in holdings.items():

            if data["quantity"] <= 0:
                continue

            average_price = (
                data["total_invested"]
                / data["quantity"]
            )

            result.append(
                {
                    "asset_symbol": symbol,
                    "quantity": data["quantity"],
                    "total_invested": data["total_invested"],
                    "average_buy_price": average_price,
                }
            )

        return result