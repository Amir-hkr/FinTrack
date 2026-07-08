from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TransactionType(str, Enum):
    """Transaction type."""

    BUY = "BUY"
    SELL = "SELL"


@dataclass(slots=True)
class Transaction:
    """Represents an investment transaction."""

    id: str
    asset_symbol: str
    type: TransactionType
    quantity: float
    price: float
    fee: float
    created_at: datetime
    note: str