from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware


# from app.api.errors.http_error import http_error_handler
# from app.api.errors.validation_error import http422_error_handler
# from app.api.routes.api import router as api_router
# from app.core.config import get_app_settings
# from app.core.events import create_start_app_handler, create_stop_app_handler
from app.routes.summarize_router import router as summarize_router
from app.config import settings
from app.llm.inference import load_model
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    tokenizer, model = await load_model(model_name=settings.model_name)
    app.state.tokenizer = tokenizer
    app.state.model = model
    yield
    app.state.tokenizer = None
    app.state.model = None


def get_application() -> FastAPI:
# settings = get_app_settings()

    # settings.configure_logging()

# settings = get_app_settings()

    # settings.configure_logging()

    """
    Builds the FastAPI application.

    This is the main entry point for building the application, and is called by the
    `uvicorn` ASGI server.

    Returns:
        FastAPI: The built application.
    """
    application = FastAPI(lifespan=lifespan)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.add_event_handler(
    #     "startup",
    #     create_start_app_handler(application, settings),
    # )
    # application.add_event_handler(
    #     "shutdown",
    #     create_stop_app_handler(application),
    # )

    # application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)

    # application.include_router(api_router, prefix=settings.api_prefix)
    application.include_router(summarize_router)

    return application

app = get_application()
