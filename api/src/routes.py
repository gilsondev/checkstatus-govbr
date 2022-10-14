from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src import __version__
from src.core.config import settings
from src.core.database import get_db
from src.schemas import DomainItem
from src.services import DomainService

router = APIRouter(tags=["domains"])


@router.get("/", summary="Return metadata of application")
def index():
    return {"app": settings.TITLE, "version": __version__}


@router.get(
    "/domains",
    response_model=List[DomainItem],
    summary="Fetch all domains data",
    description="Get list of domains data related by opendata repository",
)
def fetch_domains(db: Session = Depends(get_db)):
    return DomainService(db).get_all()
