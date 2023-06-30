import datetime

from pydantic import BaseModel
from ..models import blog

class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    """
        Blog create schema
    """

class BlogUpdate(BlogBase):
    """
        Blog update schema
    """

class BlogOut(BlogBase):
    """
        Blog output schema
    """
    created_at: datetime.date
    updated_at: datetime.date

    class Config:
        orm_mode = True
