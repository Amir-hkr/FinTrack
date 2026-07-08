from app.modules.portfolio.calculator import PortfolioCalculator
from app.modules.transactions.models import (
    Transaction,
    TransactionType,
)
from datetime import datetime


def test_portfolio_calculation():

    transactions = [
        Transaction(
            id="1",
            asset_symbol="BTC",
            type=TransactionType.BUY,
            quantity=1,
            price=100000,
            fee=10,
            created_at=datetime.now(),
            note="Buy BTC",
        ),
        Transaction(
            id="2",
            asset_symbol="BTC",
            type=TransactionType.SELL,
            quantity=0.3,
            price=120000,
            fee=5,
            created_at=datetime.now(),
            note="Sell BTC",
        ),
    ]

    calculator = PortfolioCalculator()

    result = calculator.calculate(
        transactions
    )

    btc = result[0]

    assert btc["asset_symbol"] == "BTC"
    assert btc["quantity"] == 0.7
    assert btc["total_invested"] == 70007