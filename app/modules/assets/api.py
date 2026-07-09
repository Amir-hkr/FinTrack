# from fastapi import APIRouter, status

# from app.core.response import success_response
# from app.modules.assets.schemas import (
#     AssetResponse,
#     CreateAssetRequest,
# )
# from app.modules.assets.service import AssetService


# router = APIRouter(
#     prefix="/assets",
#     tags=["Assets"],
# )


# service = AssetService()


# @router.get("")
# def get_assets():
#     """Return all assets."""

#     return success_response(
#         data=service.get_assets(),
#         message="Assets retrieved successfully",
#     )


# @router.get("/{symbol}")
# def get_asset_by_symbol(
#     symbol: str,
# ):
#     """Return asset by symbol."""

#     return success_response(
#         data=service.get_asset_by_symbol(symbol),
#         message="Asset retrieved successfully",
#     )


# @router.post(
#     "",
#     status_code=status.HTTP_201_CREATED,
# )
# def create_asset(
#     request: CreateAssetRequest,
# ):
#     """Create a new asset."""

#     return success_response(
#         data=service.create_asset(request),
#         message="Asset created successfully",
#         status_code=status.HTTP_201_CREATED,
#     )
from fastapi import APIRouter, status

from app.core.response import success_response
from app.modules.assets.schemas import (
    AssetResponse,
    CreateAssetRequest,
)
from app.modules.assets.service import AssetService


router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)

service = AssetService()


@router.get("")
def get_assets():
    """Return all assets."""

    return success_response(
        data=service.get_assets(),
        message="Assets retrieved successfully",
    )


@router.get("/{symbol}")
def get_asset_by_symbol(
    symbol: str,
):
    """Return asset by symbol."""

    return success_response(
        data=service.get_asset_by_symbol(symbol),
        message="Asset retrieved successfully",
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
def create_asset(
    request: CreateAssetRequest,
):
    """Create a new asset."""

    return success_response(
        data=service.create_asset(request),
        message="Asset created successfully",
        status_code=status.HTTP_201_CREATED,
    )


@router.delete("/{asset_id}")
def delete_asset(
    asset_id: str,
):
    """Delete asset."""

    service.delete_asset(asset_id)

    return success_response(
        data=None,
        message="Asset deleted successfully",
    )