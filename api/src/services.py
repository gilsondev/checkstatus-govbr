from sqlalchemy.orm import Query
from sqlalchemy.orm import Session
from src.models import Domain


class DomainService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def fetch(self, search: str = "") -> Query:
        query = self.db.query(Domain)

        if not search:
            return query

        return query.filter(
            (Domain.domain.ilike(f"%{search}%"))
            | (Domain.organization.ilike(f"%{search}%"))
        )
