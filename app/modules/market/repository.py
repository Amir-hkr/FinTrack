import json
from dataclasses import asdict
from pathlib import Path

from app.modules.market.models import MarketPrice


class MarketRepository:
    """Handle market price persistence."""

    def __init__(self) -> None:
        self._file_path = Path("data/prices.json")

        if not self._file_path.exists():
            self._file_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            self._file_path.write_text(
                "[]",
                encoding="utf-8",
            )

    def get_all(self) -> list[MarketPrice]:
        """Return all prices."""

        with self._file_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return [
            MarketPrice(**item)
            for item in data
        ]

    def get_by_symbol(
        self,
        symbol: str,
    ) -> MarketPrice | None:
        """Return price by symbol."""

        prices = self.get_all()

        for price in prices:
            if price.symbol == symbol.upper():
                return price

        return None

    def save(
        self,
        market_price: MarketPrice,
    ) -> MarketPrice:
        """Create or update price."""

        prices = self.get_all()

        updated = False

        for index, item in enumerate(prices):
            if item.symbol == market_price.symbol:
                prices[index] = market_price
                updated = True
                break

        if not updated:
            prices.append(market_price)

        self._write(prices)

        return market_price

    def _write(
        self,
        prices: list[MarketPrice],
    ) -> None:
        """Write prices to file."""

        data = [
            asdict(price)
            for price in prices
        ]

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