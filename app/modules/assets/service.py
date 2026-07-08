from app.modules.assets.models import Asset
from app.modules.assets.repository import AssetRepository
from app.modules.assets.schemas import CreateAssetRequest


class AssetService:
    """Business logic for assets."""

    def __init__(self) -> None:
        self._repository = AssetRepository()

    def get_assets(self) -> list[Asset]:
        """Return all assets."""
        return self._repository.get_all()

    def create_asset(
        self,
        request: CreateAssetRequest,
    ) -> Asset:
        """Create a new asset."""
        return self._repository.create(
            name=request.name,
            symbol=request.symbol,
            category=request.category,
        )