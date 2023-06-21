import datetime

from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=datetime.datetime.utcnow())

    blogs = relationship("Blog", back_populates="author")
