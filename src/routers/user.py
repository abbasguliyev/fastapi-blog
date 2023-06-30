from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Response

from ..db.dependency import get_db
from ..schemas import user as user_schema
from utils import security
from ..models.user import User

router = APIRouter()

@router.post("/", response_model=user_schema.UserOut)
async def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    hashed_password = security.get_hashed_password(user.password)
    user.password = hashed_password

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/", response_model=List[user_schema.UserOut])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/{id}", response_model=user_schema.UserOut)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")

    return user

@router.put("/{id}", response_model=user_schema.UserOut)
async def update_user(id: int, updated_user: user_schema.UserUpdate, db: Session = Depends(get_db)):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")

    user_query.update(**updated_user.dict(), synchronize_session=False)
    db.commit()

    return user_query.first()

@router.delete("/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")

    user_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)