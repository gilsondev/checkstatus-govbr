from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class BaseSschema(BaseModel):
    created_at: datetime = Field(description="Datetime creation of data")
    updated_at: Optional[datetime] = Field(description="Datetime of updated data")


class DomainItem(BaseSschema):
    domain: str = Field(description="Domain FQD", max_length=256)
    slug: str = Field(description="Domain slug (only hostname)", max_length=100)
    document: str = Field(description="Document of organization", max_length=20)
    organization: str = Field(description="Organization name", max_length=256)
    agent: str = Field(
        description="Name of representant of Organization", max_length=256
    )
    registered_at: datetime = Field(description="Datetime of domain was registered")
    refreshed_at: datetime = Field(
        description="Datetime of domain was refreshed to this organization"
    )

    class Config:
        orm_mode = True
