from dataclasses import dataclass


@dataclass(slots=True)
class Asset:
    """Represents an investment asset."""

    id: str
    name: str
    symbol: str
    category: str