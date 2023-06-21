from fastapi import FastAPI
from sqlalchemy.orm import Session
from .db.database import engine, SessionLocal

app = FastAPI()