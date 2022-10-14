from datetime import datetime
from typing import ClassVar

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__: ClassVar[bool] = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now())
    updated_at = Column(DateTime, nullable=True)


class Domain(BaseModel):
    __tablename__ = "domains"

    domain = Column(String(256), nullable=False, unique=True)
    slug = Column(String(100), nullable=False)
    document = Column(String(20))
    organization = Column(String(256), nullable=False)
    agent = Column(String(256))
    registered_at = Column(DateTime, nullable=False)
    refreshed_at = Column(DateTime, nullable=False)
