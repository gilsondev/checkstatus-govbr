from sqlalchemy.orm import Query
from sqlalchemy.orm import Session
from src.models import Domain


class DomainService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def fetch(self) -> Query:
        return self.db.query(Domain).order_by(Domain.domain)

    def search(self, search: str = "") -> Query:
        query = self.db.query(Domain)

        result = query.filter(
            (Domain.domain.ilike(f"%{search}%"))
            | (Domain.organization.ilike(f"%{search}%"))
        ).order_by(Domain.domain)

        return result
