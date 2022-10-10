from fastapi import APIRouter

from src import __version__
from src.core.config import settings


router = APIRouter(tags=["domains", "status"])


@router.get("/")
def index():
    return {"app": settings.TITLE, "version": __version__}
