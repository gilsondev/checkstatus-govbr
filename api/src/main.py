import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from sentry_sdk import set_tag
from src.core.config import settings
from src.routes import router as core_router


def get_application() -> FastAPI:
    sentry_sdk.init(
        dsn="https://011f53de8eea0a53cb44e163d0453eb5@o4506032925900800.ingest.sentry.io/4506032926031872",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
    )
    set_tag("app", "Checkstatus API")

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    application.include_router(core_router)

    # Configure fastapi pagination
    add_pagination(application)

    return application


app = get_application()
