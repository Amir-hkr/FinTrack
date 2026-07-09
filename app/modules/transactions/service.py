from fastapi import HTTPException, status

from app.modules.assets.repository import AssetRepository
from app.modules.transactions.models import (
    Transaction,
    TransactionType,
)
from app.modules.transactions.repository import TransactionRepository
from app.modules.transactions.schemas import CreateTransactionRequest


class TransactionService:
    """Business logic for transactions."""

    def __init__(self) -> None:
        self._repository = TransactionRepository()
        self._asset_repository = AssetRepository()

    def _to_response(
        self,
        transaction: Transaction,
    ) -> dict:
        """Convert transaction to response format."""

        return {
            "id": transaction.id,
            "asset_symbol": transaction.asset_symbol,
            "type": transaction.type,
            "quantity": transaction.quantity,
            "price": transaction.price,
            "fee": transaction.fee,
            "total_value": (
                transaction.quantity * transaction.price
                + transaction.fee
            ),
            "created_at": transaction.created_at,
            "note": transaction.note,
        }

    def get_transactions(self) -> list[dict]:
        """Return all transactions."""

        transactions = self._repository.get_all()

        return [
            self._to_response(transaction)
            for transaction in transactions
        ]

    def _get_current_quantity(
        self,
        symbol: str,
    ) -> float:
        """Calculate current asset quantity."""

        transactions = self._repository.get_all()

        quantity = 0

        for transaction in transactions:
            if transaction.asset_symbol != symbol.upper():
                continue

            if transaction.type == TransactionType.BUY:
                quantity += transaction.quantity

            elif transaction.type == TransactionType.SELL:
                quantity -= transaction.quantity

        return quantity

    def create_transaction(
        self,
        request: CreateTransactionRequest,
    ) -> dict:
        """Create a new transaction."""

        asset = self._asset_repository.get_by_symbol(
            request.asset_symbol
        )

        if asset is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Asset '{request.asset_symbol.upper()}' not found.",
            )

        if request.type == TransactionType.SELL:

            current_quantity = self._get_current_quantity(
                request.asset_symbol
            )

            if request.quantity > current_quantity:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=(
                        f"Insufficient "
                        f"{request.asset_symbol.upper()} balance."
                    ),
                )

        transaction = self._repository.create(
            asset_symbol=request.asset_symbol,
            type=request.type,
            quantity=request.quantity,
            price=request.price,
            fee=request.fee,
            note=request.note,
        )

        return self._to_response(transaction)

    def delete_transaction(
        self,
        transaction_id: str,
    ) -> None:
        """Delete transaction."""

        deleted = self._repository.delete(
            transaction_id
        )

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Transaction not found.",
            )