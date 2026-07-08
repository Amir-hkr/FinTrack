from pydantic import BaseModel, ConfigDict, Field


class CreateAssetRequest(BaseModel):
    """Request model for creating an asset."""

    name: str = Field(min_length=2, max_length=50)
    symbol: str = Field(min_length=1, max_length=10)
    category: str = Field(min_length=2, max_length=30)


class AssetResponse(BaseModel):
    """Response model for an asset."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    symbol: str
    category: str