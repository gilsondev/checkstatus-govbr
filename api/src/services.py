from sqlalchemy.orm import Query
from sqlalchemy.orm import Session
from src.models import Domain


class DomainService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def fetch(self) -> Query:
        return self.db.query(Domain)
