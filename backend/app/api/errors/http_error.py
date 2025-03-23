"""HTTP error handler."""
from __future__ import annotations

from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """HTTP error handler.

    Args:
        _: The request object.
        exc: The HTTP exception.

    Returns:
        JSONResponse: The JSON response.
    """

    return JSONResponse({'errors': [exc.detail]}, status_code=exc.status_code)
