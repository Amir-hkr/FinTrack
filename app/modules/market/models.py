from dataclasses import dataclass


@dataclass(slots=True)
class MarketPrice:
    """Represent current market price."""

    symbol: str
    price: float