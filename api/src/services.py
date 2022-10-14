from typing import List

from sqlalchemy.orm import Session
from src.models import Domain
from src.schemas import DomainItem


class DomainService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> List[DomainItem]:
        return self.db.query(Domain).all()
