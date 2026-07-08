from app.modules.market.models import MarketPrice
from app.modules.market.repository import MarketRepository


class MarketService:
    """Business logic for market prices."""

    def __init__(self) -> None:
        self._repository = MarketRepository()

    def get_prices(self) -> list[MarketPrice]:
        """Return all market prices."""

        return self._repository.get_all()

    def get_price(
        self,
        symbol: str,
    ) -> MarketPrice | None:
        """Return price by symbol."""

        return self._repository.get_by_symbol(
            symbol
        )

    def update_price(
        self,
        symbol: str,
        price: float,
    ) -> MarketPrice:
        """Create or update market price."""

        market_price = MarketPrice(
            symbol=symbol.upper(),
            price=price,
        )

        return self._repository.save(
            market_price
        )