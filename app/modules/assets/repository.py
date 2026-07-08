import json
from pathlib import Path
from uuid import uuid4
from dataclasses import asdict
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