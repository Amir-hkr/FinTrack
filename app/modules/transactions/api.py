from fastapi import APIRouter, status

from app.modules.transactions.schemas import (
    CreateTransactionRequest,
    TransactionResponse,
)
from app.modules.transactions.service import TransactionService


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


service = TransactionService()


@router.get(
    "",
    response_model=list[dict],
)
def get_transactions():
    """Return all transactions."""

    return service.get_transactions()


@router.post(
    "",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
)
def create_transaction(
    request: CreateTransactionRequest,
):
    """Create a new transaction."""

    return service.create_transaction(request)