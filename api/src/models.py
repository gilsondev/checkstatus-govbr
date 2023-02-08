from datetime import datetime
from typing import ClassVar
from typing import TypeAlias

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import declarative_base  # type: ignore


Base: TypeAlias = declarative_base()  # type: ignore


class BaseModel(Base):
    Alias = Base
    __abstract__: ClassVar[bool] = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now())
    updated_at = Column(DateTime, nullable=True)


class Domain(BaseModel):
    __tablename__ = "domains"

    domain = Column(String(256), nullable=False, unique=True)
    slug = Column(String(100), nullable=False)
    document = Column(String(20))
    document_normalized = Column(String(20))
    organization = Column(String(256), nullable=False)
    organization_normalized = Column(String(256), nullable=False)
    agent = Column(String(256))
    agent_normalized = Column(String(256))
    nameservers = Column(postgresql.ARRAY(String))
    department = Column(String(256))
    department_normalized = Column(String(256))
    department_email = Column(String(255))
    status = Column(postgresql.ARRAY(String))
    registered_at = Column(DateTime, nullable=False)
    refreshed_at = Column(DateTime, nullable=False)
