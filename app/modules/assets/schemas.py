from pydantic import BaseModel, ConfigDict, Field, field_validator


class CreateAssetRequest(BaseModel):
    """Request model for creating an asset."""

    name: str = Field(
        min_length=2,
        max_length=50,
    )

    symbol: str = Field(
        min_length=1,
        max_length=10,
    )

    category: str = Field(
        min_length=2,
        max_length=30,
    )

    @field_validator("name", "category")
    @classmethod
    def clean_text(
        cls,
        value: str,
    ) -> str:
        """Clean text fields."""

        return value.strip().title()

    @field_validator("symbol")
    @classmethod
    def clean_symbol(
        cls,
        value: str,
    ) -> str:
        """Normalize asset symbol."""

        return value.strip().upper()


class AssetResponse(BaseModel):
    """Response model for an asset."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    symbol: str
    category: str