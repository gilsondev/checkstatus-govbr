from typing import Optional

from sqlalchemy import or_
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session
from src.models import Domain


class DomainService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def fetch(self, filters: Optional[dict]) -> Query:
        query = self.db.query(Domain)

        query = query.filter(
            or_(Domain.available == filters["available"], filters["available"] is None),
            or_(Domain.status.any(filters["status"]), filters["status"] is None),
        ).order_by(Domain.domain)

        return query

    def search(
        self,
        filters: Optional[dict],
        search: str = "",
    ) -> Query:
        query = self.db.query(Domain)

        query = query.filter(
            or_(
                Domain.domain.ilike(f"%{search}%"),
                Domain.organization.ilike(f"%{search}%"),
            ),
            or_(Domain.available == filters["available"], filters["available"] is None),
            or_(Domain.status.any(filters["status"]), filters["status"] is None),
        ).order_by(Domain.domain)

        return query
