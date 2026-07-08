from datetime import datetime

from pydantic import BaseModel, Field

from app.modules.transactions.models import TransactionType


class CreateTransactionRequest(BaseModel):
    """Request model for creating a transaction."""

    asset_symbol: str = Field(
        min_length=1,
        max_length=10,
    )

    type: TransactionType

    quantity: float = Field(
        gt=0,
    )

    price: float = Field(
        gt=0,
    )

    fee: float = Field(
        default=0,
        ge=0,
    )

    note: str = Field(
        default="",
        max_length=200,
    )


class TransactionResponse(BaseModel):
    """Response model for a transaction."""

    id: str
    asset_symbol: str
    type: TransactionType
    quantity: float
    price: float
    fee: float
    created_at: datetime
    note: str