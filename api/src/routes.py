from typing import Any
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from src import __version__
from src.core.config import settings
from src.core.database import get_db
from src.schemas import DomainItem
from src.services import DomainService

router = APIRouter(tags=["domains"])


@router.get("/", summary="Return metadata of application")
def index() -> Any:
    return {"app": settings.TITLE, "version": __version__}


@router.get(
    "/domains",
    response_model=Page[DomainItem],
    summary="Fetch all domains data",
    description="Get list of domains data related by opendata repository",
)
def fetch_domains(
    db: Session = Depends(get_db),
    search: Optional[str] = None,
    available: Optional[bool] = None,
    status: Optional[str] = None,
) -> Any:  # noqa

    if search:
        return paginate(
            DomainService(db).search(
                {"available": available, "status": status}, search=search
            )
        )

    return paginate(DomainService(db).fetch({"available": available, "status": status}))
