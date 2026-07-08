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