from dataclasses import asdict, is_dataclass
from datetime import datetime
from enum import Enum
from typing import Any

from fastapi.responses import JSONResponse


def serialize_data(data: Any):
    """Convert data to JSON serializable format."""

    if isinstance(data, Enum):
        return data.value

    if isinstance(data, datetime):
        return data.isoformat()

    if is_dataclass(data):
        return serialize_data(asdict(data))

    if isinstance(data, list):
        return [
            serialize_data(item)
            for item in data
        ]

    if isinstance(data, dict):
        return {
            key: serialize_data(value)
            for key, value in data.items()
        }

    return data


def success_response(
    data: Any = None,
    message: str = "Success",
    status_code: int = 200,
):
    """Return successful API response."""

    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": serialize_data(data),
        },
    )


def error_response(
    message: str,
    status_code: int = 400,
    error_code: str | None = None,
):
    """Return error API response."""

    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "error_code": error_code,
        },
    )