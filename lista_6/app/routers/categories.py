from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.models import User, Post, Comment, Category, Like
from app.schemas import (
    UserSchema, UserCreateSchema,
    PostSchema, PostCreateSchema,
    CommentSchema, CommentCreateSchema,
    CategorySchema, CategoryCreateSchema,
    LikeSchema, LikeCreateSchema
)
from app.database import get_db

category_router = SQLAlchemyCRUDRouter(
    schema=CategorySchema,
    create_schema=CategoryCreateSchema,
    db_model=Category,
    db=get_db,
    prefix="categories"
)