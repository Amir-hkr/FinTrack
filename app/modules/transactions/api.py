from fastapi import APIRouter, status

from app.core.response import success_response
from app.modules.transactions.schemas import (
    CreateTransactionRequest,
)
from app.modules.transactions.service import TransactionService


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


service = TransactionService()


@router.get("")
def get_transactions():
    """Return all transactions."""

    return success_response(
        data=service.get_transactions(),
        message="Transactions retrieved successfully",
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
def create_transaction(
    request: CreateTransactionRequest,
):
    """Create a new transaction."""

    return success_response(
        data=service.create_transaction(request),
        message="Transaction created successfully",
        status_code=status.HTTP_201_CREATED,
    )