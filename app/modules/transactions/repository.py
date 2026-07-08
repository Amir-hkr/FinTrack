import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from app.modules.transactions.models import Transaction, TransactionType


class TransactionRepository:
    """Handle transaction persistence."""

    def __init__(self) -> None:
        self._file_path = Path("data/transactions.json")

        if not self._file_path.exists():
            self._file_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )
            self._file_path.write_text(
                "[]",
                encoding="utf-8",
            )

    def get_all(self) -> list[Transaction]:
        """Return all transactions."""

        with self._file_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return [
            Transaction(
                id=item["id"],
                asset_symbol=item["asset_symbol"],
                type=TransactionType(item["type"]),
                quantity=item["quantity"],
                price=item["price"],
                fee=item["fee"],
                created_at=datetime.fromisoformat(
                    item["created_at"]
                ),
                note=item["note"],
            )
            for item in data
        ]

    def create(
        self,
        asset_symbol: str,
        type: TransactionType,
        quantity: float,
        price: float,
        fee: float,
        note: str,
    ) -> Transaction:
        """Create a new transaction."""

        transactions = self.get_all()

        transaction = Transaction(
            id=str(uuid4()),
            asset_symbol=asset_symbol.upper(),
            type=type,
            quantity=quantity,
            price=price,
            fee=fee,
            created_at=datetime.now(),
            note=note,
        )

        transactions.append(transaction)

        self._save(transactions)

        return transaction

    def _save(
        self,
        transactions: list[Transaction],
    ) -> None:
        """Save transactions."""

        data = []

        for transaction in transactions:
            item = asdict(transaction)
            item["type"] = transaction.type.value
            item["created_at"] = transaction.created_at.isoformat()
            data.append(item)

        with self._file_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )