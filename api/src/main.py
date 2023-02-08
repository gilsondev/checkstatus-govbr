from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from src.core.config import settings
from src.routes import router as core_router


def get_application() -> FastAPI:
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
