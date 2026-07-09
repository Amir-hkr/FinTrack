# from fastapi import HTTPException, status

# from app.modules.assets.models import Asset
# from app.modules.assets.repository import AssetRepository
# from app.modules.assets.schemas import CreateAssetRequest


# class AssetService:
#     """Business logic for assets."""

#     def __init__(self) -> None:
#         self._repository = AssetRepository()

#     def get_assets(self) -> list[Asset]:
#         """Return all assets."""
#         return self._repository.get_all()

#     def get_asset_by_symbol(
#         self,
#         symbol: str,
#     ) -> Asset:
#         """Return asset by symbol."""

#         asset = self._repository.get_by_symbol(symbol)

#         if asset is None:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"Asset with symbol '{symbol.upper()}' not found.",
#             )

#         return asset

#     def create_asset(
#         self,
#         request: CreateAssetRequest,
#     ) -> Asset:
#         """Create a new asset."""

#         existing_asset = self._repository.get_by_symbol(request.symbol)

#         if existing_asset is not None:
#             raise HTTPException(
#                 status_code=status.HTTP_409_CONFLICT,
#                 detail=f"Asset with symbol '{request.symbol.upper()}' already exists.",
#             )

#         return self._repository.create(
#             name=request.name,
#             symbol=request.symbol,
#             category=request.category,
#         )
from fastapi import HTTPException, status

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

    def get_asset_by_symbol(
        self,
        symbol: str,
    ) -> Asset:
        """Return asset by symbol."""

        asset = self._repository.get_by_symbol(symbol)

        if asset is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Asset with symbol '{symbol.upper()}' not found.",
            )

        return asset

    def create_asset(
        self,
        request: CreateAssetRequest,
    ) -> Asset:
        """Create a new asset."""

        existing_asset = self._repository.get_by_symbol(
            request.symbol
        )

        if existing_asset is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Asset with symbol '{request.symbol.upper()}' already exists.",
            )

        return self._repository.create(
            name=request.name,
            symbol=request.symbol,
            category=request.category,
        )

    def delete_asset(
        self,
        asset_id: str,
    ) -> None:
        """Delete asset by id."""

        deleted = self._repository.delete(asset_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Asset not found.",
            )