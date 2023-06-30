from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Response

from ..db.dependency import get_db
from ..schemas import blog as blog_schema
from ..models.blog import Blog
router = APIRouter()


@router.get("/", response_model=List[blog_schema.BlogOut])
async def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@router.post("/", response_model=blog_schema.BlogOut)
async def create_blog(blog: blog_schema.BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@router.get("/{id}", response_model=blog_schema.BlogOut)
async def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id: {id} was not found")

    return blog


@router.put("/{id}", response_model=blog_schema.BlogOut)
async def update_blog(id: int, updated_blog: blog_schema.BlogUpdate, db: Session = Depends(get_db)):
    blog_query = db.query(Blog).filter(Blog.id == id)
    blog = blog_query.first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")

    blog_query.update(updated_blog.dict(), synchronize_session=False)
    db.commit()

    return blog_query.first()

@router.delete("/{id}")
async def delete_blog(id: int, db: Session = Depends(get_db)):
    blog_query = db.query(Blog).filter(Blog.id == id)
    blog = blog_query.first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")

    blog_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


