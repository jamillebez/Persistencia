from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user_router, post_router, comment_router, category_router, like_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(category_router)
app.include_router(like_router)