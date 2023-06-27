from fastapi import FastAPI
from .db.database import engine
from .routers import blog as blog_router
from .models import blog as blog_model, user as user_model

app = FastAPI()

app.include_router(blog_router.router)
