from fastapi import APIRouter, status

from app.modules.assets.schemas import AssetResponse, CreateAssetRequest
from app.modules.assets.service import AssetService

router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)

service = AssetService()


@router.get(
    "",
    response_model=list[AssetResponse],
)
def get_assets():
    """Return all assets."""
    return service.get_assets()


@router.get(
    "/{symbol}",
    response_model=AssetResponse,
)
def get_asset_by_symbol(
    symbol: str,
):
    """Return asset by symbol."""
    return service.get_asset_by_symbol(symbol)


@router.post(
    "",
    response_model=AssetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_asset(
    request: CreateAssetRequest,
):
    """Create a new asset."""
    return service.create_asset(request)