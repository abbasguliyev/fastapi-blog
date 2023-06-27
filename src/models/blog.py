import datetime

from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    slug = Column(String(300))
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())

    author = relationship('User', back_populates='blogs')
