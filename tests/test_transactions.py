from app.modules.transactions.models import TransactionType
from app.modules.transactions.repository import TransactionRepository


def test_create_buy_transaction():

    repository = TransactionRepository()

    transaction = repository.create(
        asset_symbol="BTC",
        type=TransactionType.BUY,
        quantity=1,
        price=100000,
        fee=10,
        note="Test buy",
    )

    assert transaction.asset_symbol == "BTC"
    assert transaction.type == TransactionType.BUY
    assert transaction.quantity == 1


def test_create_sell_transaction():

    repository = TransactionRepository()

    transaction = repository.create(
        asset_symbol="BTC",
        type=TransactionType.SELL,
        quantity=0.5,
        price=120000,
        fee=5,
        note="Test sell",
    )

    assert transaction.type == TransactionType.SELL
    assert transaction.quantity == 0.5


def test_get_transactions():

    repository = TransactionRepository()

    transactions = repository.get_all()

    assert len(transactions) > 0