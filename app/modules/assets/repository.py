import json
from dataclasses import asdict
from pathlib import Path
from uuid import uuid4

from app.modules.assets.models import Asset


class AssetRepository:
    """Handle asset persistence."""

    def __init__(self) -> None:
        self._file_path = Path("data/assets.json")

        if not self._file_path.exists():
            self._file_path.parent.mkdir(parents=True, exist_ok=True)
            self._file_path.write_text("[]", encoding="utf-8")

    def get_all(self) -> list[Asset]:
        """Return all assets."""

        with self._file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Asset(**item) for item in data]

    def get_by_symbol(
        self,
        symbol: str,
    ) -> Asset | None:
        """Return asset by symbol."""

        for asset in self.get_all():
            if asset.symbol == symbol.upper():
                return asset

        return None

    def create(
        self,
        name: str,
        symbol: str,
        category: str,
    ) -> Asset:
        """Create a new asset."""

        assets = self.get_all()

        asset = Asset(
            id=str(uuid4()),
            name=name,
            symbol=symbol.upper(),
            category=category,
        )

        assets.append(asset)

        self._save(assets)

        return asset

    def update(
        self,
        asset: Asset,
    ) -> Asset:
        """Update an existing asset."""

        assets = self.get_all()

        for index, current_asset in enumerate(assets):
            if current_asset.id == asset.id:
                assets[index] = asset
                break

        self._save(assets)

        return asset

    def delete(
        self,
        symbol: str,
    ) -> None:
        """Delete asset by symbol."""

        assets = [
            asset
            for asset in self.get_all()
            if asset.symbol != symbol.upper()
        ]

        self._save(assets)

    def _save(
        self,
        assets: list[Asset],
    ) -> None:
        """Save assets."""

        data = [asdict(asset) for asset in assets]

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