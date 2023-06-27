import datetime

from pydantic import BaseModel
from ..models import user

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    is_active: bool = True
    is_superuser: bool = False

class UserCreate(UserBase):
    """
        User create schema
    """

class UserUpdate(UserBase):
    """
        User update schema
    """

class UserOut(UserBase):
    """
        User output schema
    """
    created_at: datetime.date
    updated_at: datetime.date

    class Config:
        orm_mode = True
