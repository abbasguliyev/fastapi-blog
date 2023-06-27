from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from ..db.dependency import get_db
from ..schemas import blog
from ..models.blog import Blog
router = APIRouter(prefix="/posts")

@router.get("/", response_model=List[blog.BlogOut])
async def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs