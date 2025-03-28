"""Validation error handler."""
from __future__ import annotations

from fastapi.exceptions import RequestValidationError
from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http422_error_handler(
    _: Request,
    exc: RequestValidationError | ValidationError,
) -> JSONResponse:
    """Validation error handler.

    Args:
        _: The request object.
        exc: The validation exception.

    Returns:
        JSONResponse: The JSON response.
    """

    return JSONResponse(
        {'errors': exc.errors()},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


validation_error_response_definition['properties'] = {
    'errors': {
        'title': 'Errors',
        'type': 'array',
        'items': {'$ref': f'{REF_PREFIX}ValidationError'},
    },
}
