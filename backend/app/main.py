from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.v1.endpoints.summarizer import router as summarizer_router
from app.config import settings
from app.llm.inference import load_model

@asynccontextmanager
async def lifespan(application: FastAPI):
    """Lifecycle manager for the FastAPI application."""
    # Load model on startup
    tokenizer, model = await load_model(model_name=settings.model_name)
    application.state.tokenizer = tokenizer
    application.state.model = model
    yield
    # Cleanup on shutdown
    application.state.tokenizer = None
    application.state.model = None


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured application instance
    """
    application = FastAPI(
        title=settings.project_name,
        version=settings.version,
        debug=settings.debug,
        lifespan=lifespan,
    )

    # Configure CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(summarizer_router, prefix=settings.api_prefix, tags=["summarizer"])

    return application

app = create_application()
